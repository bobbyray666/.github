## 2024-11-20 - Regex Optimization in Python Loops
**Learning:** Compiling regex patterns (`re.sub`, `re.match`) on every invocation within loops or helper methods creates measurable overhead due to redundant parsing and compilation.
**Action:** When a method heavily uses regular expressions (like `slugify` processing multiple text fragments), always extract and pre-compile those patterns at the module or class level (`_RE_NON_ALNUM = re.compile(...)`) to process them once and reuse them efficiently.
## 2024-11-20 - Redundant Network Requests in Markdown Tests
**Learning:** Repeatedly validating the same external URL across multiple markdown files without caching causes significant I/O bottleneck in test suites.
**Action:** Add an in-memory `set` to track and cache checked URLs in link validation tests to bypass redundant external network requests.
