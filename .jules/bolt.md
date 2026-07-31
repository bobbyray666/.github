# Codebase Performance Learnings

## Critical Learnings
- In Python `unittest` tests, particularly those that dynamically iterate over files or lists of resources, compiling regular expressions inside iterative loops introduces a non-trivial performance overhead.
- Compiling regular expressions via `re.compile` should always be done once outside of loops (e.g., at the function, class, or module level) and reused across elements.

## Performance Patterns
- Avoid compiling regular expressions repeatedly when analyzing batches of markdown files (such as `test_markdown_links`).
- Moving compiling overhead outside of `for` loops results in a cleaner separation of pattern definitions from processing logic and reduces CPU allocation cycles.
