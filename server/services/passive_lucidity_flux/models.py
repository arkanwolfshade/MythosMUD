"""Data models for passive lucidity flux."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CachedRoom:
    """Cached room entry with timestamp for TTL management."""

    room: Any
    timestamp: float


@dataclass(frozen=True)
class PassiveFluxContext:
    """Resolved environmental context for passive flux evaluation."""

    base_flux: float
    tags: frozenset[str] = field(default_factory=frozenset)
    source: str = "unspecified"
    metadata: dict[str, Any] = field(default_factory=dict)
