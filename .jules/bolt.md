## 2024-11-20 - Regex Optimization in Python Loops
**Learning:** Compiling regex patterns (`re.sub`, `re.match`) on every invocation within loops or helper methods creates measurable overhead due to redundant parsing and compilation.
**Action:** When a method heavily uses regular expressions (like `slugify` processing multiple text fragments), always extract and pre-compile those patterns at the module or class level (`_RE_NON_ALNUM = re.compile(...)`) to process them once and reuse them efficiently.

## 2024-12-10 - Optimize Collection Type for Membership Tests in Loops
**Learning:** Initializing collections as a `list` for parsed items like heading slugs leads to unnecessary overhead when they are later used for O(N) membership lookups (`in` operator) in loops.
**Action:** When performing membership tests inside loops (such as verifying parsed anchors against heading slugs), always initialize the collection as a `set` rather than a `list` to reduce lookup time complexity from O(N) to O(1) constant time and avoid O(N^2) overhead patterns.
