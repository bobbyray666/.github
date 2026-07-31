## 2026-07-25 - Python Set for O(1) Membership Testing in Markdown Link Validation
**Learning:** Using a python set instead of a list for collections like anchor slugs drastically improves performance of membership lookups inside validation loops, reducing lookup time complexity from O(N) to O(1). For larger files or multiple documents, this saves significant CPU cycles.
**Action:** When gathering unique elements (such as slugs, IDs, or keys) to run membership tests (`assertIn`, `in`), initialize the collection using `set()` and use `.add()` instead of `.append()`.
