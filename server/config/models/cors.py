"""
CORS (Cross-Origin Resource Sharing) configuration model.
"""

import json
from typing import Any

from pydantic import AliasChoices, Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CORSConfig(BaseSettings):
    """
    Cross-origin resource sharing configuration.

    Configuration precedence (highest to lowest):
    1. Environment variables (CORS_* prefix, e.g., CORS_ALLOW_ORIGINS)
    2. Legacy environment variables (ALLOWED_ORIGINS, ALLOWED_METHODS, etc.)
    3. Field defaults

    Wildcard origins ("*") are allowed but logged as warnings in production.
    """

    allow_origins: list[str] = Field(
        default_factory=lambda: ["http://localhost:5173", "http://127.0.0.1:5173"],
        validation_alias=AliasChoices(
            "CORS_ALLOW_ORIGINS",
            "CORS_ORIGINS",
            "CORS_ALLOWED_ORIGINS",
            "ALLOWED_ORIGINS",
            "allow_origins",
            "origins",
            "allowed_origins",
        ),
        description="Origins permitted to access the MythosMUD API",
    )
    allow_credentials: bool = Field(
        default=True,
        validation_alias=AliasChoices("CORS_ALLOW_CREDENTIALS", "allow_credentials", "credentials"),
        description="Whether credentialed requests are accepted",
    )
    allow_methods: list[str] = Field(
        default_factory=lambda: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        validation_alias=AliasChoices("CORS_ALLOW_METHODS", "ALLOWED_METHODS", "allow_methods", "methods"),
        description="HTTP methods permitted by CORS responses",
    )
    allow_headers: list[str] = Field(
        default_factory=lambda: [
            "Content-Type",
            "Authorization",
            "X-Requested-With",
            "Accept",
            "Accept-Language",
        ],
        validation_alias=AliasChoices("CORS_ALLOW_HEADERS", "ALLOWED_HEADERS", "allow_headers", "headers"),
        description="Request headers permitted by CORS responses",
    )
    expose_headers: list[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices("CORS_EXPOSE_HEADERS", "expose_headers"),
        description="Response headers exposed to browser clients",
    )
    max_age: int = Field(
        default=600,
        validation_alias=AliasChoices("CORS_MAX_AGE", "max_age"),
        description="Seconds browsers may cache CORS preflight responses",
    )

    model_config = SettingsConfigDict(env_prefix="CORS_", case_sensitive=False, extra="ignore")

    @model_validator(mode="after")
    def _validate_and_warn_wildcards(self) -> "CORSConfig":
        """Validate CORS configuration and warn about wildcard origins."""
        if "*" in self.allow_origins:
            logger.warning(
                "Wildcard origin (*) detected in CORS configuration. "
                "This allows requests from any origin and should only be used in development.",
                allow_origins=self.allow_origins,
            )
        return self

    @staticmethod
    def _validate_non_empty(cleaned: list[str], allow_empty: bool) -> None:
        """Validate that cleaned list is not empty if allow_empty is False."""
        if not cleaned and not allow_empty:
            raise ValueError("At least one entry must be provided")

    @staticmethod
    def _clean_list_items(items: list[Any]) -> list[str]:
        """Clean and filter list items, removing empty strings."""
        return [str(item).strip() for item in items if str(item).strip()]

    @staticmethod
    def _parse_json_array(candidate: str, allow_empty: bool) -> list[str] | None:
        """Parse JSON array string if it looks like one, otherwise return None."""
        if not (candidate.startswith("[") and candidate.endswith("]")):
            return None
        try:
            loaded = json.loads(candidate)
            if isinstance(loaded, list):
                cleaned = CORSConfig._clean_list_items(loaded)
                CORSConfig._validate_non_empty(cleaned, allow_empty)
                return cleaned
        except json.JSONDecodeError:
            pass
        return None

    @staticmethod
    def _parse_comma_separated(candidate: str, allow_empty: bool) -> list[str]:
        """Parse comma-separated string into cleaned list."""
        items = [item.strip() for item in candidate.split(",") if item.strip()]
        CORSConfig._validate_non_empty(items, allow_empty)
        return items

    @staticmethod
    def _parse_csv(value: object, allow_empty: bool) -> list[str]:
        """Parse comma separated strings or lists into a cleaned list of strings."""
        if value is None:
            if allow_empty:
                return []
            raise ValueError("At least one entry must be provided")
        if isinstance(value, list):
            cleaned = CORSConfig._clean_list_items(value)
            CORSConfig._validate_non_empty(cleaned, allow_empty)
            return cleaned
        if isinstance(value, str):
            candidate = value.strip()
            json_result = CORSConfig._parse_json_array(candidate, allow_empty)
            if json_result is not None:
                return json_result
            return CORSConfig._parse_comma_separated(candidate, allow_empty)
        raise ValueError("Value must be a list of strings or a comma-separated string")

    @field_validator("allow_origins", mode="before")
    @classmethod
    def parse_allow_origins(cls, value: object) -> list[str]:
        """Parse allowed origins from various input formats."""
        return cls._parse_csv(value, allow_empty=False)

    @field_validator("allow_methods", mode="before")
    @classmethod
    def parse_allow_methods(cls, value: object) -> list[str]:
        """Parse and validate CORS allowed methods. Converts all methods to uppercase."""
        methods = cls._parse_csv(value, allow_empty=False)
        return [method.upper() for method in methods]

    @field_validator("allow_headers", mode="before")
    @classmethod
    def parse_allow_headers(cls, value: object) -> list[str]:
        """Parse and validate CORS allowed headers."""
        return cls._parse_csv(value, allow_empty=False)

    @field_validator("max_age", mode="before")
    @classmethod
    def parse_max_age(cls, value: object) -> int:
        """Parse and validate CORS max age value. Returns default 600 if invalid."""
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        return 600

    @field_validator("expose_headers", mode="before")
    @classmethod
    def parse_expose_headers(cls, value: object) -> list[str]:
        """Parse and validate CORS exposed headers. Allows empty list."""
        return cls._parse_csv(value, allow_empty=True)

    @field_validator("max_age")
    @classmethod
    def validate_max_age(cls, value: int) -> int:
        """Validate that max_age is non-negative."""
        if value < 0:
            raise ValueError("max_age must be non-negative")
        return value
