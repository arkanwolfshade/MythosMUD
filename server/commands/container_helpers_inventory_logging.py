"""Shared logger for container inventory helpers (typed for basedpyright)."""

from typing import cast

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))
