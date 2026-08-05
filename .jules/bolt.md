## 2024-05-14 - [Regular Expression Optimization]
**Learning:** Implicit compilation of regular expressions using `re.sub(r'...', ...)` inside loop and repeated function calls causes unnecessary regex parsing and compilation overhead, especially in core routines like `slugify` that are called per matched item across a document collection.
**Action:** When a method applies string manipulation with fixed patterns, always pre-compile regular expressions as class or module-level variables (e.g., using `re.compile`) to shift overhead from invocation time to initialization time.
