## 2024-11-20 - Regex Optimization in Python Loops
**Learning:** Compiling regex patterns (`re.sub`, `re.match`) on every invocation within loops or helper methods creates measurable overhead due to redundant parsing and compilation.
**Action:** When a method heavily uses regular expressions (like `slugify` processing multiple text fragments), always extract and pre-compile those patterns at the module or class level (`_RE_NON_ALNUM = re.compile(...)`) to process them once and reuse them efficiently.

## 2024-11-20 - Set for O(1) Membership Tests in Loops
**Learning:** Performing membership tests (like `in` or `assertIn`) against a `list` inside a loop creates O(N^2) time complexity overhead, which can be significant when processing many items like parsed document links.
**Action:** When performing membership tests inside loops (such as verifying parsed anchors against heading slugs), always initialize the collection as a `set` rather than a `list` to reduce lookup time complexity from O(N) to O(1) constant time and avoid O(N^2) overhead patterns.
