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
    ):
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
        command_data: dict,
        _current_user: dict,
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

        # Get player
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            return {"result": "You are not recognized by the cosmic forces."}

        # Extract spell name and optional target
        spell_name = command_data.get("spell_name") or command_data.get("spell")
        target_name = command_data.get("target")

        if not spell_name:
            return {"result": "Usage: /cast <spell_name> [target]"}

        # Check if player is resting and interrupt rest
        # Get connection_manager from magic_service if available
        try:
            app = getattr(self.magic_service, "_app_instance", None)
            if not app:
                # Try to get from player_service
                app = getattr(self.magic_service.player_service, "_app_instance", None)

            if app:
                connection_manager = getattr(app.state, "connection_manager", None)
                if connection_manager:
                    player_id = uuid.UUID(player.player_id) if isinstance(player.player_id, str) else player.player_id

                    if is_player_resting(player_id, connection_manager):
                        await _cancel_rest_countdown(player_id, connection_manager)
                        logger.info(
                            "Rest interrupted by spellcasting",
                            player_id=player_id,
                            player_name=player_name,
                            spell=spell_name,
                        )
        except (AttributeError, ImportError, TypeError) as e:
            logger.debug("Could not check rest state for spellcasting", player_name=player_name, error=str(e))

        # Cast spell
        result = await self.magic_service.cast_spell(player.player_id, spell_name, target_name)

        if not result.get("success"):
            return {"result": result.get("message", "Spell casting failed.")}

        # Send chat announcements
        await self._announce_spell_cast(player, result, spell_name, target_name)

        # Build response message
        message = result.get("message", f"{spell_name} cast successfully.")
        if result.get("effect_result"):
            effect_msg = result["effect_result"].get("message", "")
            if effect_msg:
                message += f" {effect_msg}"

        return {"result": message}

    async def handle_spells_command(
        self,
        _command_data: dict,
        _current_user: dict,
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
        command_data: dict,
        _current_user: dict,
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /spell command - show spell details.

        Args:
            command_data: Command data dictionary
            current_user: Current user information
            request: FastAPI request object
            alias_storage: Alias storage instance
            player_name: Player name

        Returns:
            dict: Command result
        """
        logger.debug("Handling spell command", player_name=player_name, command_data=command_data)

        # Get player
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            return {"result": "You are not recognized by the cosmic forces."}

        # Extract spell name
        spell_name = command_data.get("spell_name") or command_data.get("spell")
        if not spell_name:
            return {"result": "Usage: /spell <spell_name>"}

        # Get spell
        spell = self.spell_registry.get_spell_by_name(spell_name)
        if not spell:
            return {"result": f"Spell '{spell_name}' not found."}

        # Check if player knows it
        player_spell = await self.player_spell_repository.get_player_spell(player.player_id, spell.spell_id)
        mastery = player_spell.mastery if player_spell else None

        # Build spell info
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

        # Add material requirements
        if spell.materials:
            lines.append("")
            lines.append("Required Materials:")
            for material in spell.materials:
                consumed_text = " (consumed)" if material.consumed else " (reusable)"
                lines.append(f"  - {material.item_id}{consumed_text}")

        return {"result": "\n".join(lines)}

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
        command_data: dict,
        _current_user: dict,
        _request: Any,
        _alias_storage: AliasStorage | None,
        player_name: str,
    ) -> dict[str, str]:
        """
        Handle /learn command - learn a spell from various sources.

        Args:
            command_data: Command data dictionary
            _current_user: Current user information
            _request: FastAPI request object
            _alias_storage: Alias storage instance
            player_name: Player name

        Returns:
            dict: Command result
        """
        logger.debug("Handling learn command", player_name=player_name, command_data=command_data)

        if not self.spell_learning_service:
            return {"result": "Spell learning system not initialized."}

        # Get player
        player = await self.magic_service.player_service.persistence.get_player_by_name(player_name)
        if not player:
            return {"result": "You are not recognized by the cosmic forces."}

        # Extract spell name
        spell_name = command_data.get("spell_name") or command_data.get("spell")
        if not spell_name:
            return {"result": "Usage: /learn <spell_name>"}

        # Learn the spell (from unknown source - could be extended for specific sources)
        result = await self.spell_learning_service.learn_spell(player.player_id, spell_name, source="command")

        if not result.get("success"):
            return {"result": result.get("message", "Failed to learn spell.")}

        message = result.get("message", f"Learned {spell_name}!")
        if result.get("corruption_applied", 0) > 0:
            message += f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."

        return {"result": message}

    async def handle_stop_command(
        self,
        _command_data: dict,
        _current_user: dict,
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
    command_data: dict,
    current_user: dict,
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
    command_data: dict,
    current_user: dict,
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
    command_data: dict,
    current_user: dict,
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
    command_data: dict,
    current_user: dict,
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
    command_data: dict,
    current_user: dict,
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
