"""Component hook coordination for freshly minted item instances."""

from __future__ import annotations

from typing import Any

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def initialize_components(
    prototype: Any,
    overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Prepare component state metadata for a new item instance.

    This routine currently records the component identifiers declared on the prototype
    so downstream systems can attach rich behaviour in later phases. It also merges any
    override payloads supplied by administrative tooling.
    """

    overrides = overrides or {}
    prototype_components = list(getattr(prototype, "effect_components", []))

    metadata: dict[str, Any] = {}
    if prototype_components:
        metadata["components"] = prototype_components

    if overrides_metadata := overrides.get("metadata"):
        metadata.setdefault("overrides", {})["metadata"] = overrides_metadata

    if overrides_components := overrides.get("effect_components"):
        metadata.setdefault("overrides", {})["effect_components"] = overrides_components

    if metadata:
        logger.debug(
            "Initialized item components",
            prototype_id=getattr(prototype, "prototype_id", "unknown"),
            components=metadata.get("components", []),
            overrides=list(metadata.get("overrides", {}).keys()),
        )

    return metadata
