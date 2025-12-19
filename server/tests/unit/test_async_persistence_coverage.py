"""
Coverage tests for AsyncPersistenceLayer.
Targets missing branches and error handling in server/async_persistence.py.
"""

import uuid
from typing import Any
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.exceptions import DatabaseError


class TestAsyncPersistenceCoverage:
    """Test missing branches in async persistence facade."""

    def test_process_room_rows_prefix_branch(self) -> None:
        """Test _process_room_rows when stable_id already has the expected prefix."""
        persistence = AsyncPersistenceLayer(_db_path="mock")

        # Expected prefix: plane_zone_subzone_
        # stable_id: earth_arkham_sanitarium_room_1
        # zone_stable_id: earth/arkham
        # subzone_stable_id: sanitarium

        rooms_rows = [
            {
                "stable_id": "earth_arkham_sanitarium_room_1",
                "name": "Room 1",
                "description": "Desc",
                "attributes": {"environment": "indoors"},
                "subzone_stable_id": "sanitarium",
                "zone_stable_id": "earth/arkham",
            }
        ]

        result = persistence._process_room_rows(rooms_rows)
        assert result[0]["room_id"] == "earth_arkham_sanitarium_room_1"

    def test_process_exit_rows_prefix_branch(self) -> None:
        """Test _process_exit_rows when stable_ids already have the expected prefix."""
        persistence = AsyncPersistenceLayer(_db_path="mock")

        exits_rows = [
            {
                "from_room_stable_id": "earth_arkham_sanitarium_room_1",
                "to_room_stable_id": "earth_arkham_sanitarium_room_2",
                "direction": "north",
                "from_subzone_stable_id": "sanitarium",
                "from_zone_stable_id": "earth/arkham",
                "to_subzone_stable_id": "sanitarium",
                "to_zone_stable_id": "earth/arkham",
            }
        ]

        result = persistence._process_exit_rows(exits_rows)
        assert result["earth_arkham_sanitarium_room_1"]["north"] == "earth_arkham_sanitarium_room_2"

    @pytest.mark.asyncio
    async def test_get_user_by_username_case_insensitive_error(self) -> None:
        """Test get_user_by_username_case_insensitive error handling."""
        persistence = AsyncPersistenceLayer(_db_path="mock")

        # Mock get_async_session to raise an error
        with patch("server.async_persistence.get_async_session") as mock_session_gen:
            mock_session = AsyncMock()
            from sqlalchemy.exc import SQLAlchemyError

            mock_session.execute.side_effect = SQLAlchemyError("DB error")

            async def mock_gen():
                yield mock_session

            mock_session_gen.return_value = mock_gen()

            with pytest.raises(DatabaseError, match="Database error retrieving user"):
                await persistence.get_user_by_username_case_insensitive("test")

    @pytest.mark.asyncio
    async def test_delegate_methods(self) -> None:
        """Test delegate methods in AsyncPersistenceLayer."""
        persistence = AsyncPersistenceLayer(_db_path="mock")
        # Mock repositories
        persistence._player_repo = Mock()
        # Set async methods
        persistence._player_repo.get_player_by_name = AsyncMock()
        persistence._player_repo.get_player_by_id = AsyncMock()
        persistence._player_repo.get_players_by_user_id = AsyncMock()
        persistence._player_repo.get_active_players_by_user_id = AsyncMock()
        persistence._player_repo.get_player_by_user_id = AsyncMock()
        persistence._player_repo.soft_delete_player = AsyncMock()
        persistence._player_repo.save_player = AsyncMock()
        persistence._player_repo.list_players = AsyncMock()
        persistence._player_repo.get_players_in_room = AsyncMock()
        persistence._player_repo.save_players = AsyncMock()
        persistence._player_repo.delete_player = AsyncMock()
        persistence._player_repo.update_player_last_active = AsyncMock()

        persistence._room_repo = Mock()
        persistence._profession_repo = AsyncMock()
        persistence._experience_repo = AsyncMock()
        persistence._health_repo = AsyncMock()
        persistence._container_repo = AsyncMock()

        player_id = uuid.uuid4()
        user_id = str(uuid.uuid4())

        await persistence.get_player_by_name("name")
        persistence._player_repo.get_player_by_name.assert_called_once()

        await persistence.get_player_by_id(player_id)
        persistence._player_repo.get_player_by_id.assert_called_once()

        await persistence.get_players_by_user_id(user_id)
        persistence._player_repo.get_players_by_user_id.assert_called_once()

        await persistence.get_active_players_by_user_id(user_id)
        persistence._player_repo.get_active_players_by_user_id.assert_called_once()

        await persistence.get_player_by_user_id(user_id)
        persistence._player_repo.get_player_by_user_id.assert_called_once()

        await persistence.soft_delete_player(player_id)
        persistence._player_repo.soft_delete_player.assert_called_once()

        await persistence.save_player(Mock())
        persistence._player_repo.save_player.assert_called_once()

        await persistence.list_players()
        persistence._player_repo.list_players.assert_called_once()

        persistence.get_room_by_id("room")
        persistence._room_repo.get_room_by_id.assert_called_once()

        # async_list_rooms returns list[Room], not a coroutine
        persistence._room_repo.list_rooms.return_value = []
        await persistence.async_list_rooms()
        persistence._room_repo.list_rooms.assert_called_once()

        await persistence.get_players_in_room("room")
        persistence._player_repo.get_players_in_room.assert_called_once()

        await persistence.save_players([])
        persistence._player_repo.save_players.assert_called_once()

        await persistence.delete_player(player_id)
        persistence._player_repo.delete_player.assert_called_once()

        await persistence.update_player_last_active(player_id)
        persistence._player_repo.update_player_last_active.assert_called_once()

        await persistence.get_profession_by_id(1)
        persistence._profession_repo.get_profession_by_id.assert_called_once()

        # validate_and_fix_player_room is synchronous
        persistence._player_repo.validate_and_fix_player_room.return_value = True
        persistence.validate_and_fix_player_room(Mock())
        persistence._player_repo.validate_and_fix_player_room.assert_called_once()

        mock_player = Mock()
        mock_player.player_id = player_id
        await persistence.apply_lucidity_loss(mock_player, 10)
        persistence._experience_repo.update_player_stat_field.assert_called_once()

        await persistence.apply_fear(mock_player, 10)
        assert persistence._experience_repo.update_player_stat_field.call_count == 2

        await persistence.apply_corruption(mock_player, 10)
        assert persistence._experience_repo.update_player_stat_field.call_count == 3

        await persistence.heal_player(mock_player, 10)
        persistence._health_repo.heal_player.assert_called_once()

        await persistence.async_heal_player(mock_player, 10)
        assert persistence._health_repo.heal_player.call_count == 2

        await persistence.damage_player(mock_player, 10)
        persistence._health_repo.damage_player.assert_called_once()

        await persistence.async_damage_player(mock_player, 10)
        assert persistence._health_repo.damage_player.call_count == 2

        await persistence.create_container("env")
        persistence._container_repo.create_container.assert_called_once()

        await persistence.get_container(player_id)
        persistence._container_repo.get_container.assert_called_once()

        await persistence.get_containers_by_room_id("room")
        persistence._container_repo.get_containers_by_room_id.assert_called_once()

        await persistence.get_containers_by_entity_id(player_id)
        persistence._container_repo.get_containers_by_entity_id.assert_called_once()

        await persistence.update_container(player_id)
        persistence._container_repo.update_container.assert_called_once()

        await persistence.get_decayed_containers()
        persistence._container_repo.get_decayed_containers.assert_called_once()

        await persistence.delete_container(player_id)
        persistence._container_repo.delete_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_professions_error(self) -> None:
        """Test get_professions error handling."""
        persistence = AsyncPersistenceLayer(_db_path="mock")

        with patch("server.async_persistence.get_async_session") as mock_session_gen:
            mock_session = AsyncMock()
            from sqlalchemy.exc import SQLAlchemyError

            mock_session.execute.side_effect = SQLAlchemyError("DB error")

            async def mock_gen():
                yield mock_session

            mock_session_gen.return_value = mock_gen()

            with pytest.raises(DatabaseError, match="Database error retrieving professions"):
                await persistence.get_professions()

    def test_build_room_objects(self) -> None:
        """Test _build_room_objects logic."""
        persistence = AsyncPersistenceLayer(_db_path="mock")

        room_data_list = [
            {
                "room_id": "earth_arkham_sanitarium_room_foyer_001",
                "name": "Foyer",
                "description": "Foyer desc",
                "attributes": {"environment": "indoors"},
                "plane": "earth",
                "zone": "arkham",
                "sub_zone": "sanitarium",
            }
        ]
        exits_by_room = {"earth_arkham_sanitarium_room_foyer_001": {"north": "hallway"}}
        result_container: dict[str, Any] = {"rooms": {}}

        persistence._build_room_objects(room_data_list, exits_by_room, result_container)

        assert "earth_arkham_sanitarium_room_foyer_001" in result_container["rooms"]
        room = result_container["rooms"]["earth_arkham_sanitarium_room_foyer_001"]
        assert room.name == "Foyer"
        assert room.exits == {"north": "hallway"}

    @pytest.mark.asyncio
    async def test_async_persistence_close(self) -> None:
        """Test close method (no-op)."""
        persistence = AsyncPersistenceLayer(_db_path="mock")
        await persistence.close()  # Should not raise

    def test_load_room_cache_error(self) -> None:
        """Test _load_room_cache handling errors from result_container."""
        with patch("server.async_persistence.AsyncPersistenceLayer._async_load_room_cache") as mock_load:
            # Simulate a RuntimeError inside the async thread
            def side_effect(result):
                result["error"] = RuntimeError("Thread failure")

            mock_load.side_effect = side_effect

            persistence = AsyncPersistenceLayer(_db_path="mock")
            # The constructor calls _load_room_cache, which should handle the error
            assert persistence._room_cache == {}

    def test_load_room_cache_base_exception(self) -> None:
        """Test _load_room_cache handling BaseException from result_container."""
        with patch("server.async_persistence.AsyncPersistenceLayer._async_load_room_cache") as mock_load:
            # BaseException should be re-raised
            def side_effect(result):
                result["error"] = KeyboardInterrupt()

            mock_load.side_effect = side_effect

            with pytest.raises(KeyboardInterrupt):
                AsyncPersistenceLayer(_db_path="mock")

    def test_get_database_url_missing(self) -> None:
        """Test _get_database_url raises error when env var missing."""
        persistence = AsyncPersistenceLayer(_db_path="mock")
        with patch("os.getenv", return_value=None):
            with pytest.raises(ValueError, match="DATABASE_URL environment variable not set"):
                persistence._get_database_url()
