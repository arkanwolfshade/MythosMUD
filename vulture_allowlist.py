"""Allowlist of intentional 'unused' server symbols for Vulture."""

# Vulture allowlist: valid Python that references intentional "unused" names.
# See .cursor/plans/dead_code_analysis_and_removal_746bc5c1.plan.md section 4.
# Side-effect imports (router registration, model registration) and reserved stubs
# are kept; __exit__ unused params use _exc_val/_exc_tb in source (vulture ignores _).
#
# TYPE_CHECKING-only import in chat_service (used in cast() as string at runtime).
from server.game import chat_service

# Intentional reference for vulture allowlist; _ avoids Ruff B018. UserManagerProtocol is TYPE_CHECKING-only.
_ = chat_service.UserManagerProtocol  # type: ignore[attr-defined]
