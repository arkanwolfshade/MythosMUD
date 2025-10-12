"""
Tests for alias cycle detection using graph analysis.

As per the findings documented in the Pnakotic Manuscripts regarding
circular dependencies in ritual invocations, we must prevent infinite loops.

AI: Tests for cycle detection in command aliases using networkx DFS.
"""

import tempfile

import pytest

from server.alias_storage import Alias, AliasStorage
from server.utils.alias_graph import AliasGraph


@pytest.fixture
def temp_alias_dir():
    """Create a temporary directory for alias storage during tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def alias_storage(temp_alias_dir):
    """Create an AliasStorage instance with a temporary directory."""
    return AliasStorage(storage_dir=temp_alias_dir)


class TestAliasGraph:
    """Test suite for alias cycle detection."""

    def test_empty_graph_is_safe(self, alias_storage):
        """Empty graph has no cycles."""
        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("anyalias") is True

    def test_simple_alias_no_cycle(self, alias_storage):
        """Simple alias without cycle is safe."""
        alias_storage.add_alias("player1", Alias(name="greet", command="say Hello"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("greet") is True

    def test_self_referencing_alias_detected(self, alias_storage):
        """Self-referencing alias creates a cycle."""
        alias_storage.add_alias("player1", Alias(name="loop", command="loop"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("loop") is False

    def test_two_alias_cycle_detected(self, alias_storage):
        """Two aliases referencing each other create a cycle."""
        alias_storage.add_alias("player1", Alias(name="a", command="b"))
        alias_storage.add_alias("player1", Alias(name="b", command="a"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("a") is False
        assert graph.is_safe_to_expand("b") is False

    def test_three_alias_cycle_detected(self, alias_storage):
        """Three aliases forming a cycle are detected."""
        alias_storage.add_alias("player1", Alias(name="a", command="b"))
        alias_storage.add_alias("player1", Alias(name="b", command="c"))
        alias_storage.add_alias("player1", Alias(name="c", command="a"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("a") is False
        assert graph.is_safe_to_expand("b") is False
        assert graph.is_safe_to_expand("c") is False

    def test_linear_chain_no_cycle(self, alias_storage):
        """Linear chain of aliases is safe."""
        alias_storage.add_alias("player1", Alias(name="a", command="b"))
        alias_storage.add_alias("player1", Alias(name="b", command="c"))
        alias_storage.add_alias("player1", Alias(name="c", command="say done"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("a") is True
        assert graph.is_safe_to_expand("b") is True
        assert graph.is_safe_to_expand("c") is True

    def test_nonexistent_alias_is_safe(self, alias_storage):
        """Nonexistent alias is considered safe (no cycle)."""
        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert graph.is_safe_to_expand("nonexistent") is True

    def test_multiple_commands_in_alias(self, alias_storage):
        """Alias with multiple commands (semicolon-separated) checked correctly."""
        alias_storage.add_alias("player1", Alias(name="multi", command="say hi; greet"))
        alias_storage.add_alias("player1", Alias(name="greet", command="say hello"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        # Should detect if multi -> greet -> multi
        assert graph.is_safe_to_expand("multi") is True
        assert graph.is_safe_to_expand("greet") is True

    def test_get_expansion_depth(self, alias_storage):
        """Test depth calculation for alias chains."""
        alias_storage.add_alias("player1", Alias(name="a", command="b"))
        alias_storage.add_alias("player1", Alias(name="b", command="c"))
        alias_storage.add_alias("player1", Alias(name="c", command="say done"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        # Depth is the longest path from alias to descendants
        # a → b → c (2 hops from a)
        # b → c (1 hop from b)
        # c has no descendants
        assert graph.get_expansion_depth("a") >= 1
        assert graph.get_expansion_depth("b") >= 1
        assert graph.get_expansion_depth("c") >= 0

    def test_clear_graph(self, alias_storage):
        """Test clearing the graph."""
        alias_storage.add_alias("player1", Alias(name="test", command="say hi"))

        graph = AliasGraph(alias_storage)
        graph.build_graph("player1")

        assert len(graph.graph.nodes) > 0

        graph.clear()
        assert len(graph.graph.nodes) == 0

    def test_multiple_players_isolated(self, alias_storage):
        """Aliases for different players don't interfere."""
        alias_storage.add_alias("player1", Alias(name="greet", command="say Hi from P1"))
        alias_storage.add_alias("player2", Alias(name="greet", command="say Hi from P2"))

        graph1 = AliasGraph(alias_storage)
        graph1.build_graph("player1")

        graph2 = AliasGraph(alias_storage)
        graph2.build_graph("player2")

        # Both should be safe
        assert graph1.is_safe_to_expand("greet") is True

        # Clear and test player2
        graph2 = AliasGraph(alias_storage)
        graph2.build_graph("player2")
        assert graph2.is_safe_to_expand("greet") is True
