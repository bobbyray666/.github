## 2024-05-18 - Compiling Regular Expressions for Performance
**Learning:** In the link validation script (`tests/test_markdown.py`), regular expressions were being compiled inside the `slugify` method and loops. Since `slugify` is called for every heading in every markdown file, this redundant regex compilation wastes CPU cycles and unnecessarily increases parsing overhead.
**Action:** When validating links or parsing text across multiple files, pre-compile all regular expressions using `re.compile()` at the class or module level to eliminate redundant compilation during iterations.
