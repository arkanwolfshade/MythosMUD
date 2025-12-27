"""
Unit tests for alias graph circular dependency detection.

Tests the AliasGraph class for detecting circular dependencies in alias expansions.
"""

from unittest.mock import MagicMock

import pytest

from server.utils.alias_graph import AliasGraph


@pytest.fixture
def mock_alias_storage():
    """Create a mock alias storage."""
    storage = MagicMock()
    storage.get_player_aliases = MagicMock(return_value=[])
    return storage


@pytest.fixture
def alias_graph(mock_alias_storage):
    """Create an AliasGraph instance."""
    return AliasGraph(mock_alias_storage)


def test_alias_graph_initialization(alias_graph, mock_alias_storage):
    """Test AliasGraph initialization."""
    assert alias_graph.alias_storage == mock_alias_storage
    assert alias_graph.graph is not None
    assert len(alias_graph.graph.nodes) == 0


def test_build_graph_no_aliases(alias_graph, mock_alias_storage):
    """Test build_graph with no aliases."""
    mock_alias_storage.get_player_aliases.return_value = []
    
    alias_graph.build_graph("TestPlayer")
    
    assert len(alias_graph.graph.nodes) == 0
    assert len(alias_graph.graph.edges) == 0


def test_build_graph_single_alias(alias_graph, mock_alias_storage):
    """Test build_graph with a single alias."""
    mock_alias = MagicMock()
    mock_alias.name = "go_north"
    mock_alias.command = "go north"
    mock_alias_storage.get_player_aliases.return_value = [mock_alias]
    
    alias_graph.build_graph("TestPlayer")
    
    assert "go_north" in alias_graph.graph.nodes
    # The alias references "go" (first word of command), so there should be an edge
    assert len(alias_graph.graph.edges) == 1
    assert ("go_north", "go") in alias_graph.graph.edges


def test_build_graph_alias_references_other_alias(alias_graph, mock_alias_storage):
    """Test build_graph when an alias references another alias."""
    mock_alias1 = MagicMock()
    mock_alias1.name = "n"
    mock_alias1.command = "go_north"
    
    mock_alias2 = MagicMock()
    mock_alias2.name = "go_north"
    mock_alias2.command = "go north"
    
    mock_alias_storage.get_player_aliases.return_value = [mock_alias1, mock_alias2]
    
    alias_graph.build_graph("TestPlayer")
    
    assert "n" in alias_graph.graph.nodes
    assert "go_north" in alias_graph.graph.nodes
    assert ("n", "go_north") in alias_graph.graph.edges


def test_extract_alias_references_simple_command(alias_graph):
    """Test _extract_alias_references with a simple command."""
    result = alias_graph._extract_alias_references("go north")
    assert result == ["go"]


def test_extract_alias_references_multiple_commands(alias_graph):
    """Test _extract_alias_references with multiple commands separated by semicolon."""
    result = alias_graph._extract_alias_references("go north; look")
    assert "go" in result
    assert "look" in result


def test_extract_alias_references_with_and(alias_graph):
    """Test _extract_alias_references with && separator."""
    result = alias_graph._extract_alias_references("go north && look")
    assert "go" in result
    assert "look" in result


def test_extract_alias_references_with_or(alias_graph):
    """Test _extract_alias_references with || separator."""
    result = alias_graph._extract_alias_references("go north || look")
    assert "go" in result
    assert "look" in result


def test_detect_cycle_no_cycle(alias_graph, mock_alias_storage):
    """Test detect_cycle when no cycle exists."""
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_alias_storage.get_player_aliases.return_value = [mock_alias]
    
    alias_graph.build_graph("TestPlayer")
    
    result = alias_graph.detect_cycle("n")
    assert result is None


def test_detect_cycle_simple_cycle(alias_graph, mock_alias_storage):
    """Test detect_cycle with a simple circular dependency."""
    mock_alias1 = MagicMock()
    mock_alias1.name = "a"
    mock_alias1.command = "b"
    
    mock_alias2 = MagicMock()
    mock_alias2.name = "b"
    mock_alias2.command = "a"
    
    mock_alias_storage.get_player_aliases.return_value = [mock_alias1, mock_alias2]
    
    alias_graph.build_graph("TestPlayer")
    
    result = alias_graph.detect_cycle("a")
    assert result is not None
    assert "a" in result
    assert "b" in result


def test_detect_cycle_node_not_in_graph(alias_graph):
    """Test detect_cycle when node is not in graph."""
    result = alias_graph.detect_cycle("nonexistent")
    assert result is None


def test_is_safe_to_expand_safe(alias_graph, mock_alias_storage):
    """Test is_safe_to_expand when alias is safe."""
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_alias_storage.get_player_aliases.return_value = [mock_alias]
    
    alias_graph.build_graph("TestPlayer")
    
    assert alias_graph.is_safe_to_expand("n") is True


def test_is_safe_to_expand_unsafe(alias_graph, mock_alias_storage):
    """Test is_safe_to_expand when alias would create cycle."""
    mock_alias1 = MagicMock()
    mock_alias1.name = "a"
    mock_alias1.command = "b"
    
    mock_alias2 = MagicMock()
    mock_alias2.name = "b"
    mock_alias2.command = "a"
    
    mock_alias_storage.get_player_aliases.return_value = [mock_alias1, mock_alias2]
    
    alias_graph.build_graph("TestPlayer")
    
    assert alias_graph.is_safe_to_expand("a") is False


def test_get_expansion_depth_no_node(alias_graph):
    """Test get_expansion_depth when node is not in graph."""
    result = alias_graph.get_expansion_depth("nonexistent")
    assert result == 0


def test_get_expansion_depth_single_node(alias_graph, mock_alias_storage):
    """Test get_expansion_depth with a single node."""
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_alias_storage.get_player_aliases.return_value = [mock_alias]
    
    alias_graph.build_graph("TestPlayer")
    
    result = alias_graph.get_expansion_depth("n")
    assert result >= 1


def test_get_expansion_depth_chain(alias_graph, mock_alias_storage):
    """Test get_expansion_depth with a chain of aliases."""
    mock_alias1 = MagicMock()
    mock_alias1.name = "a"
    mock_alias1.command = "b"
    
    mock_alias2 = MagicMock()
    mock_alias2.name = "b"
    mock_alias2.command = "go north"
    
    mock_alias_storage.get_player_aliases.return_value = [mock_alias1, mock_alias2]
    
    alias_graph.build_graph("TestPlayer")
    
    result = alias_graph.get_expansion_depth("a")
    assert result >= 2


def test_clear(alias_graph, mock_alias_storage):
    """Test clear method."""
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_alias_storage.get_player_aliases.return_value = [mock_alias]
    
    alias_graph.build_graph("TestPlayer")
    assert len(alias_graph.graph.nodes) > 0
    
    alias_graph.clear()
    assert len(alias_graph.graph.nodes) == 0
    assert len(alias_graph.graph.edges) == 0
