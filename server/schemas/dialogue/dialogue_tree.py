"""Nav-only dialogue tree schema for #583.

Rejects unknown next targets, missing start, and empty nodes on write.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, model_validator


class DialogueOption(BaseModel):
    """Player-facing option; next null/omitted ends the conversation."""

    label: str = Field(min_length=1)
    # Empty string is accidental; null/omitted ends the conversation.
    next: str | None = Field(default=None, min_length=1)


class DialogueNode(BaseModel):
    """One NPC line plus numbered options."""

    text: str = Field(min_length=1)
    options: list[DialogueOption] = Field(default_factory=list)


class DialogueTree(BaseModel):
    """Root tree: start node id and nodes map."""

    start: str = Field(min_length=1)
    nodes: dict[str, DialogueNode] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_graph(self) -> DialogueTree:
        """Ensure start exists and every option next points at a known node or null."""
        if self.start not in self.nodes:
            raise ValueError(f"start node '{self.start}' is not in nodes")
        # pylint: disable=no-member  # Reason: Pydantic instance field; pylint sees FieldInfo on class attr
        for node_id, node in self.nodes.items():
            for option in node.options:
                if option.next is not None and option.next not in self.nodes:
                    raise ValueError(f"node '{node_id}' option '{option.label}' next '{option.next}' is unknown")
        return self
