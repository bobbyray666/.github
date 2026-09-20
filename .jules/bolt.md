## 2024-11-20 - Regex Optimization in Python Loops
**Learning:** Compiling regex patterns (`re.sub`, `re.match`) on every invocation within loops or helper methods creates measurable overhead due to redundant parsing and compilation.
**Action:** When a method heavily uses regular expressions (like `slugify` processing multiple text fragments), always extract and pre-compile those patterns at the module or class level (`_RE_NON_ALNUM = re.compile(...)`) to process them once and reuse them efficiently.

## 2024-05-24 - O(N^2) Overhead in List Lookups Inside Loops
**Learning:** Performing membership tests (`in`) against a `list` inside a loop creates an O(N^2) time complexity bottleneck. In this codebase, verifying parsed anchors against heading slugs using a list caused unnecessary overhead.
**Action:** Always initialize the collection as a `set` locally before the loop when performing membership tests inside loops, reducing lookup time complexity from O(N) to O(1). Do not modify the return types of shared helper methods to avoid breaking caller logic.
