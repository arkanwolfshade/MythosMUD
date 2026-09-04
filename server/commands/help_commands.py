"""
Help command adapter module.

The original help command handler lives in system_commands.py. This lightweight
module re-exports the handler for backward compatibility with callers that
import from server.commands.help_commands.
"""

from server.commands.system_commands import handle_help_command

__all__ = ["handle_help_command"]
