# pylint: disable=pointless-string-statement,missing-module-docstring  # Reason: Module docstring must come after from __future__ imports per Python spec, but Pylint incorrectly flags it

from __future__ import annotations

"""
Magic command handlers for spellcasting.

This module implements the /cast, /spells, and /spell commands.
"""

# pylint: disable=too-many-arguments  # Reason: Magic commands require many parameters for spell context and validation
# pylint: disable=wrong-import-position  # Reason: Imports must come after from __future__ and docstring per Python spec
# ruff: noqa: E402, I001  # Reason: from __future__ imports must come before module docstring per Python spec, so imports come after docstring

import uuid  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec
from typing import TYPE_CHECKING, Any  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec

from server.alias_storage import AliasStorage  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec
from server.commands.rest_command import _cancel_rest_countdown, is_player_resting  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec
from server.game.magic.spell_registry import SpellRegistry  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec
from server.structured_logging.enhanced_logging_config import get_logger  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Import must come after from __future__ and docstring per Python spec

if TYPE_CHECKING:
    from server.game.chat_service import ChatService
    from server.game.magic.magic_service import MagicService
    from server.game.magic.spell_learning_service import SpellLearningService

logger = get_logger(__name__)


class SpellCommandError(Exception):
    """Internal error type for control flow in /spell command handling."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class MagicCommandHandler:
    """
    Handler for magic-related commands.

    Processes /cast, /spells, and /spell commands.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Magic command handler initialization requires many service dependencies
        self,
        magic_service: MagicService,
        spell_registry: SpellRegistry,
        player_spell_repository: PlayerSpellRepository | None = None,
        spell_learning_service: SpellLearningService | None = None,
        chat_service: ChatService | None = None,
    ) -> None:
        """
        Initialize the magic command handler.

        Args:
            magic_service: Magic service for casting spells
            spell_registry: Registry for spell lookups
            player_spell_repository: Optional repository for spell queries
            spell_learning_service: Optional service for spell learning
            chat_service: Optional chat service for announcements
        """
        self.magic_service = magic_service
        self.spell_registry = spell_registry
        self.player_spell_repository = player_spell_repository or PlayerSpellRepository()
        self.spell_learning_service = spell_learning_service
        self.chat_service = chat_service
        logger.info("MagicCommandHandler initialized")

    async def handle_cast_command(
        self,
        command_data: dict[str, Any],
        _current_user: dict[str, Any],
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /cast command.

        Args:
            command_data: Command data dictionary
            current_user: Current user information
            request: FastAPI request object
            alias_storage: Alias storage instance
            player_name: Player name

        Returns:
            dict: Command result
        """
        logger.debug("Handling cast command", player_name=player_name, command_data=command_data)

        preparation = await self._prepare_cast(command_data, player_name)
        if preparation["error"]:
            return {"result": preparation["error"]}

        player = preparation["player"]
        spell_name = preparation["spell_name"]
        target_name = preparation["target_name"]

        await self._interrupt_rest_for_cast(player, player_name, spell_name)

        result = await self.magic_service.cast_spell(player.player_id, spell_name, target_name)

        return await self._build_cast_response(player, result, spell_name, target_name)

    async def _prepare_cast(self, command_data: dict[str, Any], player_name: str) -> dict[str, Any]:
        """Resolve player and spell parameters for a cast; returns error message if preconditions fail."""
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            return {
                "error": "You are not recognized by the cosmic forces.",
                "player": None,
                "spell_name": None,
                "target_name": None,
            }

        current_dp = (player.get_stats() or {}).get("current_dp", 1)
        if current_dp <= 0:
            return {
                "error": "You are incapacitated and cannot cast spells.",
                "player": None,
                "spell_name": None,
                "target_name": None,
            }

        spell_name = command_data.get("spell_name") or command_data.get("spell")
        target_name = command_data.get("target")

        if not spell_name:
            return {
                "error": "Usage: /cast <spell_name> [target]",
                "player": None,
                "spell_name": None,
                "target_name": None,
            }

        return {"error": None, "player": player, "spell_name": spell_name, "target_name": target_name}

    async def _build_cast_response(
        self,
        player: Any,
        result: dict[str, Any],
        spell_name: str,
        target_name: str | None,
    ) -> dict[str, str]:
        """Build the response payload for a cast result and send announcements."""
        if not result.get("success"):
            return {"result": result.get("message", "Spell casting failed.")}

        await self._announce_spell_cast(player, result, spell_name, target_name)

        message = self._build_cast_success_message(result, spell_name)
        return {"result": message}

    def _build_cast_success_message(self, result: dict[str, Any], spell_name: str) -> str:
        """Build the final success message for a cast spell."""
        message = result.get("message", f"{spell_name} cast successfully.")
        effect_result = result.get("effect_result") or {}
        effect_msg = effect_result.get("message", "")
        if effect_msg:
            message += f" {effect_msg}"
        return str(message)

    async def _interrupt_rest_for_cast(self, player: Any, player_name: str, spell_name: str) -> None:
        """If player is resting, cancel rest countdown so they can cast. Swallows errors so cast can proceed."""
        try:
            app = getattr(self.magic_service, "_app_instance", None)
            if not app:
                app = getattr(self.magic_service.player_service, "_app_instance", None)
            if not app:
                return
            connection_manager = getattr(app.state, "connection_manager", None)
            if not connection_manager:
                return
            player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id
            if not is_player_resting(player_id, connection_manager):
                return
            await _cancel_rest_countdown(player_id, connection_manager)
            logger.info(
                "Rest interrupted by spellcasting",
                player_id=player_id,
                player_name=player_name,
                spell=spell_name,
            )
        except (AttributeError, ImportError, TypeError) as e:
            logger.debug("Could not check rest state for spellcasting", player_name=player_name, error=str(e))

    async def handle_spells_command(
        self,
        _command_data: dict[str, Any],
        _current_user: dict[str, Any],
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /spells command - list learned spells.

        Args:
            command_data: Command data dictionary
            current_user: Current user information
            request: FastAPI request object
            alias_storage: Alias storage instance
            player_name: Player name

        Returns:
            dict: Command result
        """
        logger.debug("Handling spells command", player_name=player_name)

        # Get player
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            return {"result": "You are not recognized by the cosmic forces."}

        # Get learned spells
        player_spells = await self.player_spell_repository.get_player_spells(player.player_id)

        if not player_spells:
            return {"result": "You have not learned any spells."}

        # Build spell list
        lines = ["Learned Spells:", ""]
        for player_spell in player_spells:
            spell = self.spell_registry.get_spell(str(player_spell.spell_id))
            if spell:
                lines.append(f"  {spell.name} - Mastery: {player_spell.mastery}%")
            else:
                lines.append(f"  {str(player_spell.spell_id)} - Mastery: {player_spell.mastery}%")

        return {"result": "\n".join(lines)}

    async def handle_spell_command(
        self,
        command_data: dict[str, Any],
        _current_user: dict[str, Any],
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /spell command - show spell details.
        """
        logger.debug("Handling spell command", player_name=player_name, command_data=command_data)

        try:
            context = await self._resolve_spell_context(command_data, player_name)
        except SpellCommandError as exc:
            return {"result": exc.message}

        detail_lines = self._build_spell_detail_lines(context["spell"], context["mastery"])
        return {"result": "\n".join(detail_lines)}

    async def _resolve_spell_context(self, command_data: dict[str, Any], player_name: str) -> dict[str, Any]:
        """Resolve player, spell, and mastery for /spell; raise SpellCommandError on failure."""
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            raise SpellCommandError("You are not recognized by the cosmic forces.")

        spell_name = command_data.get("spell_name") or command_data.get("spell")
        if not spell_name:
            raise SpellCommandError("Usage: /spell <spell_name>")

        spell = self.spell_registry.get_spell_by_name(spell_name)
        if not spell:
            raise SpellCommandError(f"Spell '{spell_name}' not found.")

        player_spell = await self.player_spell_repository.get_player_spell(player.player_id, spell.spell_id)
        mastery = player_spell.mastery if player_spell else None

        return {"spell": spell, "mastery": mastery}

    @staticmethod
    def _build_spell_detail_lines(spell: Any, mastery: int | None) -> list[str]:
        """Build the detailed description lines for a spell."""
        lines = [
            f"Spell: {spell.name}",
            f"Description: {spell.description}",
            f"School: {spell.school.value}",
            f"MP Cost: {spell.mp_cost}",
        ]

        if spell.requires_lucidity():
            lines.append(f"Lucidity Cost: {spell.lucidity_cost}")

        if spell.corruption_on_cast > 0:
            lines.append(f"Corruption on Cast: {spell.corruption_on_cast}")

        if spell.casting_time_seconds > 0:
            lines.append(f"Casting Time: {spell.casting_time_seconds} seconds")

        lines.append(f"Target Type: {spell.target_type.value}")
        lines.append(f"Range: {spell.range_type.value}")
        lines.append(f"Effect: {spell.effect_type.value}")

        if mastery is not None:
            lines.append(f"Your Mastery: {mastery}%")
        else:
            lines.append("Status: Not learned")

        if getattr(spell, "materials", None):
            lines.append("")
            lines.append("Required Materials:")
            for material in spell.materials:
                consumed_text = " (consumed)" if material.consumed else " (reusable)"
                lines.append(f"  - {material.item_id}{consumed_text}")

        return lines

    async def _announce_spell_cast(
        self, player: Any, _result: dict[str, Any], spell_name: str, target_name: str | None
    ) -> None:
        """
        Announce spell casting to room and caster.

        Args:
            player: Player object
            result: Cast result dictionary
            spell_name: Spell name
            target_name: Optional target name
        """
        if not self.chat_service:
            return

        # Room announcement (to all occupants)
        room_message = f"{player.name} gestures and chants an incantation..."
        if target_name:
            room_message += f" targeting {target_name}"

        # Send to room via chat service (includes caster)
        player_id = getattr(player, "id", None) or getattr(player, "player_id", None)
        if player_id:
            try:
                result = await self.chat_service.send_say_message(player_id, room_message)
                if not result.get("success"):
                    logger.warning(
                        "Failed to send spell cast announcement",
                        player_name=player.name,
                        spell_name=spell_name,
                        error=result.get("error"),
                    )
            except OSError as e:
                logger.error(
                    "Error sending spell cast announcement",
                    player_name=player.name,
                    spell_name=spell_name,
                    error=str(e),
                )
        else:
            logger.warning(
                "Cannot send spell cast announcement - player ID not found",
                player_name=player.name,
                spell_name=spell_name,
            )

        logger.debug("Spell cast announcement", player_name=player.name, spell_name=spell_name)

    async def handle_learn_command(
        self,
        command_data: dict[str, Any],
        _current_user: dict[str, Any],
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /learn command - learn a spell from various sources.
        """
        logger.debug("Handling learn command", player_name=player_name, command_data=command_data)

        try:
            context = await self._resolve_learn_context(command_data, player_name)
        except SpellCommandError as exc:
            return {"result": exc.message}

        svc = self.spell_learning_service
        if not svc:
            return {"result": "Spell learning system not initialized."}
        result = await svc.learn_spell(
            context["player"].player_id,
            context["spell_name"],
            source="command",
        )
        return await self._build_learn_response(result, context["spell_name"], context["player"])

    async def _resolve_learn_context(self, command_data: dict[str, Any], player_name: str) -> dict[str, Any]:
        """Resolve player and spell name for /learn; raise SpellCommandError on failure."""
        if not self.spell_learning_service:
            raise SpellCommandError("Spell learning system not initialized.")

        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            raise SpellCommandError("You are not recognized by the cosmic forces.")

        spell_name = command_data.get("spell_name") or command_data.get("spell")
        if not spell_name:
            raise SpellCommandError("Usage: /learn <spell_name>")

        return {"player": player, "spell_name": spell_name}

    async def _build_learn_response(self, result: dict[str, Any], spell_name: str, player: Any) -> dict[str, Any]:
        """Build the response payload for a learn result; includes player_update for Character Info panel."""
        if not result.get("success"):
            return {"result": result.get("message", "Failed to learn spell.")}

        message = result.get("message", f"Learned {spell_name}!")
        if result.get("corruption_applied", 0) > 0:
            message += f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."

        out: dict[str, Any] = {"result": message}
        player_after = await self.magic_service.player_service.persistence.get_player_by_id(player.player_id)
        if player_after:
            stats = player_after.get_stats() or {}
            out["player_update"] = {"stats": {"corruption": stats.get("corruption", 0)}}
        return out

    async def handle_stop_command(
        self,
        _command_data: dict[str, Any],
        _current_user: dict[str, Any],
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /stop command - interrupt current spell casting.

        Args:
            command_data: Command data dictionary
            _current_user: Current user information
            _request: FastAPI request object
            _alias_storage: Alias storage instance
            player_name: Player name

        Returns:
            dict: Command result
        """
        logger.debug("Handling stop command", player_name=player_name)

        # Get player
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            return {"result": "You are not recognized by the cosmic forces."}

        # Interrupt casting
        result = await self.magic_service.interrupt_casting(player.player_id)

        if not result.get("success"):
            return {"result": result.get("message", "Failed to interrupt casting.")}

        return {"result": result.get("message", "Casting interrupted.")}


# Command handler functions for integration with CommandService
async def handle_cast_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /cast command.

    This is a wrapper function for integration with CommandService.
    """
    # Get services from request app state
    magic_service = getattr(request.app.state, "magic_service", None)
    spell_registry = getattr(request.app.state, "spell_registry", None)

    if not magic_service or not spell_registry:
        return {"result": "Magic system not initialized."}

    handler = MagicCommandHandler(magic_service, spell_registry)
    return await handler.handle_cast_command(command_data, current_user, request, alias_storage, player_name)


async def handle_spells_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /spells command.

    This is a wrapper function for integration with CommandService.
    """
    magic_service = getattr(request.app.state, "magic_service", None)
    spell_registry = getattr(request.app.state, "spell_registry", None)

    if not magic_service or not spell_registry:
        return {"result": "Magic system not initialized."}

    handler = MagicCommandHandler(magic_service, spell_registry)
    return await handler.handle_spells_command(command_data, current_user, request, alias_storage, player_name)


async def handle_spell_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /spell command.

    This is a wrapper function for integration with CommandService.
    """
    magic_service = getattr(request.app.state, "magic_service", None)
    spell_registry = getattr(request.app.state, "spell_registry", None)

    if not magic_service or not spell_registry:
        return {"result": "Magic system not initialized."}

    handler = MagicCommandHandler(magic_service, spell_registry)
    return await handler.handle_spell_command(command_data, current_user, request, alias_storage, player_name)


async def handle_learn_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /learn command.

    This is a wrapper function for integration with CommandService.
    """
    magic_service = getattr(request.app.state, "magic_service", None)
    spell_registry = getattr(request.app.state, "spell_registry", None)
    spell_learning_service = getattr(request.app.state, "spell_learning_service", None)

    if not magic_service or not spell_registry:
        return {"result": "Magic system not initialized."}

    handler = MagicCommandHandler(magic_service, spell_registry, spell_learning_service=spell_learning_service)
    return await handler.handle_learn_command(command_data, current_user, request, alias_storage, player_name)


async def handle_stop_command(
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /stop command.

    This is a wrapper function for integration with CommandService.
    """
    magic_service = getattr(request.app.state, "magic_service", None)
    spell_registry = getattr(request.app.state, "spell_registry", None)

    if not magic_service or not spell_registry:
        return {"result": "Magic system not initialized."}

    handler = MagicCommandHandler(magic_service, spell_registry)
    return await handler.handle_stop_command(command_data, current_user, request, alias_storage, player_name)
