## 2024-05-24 - Python Regex Compilation Overhead in Loops
**Learning:** In Python, dynamically compiling regular expressions with methods like `re.sub` or `re.compile` inside frequently called methods (like parsing logic executed in a loop) introduces redundant parsing and compilation overhead that slows down execution.
**Action:** Always pre-compile regular expressions as class-level or module-level constants (e.g., using `re.compile()`) outside of loops or file iteration blocks to prevent unnecessary CPU overhead.
