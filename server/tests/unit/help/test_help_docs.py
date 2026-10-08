"""
Tests for the JSON-backed help documentation (server/help/commands.json, guides.json).

These guard the documentation itself: schema validity, unique topic names, HTML that survives the client
sanitizer, and one documented entry per registered command handler.
"""

# pyright: reportPrivateUsage=false
# Reason: _COMMAND_HANDLERS is the registration table the drift test compares the docs against.

from __future__ import annotations

from html.parser import HTMLParser
from typing import override

import pytest

from server.commands.command_service import _COMMAND_HANDLERS
from server.help import help_content
from server.help.help_content import CommandDoc, GuideDoc, HelpDocs, get_help_content, get_manual, load_help_docs

# Mirrors INCOMING_HTML_DOMPURIFY_CONFIG in client/src/utils/security.ts: anything else is stripped client-side.
ALLOWED_TAGS = frozenset({"b", "i", "em", "strong", "br", "p", "span", "div", "ul", "ol", "li", "code", "pre"})
ALLOWED_ATTRS = frozenset({"class"})


BLOCK_TAGS = frozenset({"p", "ul", "ol", "pre", "div"})
VOID_TAGS = frozenset({"br"})


class _AllowlistChecker(HTMLParser):
    """Collect every tag or attribute the client sanitizer would remove, and text left outside a block element."""

    def __init__(self) -> None:
        super().__init__()
        self.violations: list[str] = []
        self._open: list[str] = []

    @override
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in ALLOWED_TAGS:
            self.violations.append(f"<{tag}>")
        if not self._open and tag not in BLOCK_TAGS:
            self.violations.append(f"top-level <{tag}> (wrap it in <p>)")
        self.violations.extend(f"{tag}[{name}]" for name, _ in attrs if name not in ALLOWED_ATTRS)
        if tag not in VOID_TAGS:
            self._open.append(tag)

    @override
    def handle_endtag(self, tag: str) -> None:
        if tag in self._open:
            while self._open and self._open.pop() != tag:
                pass

    @override
    def handle_data(self, data: str) -> None:
        if data.strip() and not self._open:
            self.violations.append(f"bare text (wrap it in <p>): {data.strip()[:30]!r}")


def _command(
    name: str, *, category: str = "Exploration", admin_only: bool = False, see_also: list[str] | None = None
) -> CommandDoc:
    """A complete synthetic entry: loaded docs always carry every optional list, so test doubles must too."""
    return {
        "name": name,
        "category": category,
        "summary": "Summary.",
        "usage": [name],
        "aliases": [],
        "admin_only": admin_only,
        "arguments": [],
        "examples": [],
        "see_also": see_also or [],
        "details_html": [],
    }


def _violations(html: str) -> list[str]:
    checker = _AllowlistChecker()
    checker.feed(html)
    checker.close()
    return checker.violations


def _fragments() -> list[tuple[str, str]]:
    docs = load_help_docs()
    commands = [(f"command:{cmd['name']}", "\n".join(cmd.get("details_html", []))) for cmd in docs["commands"]]
    guides = [(f"guide:{guide['id']}", "\n".join(guide.get("details_html", []))) for guide in docs["guides"]]
    return commands + guides


def _all_topics(docs: HelpDocs) -> list[str]:
    topics = [guide["id"] for guide in docs["guides"]]
    for cmd in docs["commands"]:
        topics.append(cmd["name"])
        topics.extend(cmd.get("aliases", []))
    return topics


def test_the_documentation_loads_and_validates_against_the_schema() -> None:
    docs = load_help_docs()

    assert docs["commands"]


def test_no_topic_name_is_used_twice() -> None:
    topics = _all_topics(load_help_docs())

    duplicates = sorted({topic for topic in topics if topics.count(topic) > 1})
    assert duplicates == []


def test_see_also_only_points_at_documented_topics() -> None:
    docs = load_help_docs()
    known = set(_all_topics(docs))
    entries: list[CommandDoc | GuideDoc] = [*docs["commands"], *docs["guides"]]

    dangling = {
        (entry.get("name") or entry.get("id"), target)
        for entry in entries
        for target in entry.get("see_also", [])
        if target not in known
    }
    assert dangling == set()


