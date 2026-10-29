"""
What code that hands out items needs from the item granter (ADR-029 step 4c-i).

Kept import-free: the app container names this type, and the granter itself reaches the item factory and the
monitoring and realtime modules, which import the container. ItemGranter (item_grant.py) implements it.
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import Protocol


class ItemGiver(Protocol):
    """Creates items in players' inventories, committed before it returns."""

    async def has_free_slot(self, player_id: uuid.UUID) -> bool:
        """True if the player could take one more stack (False for no such player)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return

    async def grant(
        self, player_id: uuid.UUID, prototype_id: str, quantity: int = 1, *, origin: Mapping[str, object]
    ) -> None:
        """Add ``quantity`` of a new ``prototype_id`` item to the player's carried stacks, committed."""
