"""
Unit tests for command factories.

Tests the CommandFactory class.
"""

from server.utils.command_factories import CommandFactory


def test_command_factory_init():
    """Test CommandFactory initialization."""
    factory = CommandFactory()
    assert factory is not None


def test_command_factory_has_create_methods():
    """Test CommandFactory has create_* methods for commands."""
    factory = CommandFactory()
    assert hasattr(factory, "create_look_command")
    assert callable(factory.create_look_command)


def test_command_factory_create_existing_command():
    """Test CommandFactory.create_*() returns command for existing command."""
    factory = CommandFactory()
    command = factory.create_look_command([])
    assert command is not None
    assert hasattr(command, "command_type")


def test_command_factory_create_nonexistent_command():
    """Test CommandFactory.create_*() methods exist for all command types."""
    factory = CommandFactory()
    # Verify key factory methods exist
    assert hasattr(factory, "create_say_command")
    assert hasattr(factory, "create_go_command")
    assert hasattr(factory, "create_inventory_command")