@pytest.mark.parametrize(("label", "html"), _fragments(), ids=[label for label, _ in _fragments()])
def test_details_html_uses_only_what_the_client_sanitizer_keeps(label: str, html: str) -> None:
    assert _violations(html) == [], label


@pytest.mark.parametrize("topic", sorted(set(_all_topics(load_help_docs()))))
def test_every_rendered_entry_uses_only_what_the_client_sanitizer_keeps(topic: str) -> None:
    assert _violations(get_help_content(topic, is_admin=True)) == []


def test_every_registered_handler_is_documented() -> None:
    documented = set(_all_topics(load_help_docs()))

    undocumented = sorted(set(_COMMAND_HANDLERS) - documented)
    assert undocumented == []


def test_every_documented_command_has_a_handler() -> None:
    names = {cmd["name"] for cmd in load_help_docs()["commands"]}

    phantom = sorted(names - set(_COMMAND_HANDLERS))
    assert phantom == []


def test_an_alias_shows_the_same_entry_as_its_command() -> None:
    aliased = [cmd for cmd in load_help_docs()["commands"] if cmd.get("aliases")]

    for cmd in aliased:
        for alias in cmd.get("aliases", []):
            assert get_help_content(alias, is_admin=True) == get_help_content(cmd["name"], is_admin=True)


def test_the_docs_do_not_describe_diagonal_movement() -> None:
    """The game has no diagonal movement. The Direction enum still lists diagonals, so docs must not echo it."""
    docs = load_help_docs()
    text = " ".join(get_help_content(topic, is_admin=True) for topic in _all_topics(docs)).lower()

    for word in ("diagonal", "northeast", "northwest", "southeast", "southwest"):
        assert word not in text, word


def test_the_index_lists_commands_by_category_and_points_at_the_manual() -> None:
    index = get_help_content()

    assert "MythosMUD Help" in index
    assert "<strong>look</strong>" in index
    assert "ESC menu" in index


def test_a_near_miss_gets_suggestions() -> None:
    result = get_help_content("lok")

    assert "Topic Not Found" in result
    assert "<code>look</code>" in result


def test_a_topic_is_matched_without_regard_to_case_or_a_leading_slash() -> None:
    assert get_help_content("/LOOK") == get_help_content("look")


def test_the_topic_is_escaped_in_the_not_found_notice() -> None:
    result = get_help_content("<b>x</b>")

    assert "<b>x</b>" not in result
    assert "&lt;b&gt;x&lt;/b&gt;" in result


def test_admin_commands_are_hidden_from_everyone_else() -> None:
    admin_names = {cmd["name"] for cmd in load_help_docs()["commands"] if cmd.get("admin_only")}
    assert admin_names, "expected at least one admin-only command (npc)"

    player_view = get_manual(is_admin=False)
    admin_view = get_manual(is_admin=True)

    assert admin_names.isdisjoint(cmd["name"] for cmd in player_view["commands"])
    assert admin_names <= {cmd["name"] for cmd in admin_view["commands"]}
    for name in admin_names:
        assert "Topic Not Found" in get_help_content(name)
        assert "Topic Not Found" not in get_help_content(name, is_admin=True)
        assert f"<strong>{name}</strong>" not in get_help_content()
        assert f"<strong>{name}</strong>" in get_help_content(is_admin=True)


def test_hidden_admin_commands_are_not_offered_as_suggestions_or_see_also(monkeypatch: pytest.MonkeyPatch) -> None:
    docs: HelpDocs = {
        "commands": [
            _command("peek", see_also=["secret"]),
            _command("secret", category="Administration", admin_only=True),
        ],
        "guides": [],
    }
    monkeypatch.setattr(help_content, "load_help_docs", lambda: docs)

    assert get_manual(is_admin=False)["commands"][0]["see_also"] == []
    assert get_manual(is_admin=True)["commands"][0]["see_also"] == ["secret"]
    assert "secret" not in get_help_content("secrt")
    assert "<code>secret</code>" in get_help_content("secrt", is_admin=True)
