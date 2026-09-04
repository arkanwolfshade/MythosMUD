"""One-off idempotent patch: add limbo arena world seed to e2e/unit DML (mirrors mythos_dev)."""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "db"

ARENA_ZONE_LINE = (
    "d2b2dd0e-c126-53db-b832-39b61054b8c6\tlimbo/arena\tarena\tarena\tindoors\t"
    "A gladiator ring suspended in limbo: eleven by eleven cells of sand and shadow, "
    "where combatants are sent from the tutorial or from death. The crowd is unseen "
    "but ever watching.\t[]\t"
    '{"combat_modifier": 1.2, "exploration_bonus": 0, "npc_spawn_modifier": 1, '
    '"lucidity_drain_rate": 0}\n'
)
ARENA_SUBZONE_LINE = (
    "fce4aca2-c973-5c94-a481-cb33f1a1577b\td2b2dd0e-c126-53db-b832-39b61054b8c6\t"
    "arena\tarena\tindoors\tThe arena grid: eleven by eleven cells, north/south/east/west. "
    "Center (5,5) is the entrance and respawn point.\t{}\n"
)
ZONE_CFG_LINE = (
    "65789f9f-34e1-5310-a6f5-04679546662e\td2b2dd0e-c126-53db-b832-39b61054b8c6\tfce4aca2-c973-5c94-a481-cb33f1a1577b\n"
)
KATMANDU_TAIL = (
    "b12622d5-7212-522d-8ab8-a7f978cf91b2\tyeng/katmandu\tkatmandu\tcity\toutdoors\t"
    "A mystical city in the plane of Yeng, where reality bends and the laws of physics "
    "are mere suggestions\t"
    '["ethereal_mist", "dimensional_rain", "reality_shift"]\t'
    '{"combat_modifier": 1.4, "exploration_bonus": 1, "npc_spawn_modifier": 1.8, '
    '"lucidity_drain_rate": 0.25}\n'
)
PALANCE_LINE = (
    "95a19338-130c-5e58-833b-1e3a2691709d\tb12622d5-7212-522d-8ab8-a7f978cf91b2\t"
    "palance\tpalance\tindoors\tThe ancient palace complex where reality itself seems "
    "to shift and change, home to eldritch entities and forbidden knowledge\t"
    '{"combat_modifier": 1.6, "exploration_bonus": 1.2, "npc_spawn_modifier": 2, '
    '"access_requirements": ["dimensional_key", "reality_anchor"], '
    '"lucidity_drain_rate": 0.3}\n'
)
LIMBO_VOID_LINE = (
    "fb34e40a-0cd9-5b8d-abc9-4872091d9129\tbf4475de-d989-5585-8806-20dbeb7c724d\tlimbo_death_void\tThe Spaces Between\t"
)


def _load_arena_rooms(schema: str) -> str:
    raw = (DB / "_patch_arena_rooms_e2e.txt").read_text(encoding="utf-8-sig")
    return raw.replace("mythos_e2e", schema)


def _load_arena_links(schema: str) -> str:
    raw = (DB / "_patch_arena_links_e2e.txt").read_text(encoding="utf-8-sig")
    return raw.replace("mythos_e2e", schema)


def _with_trailing_nl(block: str) -> str:
    return block if block.endswith("\n") else block + "\n"


def _insert_after_line_containing(text: str, line_contains: str, insertion: str, path: pathlib.Path) -> str:
    void_idx = text.find(line_contains)
    if void_idx < 0:
        raise SystemExit(f"{path}: limbo_death_void room row not found")
    rest = text[void_idx:]
    end_void_line = rest.find("\n")
    if end_void_line < 0:
        raise SystemExit(f"{path}: malformed after limbo void")
    insert_at = void_idx + end_void_line + 1
    return text[:insert_at] + _with_trailing_nl(insertion) + text[insert_at:]


def _append_before_copy_terminator(
    text: str,
    copy_header: str,
    block: str,
    path: pathlib.Path,
    label: str,
) -> str:
    marker = copy_header if copy_header.endswith("\n") else copy_header + "\n"
    ci = text.find(marker)
    if ci < 0:
        raise SystemExit(f"{path}: {label} COPY header not found")
    rel = text[ci + len(marker) :]
    term = rel.find("\n\\.\n")
    if term < 0:
        raise SystemExit(f"{path}: {label} COPY terminator not found")
    abs_term = ci + len(marker) + term
    body = _with_trailing_nl(block)
    return text[:abs_term] + "\n" + body + text[abs_term:]


def _apply_zones_and_subzones(text: str, path: pathlib.Path, actions: list[str]) -> str:
    if KATMANDU_TAIL not in text:
        raise SystemExit(f"{path}: expected katmandu zone row missing")
    text = text.replace(KATMANDU_TAIL, KATMANDU_TAIL + ARENA_ZONE_LINE, 1)
    actions.append("zones: +limbo/arena")
    if PALANCE_LINE not in text:
        raise SystemExit(f"{path}: expected palance subzone row missing")
    text = text.replace(PALANCE_LINE, PALANCE_LINE + ARENA_SUBZONE_LINE, 1)
    actions.append("subzones: +arena")
    return text


def _apply_arena_room_rows(text: str, path: pathlib.Path, schema: str, actions: list[str]) -> str:
    text = _insert_after_line_containing(text, LIMBO_VOID_LINE, _load_arena_rooms(schema), path)
    actions.append("rooms: +121 arena cells")
    return text


def _apply_arena_room_links(text: str, path: pathlib.Path, schema: str, actions: list[str]) -> str:
    header = f"COPY {schema}.room_links (id, from_room_id, to_room_id, direction, attributes) FROM stdin;\n"
    text = _append_before_copy_terminator(text, header, _load_arena_links(schema), path, "room_links")
    actions.append("room_links: +arena grid links")
    return text


def _apply_zone_configuration_row(text: str, path: pathlib.Path, schema: str, actions: list[str]) -> str:
    header = f"COPY {schema}.zone_configurations (id, zone_id, subzone_id) FROM stdin;\n"
    text = _append_before_copy_terminator(text, header, ZONE_CFG_LINE, path, "zone_configurations")
    actions.append("zone_configurations: +arena")
    return text


def patch_file(path: pathlib.Path, schema: str) -> list[str]:
    """Apply arena seed slices to one DML file; return human-readable action lines."""
    text = path.read_text(encoding="utf-8")
    if "d2b2dd0e-c126-53db-b832-39b61054b8c6\tlimbo/arena" in text:
        return [f"{path.name}: already contains limbo/arena zone; skip"]

    actions: list[str] = []
    text = _apply_zones_and_subzones(text, path, actions)
    text = _apply_arena_room_rows(text, path, schema, actions)
    text = _apply_arena_room_links(text, path, schema, actions)
    text = _apply_zone_configuration_row(text, path, schema, actions)
    _ = path.write_text(text, encoding="utf-8", newline="\n")
    actions.insert(0, path.name)
    return actions


def main() -> None:
    """Patch mythos_e2e and mythos_unit DML files when patch snippet files are present."""
    for rel, schema in (
        ("mythos_e2e_dml.sql", "mythos_e2e"),
        ("mythos_unit_dml.sql", "mythos_unit"),
    ):
        out = patch_file(DB / rel, schema)
        for line in out:
            print(line)


if __name__ == "__main__":
    main()
