## 2024-11-20 - Regex Optimization in Python Loops
**Learning:** Compiling regex patterns (`re.sub`, `re.match`) on every invocation within loops or helper methods creates measurable overhead due to redundant parsing and compilation.
**Action:** When a method heavily uses regular expressions (like `slugify` processing multiple text fragments), always extract and pre-compile those patterns at the module or class level (`_RE_NON_ALNUM = re.compile(...)`) to process them once and reuse them efficiently.

## 2024-11-20 - O(1) Lookups in Loop Iterations
**Learning:** Using a list for membership checking (`in`) within an inner loop creates an O(N^2) complexity pattern. In `test_markdown.py`, checking if an anchor exists in a list of slugs within a loop over all links caused unnecessary overhead.
**Action:** When performing membership tests inside loops (like verifying if parsed anchors exist in heading slugs), always use a `set` for the lookups to reduce O(N) operations to O(1) constant time.
