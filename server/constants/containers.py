"""
Shared container limits.

Kept import-free so models, schemas, and item metadata can all use it without import cycles.
"""

# Global ceiling on any container's capacity; each container's real size comes from its prototype.
# Mirrored by containers_capacity_slots_check in db/schema.sql and db/migrations.
MAX_CONTAINER_CAPACITY_SLOTS: int = 200

# containers.source_type of a player's bank deposit box (see server/services/bank_service.py).
BANK_SOURCE_TYPE: str = "bank"

# Valid containers.source_type values. Mirrors ContainerSourceType (server/models/container.py, kept in
# step by a unit test) and containers_source_type_check in db/schema.sql and db/migrations.
CONTAINER_SOURCE_TYPES: tuple[str, ...] = ("environment", "equipment", "corpse", BANK_SOURCE_TYPE)
