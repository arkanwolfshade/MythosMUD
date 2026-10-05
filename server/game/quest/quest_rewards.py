"""
Quest reward application for QuestService.

Split out of quest_service.py (file size). QuestService inherits these methods; it provides the
reward services through its constructor. Every reward is best-effort: a failing reward is logged
and never blocks quest completion.
"""

# pyright: reportUninitializedInstanceVariable=false
# Reason: mixin; QuestService.__init__ sets the service attributes declared below.

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable
from typing import Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.player import Player
from server.schemas.quest import QuestDefinitionSchema, QuestRewardSchema
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class XpGranter(Protocol):  # pylint: disable=too-few-public-methods  # Reason: single-method structural type
    """LevelService surface used by XP rewards."""

    async def grant_xp(self, player_id: uuid.UUID, amount: int) -> object:
        """Grant experience to a player."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return


class SpellLearner(Protocol):  # pylint: disable=too-few-public-methods  # Reason: single-method structural type
    """SpellLearningService surface used by spell rewards."""

    async def learn_spell_from_quest(self, player_id: uuid.UUID, quest_id: str, spell_id: str) -> object:
        """Teach a spell granted by a quest."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return


class PlayerStore(Protocol):
    """AsyncPersistenceLayer surface used by the respawn_room reward."""

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Load a player."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return

    async def save_player(self, player: Player) -> None:
        """Persist a player."""


def _config_value(reward: QuestRewardSchema, *keys: str) -> object:
    """First truthy config value among keys (reward config is untyped JSONB)."""
    for key in keys:
        value = cast(object, reward.config.get(key))
        if value:
            return value
    return None


def _inventory_has_slot(inventory_service: object, player_id: uuid.UUID) -> bool:
    """True unless the inventory service says the player's inventory is full."""
    checker = cast(Callable[[uuid.UUID], object] | None, getattr(inventory_service, "has_inventory_slot", None))
    return True if checker is None else bool(checker(player_id))


class QuestRewardsMixin:
    """Applies a completed quest's rewards; the host (QuestService) provides the services."""

    _level_service: XpGranter | None
    _spell_learning_service: SpellLearner | None
    _inventory_service: object | None
    _async_persistence: object | None

    async def _apply_xp_reward(self, player_id: uuid.UUID, quest_id: str, reward: QuestRewardSchema) -> None:
        """Apply a single XP reward. No-op if no level service or zero amount."""
        amount = _config_value(reward, "amount")
        if not isinstance(amount, int) or not self._level_service:
            return
        try:
            _ = await self._level_service.grant_xp(player_id, amount)
        except Exception as e:  # pylint: disable=broad-except  # Reason: XP reward must not crash quest completion; log and continue
            logger.warning(
                "Failed to grant quest XP", player_id=str(player_id), quest_id=quest_id, amount=amount, error=str(e)
            )

    async def _apply_spell_reward(self, player_id: uuid.UUID, quest_id: str, reward: QuestRewardSchema) -> None:
        """Apply a single spell reward. No-op if no spell_learning_service or no spell_id."""
        spell_id = _config_value(reward, "spell_id", "spell")
        if not isinstance(spell_id, str) or not self._spell_learning_service:
            return
        try:
            _ = await self._spell_learning_service.learn_spell_from_quest(player_id, quest_id, spell_id)
        except Exception as e:  # pylint: disable=broad-except  # Reason: Spell reward must not crash quest completion; log and continue
            logger.warning(
                "Failed to grant quest spell",
                player_id=str(player_id),
                quest_id=quest_id,
                spell_id=spell_id,
                error=str(e),
            )

    async def _apply_item_reward(self, player_id: uuid.UUID, quest_id: str, reward: QuestRewardSchema) -> None:
        """Apply a single item reward. Skips if inventory full (per plan)."""
        if not self._inventory_service:
            return
        if not _inventory_has_slot(self._inventory_service, player_id):
            logger.warning("Quest item reward skipped: inventory full", player_id=str(player_id), quest_id=quest_id)
            return
        item_id = _config_value(reward, "item_id", "item")
        if not isinstance(item_id, str):
            return
        add = cast(
            Callable[[uuid.UUID, str, int], Awaitable[object]] | None,
            getattr(self._inventory_service, "add_item_to_inventory", None),
        )
        if add is None:
            return
        try:
            _ = await add(player_id, item_id, 1)
        except Exception as e:  # pylint: disable=broad-except  # Reason: Item reward must not crash quest completion; log and continue
            logger.warning(
                "Failed to grant quest item", player_id=str(player_id), quest_id=quest_id, item_id=item_id, error=str(e)
            )

    async def _apply_respawn_room_reward(self, player_id: uuid.UUID, quest_id: str, reward: QuestRewardSchema) -> None:
        """Point the player's respawn at config.room_id (leaving the tutorial -> Sanitarium Main Foyer)."""
        room_id = _config_value(reward, "room_id")
        if not isinstance(room_id, str):
            logger.warning("respawn_room reward without config.room_id", quest_id=quest_id)
            return
        store = cast("PlayerStore | None", self._async_persistence)
        if store is None:
            return
        try:
            player = await store.get_player_by_id(player_id)
            if player is None:
                return
            player.respawn_room_id = room_id
            await store.save_player(player)
        except (DatabaseError, SQLAlchemyError) as e:
            logger.warning(
                "Failed to apply respawn_room quest reward",
                player_id=str(player_id),
                quest_id=quest_id,
                room_id=room_id,
                error=str(e),
            )

    async def _apply_rewards(self, player_id: uuid.UUID, quest_id: str, definition: QuestDefinitionSchema) -> None:
        """Apply XP, item, spell, and respawn_room rewards. Block item if inventory full (per plan)."""
        for reward in definition.rewards:
            if reward.type == "xp":
                await self._apply_xp_reward(player_id, quest_id, reward)
            elif reward.type == "spell":
                await self._apply_spell_reward(player_id, quest_id, reward)
            elif reward.type == "item":
                await self._apply_item_reward(player_id, quest_id, reward)
            elif reward.type == "respawn_room":
                await self._apply_respawn_room_reward(player_id, quest_id, reward)

    def _turn_in_inventory_full_error(
        self, player_id: uuid.UUID, definition: QuestDefinitionSchema
    ) -> dict[str, object] | None:
        """Return inventory-full error when an item reward needs a free slot."""
        if not self._inventory_service:
            return None
        needs_slot = any(reward.type == "item" for reward in definition.rewards)
        if needs_slot and not _inventory_has_slot(self._inventory_service, player_id):
            return {"success": False, "message": "Your inventory is full. Free a slot before turning in."}
        return None
