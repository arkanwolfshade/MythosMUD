"""
Base Pydantic model classes for MythosMUD schemas.

This module provides base classes with standard security configurations
to ensure consistent validation and security across all schemas.
"""

from pydantic import BaseModel, ConfigDict


class SecureBaseModel(BaseModel):
    """
    Base model with standard security configuration.

    All models that handle user input or API requests should inherit from this
    to ensure consistent security settings across the codebase.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )


class ResponseBaseModel(BaseModel):
    """
    Base model for API response schemas.

    Response models may need additional configuration like from_attributes
    for ORM conversion, while maintaining security settings.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )
