
## 2024-08-04 - Regex Compilation Overhead
**Learning:** Recompiling regular expressions inside a frequently called function (`slugify`) within test file iteration blocks leads to redundant compilation and parser CPU overhead.
**Action:** Pre-compile regular expressions (e.g., using `re.compile()`) as class or module-level variables when they will be executed frequently to avoid unnecessary repeated compilation in loops.
