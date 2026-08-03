"""In-memory dialogue session service for classic MUD talk (#583).

Loads trees by NPC definition id; session cursor is (player_id -> npc/node).
Cleared on leave room, other NPC, or end (next null).
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from server.persistence.repositories.dialogue_definition_repository import DialogueDefinitionRepository
from server.schemas.dialogue import DialogueTree
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class DialogueCursor:
    """Active conversation position for one player."""

    npc_id: str
    npc_name: str
    npc_definition_id: int
    node_id: str
    dialogue_id: str


@dataclass
class DialoguePrompt:
    """Formatted NPC line plus numbered option labels for the player."""

    text: str
    options: list[str]
    ended: bool = False


def format_dialogue_prompt(npc_name: str, node_text: str, option_labels: list[str]) -> str:
    """Build personal-system message body for a dialogue node."""
    lines = [f'{npc_name} says: "{node_text}"']
    if option_labels:
        lines.append("")
        for i, label in enumerate(option_labels, start=1):
            lines.append(f"{i}. {label}")
        lines.append("")
        lines.append("Use: talk <number>")
    return "\n".join(lines)


class DialogueService:
    """Load dialogue trees and track per-player session cursors."""

    def __init__(self, repository: DialogueDefinitionRepository | None = None) -> None:
        self._repo: DialogueDefinitionRepository = repository or DialogueDefinitionRepository()
        self._cursors: dict[str, DialogueCursor] = {}

    @staticmethod
    def _player_key(player_id: uuid.UUID | str) -> str:
        return str(player_id)

    def clear_cursor(self, player_id: uuid.UUID | str) -> None:
        """Drop the player's dialogue cursor if any."""
        _ = self._cursors.pop(self._player_key(player_id), None)

    def get_cursor(self, player_id: uuid.UUID | str) -> DialogueCursor | None:
        """Return active cursor or None."""
        return self._cursors.get(self._player_key(player_id))

    async def start_with_npc(
        self,
        player_id: uuid.UUID | str,
        *,
        npc_id: str,
        npc_name: str,
        npc_definition_id: int,
    ) -> DialoguePrompt | str:
        """
        Begin (or restart) dialogue with an NPC.

        Returns DialoguePrompt on success, or an error string.
        """
        row = await self._repo.get_by_npc_definition_id(npc_definition_id)
        if not row:
            return f"{npc_name} has nothing to say."
        try:
            tree = DialogueTree.model_validate(row.definition)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: invalid DB trees must not crash talk
            logger.warning(
                "Invalid dialogue tree",
                dialogue_id=row.id,
                error=str(e),
            )
            return f"{npc_name} seems confused and falls silent."
        return self._present_node(
            player_id,
            tree=tree,
            dialogue_id=row.id,
            node_id=tree.start,
            npc_id=npc_id,
            npc_name=npc_name,
            npc_definition_id=npc_definition_id,
        )

    async def choose_option(self, player_id: uuid.UUID | str, option_index: int) -> DialoguePrompt | str:
        """
        Advance from the current cursor by 1-based option index.

        Returns DialoguePrompt, or an error string.
        """
        cursor = self.get_cursor(player_id)
        if not cursor:
            return "You are not in a conversation. Use: talk <npc>"
        row = await self._repo.get_by_id(cursor.dialogue_id)
        if not row:
            self.clear_cursor(player_id)
            return "The conversation fades."
        try:
            tree = DialogueTree.model_validate(row.definition)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: invalid DB trees must not crash talk
            logger.warning("Invalid dialogue tree", dialogue_id=row.id, error=str(e))
            self.clear_cursor(player_id)
            return "The conversation fades."
        node = tree.nodes.get(cursor.node_id)
        if not node:
            self.clear_cursor(player_id)
            return "The conversation fades."
        if option_index < 1 or option_index > len(node.options):
            return (
                f"Choose a number from 1 to {len(node.options)}." if node.options else "There is nothing more to say."
            )
        chosen = node.options[option_index - 1]
        if chosen.next is None:
            self.clear_cursor(player_id)
            return DialoguePrompt(text="The conversation ends.", options=[], ended=True)
        return self._present_node(
            player_id,
            tree=tree,
            dialogue_id=cursor.dialogue_id,
            node_id=chosen.next,
            npc_id=cursor.npc_id,
            npc_name=cursor.npc_name,
            npc_definition_id=cursor.npc_definition_id,
        )

    def _present_node(
        self,
        player_id: uuid.UUID | str,
        *,
        tree: DialogueTree,
        dialogue_id: str,
        node_id: str,
        npc_id: str,
        npc_name: str,
        npc_definition_id: int,
    ) -> DialoguePrompt | str:
        """Set cursor and build prompt for node_id."""
        node = tree.nodes.get(node_id)
        if not node:
            self.clear_cursor(player_id)
            return "The conversation fades."
        self._cursors[self._player_key(player_id)] = DialogueCursor(
            npc_id=npc_id,
            npc_name=npc_name,
            npc_definition_id=npc_definition_id,
            node_id=node_id,
            dialogue_id=dialogue_id,
        )
        labels = [opt.label for opt in node.options]
        return DialoguePrompt(text=node.text, options=labels, ended=False)


# Module singleton used by talk command and go command (session-scoped).
_dialogue_service: DialogueService | None = None  # pylint: disable=invalid-name  # Reason: module singleton


def get_dialogue_service() -> DialogueService:
    """Return process-wide DialogueService singleton."""
    global _dialogue_service  # pylint: disable=global-statement  # Reason: session singleton for talk cursors
    if _dialogue_service is None:
        _dialogue_service = DialogueService()
    return _dialogue_service


def reset_dialogue_service_for_tests(  # lizard: allow tiny single-use (test singleton reset)
    service: DialogueService | None = None,
) -> None:
    """Replace or clear the singleton (unit tests only)."""
    global _dialogue_service  # pylint: disable=global-statement  # Reason: test isolation
    _dialogue_service = service
