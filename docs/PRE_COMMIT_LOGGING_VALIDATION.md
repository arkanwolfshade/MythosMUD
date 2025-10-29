# Pre-commit Logging Validation

## Overview

The enhanced logging system now includes pre-commit hooks that automatically validate logging patterns to ensure all code uses the enhanced logging system correctly.

## Implementation

### Pre-commit Hook Configuration

The logging validation is implemented in `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: logging-pattern-lint
      name: Enhanced Logging Pattern Linter
      entry: python scripts/lint_logging_patterns.py
      language: system
      types: [python]
      pass_filenames: false
      always_run: true
      stages: [pre-commit]
```

### Logging Pattern Linter

The linter script `scripts/lint_logging_patterns.py` performs the following validations:

#### ✅ **Validates Enhanced Logging Usage**

- Ensures `from server.logging.enhanced_logging_config import get_logger` is used
- Checks that `get_logger(__name__)` is used instead of `logging.getLogger()`

#### ❌ **Detects Forbidden Patterns**

- `import logging` statements
- `from logging import getLogger` statements
- `logging.getLogger()` calls
- `context={"key": "value"}` parameters
- f-string formatting in log messages
- String formatting in log calls

#### 🔍 **Scope of Validation**

- Scans all Python files in the `server/` directory
- Excludes test files, `__pycache__`, and virtual environment files
- Provides detailed error messages with line numbers

## Usage

### Automatic Validation

The linter runs automatically on every commit via pre-commit hooks:

```bash
git commit -m "Your commit message"
# Pre-commit hooks run automatically
# If logging violations are found, the commit is blocked
```

### Manual Validation

You can run the linter manually:

```bash
python scripts/lint_logging_patterns.py
```

### Pre-commit Installation

To install the pre-commit hooks:

```bash
pre-commit install
```

## Error Messages

The linter provides clear error messages for each violation:

```
File: server/example.py
  Line 10: FORBIDDEN: import logging - Use enhanced logging instead
  Line 15: FORBIDDEN: context={'key': 'value'} parameter - Use direct key-value pairs instead
  Line 20: FORBIDDEN: f-string formatting in log messages - Use structured logging instead
```

## Correct Usage Examples

The linter enforces these correct patterns:

```python
# ✅ CORRECT - Enhanced logging import
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)

# ✅ CORRECT - Structured logging
logger.info("User action completed", user_id=user.id, action="login", success=True)

# ✅ CORRECT - Error logging with context
logger.error("Operation failed", operation="user_creation", error=str(e), retry_count=3)
```

## Forbidden Patterns

The linter blocks these patterns:

```python
# ❌ FORBIDDEN - Default logging import
import logging
logger = logging.getLogger(__name__)

# ❌ FORBIDDEN - Deprecated context parameter
logger.info("message", context={"key": "value"})

# ❌ FORBIDDEN - String formatting
logger.info(f"User {user_id} performed {action}")
```

## Integration with Development Workflow

### Pre-commit Integration

- Runs automatically on every commit
- Blocks commits with logging violations
- Provides immediate feedback on violations

### CI/CD Integration

- Can be integrated into CI/CD pipelines
- Ensures consistent logging across the codebase
- Prevents deployment of code with logging violations

### Development Tools

- Works with any text editor or IDE
- Provides real-time feedback during development
- Integrates with existing pre-commit hook infrastructure

## Benefits

### 🚀 **Automated Validation**

- No manual checking required
- Consistent enforcement across all developers
- Immediate feedback on violations

### 🛡️ **Prevents Regressions**

- Blocks commits with deprecated logging patterns
- Ensures all new code uses enhanced logging
- Maintains code quality standards

### 📚 **Educational**

- Clear error messages explain what's wrong
- Provides examples of correct usage
- Helps developers learn proper logging patterns

### 🔧 **Maintainable**

- Centralized validation logic
- Easy to update validation rules
- Consistent with project standards

## Troubleshooting

### Common Issues

#### Pre-commit Hook Not Running

```bash
# Reinstall pre-commit hooks
pre-commit install
```

#### False Positives

If the linter reports false positives, update the validation logic in `scripts/lint_logging_patterns.py`.

#### Performance Issues

The linter excludes virtual environment files and test files to improve performance.

### Getting Help

For issues with the logging pattern linter:

1. Check the error messages for specific violations
2. Refer to `docs/LOGGING_BEST_PRACTICES.md` for correct usage
3. See `docs/examples/logging/` for examples
4. Update the linter script if needed

## Future Enhancements

Potential improvements to the logging pattern linter:

- **Auto-fix capability**: Automatically fix simple violations
- **IDE integration**: Real-time validation in editors
- **Custom rules**: Project-specific validation rules
- **Performance optimization**: Faster validation for large codebases
- **Integration with other tools**: ESLint, Black, etc.

## Documentation References

- **Complete Guide**: [docs/LOGGING_BEST_PRACTICES.md](LOGGING_BEST_PRACTICES.md)
- **Quick Reference**: [docs/LOGGING_QUICK_REFERENCE.md](LOGGING_QUICK_REFERENCE.md)
- **Examples**: [docs/examples/logging/](examples/logging/)
- **Development Guide**: [docs/DEVELOPMENT.md](DEVELOPMENT.md)

The pre-commit logging validation ensures that all future development maintains the high standards of the enhanced logging system while providing immediate feedback to developers.
