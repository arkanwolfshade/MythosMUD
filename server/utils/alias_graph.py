"""
Alias circular dependency detection using graph analysis.

This module provides graph-based detection of circular dependencies in alias expansions,
preventing alias bombs and infinite recursion attacks.

AI: This implements DFS-based cycle detection to prevent recursive alias expansion attacks.
"""

import re

import networkx as nx

from ..alias_storage import AliasStorage
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class AliasGraph:
    """
    Graph-based circular dependency detection for alias expansion.

    Uses depth-first search (via networkx) to detect cycles before expansion.
    This prevents "alias bombs" where recursive aliases create infinite loops.

    AI: This is a critical security component preventing DoS via recursive aliases.
    """

    def __init__(self, alias_storage: AliasStorage):
        """
        Initialize alias graph analyzer.

        Args:
            alias_storage: Storage backend containing player aliases
        """
        self.alias_storage = alias_storage
        self.graph: nx.DiGraph = nx.DiGraph()
        logger.debug("AliasGraph initialized")

    def build_graph(self, player_name: str) -> None:
        """
        Build dependency graph for a player's aliases.

        Creates a directed graph where edges represent alias dependencies.
        For example, if alias "a" expands to "b", we create edge a→b.

        Args:
            player_name: Player whose aliases to analyze

        AI: Constructs the alias dependency graph for cycle detection.
        """
        aliases = self.alias_storage.get_player_aliases(player_name)

        for alias in aliases:
            self.graph.add_node(alias.name)

            # Parse alias command to find referenced aliases
            referenced = self._extract_alias_references(alias.command)

            for ref in referenced:
                self.graph.add_edge(alias.name, ref)
                logger.debug("Added alias dependency edge", player=player_name, from_alias=alias.name, to_alias=ref)

    def _extract_alias_references(self, command: str) -> list[str]:
        """
        Extract potential alias names from a command string.

        Looks for words that could be alias names at the start of the command
        or after command separators (;, &&, ||).

        Args:
            command: Command string to analyze

        Returns:
            List of potential alias names referenced in the command

        AI: Simple word extraction - could be enhanced with better command parsing.
        """
        # Split command by common separators
        parts = re.split(r"[;&|]+", command)

        potential_aliases = []
        for part in parts:
            # Get first word (potential command/alias)
            words = part.strip().split()
            if words:
                potential_aliases.append(words[0])

        return potential_aliases

    def detect_cycle(self, alias_name: str) -> list[str] | None:
        """
        Detect if expanding this alias would create a cycle.

        Uses networkx's cycle detection algorithm (DFS-based).

        Args:
            alias_name: Name of alias to check

        Returns:
            List of alias names forming the cycle if found, None otherwise

        AI: Returns the actual cycle path for debugging and user feedback.
        """
        try:
            # Check if node exists in graph
            if alias_name not in self.graph:
                return None

            cycle = nx.find_cycle(self.graph, source=alias_name, orientation="original")
            cycle_path = [edge[0] for edge in cycle]

            logger.warning("Circular alias dependency detected", alias=alias_name, cycle=cycle_path)

            return cycle_path

        except nx.NetworkXNoCycle:
            return None
        except nx.NodeNotFound:
            # Node doesn't exist in graph
            return None

    def is_safe_to_expand(self, alias_name: str) -> bool:
        """
        Check if alias can be safely expanded without creating cycles.

        Args:
            alias_name: Name of alias to check

        Returns:
            True if safe to expand, False if would create cycle

        AI: Primary safety check - call this before expanding any alias.
        """
        cycle = self.detect_cycle(alias_name)
        is_safe = cycle is None

        if not is_safe:
            logger.warning("Alias expansion blocked due to circular dependency", alias=alias_name, cycle=cycle)

        return is_safe

    def get_expansion_depth(self, alias_name: str) -> int:
        """
        Calculate maximum expansion depth for an alias.

        Returns the length of the longest path from this alias to a leaf node.
        Useful for detecting deeply nested (but non-circular) aliases.

        Args:
            alias_name: Name of alias to analyze

        Returns:
            Maximum depth of alias expansion chain

        AI: Additional safety metric - can set limits on expansion depth.
        """
        if alias_name not in self.graph:
            return 0

        try:
            # Get all simple paths from this alias
            descendants = nx.descendants(self.graph, alias_name)
            if not descendants:
                return 1

            max_depth = 0
            for desc in descendants:
                try:
                    paths = list(nx.all_simple_paths(self.graph, alias_name, desc))
                    if paths:
                        max_depth = max(max_depth, max(len(p) for p in paths))
                except nx.NetworkXNoPath:
                    continue

            return max_depth

        except (nx.NetworkXException, KeyError, ValueError) as e:
            logger.error("Error calculating expansion depth", alias=alias_name, error=str(e))
            return 0

    def clear(self) -> None:
        """Clear the dependency graph."""
        self.graph.clear()
        logger.debug("AliasGraph cleared")
