"""
Structured logging package for MythosMUD.

This package provides enhanced logging functionality including structured logging,
performance monitoring, and security-aware log handling.

All imports should use explicit paths like 'from server.structured_logging.enhanced_logging_config import get_logger'.

The directory was renamed from 'logging' to 'structured_logging' to avoid namespace conflicts
with Python's standard library logging module when using pytest-xdist parallel execution.
"""

# This is a namespace package that does NOT interfere with standard library 'logging' imports.
__all__ = []
