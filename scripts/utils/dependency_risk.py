"""
Shared dependency risk tiers and semver helpers for MythosMUD tooling.

Used by dependency_analyzer.py and manual_dependency_analysis.py so package lists stay in sync.
"""

from __future__ import annotations

from packaging import version

# NPM: high / medium sensitivity for minor bumps (see assess_npm_risk).
NPM_HIGH_RISK_PACKAGES: tuple[str, ...] = (
    "react",
    "react-dom",
    "typescript",
    "vite",
    "eslint",
    "@types/react",
    "@types/react-dom",
    "tailwindcss",
)

NPM_MEDIUM_RISK_PACKAGES: tuple[str, ...] = (
    "@playwright/test",
    "@testing-library/react",
    "prettier",
    "typescript-eslint",
    "@vitejs/plugin-react",
)

# Python: high / medium sensitivity for minor bumps (see assess_python_risk).
PYTHON_HIGH_RISK_PACKAGES: tuple[str, ...] = (
    "fastapi",
    "pydantic",
    "sqlalchemy",
    "uvicorn",
    "pytest",
    "pytest-asyncio",
    "structlog",
)

PYTHON_MEDIUM_RISK_PACKAGES: tuple[str, ...] = (
    "httpx",
    "argon2-cffi",
    "fastapi-users",
    "click",
    "nats-py",
)


def categorize_update(current_ver: str, latest_ver: str) -> str:
    """Categorize update by semver (major / minor / patch / none / unknown)."""
    try:
        current = version.parse(current_ver)
        latest = version.parse(latest_ver)

        if latest.major > current.major:
            return "major"
        if latest.minor > current.minor:
            return "minor"
        if latest.micro > current.micro:
            return "patch"
        return "none"
    except Exception:
        return "unknown"


def assess_npm_risk(package_name: str, current: str, latest: str) -> str:
    """Assess risk level for NPM package updates."""
    update_type = categorize_update(current, latest)

    if update_type == "major":
        return "HIGH"
    if update_type == "minor" and package_name in NPM_HIGH_RISK_PACKAGES:
        return "MEDIUM"
    if update_type == "minor" and package_name in NPM_MEDIUM_RISK_PACKAGES:
        return "LOW"
    if update_type == "patch":
        return "LOW"
    return "LOW"


def assess_python_risk(package_name: str, current: str, latest: str) -> str:
    """Assess risk level for Python package updates."""
    update_type = categorize_update(current, latest)

    if update_type == "major":
        return "HIGH"
    if update_type == "minor" and package_name in PYTHON_HIGH_RISK_PACKAGES:
        return "MEDIUM"
    if update_type == "minor" and package_name in PYTHON_MEDIUM_RISK_PACKAGES:
        return "LOW"
    if update_type == "patch":
        return "LOW"
    return "LOW"
