"""
Unit tests for alias storage utilities.

Tests the AliasStorage class for managing player command aliases in JSON format.
"""

# pyright: reportPrivateUsage=false
# Reason: whitebox tests exercise path-injection barriers on protected load/save helpers.

import json
import os
import tempfile
from collections.abc import Generator
from datetime import datetime
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock, patch

import pytest

from server.alias_storage import AliasPayload, AliasRecord, AliasStorage
from server.models.alias import Alias

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def temp_storage_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for alias storage."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def alias_storage(temp_storage_dir: Path) -> AliasStorage:
    """Create an AliasStorage instance with temporary directory."""
    return AliasStorage(storage_dir=str(temp_storage_dir))


@pytest.fixture
def sample_alias() -> Alias:
    """Create a sample alias for testing."""
    return Alias(name="n", command="go north")


@pytest.fixture
def sample_alias2() -> Alias:
    """Create another sample alias for testing."""
    return Alias(name="s", command="go south")


def test_alias_storage_init_with_storage_dir(temp_storage_dir: Path) -> None:
    """Test AliasStorage initialization with storage_dir parameter."""
    storage = AliasStorage(storage_dir=str(temp_storage_dir))
    assert storage.storage_dir == temp_storage_dir
    assert storage.storage_dir.exists()


