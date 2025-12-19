"""
Tests for magic command handlers.

This module tests the /cast, /spells, /spell, /learn, and /stop commands.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.magic_commands import (
    MagicCommandHandler,
    handle_cast_command,
    handle_learn_command,
    handle_spell_command,
    handle_spells_command,
    handle_stop_command,
)


class TestMagicCommandHandlerInit:
    """Test MagicCommandHandler initialization."""

    def test_magic_command_handler_init_defaults(self) -> None:
        """Test initialization with required services only."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()

        with patch("server.commands.magic_commands.logger"):
            handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

            assert handler.magic_service == mock_magic_service
            assert handler.spell_registry == mock_spell_registry
            assert handler.player_spell_repository is not None
            assert handler.spell_learning_service is None
            assert handler.chat_service is None

    def test_magic_command_handler_init_with_all_services(self) -> None:
        """Test initialization with all optional services."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_spell_repo = MagicMock()
        mock_learning_service = MagicMock()
        mock_chat_service = MagicMock()

        with patch("server.commands.magic_commands.logger"):
            handler = MagicCommandHandler(
                mock_magic_service,
                mock_spell_registry,
                player_spell_repository=mock_spell_repo,
                spell_learning_service=mock_learning_service,
                chat_service=mock_chat_service,
            )

            assert handler.player_spell_repository == mock_spell_repo
            assert handler.spell_learning_service == mock_learning_service
            assert handler.chat_service == mock_chat_service


class TestHandleCastCommand:
    """Test handle_cast_command method."""

    @pytest.mark.asyncio
    async def test_handle_cast_command_success(self) -> None:
        """Test successful spell casting."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.name = "TestPlayer"
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.cast_spell = AsyncMock(
            return_value={
                "success": True,
                "message": "Spell cast successfully.",
                "effect_result": {"message": "Target healed."},
            }
        )

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data = {"spell_name": "Heal", "target": "self"}
        result = await handler.handle_cast_command(command_data, {}, None, None, "TestPlayer")

        assert "Spell cast successfully" in result["result"]
        assert "Target healed" in result["result"]
        mock_magic_service.cast_spell.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_cast_command_player_not_found(self) -> None:
        """Test cast command when player is not found."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name.return_value = None

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data = {"spell_name": "Heal"}
        result = await handler.handle_cast_command(command_data, {}, None, None, "TestPlayer")

        assert "not recognized by the cosmic forces" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_cast_command_no_spell_name(self) -> None:
        """Test cast command with no spell name."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data: dict[str, Any] = {}
        result = await handler.handle_cast_command(command_data, {}, None, None, "TestPlayer")

        assert "Usage: /cast" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_cast_command_uses_spell_key(self) -> None:
        """Test cast command using 'spell' key instead of 'spell_name'."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.cast_spell = AsyncMock(return_value={"success": True, "message": "Spell cast."})

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data = {"spell": "Heal"}
        result = await handler.handle_cast_command(command_data, {}, None, None, "TestPlayer")

        assert "Spell cast" in result["result"]
        mock_magic_service.cast_spell.assert_called_once_with(mock_player.player_id, "Heal", None)

    @pytest.mark.asyncio
    async def test_handle_cast_command_failure(self) -> None:
        """Test cast command when spell casting fails."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.cast_spell = AsyncMock(return_value={"success": False, "message": "Not enough MP"})

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data = {"spell_name": "Fireball"}
        result = await handler.handle_cast_command(command_data, {}, None, None, "TestPlayer")

        assert "Not enough MP" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_cast_command_with_announcement(self) -> None:
        """Test cast command with chat service announcement."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_chat_service = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.name = "TestPlayer"
        mock_player.id = mock_player.player_id
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.cast_spell = AsyncMock(return_value={"success": True, "message": "Spell cast."})
        mock_chat_service.send_say_message = AsyncMock(return_value={"success": True})

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, chat_service=mock_chat_service)

        command_data = {"spell_name": "Heal", "target": "self"}
        result = await handler.handle_cast_command(command_data, {}, None, None, "TestPlayer")

        assert "result" in result
        mock_chat_service.send_say_message.assert_called_once()


class TestHandleSpellsCommand:
    """Test handle_spells_command method."""

    @pytest.mark.asyncio
    async def test_handle_spells_command_success(self) -> None:
        """Test successful spells listing."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_player_spell = MagicMock()
        mock_player_spell.spell_id = "spell-1"
        mock_player_spell.mastery = 50
        mock_spell_repo.get_player_spells.return_value = [mock_player_spell]

        mock_spell = MagicMock()
        mock_spell.name = "Fireball"
        mock_spell_registry.get_spell.return_value = mock_spell

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        result = await handler.handle_spells_command({}, {}, None, None, "TestPlayer")

        assert "Learned Spells:" in result["result"]
        assert "Fireball" in result["result"]
        assert "Mastery: 50%" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spells_command_no_spells(self) -> None:
        """Test spells command when player has no spells."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_spell_repo.get_player_spells.return_value = []

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        result = await handler.handle_spells_command({}, {}, None, None, "TestPlayer")

        assert "not learned any spells" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spells_command_spell_not_in_registry(self) -> None:
        """Test spells command when spell is not in registry."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_player_spell = MagicMock()
        mock_player_spell.spell_id = "spell-1"
        mock_player_spell.mastery = 50
        mock_spell_repo.get_player_spells.return_value = [mock_player_spell]

        mock_spell_registry.get_spell.return_value = None

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        result = await handler.handle_spells_command({}, {}, None, None, "TestPlayer")

        assert "spell-1" in result["result"]
        assert "Mastery: 50%" in result["result"]


