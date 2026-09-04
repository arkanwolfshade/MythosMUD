"""
Unit tests for alias_graph utilities.

Tests the AliasGraph class.
"""

from unittest.mock import MagicMock

from server.utils.alias_graph import AliasGraph


def test_alias_graph_init():
    """Test AliasGraph initialization."""
    mock_storage = MagicMock()
    graph = AliasGraph(mock_storage)
    assert graph.alias_storage == mock_storage
    assert len(graph.graph.nodes) == 0


def test_alias_graph_build_graph():
    """Test AliasGraph.build_graph() builds dependency graph."""
    mock_storage = MagicMock()
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_storage.get_player_aliases.return_value = [mock_alias]

    graph = AliasGraph(mock_storage)
    graph.build_graph("player1")
    assert "n" in graph.graph


def test_alias_graph_detect_cycle_no_cycle():
    """Test AliasGraph.detect_cycle() returns None when no cycle."""
    mock_storage = MagicMock()
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_storage.get_player_aliases.return_value = [mock_alias]

    graph = AliasGraph(mock_storage)
    graph.build_graph("player1")
    result = graph.detect_cycle("n")
    assert result is None


def test_alias_graph_is_safe_to_expand():
    """Test AliasGraph.is_safe_to_expand() returns True when safe."""
    mock_storage = MagicMock()
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_storage.get_player_aliases.return_value = [mock_alias]

    graph = AliasGraph(mock_storage)
    graph.build_graph("player1")
    result = graph.is_safe_to_expand("n")
    assert result is True


def test_alias_graph_get_expansion_depth():
    """Test AliasGraph.get_expansion_depth() returns depth."""
    mock_storage = MagicMock()
    mock_alias = MagicMock()
    mock_alias.name = "n"
    mock_alias.command = "go north"
    mock_storage.get_player_aliases.return_value = [mock_alias]

    graph = AliasGraph(mock_storage)
    graph.build_graph("player1")
    depth = graph.get_expansion_depth("n")
    assert depth >= 0


def test_alias_graph_clear():
    """Test AliasGraph.clear() clears the graph."""
    mock_storage = MagicMock()
    graph = AliasGraph(mock_storage)
    graph.build_graph("player1")
    graph.clear()
    assert len(graph.graph.nodes) == 0
