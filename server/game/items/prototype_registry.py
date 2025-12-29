from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path

from pydantic import ValidationError

from server.game.items.models import ItemPrototypeModel
from server.monitoring.monitoring_dashboard import get_monitoring_dashboard
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PrototypeRegistryError(Exception):
    """Raised when prototype registry lookups fail."""


class PrototypeRegistry:
    """In-memory registry for validated item prototypes."""

    def __init__(self, prototypes: dict[str, ItemPrototypeModel], invalid_entries: list[dict]):
        self._prototypes = prototypes
        self._invalid_entries = invalid_entries

    @classmethod
    def load_from_path(cls, directory: Path | str) -> PrototypeRegistry:
        directory_path = Path(directory)
        dashboard = get_monitoring_dashboard()
        if not directory_path.exists():
            dashboard.record_registry_failure(
                source="prototype_registry",
                error="directory_missing",
                metadata={"path": str(directory_path)},
            )
            raise PrototypeRegistryError(f"Prototype directory not found: {directory_path}")

        prototypes: dict[str, ItemPrototypeModel] = {}
        invalid_entries: list[dict] = []

        for json_file in sorted(directory_path.glob("*.json")):
            try:
                payload = json.loads(json_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                logger.warning(
                    "invalid prototype payload",
                    prototype_id=json_file.stem,
                    file_path=str(json_file),
                    error=str(exc),
                )
                dashboard.record_registry_failure(
                    source="prototype_registry",
                    error="json_decode_error",
                    metadata={"file_path": str(json_file), "error": str(exc)},
                )
                continue

            try:
                prototype = ItemPrototypeModel.model_validate(payload)
            except ValidationError as exc:
                logger.warning(
                    "invalid prototype payload",
                    prototype_id=payload.get("prototype_id") or json_file.stem,
                    file_path=str(json_file),
                    errors=exc.errors(),
                )
                invalid_entries.append(
                    {
                        "prototype_id": payload.get("prototype_id") or json_file.stem,
                        "file_path": str(json_file),
                        "errors": exc.errors(),
                    }
                )
                dashboard.record_registry_failure(
                    source="prototype_registry",
                    error="validation_error",
                    metadata={
                        "prototype_id": payload.get("prototype_id") or json_file.stem,
                        "file_path": str(json_file),
                    },
                )
                continue

            effect_components = list(getattr(prototype, "effect_components", []))
            if "component.durability" in effect_components and getattr(prototype, "durability", None) is None:
                dashboard.record_durability_anomaly(
                    prototype_id=prototype.prototype_id,
                    durability=None,
                    reason="missing_durability_value",
                    metadata={"file_path": str(json_file)},
                )

            prototypes[prototype.prototype_id] = prototype

        return cls(prototypes, invalid_entries)

    def get(self, prototype_id: str) -> ItemPrototypeModel:
        try:
            return self._prototypes[prototype_id]
        except KeyError as exc:
            raise PrototypeRegistryError(f"Prototype not found: {prototype_id}") from exc

    def find_by_tag(self, tag: str) -> list[ItemPrototypeModel]:
        return [prototype for prototype in self._prototypes.values() if tag in prototype.tags]

    def all(self) -> Iterable[ItemPrototypeModel]:
        return self._prototypes.values()

    def invalid_entries(self) -> list[dict]:
        return list(self._invalid_entries)