class TestHandleSpellCommand:
    """Test handle_spell_command method."""

    @pytest.mark.asyncio
    async def test_handle_spell_command_success_learned(self) -> None:
        """Test successful spell command for learned spell."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_spell = MagicMock()
        mock_spell.name = "Fireball"
        mock_spell.description = "A ball of fire"
        mock_spell.school.value = "Evocation"
        mock_spell.mp_cost = 10
        mock_spell.requires_lucidity.return_value = False
        mock_spell.corruption_on_cast = 0
        mock_spell.casting_time_seconds = 0
        mock_spell.target_type.value = "self"
        mock_spell.range_type.value = "touch"
        mock_spell.effect_type.value = "damage"
        mock_spell.materials = []
        mock_spell_registry.get_spell_by_name.return_value = mock_spell

        mock_player_spell = MagicMock()
        mock_player_spell.mastery = 75
        mock_spell_repo.get_player_spell = AsyncMock(return_value=mock_player_spell)

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        command_data = {"spell_name": "Fireball"}
        result = await handler.handle_spell_command(command_data, {}, None, None, "TestPlayer")

        assert "Spell: Fireball" in result["result"]
        assert "Your Mastery: 75%" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spell_command_not_learned(self) -> None:
        """Test spell command for spell not learned."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_spell = MagicMock()
        mock_spell.name = "Fireball"
        mock_spell.description = "A ball of fire"
        mock_spell.school.value = "Evocation"
        mock_spell.mp_cost = 10
        mock_spell.requires_lucidity.return_value = False
        mock_spell.corruption_on_cast = 0
        mock_spell.casting_time_seconds = 0
        mock_spell.target_type.value = "self"
        mock_spell.range_type.value = "touch"
        mock_spell.effect_type.value = "damage"
        mock_spell.materials = []
        mock_spell_registry.get_spell_by_name.return_value = mock_spell

        mock_spell_repo.get_player_spell = AsyncMock(return_value=None)

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        command_data = {"spell_name": "Fireball"}
        result = await handler.handle_spell_command(command_data, {}, None, None, "TestPlayer")

        assert "Status: Not learned" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spell_command_no_spell_name(self) -> None:
        """Test spell command with no spell name."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data: dict[str, Any] = {}
        result = await handler.handle_spell_command(command_data, {}, None, None, "TestPlayer")

        assert "Usage: /spell" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spell_command_spell_not_found(self) -> None:
        """Test spell command when spell is not found."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_spell_registry.get_spell_by_name.return_value = None

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data = {"spell_name": "UnknownSpell"}
        result = await handler.handle_spell_command(command_data, {}, None, None, "TestPlayer")

        assert "not found" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spell_command_with_lucidity_cost(self) -> None:
        """Test spell command showing lucidity cost."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_spell = MagicMock()
        mock_spell.name = "Mind Blast"
        mock_spell.description = "A mental attack"
        mock_spell.school.value = "Mentalism"
        mock_spell.mp_cost = 5
        mock_spell.requires_lucidity.return_value = True
        mock_spell.lucidity_cost = 10
        mock_spell.corruption_on_cast = 0
        mock_spell.casting_time_seconds = 0
        mock_spell.target_type.value = "target"
        mock_spell.range_type.value = "sight"
        mock_spell.effect_type.value = "damage"
        mock_spell.materials = []
        mock_spell_registry.get_spell_by_name.return_value = mock_spell

        mock_spell_repo.get_player_spell = AsyncMock(return_value=None)

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        command_data = {"spell_name": "Mind Blast"}
        result = await handler.handle_spell_command(command_data, {}, None, None, "TestPlayer")

        assert "Lucidity Cost: 10" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spell_command_with_materials(self) -> None:
        """Test spell command showing material requirements."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_material = MagicMock()
        mock_material.item_id = "crystal"
        mock_material.consumed = True

        mock_spell = MagicMock()
        mock_spell.name = "Summon"
        mock_spell.description = "Summon a creature"
        mock_spell.school.value = "Conjuration"
        mock_spell.mp_cost = 20
        mock_spell.requires_lucidity.return_value = False
        mock_spell.corruption_on_cast = 0
        mock_spell.casting_time_seconds = 0
        mock_spell.target_type.value = "self"
        mock_spell.range_type.value = "touch"
        mock_spell.effect_type.value = "summon"
        mock_spell.materials = [mock_material]
        mock_spell_registry.get_spell_by_name.return_value = mock_spell

        mock_spell_repo.get_player_spell = AsyncMock(return_value=None)

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry, player_spell_repository=mock_spell_repo)

        command_data = {"spell_name": "Summon"}
        result = await handler.handle_spell_command(command_data, {}, None, None, "TestPlayer")

        assert "Required Materials:" in result["result"]
        assert "crystal" in result["result"]
        assert "(consumed)" in result["result"]


