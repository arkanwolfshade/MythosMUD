"""
Shared container limits.

Kept import-free so models, schemas, and item metadata can all use it without import cycles.
"""

# Global ceiling on any container's capacity; each container's real size comes from its prototype.
# Mirrored by containers_capacity_slots_check in db/schema.sql and db/migrations.
MAX_CONTAINER_CAPACITY_SLOTS: int = 200
