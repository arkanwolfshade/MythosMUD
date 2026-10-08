"""
Help content for MythosMUD.

The documentation itself lives in ``commands.json`` and ``guides.json`` beside this module, validated against
``help_schema.json``. This module loads them once, filters by role, and renders the HTML shown by the in-game
``help`` command. The authenticated ``/v1/api/help`` endpoint serves the same data to the Manual page.

``details_html`` may only use tags and attributes the client's DOMPurify allowlist keeps (see
``client/src/utils/security.ts``); ``test_help_docs.py`` enforces that.
"""

import json
from collections.abc import Mapping
from difflib import get_close_matches
from functools import lru_cache, partial
from html import escape
from pathlib import Path
from typing import NotRequired, TypedDict, cast

from jsonschema import validate

_HELP_DIR = Path(__file__).parent
_MAX_SUGGESTIONS = 3


class HelpArgument(TypedDict):
    """One documented command argument."""

    name: str
    required: bool
    description: str


class HelpExample(TypedDict):
    """One example invocation with an optional explanation."""

    input: str
    note: NotRequired[str]


class CommandDoc(TypedDict):
    """Documentation for one player-facing command. Optional authored fields are always present (empty by default)."""

    name: str
    category: str
    summary: str
    usage: list[str]
    aliases: list[str]
    admin_only: bool
    arguments: list[HelpArgument]
    examples: list[HelpExample]
    see_also: list[str]
    details_html: list[str]


class GuideDoc(TypedDict):
    """A concept guide, reachable as ``help <id>`` and on the Manual page. Optional fields are always present."""

    id: str
    title: str
    group: str
    summary: str
    see_also: list[str]
    details_html: list[str]


class _RawCommand(TypedDict):
    """A command as authored in commands.json, where optional fields may be absent."""

    name: str
    category: str
    summary: str
    usage: list[str]
    aliases: NotRequired[list[str]]
    admin_only: NotRequired[bool]
    arguments: NotRequired[list[HelpArgument]]
    examples: NotRequired[list[HelpExample]]
    see_also: NotRequired[list[str]]
    details_html: NotRequired[list[str]]


class _RawGuide(TypedDict):
    """A guide as authored in guides.json, where optional fields may be absent."""

    id: str
    title: str
    group: str
    summary: str
    see_also: NotRequired[list[str]]
    details_html: NotRequired[list[str]]


class HelpDocs(TypedDict):
    """Everything the help system documents."""

    commands: list[CommandDoc]
    guides: list[GuideDoc]


def _read_json(filename: str) -> Mapping[str, object]:
    return cast(Mapping[str, object], json.loads((_HELP_DIR / filename).read_text(encoding="utf-8")))


def _complete_command(raw: _RawCommand) -> CommandDoc:
    return {
        "name": raw["name"],
        "category": raw["category"],
        "summary": raw["summary"],
        "usage": raw["usage"],
        "aliases": raw.get("aliases", []),
        "admin_only": raw.get("admin_only", False),
        "arguments": raw.get("arguments", []),
        "examples": raw.get("examples", []),
        "see_also": raw.get("see_also", []),
        "details_html": raw.get("details_html", []),
    }


def _complete_guide(raw: _RawGuide) -> GuideDoc:
    return {
        "id": raw["id"],
        "title": raw["title"],
        "group": raw["group"],
        "summary": raw["summary"],
        "see_also": raw.get("see_also", []),
        "details_html": raw.get("details_html", []),
    }


@lru_cache(maxsize=1)
def load_help_docs() -> HelpDocs:
    """Load and schema-validate the help documentation (cached for the process lifetime)."""
    schema = _read_json("help_schema.json")  # its $schema key selects the draft
    commands_file = _read_json("commands.json")
    guides_file = _read_json("guides.json")
    validate(commands_file, schema)
    validate(guides_file, schema)
    return {
        "commands": [_complete_command(c) for c in cast(list[_RawCommand], commands_file.get("commands", []))],
        "guides": [_complete_guide(g) for g in cast(list[_RawGuide], guides_file.get("guides", []))],
    }


def _visible_names(commands: list[CommandDoc], guides: list[GuideDoc]) -> set[str]:
    names = {guide["id"] for guide in guides}
    for cmd in commands:
        names.add(cmd["name"])
        names.update(cmd["aliases"])
    return names


def _with_visible_see_also[Doc: (CommandDoc, GuideDoc)](doc: Doc, visible: set[str]) -> Doc:
    scrubbed = doc.copy()
    scrubbed["see_also"] = [topic for topic in doc["see_also"] if topic in visible]
    return scrubbed


def get_manual(is_admin: bool = False) -> HelpDocs:
    """Return the documentation a caller may see; admin-only entries are removed for everyone else."""
    docs = load_help_docs()
    commands = [cmd for cmd in docs["commands"] if is_admin or not cmd["admin_only"]]
    guides = docs["guides"]
    visible = _visible_names(commands, guides)
    return {
        "commands": [_with_visible_see_also(cmd, visible) for cmd in commands],
        "guides": [_with_visible_see_also(guide, visible) for guide in guides],
    }


