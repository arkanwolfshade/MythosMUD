"""
Base Pydantic model classes for MythosMUD schemas.

This module provides base classes with standard security configurations
to ensure consistent validation and security across all schemas.
"""

from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class SecureBaseModel(BaseModel):
    """
    Base model with standard security configuration.

    Every schema bound to a FastAPI request body must inherit from this — it is
    mechanically enforced by server/tests/integration/test_request_schema_security.py,
    which walks the app's route table and asserts every reachable body model is a
    subclass of this class. Response/internal models are not required to inherit it;
    extra="forbid" is an inbound control (rejecting fields an attacker adds), not an
    outbound one, so applying it to response construction buys nothing and risks
    breaking legitimate extra-field construction.

    A model that needs additional configuration (e.g. from_attributes for ORM
    conversion) declares it in its own model_config — Pydantic v2 merges base and
    subclass config, so the security settings below still apply.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )
