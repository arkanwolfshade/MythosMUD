"""
Quest service: start, progress, complete, turn-in, abandon, and quest log.

Resolves quest by common name; evaluates triggers and DAG prerequisites;
applies rewards (XP, item, spell) via injected services.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Any

from server.models.quest import QuestInstance
from server.schemas.quest import QuestDefinitionSchema
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def _call_add_item_to_inventory(fn: Any, player_id: uuid.UUID, item_id: str, count: int) -> None:
    """Call inventory add_item_to_inventory (fn from getattr). Isolates Any call for type checkers."""
    await fn(player_id, item_id, count)  # fn is Any from getattr; callable at runtime (guarded by callable(add))


def _parse_definition(definition: dict[str, Any]) -> QuestDefinitionSchema:
    """Parse and validate definition JSONB into schema."""
    return QuestDefinitionSchema.model_validate(definition)


def _goals_met(progress: dict[str, Any], definition: QuestDefinitionSchema) -> bool:
    """Return True if all goals are satisfied given current progress."""
    for i, goal in enumerate(definition.goals):
        key = str(i)
        current = progress.get(key, 0)
        if goal.type == "complete_activity":
            if current != 1:
                return False
        elif goal.type == "kill_n":
            required = goal.config.get("count", 1)
            if (current or 0) < required:
                return False
    return True


class QuestService:
    """
    Core quest logic: start by trigger, progress by events, complete/turn-in, abandon.

    Reward application (XP, item, spell) is delegated to optional injected services.
    """

    def __init__(
        self,
        quest_definition_repository: Any,
        quest_instance_repository: Any,
        level_service: Any = None,
        spell_learning_service: Any = None,
        inventory_service: Any = None,
        event_bus: Any = None,
    ) -> None:
        self._def_repo = quest_definition_repository
        self._instance_repo = quest_instance_repository
        self._level_service = level_service
        self._spell_learning_service = spell_learning_service
        self._inventory_service = inventory_service
        self._event_bus = event_bus
        logger.info("QuestService initialized")

    def set_spell_learning_service(self, service: Any) -> None:
        """Set the spell learning service (e.g. when wired after construction by the container)."""
        self._spell_learning_service = service

    async def resolve_name_to_quest_id(self, name: str) -> str | None:
        """Resolve quest common name to quest_id. Returns None if not found."""
        quest_def = await self._def_repo.get_by_name(name)
        return quest_def.id if quest_def else None

    async def _start_quest_validation_error(
        self,
        player_id: uuid.UUID,
        definition: QuestDefinitionSchema,
        existing: QuestInstance | None,
    ) -> dict[str, Any] | None:
        """Return an error dict if the player cannot start this quest; otherwise None."""
        if existing and existing.state == "active":
            return {"success": False, "message": "You already have this quest."}
        if existing and existing.state == "completed":
            return {"success": False, "message": "You have already completed this quest."}
        if not await self._check_prerequisites(player_id, definition):
            return {"success": False, "message": "Prerequisites not met."}
        return None

    async def start_quest(
        self,
        player_id: uuid.UUID,
        quest_id: str,
    ) -> dict[str, Any]:
        """
        Start a quest for the player if prerequisites are met and no active instance.

        Returns dict with success (bool), message (str), and optional error key.
        """
        pid = str(player_id)
        definition_row = await self._def_repo.get_by_id(quest_id)
        if not definition_row:
            return {"success": False, "message": "Quest not found."}
        definition = _parse_definition(dict(definition_row.definition))
        existing = await self._instance_repo.get_by_player_and_quest(player_id, quest_id)
        err = await self._start_quest_validation_error(player_id, definition, existing)
        if err:
            return err
        if existing and existing.state == "abandoned":
            await self._instance_repo.update_state_and_progress(existing.id, state="active", progress={})
            logger.info(
                "Quest re-started (was abandoned)",
                player_id=pid,
                quest_id=quest_id,
                quest_name=definition.name,
            )
            return {"success": True, "message": f"Quest started: {definition.title}"}
        await self._instance_repo.create(player_id, quest_id, state="active", progress={})
        logger.info("Quest started", player_id=pid, quest_id=quest_id, quest_name=definition.name)
        return {"success": True, "message": f"Quest started: {definition.title}"}

    async def _all_required_completed(self, player_id: uuid.UUID, quest_ids: list[str]) -> bool:
        """Return True if the player has completed every quest in quest_ids."""
        for qid in quest_ids:
            inst = await self._instance_repo.get_by_player_and_quest(player_id, qid)
            if not inst or inst.state != "completed":
                return False
        return True

    async def _any_required_completed(self, player_id: uuid.UUID, quest_ids: list[str]) -> bool:
        """Return True if the player has completed at least one quest in quest_ids."""
        for qid in quest_ids:
            inst = await self._instance_repo.get_by_player_and_quest(player_id, qid)
            if inst and inst.state == "completed":
                return True
        return False

    async def _check_prerequisites(self, player_id: uuid.UUID, definition: QuestDefinitionSchema) -> bool:
        """Check DAG: requires_all (all must be completed) and requires_any (at least one)."""
        if not await self._all_required_completed(player_id, definition.requires_all):
            return False
        if definition.requires_any and not await self._any_required_completed(player_id, definition.requires_any):
            return False
        return True

    async def start_quest_by_trigger(
        self,
        player_id: uuid.UUID,
        trigger_type: str,
        entity_id: str,
    ) -> list[dict[str, Any]]:
        """
        Evaluate triggers: for each quest offered by this entity that matches trigger, try to start.

        Returns list of result dicts (one per attempted quest).
        """
        quest_ids = await self._def_repo.list_quest_ids_offered_by(trigger_type, entity_id)
        results = []
        for quest_id in quest_ids:
            definition_row = await self._def_repo.get_by_id(quest_id)
            if not definition_row:
                continue
            definition = _parse_definition(dict(definition_row.definition))
            if not any(t.type == trigger_type and t.entity_id == entity_id for t in definition.triggers):
                continue
            result = await self.start_quest(player_id, quest_id)
            results.append(result)
        return results

    def _progress_goal(
        self,
        progress: dict[str, Any],
        goal_index: int,
        goal_type: str,
        _config: dict[str, Any],
    ) -> dict[str, Any]:
        """Update progress for one goal; return new progress dict."""
        key = str(goal_index)
        if goal_type == "complete_activity":
            return {**progress, key: 1}
        if goal_type == "kill_n":
            current = progress.get(key, 0) or 0
            return {**progress, key: current + 1}
        return progress

    async def _apply_activity_progress(
        self,
        player_id: uuid.UUID,
        instance: QuestInstance,
        definition: QuestDefinitionSchema,
        activity_target: str,
        goal_type: str,
    ) -> bool:
        """Update progress for matching goal; complete if auto_complete and all goals met. Returns True if updated."""
        for i, goal in enumerate(definition.goals):
            if goal.type != goal_type:
                continue
            if goal_type == "kill_n":
                target = goal.target or (goal.config or {}).get("npc_id", "")
            else:
                target = goal.target or ""
            if target != activity_target:
                continue
            new_progress = self._progress_goal(dict(instance.progress), i, goal_type, goal.config or {})
            await self._instance_repo.update_state_and_progress(instance.id, progress=new_progress)
            if _goals_met(new_progress, definition) and definition.auto_complete:
                await self._complete_instance(player_id, instance, definition)
            return True
        return False

    async def record_complete_activity(self, player_id: uuid.UUID, activity_target: str) -> None:
        """Record a complete_activity event; update matching active instances and complete if auto_complete."""
        active = await self._instance_repo.list_active_by_player(player_id)
        for instance in active:
            definition_row = await self._def_repo.get_by_id(instance.quest_id)
            if not definition_row:
                continue
            definition = _parse_definition(dict(definition_row.definition))
            if await self._apply_activity_progress(
                player_id, instance, definition, activity_target, "complete_activity"
            ):
                break

    async def record_kill(self, player_id: uuid.UUID, npc_definition_id: str) -> None:
        """Record a kill for kill_n goals; update matching active instances and complete if auto_complete."""
        active = await self._instance_repo.list_active_by_player(player_id)
        for instance in active:
            definition_row = await self._def_repo.get_by_id(instance.quest_id)
            if not definition_row:
                continue
            definition = _parse_definition(dict(definition_row.definition))
            if await self._apply_activity_progress(player_id, instance, definition, npc_definition_id, "kill_n"):
                break

    async def _complete_instance(
        self,
        player_id: uuid.UUID,
        instance: QuestInstance,
        definition: QuestDefinitionSchema,
    ) -> None:
        """Apply rewards and set instance to completed."""
        await self._apply_rewards(player_id, instance.quest_id, definition)
        now = datetime.now(UTC)
        await self._instance_repo.update_state_and_progress(
            instance.id,
            state="completed",
            completed_at=now,
        )
        logger.info(
            "Quest completed",
            player_id=str(player_id),
            quest_id=instance.quest_id,
            quest_name=definition.name,
        )
        if self._event_bus:
            from server.events.event_types import QuestCompleted

            self._event_bus.publish(QuestCompleted(player_id=str(player_id), quest_id=instance.quest_id))

    async def _apply_xp_reward(self, player_id: uuid.UUID, quest_id: str, reward: Any) -> None:
        """Apply a single XP reward. No-op if no level service or zero amount."""
        amount = reward.config.get("amount", 0)
        if not amount or not self._level_service:
            return
        try:
            await self._level_service.grant_xp(player_id, amount)
        except Exception as e:  # pylint: disable=broad-except  # Reason: XP reward must not crash quest completion; log and continue
            logger.warning(
                "Failed to grant quest XP",
                player_id=str(player_id),
                quest_id=quest_id,
                amount=amount,
                error=str(e),
            )

    async def _apply_spell_reward(self, player_id: uuid.UUID, quest_id: str, reward: Any) -> None:
        """Apply a single spell reward. No-op if no spell_learning_service or no spell_id."""
        spell_id = reward.config.get("spell_id") or reward.config.get("spell")
        if not spell_id or not self._spell_learning_service:
            return
        try:
            await self._spell_learning_service.learn_spell_from_quest(player_id, quest_id, spell_id)
        except Exception as e:  # pylint: disable=broad-except  # Reason: Spell reward must not crash quest completion; log and continue
            logger.warning(
                "Failed to grant quest spell",
                player_id=str(player_id),
                quest_id=quest_id,
                spell_id=spell_id,
                error=str(e),
            )

    async def _apply_item_reward(self, player_id: uuid.UUID, quest_id: str, reward: Any) -> None:
        """Apply a single item reward. Skips if inventory full (per plan)."""
        if not self._inventory_service:
            return
        has_slot = getattr(self._inventory_service, "has_inventory_slot", lambda _: True)(player_id)
        if not has_slot:
            logger.warning(
                "Quest item reward skipped: inventory full",
                player_id=str(player_id),
                quest_id=quest_id,
            )
            return
        item_id = reward.config.get("item_id") or reward.config.get("item")
        if not item_id:
            return
        try:
            add = getattr(self._inventory_service, "add_item_to_inventory", None)
            if callable(add):
                await _call_add_item_to_inventory(add, player_id, item_id, 1)
        except Exception as e:  # pylint: disable=broad-except  # Reason: Item reward must not crash quest completion; log and continue
            logger.warning(
                "Failed to grant quest item",
                player_id=str(player_id),
                quest_id=quest_id,
                item_id=item_id,
                error=str(e),
            )

    async def _apply_rewards(
        self,
        player_id: uuid.UUID,
        quest_id: str,
        definition: QuestDefinitionSchema,
    ) -> None:
        """Apply XP, item, and spell rewards. Block item if inventory full (per plan)."""
        for reward in definition.rewards:
            if reward.type == "xp":
                await self._apply_xp_reward(player_id, quest_id, reward)
            elif reward.type == "spell":
                await self._apply_spell_reward(player_id, quest_id, reward)
            elif reward.type == "item":
                await self._apply_item_reward(player_id, quest_id, reward)

    def _turn_in_validation_error(
        self,
        player_id: uuid.UUID,
        definition: QuestDefinitionSchema,
        instance: QuestInstance | None,
        at_entity_id: str,
    ) -> dict[str, Any] | None:
        """Return an error dict if turn-in is invalid; otherwise None."""
        if definition.auto_complete:
            return {"success": False, "message": "This quest completes automatically."}
        allowed_ids = list(definition.turn_in_entities or [])
        if not allowed_ids:
            return {"success": False, "message": "This quest has no turn-in location."}
        if at_entity_id not in allowed_ids:
            return {"success": False, "message": "You cannot turn in this quest here."}
        if not instance or instance.state != "active":
            return {"success": False, "message": "You do not have this quest active."}
        if not _goals_met(dict(instance.progress), definition):
            return {"success": False, "message": "Quest objectives not yet complete."}
        for reward in definition.rewards:
            if reward.type == "item" and self._inventory_service:
                has_slot = getattr(self._inventory_service, "has_inventory_slot", lambda _: True)(player_id)
                if not has_slot:
                    return {
                        "success": False,
                        "message": "Your inventory is full. Free a slot before turning in.",
                    }
        return None

    async def turn_in(
        self,
        player_id: uuid.UUID,
        quest_id: str,
        _at_entity_type: str,
        at_entity_id: str,
    ) -> dict[str, Any]:
        """
        Turn in a quest at an entity (when auto_complete is false).
        Validates turn_in_entities and inventory slot for item rewards; then applies rewards.
        """
        definition_row = await self._def_repo.get_by_id(quest_id)
        if not definition_row:
            return {"success": False, "message": "Quest not found."}
        definition = _parse_definition(dict(definition_row.definition))
        instance = await self._instance_repo.get_by_player_and_quest(player_id, quest_id)
        err = self._turn_in_validation_error(player_id, definition, instance, at_entity_id)
        if err:
            return err
        assert instance is not None  # Validation guarantees active instance when err is None
        await self._complete_instance(player_id, instance, definition)
        return {"success": True, "message": f"Quest completed: {definition.title}"}

    async def abandon(self, player_id: uuid.UUID, quest_name: str) -> dict[str, Any]:
        """Abandon an active quest by common name. No rewards."""
        quest_id = await self.resolve_name_to_quest_id(quest_name)
        if not quest_id:
            return {"success": False, "message": f"Unknown quest: {quest_name}."}
        instance = await self._instance_repo.get_by_player_and_quest(player_id, quest_id)
        if not instance:
            return {"success": False, "message": "You do not have this quest."}
        if instance.state != "active":
            return {"success": False, "message": "You can only abandon an active quest."}
        await self._instance_repo.update_state_and_progress(instance.id, state="abandoned")
        logger.info(
            "Quest abandoned",
            player_id=str(player_id),
            quest_id=quest_id,
            quest_name=quest_name,
        )
        return {"success": True, "message": "Quest abandoned."}

    async def get_quest_log(self, player_id: uuid.UUID, include_completed: bool = True) -> list[dict[str, Any]]:
        """Return quest log entries (active and optionally completed) for API/command."""
        active = await self._instance_repo.list_active_by_player(player_id)
        completed = await self._instance_repo.list_completed_by_player(player_id) if include_completed else []
        entries = []
        for instance in active + completed:
            definition_row = await self._def_repo.get_by_id(instance.quest_id)
            if not definition_row:
                continue
            definition = _parse_definition(dict(definition_row.definition))
            goals_with_progress = []
            for i, goal in enumerate(definition.goals):
                key = str(i)
                current = (instance.progress or {}).get(key, 0)
                required = 1 if goal.type == "complete_activity" else goal.config.get("count", 1)
                goals_with_progress.append(
                    {
                        "goal_type": goal.type,
                        "target": goal.target,
                        "current": current,
                        "required": required,
                        "done": current >= required if goal.type == "kill_n" else (current == 1),
                    }
                )
            entries.append(
                {
                    "quest_id": instance.quest_id,
                    "name": definition.name,
                    "title": definition.title,
                    "description": definition.description,
                    "goals_with_progress": goals_with_progress,
                    "state": instance.state,
                }
            )
        return entries
