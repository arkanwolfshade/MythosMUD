# Enhanced Logging Examples

This directory contains comprehensive examples of how to use the enhanced logging system in MythosMUD.

## Files Overview

### `correct_patterns.py`
Demonstrates the **CORRECT** way to use the enhanced logging system. This file shows:
- Proper import statements
- Structured logging with key-value pairs
- Error logging with rich context
- Performance logging with context managers
- Request context binding
- Security logging with automatic sanitization
- Async logging patterns
- Exception tracking
- Database operation logging
- API request/response logging
- WebSocket logging
- Batch processing logging

### `deprecated_patterns.py`
Demonstrates **DEPRECATED** patterns that should **NEVER** be used. This file shows:
- Forbidden import statements (`import logging`)
- String formatting in logs
- Deprecated context parameters
- Unstructured messages
- Logging sensitive data
- Wrong log levels
- Missing context in logs
- Logging in tight loops
- Blocking operations in async context

### `migration_examples.py`
Shows **before/after** examples of migrating from default logging to enhanced logging:
- Import statement migration
- Context parameter migration
- String formatting to structured logging
- Error logging enhancement
- Performance logging addition
- Request context binding
- Security logging improvement
- Database logging enhancement
- API logging improvement
- WebSocket logging enhancement
- Batch processing logging
- Exception tracking addition
- Async logging improvement
- Log level correction
- Complete function migration

### `fastapi_integration.py`
Demonstrates how to integrate enhanced logging with **FastAPI** applications:
- Request context middleware
- API request/response logging middleware
- Route handler logging
- Authentication logging
- Exception handlers
- WebSocket endpoints
- Background tasks
- Database operations
- File uploads
- Dependency injection

### `websocket_integration.py`
Demonstrates how to integrate enhanced logging with **WebSocket** connections:
- Connection management
- Message handling
- Authentication
- Rate limiting
- Message validation
- Error handling
- Heartbeat management
- Broadcasting
- Performance monitoring

### `testing_examples.py`
Demonstrates how to **test** logging behavior in unit tests and integration tests:
- Basic logging tests
- Error logging tests
- Context binding tests
- Performance logging tests
- Exception tracking tests
- API request logging tests
- WebSocket logging tests
- Security sanitization tests
- Async logging tests
- Database logging tests
- Batch logging tests
- Error handling tests
- Performance metrics tests
- Correlation ID tests
- FastAPI endpoint tests
- Middleware tests

## Usage Guidelines

### For Developers
1. **Always** refer to `correct_patterns.py` for proper logging implementation
2. **Never** use patterns shown in `deprecated_patterns.py`
3. Use `migration_examples.py` when updating existing code
4. Follow `fastapi_integration.py` for FastAPI applications
5. Follow `websocket_integration.py` for WebSocket applications
6. Use `testing_examples.py` for writing tests

### For Code Reviews
1. Check that imports use enhanced logging
2. Verify structured logging with key-value pairs
3. Ensure no string formatting in log messages
4. Confirm appropriate log levels are used
5. Check that error logs include sufficient context
6. Verify no sensitive data is logged
7. Ensure proper context binding for requests

### For AI Agents
1. Follow the patterns in `correct_patterns.py`
2. Avoid all patterns in `deprecated_patterns.py`
3. Use the migration examples when updating existing code
4. Follow the integration examples for specific frameworks
5. Use the testing examples when writing tests

## Key Principles

### ✅ DO
- Use `from server.logging.enhanced_logging_config import get_logger`
- Use structured logging with key-value pairs
- Include rich context in error logs
- Use appropriate log levels
- Bind request context for correlation
- Use performance logging for operations
- Track exceptions with context
- Test logging behavior

### ❌ DON'T
- Use `import logging` or `logging.getLogger()`
- Use string formatting in log messages
- Use deprecated `context={"key": "value"}` parameters
- Log sensitive data
- Use wrong log levels
- Ignore context in logs
- Log in tight loops
- Use blocking operations in async context

## Documentation References

- **Complete Guide**: [docs/LOGGING_BEST_PRACTICES.md](../../LOGGING_BEST_PRACTICES.md)
- **Quick Reference**: [docs/LOGGING_QUICK_REFERENCE.md](../../LOGGING_QUICK_REFERENCE.md)
- **Development Guide**: [docs/DEVELOPMENT.md](../../DEVELOPMENT.md)
- **AI Agent Guide**: [docs/DEVELOPMENT_AI.md](../../DEVELOPMENT_AI.md)

## Examples Usage

To use these examples in your code:

1. **Copy the relevant patterns** from `correct_patterns.py`
2. **Adapt them to your specific use case**
3. **Follow the testing patterns** from `testing_examples.py`
4. **Use the migration examples** when updating existing code

Remember: These examples are for reference only. Always adapt them to your specific requirements and follow the enhanced logging system guidelines.
