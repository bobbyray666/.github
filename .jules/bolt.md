## 2024-05-15 - Compile Regex Outside Loops
**Learning:** Python's `re.sub`, `re.match`, and `re.compile` calls inside tight loops (like iterating over all lines of a markdown file) add unnecessary CPU overhead for repeated parser tree build/compile phases. The `slugify` and other parser test loops had uncompiled string regex expressions inside.
**Action:** Always pre-compile regexes (`re.compile`) into static or class-level attributes when they are invoked within hot loops or helper functions like strings conversions or tests.
