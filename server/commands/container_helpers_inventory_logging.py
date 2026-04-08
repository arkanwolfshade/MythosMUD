"""Shared logger for container inventory helpers (typed for basedpyright)."""

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)