class TestHandleLearnCommand:
    """Test handle_learn_command method."""

    @pytest.mark.asyncio
    async def test_handle_learn_command_success(self) -> None:
        """Test successful spell learning."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_learning_service = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_learning_service.learn_spell = AsyncMock(return_value={"success": True, "message": "Learned Fireball!"})

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(
            mock_magic_service, mock_spell_registry, spell_learning_service=mock_learning_service
        )

        command_data = {"spell_name": "Fireball"}
        result = await handler.handle_learn_command(command_data, {}, None, None, "TestPlayer")

        assert "Learned Fireball!" in result["result"]
        mock_learning_service.learn_spell.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_learn_command_with_corruption(self) -> None:
        """Test spell learning with corruption."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_learning_service = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_learning_service.learn_spell = AsyncMock(
            return_value={"success": True, "message": "Learned DarkSpell!", "corruption_applied": 5}
        )

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(
            mock_magic_service, mock_spell_registry, spell_learning_service=mock_learning_service
        )

        command_data = {"spell_name": "DarkSpell"}
        result = await handler.handle_learn_command(command_data, {}, None, None, "TestPlayer")

        assert "Learned DarkSpell!" in result["result"]
        assert "corruption" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_learn_command_no_learning_service(self) -> None:
        """Test learn command when learning service is not initialized."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        command_data = {"spell_name": "Fireball"}
        result = await handler.handle_learn_command(command_data, {}, None, None, "TestPlayer")

        assert "Spell learning system not initialized" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_learn_command_failure(self) -> None:
        """Test learn command when learning fails."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_learning_service = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_learning_service.learn_spell = AsyncMock(return_value={"success": False, "message": "Cannot learn spell"})

        mock_magic_service.player_service.persistence = mock_persistence

        handler = MagicCommandHandler(
            mock_magic_service, mock_spell_registry, spell_learning_service=mock_learning_service
        )

        command_data = {"spell_name": "Fireball"}
        result = await handler.handle_learn_command(command_data, {}, None, None, "TestPlayer")

        assert "Cannot learn spell" in result["result"]


