"""Line-ending safety for `scripts/author_sanitarium_coords.py` (#829).

The DML seed files are stored LF in git, but `core.autocrlf` checks them out CRLF on
Windows. This script rewrites the LAST column of every Sanitarium room row (`map_style`),
and that is exactly where the difference bites: splitting CRLF text on LF leaves a stray
CR attached to the final field, so replacing that field silently drops the CR and turns
those rows into bare LF. The file ends up with mixed line endings, which git then reports
as a whole-file change and which breaks any parser matching on a specific ending.

These tests pin the round trip rather than the coordinate maths, because a corrupted seed
file is a much quieter failure than a wrong coordinate.
"""

from __future__ import annotations

import hashlib
import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Protocol, cast

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[4]

CR = chr(13)
LF = chr(10)
CRLF = CR + LF


class _CoordsModule(Protocol):
    STEP: int
    DELTA: dict[str, tuple[int, int]]
    SEED_PATH: Path

    def _read_dml(self, path: Path) -> tuple[str, bool]: ...
    def _write_dml(self, path: Path, text: str, crlf: bool) -> None: ...


@pytest.fixture(scope="module")
def coords() -> _CoordsModule:
    path = _REPO_ROOT / "scripts" / "author_sanitarium_coords.py"
    spec = importlib.util.spec_from_file_location("_author_sanitarium_coords", path)
    assert spec and spec.loader, f"cannot load {path}"
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return cast(_CoordsModule, cast(object, mod))


def _rows(ending: str) -> str:
    """Three tab-separated rows whose LAST column is the one the script rewrites."""
    return ending.join(["a\tb\tcity", "c\td\tcity", "e\tf\tcity"]) + ending


class TestLineEndingRoundTrip:
    def test_crlf_file_survives_read_and_write(self, coords: _CoordsModule, tmp_path: Path) -> None:
        path = tmp_path / "crlf.sql"
        original = _rows(CRLF).encode("utf-8")
        _ = path.write_bytes(original)

        text, crlf = coords._read_dml(path)  # pyright: ignore[reportPrivateUsage]
        assert crlf is True
        assert CR not in text, "text handed to the caller should be LF-only"
        coords._write_dml(path, text, crlf)  # pyright: ignore[reportPrivateUsage]

        assert path.read_bytes() == original

    def test_lf_file_survives_read_and_write(self, coords: _CoordsModule, tmp_path: Path) -> None:
        path = tmp_path / "lf.sql"
        original = _rows(LF).encode("utf-8")
        _ = path.write_bytes(original)

        text, crlf = coords._read_dml(path)  # pyright: ignore[reportPrivateUsage]
        assert crlf is False
        coords._write_dml(path, text, crlf)  # pyright: ignore[reportPrivateUsage]

        assert path.read_bytes() == original

    def test_rewriting_the_last_column_does_not_mix_endings(self, coords: _CoordsModule, tmp_path: Path) -> None:
        """The actual corruption: replace the final field of every row on a CRLF file."""
        path = tmp_path / "crlf.sql"
        _ = path.write_bytes(_rows(CRLF).encode("utf-8"))

        text, crlf = coords._read_dml(path)  # pyright: ignore[reportPrivateUsage]
        rows = ["\t".join(row.split("\t")[:-1] + ["interior"]) for row in text.rstrip(LF).split(LF)]
        coords._write_dml(path, LF.join(rows) + LF, crlf)  # pyright: ignore[reportPrivateUsage]

        data = path.read_bytes()
        bare_lf = data.count(LF.encode()) - data.count(CRLF.encode())
        assert bare_lf == 0, "rewriting the last column produced mixed line endings"
        assert data.count(CRLF.encode()) == 3
        assert b"interior" in data


class TestDmlPath:
    """A wrong path is not a crash - it is silently editing (or missing) the wrong file."""

    def test_seed_path_is_the_single_schema_agnostic_seed(self, coords: _CoordsModule) -> None:
        assert coords.SEED_PATH == Path("data/db/seed.sql")

    def test_the_seed_file_actually_exists(self, coords: _CoordsModule) -> None:
        """Catches a rename of the seed file, which would otherwise surface as the
        script reporting zero rooms filled rather than failing."""
        assert (_REPO_ROOT / coords.SEED_PATH).exists(), "seed file missing"


class TestCheckFlag:
    """`--check` is the only thing standing between a dry run and rewriting the seed file
    in place. If the flag were inverted or mis-wired, running it to *inspect* the result
    would silently modify the working tree instead."""

    def test_check_leaves_the_seed_file_byte_identical(self) -> None:
        script = _REPO_ROOT / "scripts" / "author_sanitarium_coords.py"
        target = _REPO_ROOT / "data/db/seed.sql"
        before = hashlib.sha256(target.read_bytes()).hexdigest()

        result = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        assert result.returncode == 0, result.stderr
        assert "(dry run)" in result.stdout, result.stdout
        after = hashlib.sha256(target.read_bytes()).hexdigest()
        assert before == after, "--check modified the seed file"


class TestLayoutInvariants:
    def test_rooms_are_one_cell_apart(self, coords: _CoordsModule) -> None:
        """STEP must stay 1: the minimap viewport counts CELLS, so any extra spacing
        directly shrinks how much of the building fits on screen."""
        assert coords.STEP == 1

    def test_cardinal_moves_are_single_steps(self, coords: _CoordsModule) -> None:
        for direction in ("north", "south", "east", "west"):
            dx, dy = coords.DELTA[direction]
            assert abs(dx) + abs(dy) == 1, f"{direction} moves {abs(dx) + abs(dy)} cells, expected 1"

    def test_vertical_moves_clear_the_side_room_row(self, coords: _CoordsModule) -> None:
        """`up`/`down` do not move in the server's BFS, so they need an offset here - but a
        one-row offset lands on the row a corridor's own side rooms occupy, which cascaded
        five rooms sideways and left their exits spanning two cells."""
        for direction in ("up", "down"):
            dx, dy = coords.DELTA[direction]
            assert abs(dy) >= 2, f"{direction} offsets only {abs(dy)} row(s); needs to clear side rooms"
            assert dx == 0, f"{direction} should not drift sideways"