def _e(text: str) -> str:
    return escape(text, quote=False)


def _subhead(text: str) -> str:
    return f'<p class="help-subhead"><strong>{_e(text)}</strong></p>'


def _ul(items: list[str]) -> str:
    return "<ul>\n" + "\n".join(f"<li>{item}</li>" for item in items) + "\n</ul>"


def _see_also_html(see_also: list[str]) -> list[str]:
    if not see_also:
        return []
    return [_subhead("See also"), "<p>" + ", ".join(f"<code>{_e(topic)}</code>" for topic in see_also) + "</p>"]


def _argument_html(arg: HelpArgument) -> str:
    kind = "required" if arg["required"] else "optional"
    return f"<code>{_e(arg['name'])}</code> ({kind}) - {_e(arg['description'])}"


def _example_html(example: HelpExample) -> str:
    note = example.get("note")
    return f"<code>{_e(example['input'])}</code>" + (f" - {_e(note)}" if note else "")


def _format_command(cmd: CommandDoc) -> str:
    title = f"<strong>{_e(cmd['name'].upper())}</strong>"
    if cmd["aliases"]:
        title += f' <span class="help-aliases">(also: {_e(", ".join(cmd["aliases"]))})</span>'
    parts = ['<div class="help-entry">', f'<p class="help-title">{title}</p>', f"<p>{_e(cmd['summary'])}</p>"]
    parts += [_subhead("Usage"), _ul([f"<code>{_e(usage)}</code>" for usage in cmd["usage"]])]
    if cmd["arguments"]:
        parts += [_subhead("Arguments"), _ul([_argument_html(arg) for arg in cmd["arguments"]])]
    if cmd["examples"]:
        parts += [_subhead("Examples"), _ul([_example_html(example) for example in cmd["examples"]])]
    parts += cmd["details_html"]
    parts += _see_also_html(cmd["see_also"])
    parts.append("</div>")
    return "\n".join(parts)


def _format_guide(guide: GuideDoc) -> str:
    title = f"<strong>{_e(guide['title'])}</strong>"
    group = f'<span class="help-aliases">({_e(guide["group"])})</span>'
    parts = [
        '<div class="help-entry">',
        f'<p class="help-title">{title} {group}</p>',
        f"<p>{_e(guide['summary'])}</p>",
        *guide["details_html"],
        *_see_also_html(guide["see_also"]),
        "</div>",
    ]
    return "\n".join(parts)


def _format_index(commands: list[CommandDoc], guides: list[GuideDoc]) -> str:
    by_category: dict[str, list[CommandDoc]] = {}
    for cmd in commands:
        by_category.setdefault(cmd["category"], []).append(cmd)
    parts = [
        '<div class="help-entry">',
        '<p class="help-title"><strong>MythosMUD Help</strong></p>',
        "<p>Welcome to the realm of forbidden knowledge. The commands available to you:</p>",
    ]
    for category, items in by_category.items():
        parts += [_subhead(category), _ul([f"<strong>{_e(c['name'])}</strong> - {_e(c['summary'])}" for c in items])]
    if guides:
        parts += [
            _subhead("Lore & Guidance"),
            _ul([f"<strong>{_e(g['id'])}</strong> - {_e(g['summary'])}" for g in guides]),
        ]
    parts += [
        "<p>For details on any topic, use <code>help &lt;topic&gt;</code> (for example <code>help look</code>).</p>",
        "<p>The full Manual opens in a new tab from the ESC menu.</p>",
        "</div>",
    ]
    return "\n".join(parts)


def _format_not_found(topic: str, candidates: set[str]) -> str:
    parts = [
        '<div class="help-entry">',
        '<p class="help-title"><strong>Topic Not Found</strong></p>',
        f"<p>No help exists for <code>{_e(topic)}</code>.</p>",
    ]
    suggestions = get_close_matches(topic, sorted(candidates), n=_MAX_SUGGESTIONS)
    if suggestions:
        parts.append("<p>Did you mean: " + ", ".join(f"<code>{_e(s)}</code>" for s in suggestions) + "?</p>")
    parts += ["<p>Use <code>help</code> to list every topic.</p>", "</div>"]
    return "\n".join(parts)


def get_help_content(topic: str | None = None, *, is_admin: bool = False) -> str:
    """
    Render help as allowlisted HTML.

    Args:
        topic: Command name, command alias, or guide id; None for the index.
        is_admin: Whether admin-only commands may be shown.

    Returns:
        HTML for the game log. Unknown (or admin-only, for non-admins) topics yield a not-found notice.
    """
    manual = get_manual(is_admin)
    commands, guides = manual["commands"], manual["guides"]
    key = (topic or "").strip().lower().lstrip("/")
    if not key:
        return _format_index(commands, guides)
    renderers = {guide["id"]: partial(_format_guide, guide) for guide in guides}
    renderers |= {name: partial(_format_command, cmd) for cmd in commands for name in (cmd["name"], *cmd["aliases"])}
    render = renderers.get(key)
    return render() if render else _format_not_found(key, set(renderers))
