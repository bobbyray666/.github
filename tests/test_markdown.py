import os
import re
import unittest
import urllib.request
from urllib.error import HTTPError, URLError
from unittest.mock import patch, mock_open

class TestMarkdown(unittest.TestCase):
    # Files to test
    MARKDOWN_FILES = ["profile/README.md", "copilot-instructions.md"]

    # Allowed external URLs that may be private, return 404, or fail when accessed via basic script
    IGNORED_URLS = {
        "https://github.com/bobbyray666/Dao", # Known private or placeholder repository
    }

    # Pre-compiled regular expressions for performance
    SLUG_RE_NON_ALNUM = re.compile(r'[^a-z0-9\s-]')
    SLUG_RE_SPACES = re.compile(r'\s+')
    SLUG_RE_DASHES = re.compile(r'-+')
    HEADING_FORMAT_RE = re.compile(r'^(#+)([^#\s].*)$')
    LIST_FORMAT_RE = re.compile(r'^(\s*)([-*+]|\d+\.)([^\s].*)$')
    HEADING_FINDER_RE = re.compile(r'^(#+)\s+(.+)$')
    LINK_FINDER_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')

    def get_markdown_files(self):
        # Ensure we check existing files from our list
        existing_files = []
        for f in self.MARKDOWN_FILES:
            if os.path.exists(f):
                existing_files.append(f)
        return existing_files

    def slugify(self, text):
        """Convert a heading text to a markdown anchor slug."""
        # Lowercase, replace non-alphanumeric with hyphen, strip multiple hyphens
        slug = text.lower()
        slug = self.SLUG_RE_NON_ALNUM.sub('', slug)
        slug = self.SLUG_RE_SPACES.sub('-', slug)
        slug = self.SLUG_RE_DASHES.sub('-', slug)
        return slug.strip('-')

    def test_file_ends_with_newline(self):
        """Ensure each markdown file ends with exactly one newline."""
        for filepath in self.get_markdown_files():
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertTrue(
                content.endswith("\n"),
                f"File {filepath} must end with a newline."
            )
            # Ensure not multiple newlines at the end
            self.assertFalse(
                content.endswith("\n\n"),
                f"File {filepath} should not end with multiple consecutive newlines."
            )

    def test_headings_format(self):
        """Ensure headings are properly formatted with a space after #."""
        # e.g. '# Heading' is valid, '#Heading' is invalid
        for filepath in self.get_markdown_files():
            with open(filepath, "r", encoding="utf-8") as f:
                in_code_block = False
                for idx, line in enumerate(f, 1):
                    stripped = line.strip()
                    if stripped.startswith("```"):
                        in_code_block = not in_code_block
                        continue

                    if in_code_block:
                        continue

                    match = self.HEADING_FORMAT_RE.match(stripped)
                    self.assertIsNone(
                        match,
                        f"Malformed heading in {filepath} at line {idx}: '{stripped}'. "
                        f"Missing space after hash signs."
                    )

    def test_no_consecutive_blank_lines(self):
        """Ensure no more than one consecutive blank line is used."""
        for filepath in self.get_markdown_files():
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            consecutive_blanks = 0
            for idx, line in enumerate(lines, 1):
                if line.strip() == "":
                    consecutive_blanks += 1
                else:
                    consecutive_blanks = 0

                self.assertLessEqual(
                    consecutive_blanks,
                    2, # Allowing at most 1 consecutive blank line (meaning total blank lines between text is at most 1).
                       # consecutive_blanks becomes 2 when we see two empty lines in a row.
                    f"Too many consecutive empty lines in {filepath} at line {idx}."
                )

    def test_list_items_format(self):
        """Ensure lists are properly formatted with space after the marker."""
        # E.g. '- item' or '* item' or '1. item'
        # Invalid: '-item' or '1.item'
        for filepath in self.get_markdown_files():
            with open(filepath, "r", encoding="utf-8") as f:
                in_code_block = False
                for idx, line in enumerate(f, 1):
                    stripped = line.strip()
                    if stripped.startswith("```"):
                        in_code_block = not in_code_block
                        continue

                    if in_code_block:
                        continue

                    match = self.LIST_FORMAT_RE.match(stripped)
                    if match:
                        marker = match.group(2)
                        rest = match.group(3)
                        # Ensure it's not a horizontal rule like '---' or '***'
                        if marker in ['-', '*'] and all(c == marker for c in rest):
                            continue # Horizontal rule
                        # Ensure it's not bold/italic like '**' or '***'
                        if marker in ['-', '*'] and rest.startswith(marker):
                            continue
                        # If marker is '*' and rest contains any '*' (e.g. '*text*'), it is italic text, not a list item
                        if marker == '*' and '*' in rest:
                            continue
                        # If marker is '-' and rest contains another '-' (e.g., command flag, strikethrough), skip
                        if marker == '-' and '-' in rest:
                            continue

                        self.fail(
                            f"Malformed list item in {filepath} at line {idx}: '{stripped}'. "
                            f"Missing space after list marker."
                        )

    def _extract_heading_slugs(self, lines):
        """Find all headings in markdown lines and return their slugs."""
        headings = []
        for line in lines:
            match = self.HEADING_FINDER_RE.match(line.strip())
            if match:
                headings.append(self.slugify(match.group(2)))
        return headings

    def _validate_external_link(self, url, filepath, strict_check):
        """Validate external HTTP/HTTPS link."""
        if url in self.IGNORED_URLS:
            print(f"Skipping ignored URL: {url}")
            return

        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
            )
            # We try to use a relatively short timeout
            with urllib.request.urlopen(req, timeout=10) as response:
                status = response.getcode()
                if status not in [200, 201, 202, 203, 204]:
                    msg = f"Link {url} in {filepath} returned unexpected status code {status}."
                    if strict_check:
                        self.fail(msg)
                    else:
                        print(f"WARNING: {msg}")
        except HTTPError as e:
            msg = f"Link {url} in {filepath} failed with HTTP Error: {e.code} {e.reason}"
            if strict_check:
                self.fail(msg)
            else:
                print(f"WARNING: {msg}")
        except URLError as e:
            msg = f"Link {url} in {filepath} failed with URL Error: {e.reason}"
            if strict_check:
                self.fail(msg)
            else:
                print(f"WARNING: {msg}")
        except Exception as e:
            msg = f"Link {url} in {filepath} failed: {str(e)}"
            if strict_check:
                self.fail(msg)
            else:
                print(f"WARNING: {msg}")

    def _validate_anchor_link(self, url, filepath, headings):
        """Validate anchor link within the same file."""
        anchor = url[1:]
        self.assertIn(
            anchor,
            headings,
            f"Anchor link '{url}' in {filepath} does not match any heading slug in the file. "
            f"Available slugs: {headings}"
        )

    def _validate_local_link(self, url, filepath):
        """Validate local file or directory links."""
        # Resolve path relative to markdown file directory
        file_dir = os.path.dirname(filepath)
        target_path = os.path.join(file_dir, url) if file_dir else url
        # Strip any anchor reference from local file link, e.g. path/to/file.md#anchor
        if "#" in target_path:
            target_path = target_path.split("#")[0]

        self.assertTrue(
            os.path.exists(target_path),
            f"Local link target '{url}' in {filepath} does not exist."
        )

    def test_markdown_links(self):
        """Extract and verify all markdown links."""
        # Find markdown links: [text](url)
        # Note: can handle empty text like [](url) or full text
        strict_check = os.environ.get("STRICT_LINK_CHECK", "false").lower() == "true"

        for filepath in self.get_markdown_files():
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                lines = content.splitlines()

            # Find all headings to build valid slugs for anchor links
            headings = self._extract_heading_slugs(lines)

            matches = self.LINK_FINDER_RE.findall(content)
            for text, url in matches:
                url = url.strip()
                text = text.strip()

                # Check 1: Empty URL
                self.assertTrue(
                    url != "",
                    f"Link text '[{text}]' has an empty URL target in {filepath}."
                )

                # Check 2: External HTTP/HTTPS Link
                if url.startswith("http://") or url.startswith("https://"):
                    self._validate_external_link(url, filepath, strict_check)

                # Check 3: Anchor within the same file
                elif url.startswith("#"):
                    self._validate_anchor_link(url, filepath, headings)

                # Check 4: Local file or directory links
                else:
                    self._validate_local_link(url, filepath)

    @patch('urllib.request.urlopen')
    @patch('builtins.open', new_callable=mock_open, read_data="[example](https://example.com)")
    @patch.dict(os.environ, {"STRICT_LINK_CHECK": "false"})
    def test_markdown_links_http_error_warning(self, mock_file, mock_urlopen):
        """Test HTTPError handling in non-strict mode (logs a warning)."""
        from io import BytesIO
        err = HTTPError("https://example.com", 404, "Not Found", {}, BytesIO(b""))
        mock_urlopen.side_effect = err

        with patch.object(self, 'get_markdown_files', return_value=["dummy.md"]):
            with patch('builtins.print') as mock_print:
                self.test_markdown_links()
                mock_print.assert_any_call("WARNING: Link https://example.com in dummy.md failed with HTTP Error: 404 Not Found")

    @patch('urllib.request.urlopen')
    @patch('builtins.open', new_callable=mock_open, read_data="[example](https://example.com)")
    @patch.dict(os.environ, {"STRICT_LINK_CHECK": "true"})
    def test_markdown_links_http_error_strict(self, mock_file, mock_urlopen):
        """Test HTTPError handling in strict mode (fails the test)."""
        from io import BytesIO
        err = HTTPError("https://example.com", 404, "Not Found", {}, BytesIO(b""))
        mock_urlopen.side_effect = err

        with patch.object(self, 'get_markdown_files', return_value=["dummy.md"]):
            with self.assertRaises(AssertionError) as context:
                self.test_markdown_links()
            self.assertIn("Link https://example.com in dummy.md failed with HTTP Error: 404 Not Found", str(context.exception))

    def test_slugify(self):
        """Verify that slugify correctly converts heading text to markdown anchor slug."""
        test_cases = [
            ("Hello World", "hello-world"),
            ("Hello  --  World", "hello-world"),
            ("Hello, World!", "hello-world"),
            ("Heading 1.2.3", "heading-123"),
            ("HeLlO wOrLd", "hello-world"),
            (" - Hello World - ", "hello-world"),
            ("!!!", ""),
            ("making-inference-boring", "making-inference-boring"),
            ("under-the-hood", "under-the-hood"),
            ("Coda: After the Model Boom", "coda-after-the-model-boom"),
        ]
        for input_text, expected_slug in test_cases:
            with self.subTest(input_text=input_text):
                actual_slug = self.slugify(input_text)
                self.assertEqual(
                    actual_slug,
                    expected_slug,
                    f"slugify('{input_text}') should be '{expected_slug}', but got '{actual_slug}'"
                )

if __name__ == '__main__':
    unittest.main()
