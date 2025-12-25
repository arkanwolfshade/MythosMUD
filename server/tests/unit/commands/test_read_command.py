"""
Tests for read command handler.

This module tests the /read command for reading spellbooks and learning spells.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.read_command import handle_read_command


class TestReadCommand:
    """Test handle_read_command function."""

    @pytest.mark.asyncio
    async def test_read_command_no_request(self) -> None:
        """Test read command when request is None."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        result = await handle_read_command(command_data, current_user, None, None, "testuser")

        assert "System error: application not available" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_no_app(self) -> None:
        """Test read command when app is not available."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_request.app = None

        result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

        assert "System error: application not available" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_no_persistence(self) -> None:
        """Test read command when persistence is not available."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        delattr(mock_app.state, "persistence")
        mock_request.app = mock_app

        result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

        assert "System error: persistence layer not available" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_no_spell_learning_service(self) -> None:
        """Test read command when spell learning service is not available."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        mock_app.state.persistence = AsyncMock()
        delattr(mock_app.state, "spell_learning_service")
        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Spell learning system not initialized" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_player_not_found(self) -> None:
        """Test read command when player is not found."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=None)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()
        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "not recognized by the cosmic forces" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_no_args(self) -> None:
        """Test read command with no arguments."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()
        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Usage: /read" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_item_not_found(self) -> None:
        """Test read command when item is not found."""
        command_data = {"args": ["nonexistent"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = "[]"
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()
        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "not found in your inventory" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_item_not_spellbook(self) -> None:
        """Test read command when item is not a spellbook."""
        command_data = {"args": ["regular_item"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = '[{"name": "regular_item", "metadata": {}}]'
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()
        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "is not a spellbook" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_empty_spellbook(self) -> None:
        """Test read command when spellbook is empty."""
        command_data = {"args": ["empty_book"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = '[{"name": "empty_book", "metadata": {"spellbook": true, "spells": []}}]'
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()
        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "empty or corrupted" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_specific_spell_success(self) -> None:
        """Test read command learning a specific spell."""
        command_data = {"args": ["spellbook", "Fireball"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.inventory = (
            '[{"name": "spellbook", "id": "book-123", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_learning_service = AsyncMock()
        mock_spell_learning_service.learn_spell.return_value = {"success": True, "message": "Learned Fireball!"}
        mock_app.state.spell_learning_service = mock_spell_learning_service

        mock_spell_registry = MagicMock()
        mock_spell = MagicMock()
        mock_spell.spell_id = "spell-1"
        mock_spell.name = "Fireball"
        mock_spell_registry.get_spell_by_name.return_value = mock_spell
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Learned Fireball!" in result["result"]
            mock_spell_learning_service.learn_spell.assert_called_once()

    @pytest.mark.asyncio
    async def test_read_command_specific_spell_with_corruption(self) -> None:
        """Test read command learning a spell with corruption."""
        command_data = {"args": ["spellbook", "DarkSpell"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.inventory = (
            '[{"name": "spellbook", "id": "book-123", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_learning_service = AsyncMock()
        mock_spell_learning_service.learn_spell.return_value = {
            "success": True,
            "message": "Learned DarkSpell!",
            "corruption_applied": 5,
        }
        mock_app.state.spell_learning_service = mock_spell_learning_service

        mock_spell_registry = MagicMock()
        mock_spell = MagicMock()
        mock_spell.spell_id = "spell-1"
        mock_spell.name = "DarkSpell"
        mock_spell_registry.get_spell_by_name.return_value = mock_spell
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Learned DarkSpell!" in result["result"]
            assert "corruption" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_read_command_specific_spell_not_in_book(self) -> None:
        """Test read command when specified spell is not in the book."""
        command_data = {"args": ["spellbook", "WrongSpell"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = '[{"name": "spellbook", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_registry = MagicMock()
        mock_spell = MagicMock()
        mock_spell.spell_id = "spell-2"  # Different from spell-1 in book
        mock_spell.name = "WrongSpell"
        mock_spell_registry.get_spell_by_name.return_value = mock_spell
        mock_app.state.spell_registry = mock_spell_registry
        mock_app.state.spell_learning_service = AsyncMock()

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "not in this spellbook" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_specific_spell_not_found_in_registry(self) -> None:
        """Test read command when spell is not found in registry."""
        command_data = {"args": ["spellbook", "UnknownSpell"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = '[{"name": "spellbook", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_registry = MagicMock()
        mock_spell_registry.get_spell_by_name.return_value = None
        mock_app.state.spell_registry = mock_spell_registry
        mock_app.state.spell_learning_service = AsyncMock()

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "not found in the spellbook" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_specific_spell_no_registry(self) -> None:
        """Test read command when spell registry is not available."""
        command_data = {"args": ["spellbook", "Fireball"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = '[{"name": "spellbook", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        delattr(mock_app.state, "spell_registry")
        mock_app.state.spell_learning_service = AsyncMock()

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Spell registry not available" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_single_spell_auto_learn(self) -> None:
        """Test read command auto-learning when book has only one spell."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.inventory = (
            '[{"name": "spellbook", "id": "book-123", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_learning_service = AsyncMock()
        mock_spell_learning_service.learn_spell.return_value = {"success": True, "message": "Learned spell-1!"}
        mock_app.state.spell_learning_service = mock_spell_learning_service

        mock_spell_registry = MagicMock()
        mock_spell = MagicMock()
        mock_spell.name = "Fireball"
        mock_spell_registry.get_spell.return_value = mock_spell
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Learned" in result["result"]
            mock_spell_learning_service.learn_spell.assert_called_once()

    @pytest.mark.asyncio
    async def test_read_command_single_spell_no_registry(self) -> None:
        """Test read command auto-learning when registry is not available."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.inventory = (
            '[{"name": "spellbook", "id": "book-123", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_learning_service = AsyncMock()
        mock_spell_learning_service.learn_spell.return_value = {"success": True, "message": "Learned spell-1!"}
        mock_app.state.spell_learning_service = mock_spell_learning_service
        delattr(mock_app.state, "spell_registry")

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Learned spell-1!" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_multiple_spells_list(self) -> None:
        """Test read command listing multiple spells."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = (
            '[{"name": "spellbook", "metadata": {"spellbook": true, "spells": ["spell-1", "spell-2"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()

        mock_spell_registry = MagicMock()
        mock_spell1 = MagicMock()
        mock_spell1.name = "Fireball"
        mock_spell2 = MagicMock()
        mock_spell2.name = "Icebolt"
        mock_spell_registry.get_spell.side_effect = [mock_spell1, mock_spell2]
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "contains the following spells" in result["result"]
            assert "Fireball" in result["result"]
            assert "Icebolt" in result["result"]
            assert "Use '/read" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_multiple_spells_some_missing_in_registry(self) -> None:
        """Test read command when some spells are missing in registry."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = (
            '[{"name": "spellbook", "metadata": {"spellbook": true, "spells": ["spell-1", "spell-2"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()

        mock_spell_registry = MagicMock()
        mock_spell1 = MagicMock()
        mock_spell1.name = "Fireball"
        mock_spell_registry.get_spell.side_effect = [mock_spell1, None]  # Second spell not found
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Fireball" in result["result"]
            assert "spell-2" in result["result"]  # Should show spell ID when not found

    @pytest.mark.asyncio
    async def test_read_command_learn_spell_failure(self) -> None:
        """Test read command when learning spell fails."""
        command_data = {"args": ["spellbook", "Fireball"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.player_id = uuid4()
        mock_player.inventory = (
            '[{"name": "spellbook", "id": "book-123", "metadata": {"spellbook": true, "spells": ["spell-1"]}}]'
        )
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_learning_service = AsyncMock()
        mock_spell_learning_service.learn_spell.return_value = {"success": False, "message": "Cannot learn spell"}
        mock_app.state.spell_learning_service = mock_spell_learning_service

        mock_spell_registry = MagicMock()
        mock_spell = MagicMock()
        mock_spell.spell_id = "spell-1"
        mock_spell.name = "Fireball"
        mock_spell_registry.get_spell_by_name.return_value = mock_spell
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            assert "Cannot learn spell" in result["result"]

    @pytest.mark.asyncio
    async def test_read_command_inventory_json_error(self) -> None:
        """Test read command when inventory JSON parsing fails."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = "invalid json"
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence
        mock_app.state.spell_learning_service = AsyncMock()

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.read_command.logger") as mock_logger:
                result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

                assert "error occurred" in result["result"].lower()
                mock_logger.error.assert_called_once()

    @pytest.mark.asyncio
    async def test_read_command_inventory_list_format(self) -> None:
        """Test read command with inventory as list (not JSON string)."""
        command_data = {"args": ["spellbook"]}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.inventory = [{"name": "spellbook", "metadata": {"spellbook": True, "spells": ["spell-1"]}}]
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.persistence = mock_persistence

        mock_spell_learning_service = AsyncMock()
        mock_spell_learning_service.learn_spell.return_value = {"success": True, "message": "Learned spell-1!"}
        mock_app.state.spell_learning_service = mock_spell_learning_service

        mock_spell_registry = MagicMock()
        mock_spell = MagicMock()
        mock_spell.name = "Fireball"
        mock_spell_registry.get_spell.return_value = mock_spell
        mock_app.state.spell_registry = mock_spell_registry

        mock_request.app = mock_app

        with patch("server.commands.read_command.get_username_from_user", return_value="testuser"):
            result = await handle_read_command(command_data, current_user, mock_request, None, "testuser")

            # Should handle list format inventory and auto-learn the spell
            assert "Learned" in result["result"]
