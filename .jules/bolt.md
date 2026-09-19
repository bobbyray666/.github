## 2024-11-20 - Regex Optimization in Python Loops
**Learning:** Compiling regex patterns (`re.sub`, `re.match`) on every invocation within loops or helper methods creates measurable overhead due to redundant parsing and compilation.
**Action:** When a method heavily uses regular expressions (like `slugify` processing multiple text fragments), always extract and pre-compile those patterns at the module or class level (`_RE_NON_ALNUM = re.compile(...)`) to process them once and reuse them efficiently.

## 2024-11-20 - O(N^2) Anti-pattern in Link Validation Lookups
**Learning:** Performing anchor link validation by repeatedly searching a `list` of parsed heading slugs inside an iteration loop creates an O(N^2) complexity bottleneck, needlessly degrading test execution performance for large documentation files.
**Action:** When validating items against a collection of extracted properties inside a loop, always convert the reference collection to a `set` before the loop to reduce lookup complexity from O(N) to O(1) and overall validation complexity to O(N).
