
## 2024-05-19 - [Compiled Regex Object Optimization]
**Learning:** Initializing `re.compile()` within loops and frequently-called methods (e.g., parsing markdown headings or links across multiple files) incurs a measurable CPU penalty due to repetitive parsing and cache-checks of the regular expression strings. Even `re.sub` incurs this overhead when using string patterns dynamically.
**Action:** Always pre-compile regular expressions using `re.compile()` as module-level constants or class-level variables outside of iterations and frequently evaluated functions to ensure the parser setup cost is only incurred once.
