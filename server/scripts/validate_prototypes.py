"""CLI entrypoint for validating MythosMUD item prototype definitions."""

import argparse
from collections.abc import Sequence
from pathlib import Path

from server.game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate item prototype definitions.")
    parser.add_argument(
        "--path",
        dest="path",
        default="data/prototypes/items",
        help="Directory containing prototype JSON files.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_arguments(argv)
    directory = Path(args.path)

    try:
        registry = PrototypeRegistry.load_from_path(directory)
    except PrototypeRegistryError as exc:
        logger.error("prototype validation failed", directory=str(directory), error=str(exc))
        return 1

    invalid_count = len(registry.invalid_entries())
    loaded_count = len(list(registry.all()))

    logger.info(
        "prototype validation completed",
        directory=str(directory),
        loaded_count=loaded_count,
        invalid_count=invalid_count,
    )

    return 0 if invalid_count == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