class TestHandleStopCommand:
    """Test handle_stop_command method."""

    @pytest.mark.asyncio
    async def test_handle_stop_command_success(self) -> None:
        """Test successful casting interruption."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.interrupt_casting = AsyncMock(
            return_value={"success": True, "message": "Casting interrupted."}
        )

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        result = await handler.handle_stop_command({}, {}, None, None, "TestPlayer")

        assert "Casting interrupted" in result["result"]
        mock_magic_service.interrupt_casting.assert_called_once_with(mock_player.player_id)

    @pytest.mark.asyncio
    async def test_handle_stop_command_failure(self) -> None:
        """Test stop command when interruption fails."""
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.interrupt_casting = AsyncMock(return_value={"success": False, "message": "Not casting"})

        handler = MagicCommandHandler(mock_magic_service, mock_spell_registry)

        result = await handler.handle_stop_command({}, {}, None, None, "TestPlayer")

        assert "Not casting" in result["result"]


class TestWrapperFunctions:
    """Test wrapper functions for command integration."""

    @pytest.mark.asyncio
    async def test_handle_cast_command_wrapper_success(self) -> None:
        """Test handle_cast_command wrapper function."""
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.cast_spell = AsyncMock(return_value={"success": True, "message": "Spell cast."})

        mock_app.state.magic_service = mock_magic_service
        mock_app.state.spell_registry = mock_spell_registry
        mock_request.app = mock_app

        command_data = {"spell_name": "Heal"}
        result = await handle_cast_command(command_data, {}, mock_request, None, "TestPlayer")

        assert "result" in result

    @pytest.mark.asyncio
    async def test_handle_cast_command_wrapper_no_magic_service(self) -> None:
        """Test handle_cast_command wrapper when magic service is not available."""
        mock_request = MagicMock()
        mock_app = MagicMock()
        delattr(mock_app.state, "magic_service")
        mock_request.app = mock_app

        result = await handle_cast_command({}, {}, mock_request, None, "TestPlayer")

        assert "Magic system not initialized" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_spells_command_wrapper_success(self) -> None:
        """Test handle_spells_command wrapper function."""
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()
        mock_spell_repo = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_spell_repo.get_player_spells.return_value = []

        mock_magic_service.player_service.persistence = mock_persistence

        mock_app.state.magic_service = mock_magic_service
        mock_app.state.spell_registry = mock_spell_registry
        mock_request.app = mock_app

        result = await handle_spells_command({}, {}, mock_request, None, "TestPlayer")

        assert "result" in result

    @pytest.mark.asyncio
    async def test_handle_spell_command_wrapper_success(self) -> None:
        """Test handle_spell_command wrapper function."""
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_spell = MagicMock()
        mock_spell.name = "Fireball"
        mock_spell.description = "A ball of fire"
        mock_spell.school.value = "Evocation"
        mock_spell.mp_cost = 10
        mock_spell.requires_lucidity.return_value = False
        mock_spell.corruption_on_cast = 0
        mock_spell.casting_time_seconds = 0
        mock_spell.target_type.value = "self"
        mock_spell.range_type.value = "touch"
        mock_spell.effect_type.value = "damage"
        mock_spell.materials = []
        mock_spell_registry.get_spell_by_name.return_value = mock_spell

        # PlayerSpellRepository is created inside handler, so we need to patch it
        from server.persistence.repositories.player_spell_repository import PlayerSpellRepository

        mock_magic_service.player_service.persistence = mock_persistence

        mock_app.state.magic_service = mock_magic_service
        mock_app.state.spell_registry = mock_spell_registry
        mock_request.app = mock_app

        with patch.object(PlayerSpellRepository, "get_player_spell", new_callable=AsyncMock, return_value=None):
            command_data = {"spell_name": "Fireball"}
            result = await handle_spell_command(command_data, {}, mock_request, None, "TestPlayer")

            assert "Spell: Fireball" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_learn_command_wrapper_success(self) -> None:
        """Test handle_learn_command wrapper function."""
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_learning_service = AsyncMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_learning_service.learn_spell = AsyncMock(return_value={"success": True, "message": "Learned Fireball!"})

        mock_magic_service.player_service.persistence = mock_persistence

        mock_app.state.magic_service = mock_magic_service
        mock_app.state.spell_registry = mock_spell_registry
        mock_app.state.spell_learning_service = mock_learning_service
        mock_request.app = mock_app

        command_data = {"spell_name": "Fireball"}
        result = await handle_learn_command(command_data, {}, mock_request, None, "TestPlayer")

        assert "Learned Fireball!" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_stop_command_wrapper_success(self) -> None:
        """Test handle_stop_command wrapper function."""
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_magic_service = MagicMock()
        mock_spell_registry = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_magic_service.player_service.persistence = mock_persistence
        mock_magic_service.interrupt_casting = AsyncMock(
            return_value={"success": True, "message": "Casting interrupted."}
        )

        mock_app.state.magic_service = mock_magic_service
        mock_app.state.spell_registry = mock_spell_registry
        mock_request.app = mock_app

        result = await handle_stop_command({}, {}, mock_request, None, "TestPlayer")

        assert "Casting interrupted" in result["result"]