def test_alias_storage_init_with_env_var(temp_storage_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test AliasStorage initialization with ALIASES_DIR environment variable."""
    monkeypatch.setenv("ALIASES_DIR", str(temp_storage_dir))
    storage = AliasStorage(storage_dir=None)
    assert storage.storage_dir == temp_storage_dir


def test_alias_storage_init_without_env_var() -> None:
    """Test AliasStorage initialization without environment variable raises error."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="ALIASES_DIR environment variable"):
            _ = AliasStorage(storage_dir=None)


def test_alias_storage_creates_directory(temp_storage_dir: Path) -> None:
    """Test that AliasStorage creates the storage directory if it doesn't exist."""
    new_dir = temp_storage_dir / "new_dir"
    _ = AliasStorage(storage_dir=str(new_dir))
    assert new_dir.exists()


def test_get_alias_file_path(alias_storage: AliasStorage) -> None:
    """Test get_alias_file_path returns correct path."""
    path = alias_storage.get_alias_file_path("TestPlayer")
    assert path.name == "TestPlayer_aliases.json"
    assert path.parent == Path(os.path.realpath(alias_storage.storage_dir))


def test_get_alias_file_path_rejects_traversal(alias_storage: AliasStorage, temp_storage_dir: Path) -> None:
    """Path-injection: traversal and separators must not escape storage_dir."""
    with pytest.raises(ValueError):
        _ = alias_storage.get_alias_file_path("../outside")
    with pytest.raises(ValueError):
        _ = alias_storage.get_alias_file_path("foo/bar")
    with pytest.raises(ValueError):
        _ = alias_storage.get_alias_file_path("foo\\bar")
    with pytest.raises(ValueError):
        _ = alias_storage.get_alias_file_path("")
    # No alias file created outside the storage root.
    assert list(temp_storage_dir.rglob("*")) == []
    outside = temp_storage_dir.parent / "outside_aliases.json"
    assert not outside.exists()


def test_load_and_save_reject_path_injection(alias_storage: AliasStorage, temp_storage_dir: Path) -> None:
    """Load/save re-check before open: attack names never open files outside storage."""
    empty_payload: AliasPayload = {"version": "1.0", "aliases": []}
    for bad_name in ("../outside", "foo/bar", "foo\\bar", ""):
        with pytest.raises(ValueError):
            _ = alias_storage._load_alias_data(bad_name)
        with pytest.raises(ValueError):
            _ = alias_storage._save_alias_data(bad_name, empty_payload)
        with pytest.raises(ValueError):
            _ = alias_storage._resolved_alias_open_path(bad_name)
    assert list(temp_storage_dir.rglob("*")) == []
    outside = temp_storage_dir.parent / "outside_aliases.json"
    assert not outside.exists()


def test_resolved_alias_open_path_stays_under_storage(alias_storage: AliasStorage) -> None:
    """Open path is absolute str under realpath(storage_dir)."""
    path = alias_storage._resolved_alias_open_path("TestPlayer")
    assert isinstance(path, str)
    base = os.path.realpath(str(alias_storage.storage_dir))
    assert os.path.commonpath([base, path]) == base
    assert path.endswith("TestPlayer_aliases.json")
    assert os.path.isabs(path)


def test_load_alias_data_nonexistent_file(alias_storage: AliasStorage) -> None:
    """Test _load_alias_data returns default structure for nonexistent file."""
    data = alias_storage._load_alias_data("TestPlayer")
    assert data == {"version": "1.0", "aliases": []}


def test_load_alias_data_existing_file(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test _load_alias_data loads existing alias file."""
    # Create alias file
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    # Load it back (AliasPayload is dict[str, object]; narrow aliases for the checker)
    data = alias_storage._load_alias_data("TestPlayer")
    assert data["version"] == "1.0"
    aliases_raw = data["aliases"]
    assert isinstance(aliases_raw, list)
    # isinstance(list) does not narrow element types for basedpyright
    aliases = cast(list[object], aliases_raw)
    assert len(aliases) == 1
    first = aliases[0]
    assert isinstance(first, dict)
    assert first["name"] == "n"


def test_load_alias_data_invalid_json(alias_storage: AliasStorage) -> None:
    """Test _load_alias_data handles invalid JSON gracefully."""
    file_path = alias_storage.get_alias_file_path("TestPlayer")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    _ = file_path.write_text("invalid json{", encoding="utf-8")

    data = alias_storage._load_alias_data("TestPlayer")
    assert data == {"version": "1.0", "aliases": []}


def test_load_alias_data_io_error(alias_storage: AliasStorage, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test _load_alias_data handles IO errors gracefully."""

    def mock_open(*_args: object, **_kwargs: object) -> object:
        raise OSError("Permission denied")

    monkeypatch.setattr("builtins.open", mock_open)

    data = alias_storage._load_alias_data("TestPlayer")
    assert data == {"version": "1.0", "aliases": []}


def test_save_alias_data_success(alias_storage: AliasStorage) -> None:
    """Test _save_alias_data successfully saves data."""
    data: AliasPayload = {"version": "1.0", "aliases": [{"name": "n", "command": "go north"}]}
    result = alias_storage._save_alias_data("TestPlayer", data)

    assert result is True
    file_path = alias_storage.get_alias_file_path("TestPlayer")
    assert file_path.exists()

    loaded = cast(AliasPayload, json.loads(file_path.read_text(encoding="utf-8")))
    assert loaded == data


def test_save_alias_data_io_error(alias_storage: AliasStorage, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test _save_alias_data handles IO errors."""

    def mock_open(*args: object, **kwargs: object) -> MagicMock:
        mode = args[1] if len(args) > 1 else kwargs.get("mode", "")
        if isinstance(mode, str) and "w" in mode:
            raise OSError("Permission denied")
        return MagicMock()

    monkeypatch.setattr("builtins.open", mock_open)

    data: AliasPayload = {"version": "1.0", "aliases": []}
    result = alias_storage._save_alias_data("TestPlayer", data)
    assert result is False


def test_get_player_aliases_empty(alias_storage: AliasStorage) -> None:
    """Test get_player_aliases returns empty list for player with no aliases."""
    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert aliases == []


def test_get_player_aliases_with_aliases(
    alias_storage: AliasStorage, sample_alias: Alias, sample_alias2: Alias
) -> None:
    """Test get_player_aliases returns aliases from file."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias, sample_alias2])

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 2
    names = {alias.name for alias in aliases}
    assert "n" in names
    assert "s" in names


def test_get_player_aliases_with_timestamps(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test get_player_aliases correctly parses timestamp strings."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    # Manually modify file to include Z suffix
    file_path = alias_storage.get_alias_file_path("TestPlayer")
    data = cast(AliasPayload, json.loads(file_path.read_text(encoding="utf-8")))
    aliases = cast(list[AliasRecord], data["aliases"])
    aliases[0]["created_at"] = "2024-01-01T12:00:00Z"
    aliases[0]["updated_at"] = "2024-01-01T12:00:00Z"
    _ = file_path.write_text(json.dumps(data), encoding="utf-8")

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1
    assert isinstance(aliases[0].created_at, datetime)
    assert isinstance(aliases[0].updated_at, datetime)


def test_get_player_aliases_invalid_alias_data(alias_storage: AliasStorage) -> None:
    """Test get_player_aliases handles invalid alias data gracefully."""
    file_path = alias_storage.get_alias_file_path("TestPlayer")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    _ = file_path.write_text(json.dumps({"version": "1.0", "aliases": [{"invalid": "data"}]}), encoding="utf-8")

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert aliases == []


def test_save_player_aliases(alias_storage: AliasStorage, sample_alias: Alias, sample_alias2: Alias) -> None:
    """Test save_player_aliases saves aliases correctly."""
    result = alias_storage.save_player_aliases("TestPlayer", [sample_alias, sample_alias2])
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 2


def test_add_alias_new(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test add_alias adds a new alias."""
    result = alias_storage.add_alias("TestPlayer", sample_alias)
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1
    assert aliases[0].name == "n"


def test_add_alias_updates_existing(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test add_alias updates existing alias."""
    assert alias_storage.add_alias("TestPlayer", sample_alias)

    updated_alias = Alias(name="n", command="go east")
    result = alias_storage.add_alias("TestPlayer", updated_alias)
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1
    assert aliases[0].command == "go east"


def test_add_alias_case_insensitive(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test add_alias is case-insensitive for alias names."""
    assert alias_storage.add_alias("TestPlayer", sample_alias)

    updated_alias = Alias(name="N", command="go west")
    result = alias_storage.add_alias("TestPlayer", updated_alias)
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1
    assert aliases[0].command == "go west"


def test_remove_alias_existing(alias_storage: AliasStorage, sample_alias: Alias, sample_alias2: Alias) -> None:
    """Test remove_alias removes existing alias."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias, sample_alias2])

    result = alias_storage.remove_alias("TestPlayer", "n")
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1
    assert aliases[0].name == "s"


def test_remove_alias_nonexistent(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test remove_alias returns False for nonexistent alias."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    result = alias_storage.remove_alias("TestPlayer", "nonexistent")
    assert result is False

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1


def test_remove_alias_case_insensitive(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test remove_alias is case-insensitive."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    result = alias_storage.remove_alias("TestPlayer", "N")
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 0


def test_get_alias_existing(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test get_alias returns existing alias."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    alias = alias_storage.get_alias("TestPlayer", "n")
    assert alias is not None
    assert alias.name == "n"
    assert alias.command == "go north"


def test_get_alias_nonexistent(alias_storage: AliasStorage) -> None:
    """Test get_alias returns None for nonexistent alias."""
    alias = alias_storage.get_alias("TestPlayer", "nonexistent")
    assert alias is None


def test_get_alias_case_insensitive(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test get_alias is case-insensitive."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    alias = alias_storage.get_alias("TestPlayer", "N")
    assert alias is not None
    assert alias.name == "n"


def test_clear_aliases(alias_storage: AliasStorage, sample_alias: Alias, sample_alias2: Alias) -> None:
    """Test clear_aliases removes all aliases."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias, sample_alias2])

    result = alias_storage.clear_aliases("TestPlayer")
    assert result is True

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 0


def test_get_alias_count(alias_storage: AliasStorage, sample_alias: Alias, sample_alias2: Alias) -> None:
    """Test get_alias_count returns correct count."""
    assert alias_storage.get_alias_count("TestPlayer") == 0

    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])
    assert alias_storage.get_alias_count("TestPlayer") == 1

    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias, sample_alias2])
    assert alias_storage.get_alias_count("TestPlayer") == 2


def test_validate_alias_name_valid(alias_storage: AliasStorage) -> None:
    """Test validate_alias_name accepts valid names."""
    assert alias_storage.validate_alias_name("test") is True
    assert alias_storage.validate_alias_name("test_alias") is True
    assert alias_storage.validate_alias_name("Test123") is True


def test_validate_alias_name_empty(alias_storage: AliasStorage) -> None:
    """Test validate_alias_name rejects empty names."""
    assert alias_storage.validate_alias_name("") is False


def test_validate_alias_name_too_long(alias_storage: AliasStorage) -> None:
    """Test validate_alias_name rejects names longer than 20 characters."""
    long_name = "a" * 21
    assert alias_storage.validate_alias_name(long_name) is False


def test_validate_alias_name_reserved(alias_storage: AliasStorage) -> None:
    """Test validate_alias_name rejects reserved commands."""
    assert alias_storage.validate_alias_name("alias") is False
    assert alias_storage.validate_alias_name("aliases") is False
    assert alias_storage.validate_alias_name("unalias") is False
    assert alias_storage.validate_alias_name("help") is False


def test_validate_alias_name_invalid_format(alias_storage: AliasStorage) -> None:
    """Test validate_alias_name rejects invalid formats."""
    assert alias_storage.validate_alias_name("123test") is False  # Starts with number
    assert alias_storage.validate_alias_name("test-alias") is False  # Contains hyphen
    assert alias_storage.validate_alias_name("test alias") is False  # Contains space


def test_validate_alias_command_valid(alias_storage: AliasStorage) -> None:
    """Test validate_alias_command accepts valid commands."""
    assert alias_storage.validate_alias_command("go north") is True
    assert alias_storage.validate_alias_command("look at item") is True


def test_validate_alias_command_empty(alias_storage: AliasStorage) -> None:
    """Test validate_alias_command rejects empty commands."""
    assert alias_storage.validate_alias_command("") is False


def test_validate_alias_command_too_long(alias_storage: AliasStorage) -> None:
    """Test validate_alias_command rejects commands longer than 200 characters."""
    long_command = "a" * 201
    assert alias_storage.validate_alias_command(long_command) is False


def test_validate_alias_command_reserved(alias_storage: AliasStorage) -> None:
    """Test validate_alias_command rejects reserved commands."""
    assert alias_storage.validate_alias_command("alias") is False
    assert alias_storage.validate_alias_command("aliases") is False
    assert alias_storage.validate_alias_command("unalias") is False
    assert alias_storage.validate_alias_command("help") is False


def test_validate_alias_command_starts_with_reserved(alias_storage: AliasStorage) -> None:
    """Test validate_alias_command rejects commands starting with reserved words."""
    assert alias_storage.validate_alias_command("alias test") is False
    assert alias_storage.validate_alias_command("help me") is False


def test_create_alias_success(alias_storage: AliasStorage) -> None:
    """Test create_alias successfully creates an alias."""
    alias = alias_storage.create_alias("TestPlayer", "n", "go north")
    assert alias is not None
    assert alias.name == "n"
    assert alias.command == "go north"

    aliases = alias_storage.get_player_aliases("TestPlayer")
    assert len(aliases) == 1


def test_create_alias_invalid_name(alias_storage: AliasStorage) -> None:
    """Test create_alias returns None for invalid name."""
    alias = alias_storage.create_alias("TestPlayer", "123invalid", "go north")
    assert alias is None


def test_create_alias_invalid_command(alias_storage: AliasStorage) -> None:
    """Test create_alias returns None for invalid command."""
    alias = alias_storage.create_alias("TestPlayer", "n", "")
    assert alias is None


def test_create_alias_limit_reached(alias_storage: AliasStorage) -> None:
    """Test create_alias returns None when alias limit is reached."""
    # Create 50 aliases
    for i in range(50):
        assert alias_storage.create_alias("TestPlayer", f"alias{i}", f"command{i}")

    # Try to create one more
    alias = alias_storage.create_alias("TestPlayer", "extra", "command")
    assert alias is None


def test_list_alias_files_empty(alias_storage: AliasStorage) -> None:
    """Test list_alias_files returns empty list when no files exist."""
    files = alias_storage.list_alias_files()
    assert files == []


def test_list_alias_files_with_files(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test list_alias_files returns list of player names."""
    assert alias_storage.save_player_aliases("Player1", [sample_alias])
    assert alias_storage.save_player_aliases("Player2", [sample_alias])

    files = alias_storage.list_alias_files()
    assert len(files) == 2
    assert "Player1" in files
    assert "Player2" in files


def test_delete_player_aliases_existing(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test delete_player_aliases removes alias file."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])
    file_path = alias_storage.get_alias_file_path("TestPlayer")
    assert file_path.exists()

    result = alias_storage.delete_player_aliases("TestPlayer")
    assert result is True
    assert not file_path.exists()


def test_delete_player_aliases_nonexistent(alias_storage: AliasStorage) -> None:
    """Test delete_player_aliases returns True for nonexistent file."""
    result = alias_storage.delete_player_aliases("TestPlayer")
    assert result is True


def test_delete_player_aliases_io_error(
    alias_storage: AliasStorage, sample_alias: Alias, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test delete_player_aliases handles IO errors."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    def mock_unlink(*_args: object, **_kwargs: object) -> None:
        raise OSError("Permission denied")

    monkeypatch.setattr(Path, "unlink", mock_unlink)

    result = alias_storage.delete_player_aliases("TestPlayer")
    assert result is False


def test_backup_aliases_success(alias_storage: AliasStorage, sample_alias: Alias) -> None:
    """Test backup_aliases creates backup file."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    result = alias_storage.backup_aliases("TestPlayer")
    assert result is True

    backup_dir = alias_storage.storage_dir / "backups"
    backup_file = backup_dir / "TestPlayer_aliases_backup.json"
    assert backup_file.exists()


def test_backup_aliases_custom_dir(alias_storage: AliasStorage, sample_alias: Alias, temp_storage_dir: Path) -> None:
    """Test backup_aliases uses custom backup directory."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    custom_backup_dir = str(temp_storage_dir / "custom_backups")
    result = alias_storage.backup_aliases("TestPlayer", backup_dir=custom_backup_dir)
    assert result is True

    backup_file = Path(custom_backup_dir) / "TestPlayer_aliases_backup.json"
    assert backup_file.exists()


def test_backup_aliases_nonexistent_file(alias_storage: AliasStorage) -> None:
    """Test backup_aliases returns False for nonexistent file."""
    result = alias_storage.backup_aliases("TestPlayer")
    assert result is False


def test_backup_aliases_io_error(
    alias_storage: AliasStorage, sample_alias: Alias, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test backup_aliases handles IO errors."""
    assert alias_storage.save_player_aliases("TestPlayer", [sample_alias])

    def mock_copy2(*_args: object, **_kwargs: object) -> None:
        raise OSError("Permission denied")

    monkeypatch.setattr("shutil.copy2", mock_copy2)

    result = alias_storage.backup_aliases("TestPlayer")
    assert result is False


def test_validate_alias_payload_no_validator(alias_storage: AliasStorage) -> None:
    """Test _validate_alias_payload returns empty list when validator unavailable."""
    with patch("server.alias_storage._get_alias_validator", return_value=None):
        data: AliasPayload = {"version": "1.0", "aliases": []}
        errors = alias_storage._validate_alias_payload(data, Path("test.json"))
        assert errors == []


def test_validate_alias_payload_with_validator(alias_storage: AliasStorage) -> None:
    """Test _validate_alias_payload uses validator when available."""
    # Typed locals: MagicMock attribute access is Any under basedpyright reportAny.
    validate_alias_bundle: MagicMock = MagicMock(return_value=["Error 1", "Error 2"])
    mock_validator: MagicMock = MagicMock()
    mock_validator.validate_alias_bundle = validate_alias_bundle

    with patch("server.alias_storage._get_alias_validator", return_value=mock_validator):
        data: AliasPayload = {"version": "1.0", "aliases": []}
        errors = alias_storage._validate_alias_payload(data, Path("test.json"))
        assert errors == ["Error 1", "Error 2"]
        validate_alias_bundle.assert_called_once_with(data, "test.json")


def test_get_alias_validator_caching():
    """Test _get_alias_validator caches the validator."""
    import server.alias_storage

    cache = server.alias_storage._alias_validator_cache
    original_validator = cache.validator
    original_failed = cache.import_failed
    try:
        cache.validator = None
        cache.import_failed = False
        with patch("schemas.validator.create_validator") as mock_create:
            mock_validator = MagicMock()
            mock_create.return_value = mock_validator

            validator1 = server.alias_storage._get_alias_validator()
            assert validator1 == mock_validator
            assert mock_create.call_count == 1

            validator2 = server.alias_storage._get_alias_validator()
            assert validator2 == mock_validator
            assert mock_create.call_count == 1
    finally:
        cache.validator = original_validator
        cache.import_failed = original_failed


def test_get_alias_validator_import_failure():
    """Test _get_alias_validator returns None when import has previously failed."""
    import server.alias_storage

    cache = server.alias_storage._alias_validator_cache
    original_validator = cache.validator
    original_failed = cache.import_failed
    try:
        cache.validator = None
        cache.import_failed = True

        validator = server.alias_storage._get_alias_validator()
        assert validator is None

        validator2 = server.alias_storage._get_alias_validator()
        assert validator2 is None
    finally:
        cache.validator = original_validator
        cache.import_failed = original_failed


def test_get_alias_validator_creation_failure():
    """Test _get_alias_validator handles validator creation failure."""
    import server.alias_storage

    cache = server.alias_storage._alias_validator_cache
    original_validator = cache.validator
    original_failed = cache.import_failed
    try:
        cache.validator = None
        cache.import_failed = False
        with patch("schemas.validator.create_validator", side_effect=Exception("Creation failed")):
            validator = server.alias_storage._get_alias_validator()
            assert validator is None
    finally:
        cache.validator = original_validator
        cache.import_failed = original_failed
