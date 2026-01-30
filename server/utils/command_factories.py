"""
Command factory methods for creating command objects from parsed arguments.

This module contains all the _create_*_command methods that were previously
in the CommandParser class. This separation reduces the size of command_parser.py
and improves maintainability.

The CommandFactory class delegates to specialized factory classes organized by
command category to keep the codebase maintainable and under size limits.
"""

# pylint: disable=too-many-public-methods  # Reason: Command factory legitimately requires many public methods for comprehensive command creation across all command categories

from ..models.command_base import BaseCommand
from .command_factories_combat import CombatCommandFactory
from .command_factories_communication import CommunicationCommandFactory
from .command_factories_exploration import ExplorationCommandFactory
from .command_factories_inventory import InventoryCommandFactory
from .command_factories_moderation import ModerationCommandFactory
from .command_factories_player_state import PlayerStateCommandFactory
from .command_factories_utility import UtilityCommandFactory


class CommandFactory:
    """Factory class for creating command objects from parsed arguments."""

    def __init__(self) -> None:
        """Initialize the command factory with specialized sub-factories."""
        self._communication = CommunicationCommandFactory()
        self._exploration = ExplorationCommandFactory()
        self._inventory = InventoryCommandFactory()
        self._moderation = ModerationCommandFactory()
        self._player_state = PlayerStateCommandFactory()
        self._combat = CombatCommandFactory()
        self._utility = UtilityCommandFactory()

    # Communication commands
    def create_say_command(self, args: list[str]) -> BaseCommand:
        """Create SayCommand from arguments."""
        return self._communication.create_say_command(args)

    def create_local_command(
        self,
        args: list[str],
        raw_command: str | None = None,
        original_command: str | None = None,
    ) -> BaseCommand:
        """Create LocalCommand from arguments."""
        return self._communication.create_local_command(
            args, raw_command=raw_command, original_command=original_command
        )

    def create_system_command(self, args: list[str]) -> BaseCommand:
        """Create SystemCommand from arguments."""
        return self._communication.create_system_command(args)

    def create_emote_command(self, args: list[str]) -> BaseCommand:
        """Create EmoteCommand from arguments."""
        return self._communication.create_emote_command(args)

    def create_me_command(self, args: list[str]) -> BaseCommand:
        """Create MeCommand from arguments."""
        return self._communication.create_me_command(args)

    def create_pose_command(self, args: list[str]) -> BaseCommand:
        """Create PoseCommand from arguments."""
        return self._communication.create_pose_command(args)

    def create_whisper_command(self, args: list[str]) -> BaseCommand:
        """Create WhisperCommand from arguments."""
        return self._communication.create_whisper_command(args)

    def create_reply_command(self, args: list[str]) -> BaseCommand:
        """Create ReplyCommand from arguments."""
        return self._communication.create_reply_command(args)

    def create_channel_command(self, args: list[str]) -> BaseCommand:
        """Create ChannelCommand from arguments."""
        return self._communication.create_channel_command(args)

    # Exploration commands
    def create_look_command(self, args: list[str]) -> BaseCommand:
        """Create LookCommand from arguments."""
        return self._exploration.create_look_command(args)

    def create_go_command(self, args: list[str]) -> BaseCommand:
        """Create GoCommand from arguments."""
        return self._exploration.create_go_command(args)

    def create_sit_command(self, args: list[str]) -> BaseCommand:
        """Create SitCommand from arguments."""
        return self._exploration.create_sit_command(args)

    def create_stand_command(self, args: list[str]) -> BaseCommand:
        """Create StandCommand from arguments."""
        return self._exploration.create_stand_command(args)

    def create_lie_command(self, args: list[str]) -> BaseCommand:
        """Create LieCommand from arguments."""
        return self._exploration.create_lie_command(args)

    def create_ground_command(self, args: list[str]) -> BaseCommand:
        """Create GroundCommand from arguments."""
        return self._exploration.create_ground_command(args)

    # Inventory commands
    def create_inventory_command(self, args: list[str]) -> BaseCommand:
        """Create InventoryCommand from arguments."""
        return self._inventory.create_inventory_command(args)

    def create_pickup_command(self, args: list[str]) -> BaseCommand:
        """Create PickupCommand from arguments."""
        return self._inventory.create_pickup_command(args)

    def create_drop_command(self, args: list[str]) -> BaseCommand:
        """Create DropCommand from arguments."""
        return self._inventory.create_drop_command(args)

    def create_put_command(self, args: list[str]) -> BaseCommand:
        """Create PutCommand from arguments."""
        return self._inventory.create_put_command(args)

    def create_get_command(self, args: list[str]) -> BaseCommand:
        """Create GetCommand from arguments."""
        return self._inventory.create_get_command(args)

    def create_equip_command(self, args: list[str]) -> BaseCommand:
        """Create EquipCommand from arguments."""
        return self._inventory.create_equip_command(args)

    def create_unequip_command(self, args: list[str]) -> BaseCommand:
        """Create UnequipCommand from arguments."""
        return self._inventory.create_unequip_command(args)

    # Moderation commands
    def create_mute_command(self, args: list[str]) -> BaseCommand:
        """Create MuteCommand from arguments."""
        return self._moderation.create_mute_command(args)

    def create_unmute_command(self, args: list[str]) -> BaseCommand:
        """Create UnmuteCommand from arguments."""
        return self._moderation.create_unmute_command(args)

    def create_mute_global_command(self, args: list[str]) -> BaseCommand:
        """Create MuteGlobalCommand from arguments."""
        return self._moderation.create_mute_global_command(args)

    def create_unmute_global_command(self, args: list[str]) -> BaseCommand:
        """Create UnmuteGlobalCommand from arguments."""
        return self._moderation.create_unmute_global_command(args)

    def create_add_admin_command(self, args: list[str]) -> BaseCommand:
        """Create AddAdminCommand from arguments."""
        return self._moderation.create_add_admin_command(args)

    def create_admin_command(self, args: list[str]) -> BaseCommand:
        """Create AdminCommand from arguments."""
        return self._moderation.create_admin_command(args)

    def create_mutes_command(self, args: list[str]) -> BaseCommand:
        """Create MutesCommand from arguments."""
        return self._moderation.create_mutes_command(args)

    # Player state commands
    def create_status_command(self, args: list[str]) -> BaseCommand:
        """Create StatusCommand from arguments."""
        return self._player_state.create_status_command(args)

    def create_time_command(self, args: list[str]) -> BaseCommand:
        """Create TimeCommand from arguments."""
        return self._player_state.create_time_command(args)

    def create_whoami_command(self, args: list[str]) -> BaseCommand:
        """Create WhoamiCommand from arguments."""
        return self._player_state.create_whoami_command(args)

    def create_who_command(self, args: list[str]) -> BaseCommand:
        """Create WhoCommand from arguments."""
        return self._player_state.create_who_command(args)

    def create_quit_command(self, args: list[str]) -> BaseCommand:
        """Create QuitCommand from arguments."""
        return self._player_state.create_quit_command(args)

    def create_logout_command(self, args: list[str]) -> BaseCommand:
        """Create LogoutCommand from arguments."""
        return self._player_state.create_logout_command(args)

    def create_rest_command(self, args: list[str]) -> BaseCommand:
        """Create RestCommand from arguments."""
        return self._player_state.create_rest_command(args)

    # Combat commands
    def create_attack_command(self, args: list[str]) -> BaseCommand:
        """Create AttackCommand from arguments."""
        return self._combat.create_attack_command(args)

    def create_punch_command(self, args: list[str]) -> BaseCommand:
        """Create PunchCommand from arguments."""
        return self._combat.create_punch_command(args)

    def create_kick_command(self, args: list[str]) -> BaseCommand:
        """Create KickCommand from arguments."""
        return self._combat.create_kick_command(args)

    def create_strike_command(self, args: list[str]) -> BaseCommand:
        """Create StrikeCommand from arguments."""
        return self._combat.create_strike_command(args)

    # Utility commands
    def create_alias_command(self, args: list[str]) -> BaseCommand:
        """Create AliasCommand from arguments."""
        return self._utility.create_alias_command(args)

    def create_aliases_command(self, args: list[str]) -> BaseCommand:
        """Create AliasesCommand from arguments."""
        return self._utility.create_aliases_command(args)

    def create_unalias_command(self, args: list[str]) -> BaseCommand:
        """Create UnaliasCommand from arguments."""
        return self._utility.create_unalias_command(args)

    def create_help_command(self, args: list[str]) -> BaseCommand:
        """Create HelpCommand from arguments."""
        return self._utility.create_help_command(args)

    def create_npc_command(self, args: list[str]) -> BaseCommand:
        """Create NPCCommand from arguments."""
        return self._utility.create_npc_command(args)

    def create_summon_command(self, args: list[str]) -> BaseCommand:
        """Create SummonCommand from arguments."""
        return self._utility.create_summon_command(args)

    def create_teleport_command(self, args: list[str]) -> BaseCommand:
        """Create TeleportCommand from arguments."""
        return self._utility.create_teleport_command(args)

    def create_goto_command(self, args: list[str]) -> BaseCommand:
        """Create GotoCommand from arguments."""
        return self._utility.create_goto_command(args)

    def create_shutdown_command(self, args: list[str]) -> BaseCommand:
        """Create ShutdownCommand from arguments."""
        return self._utility.create_shutdown_command(args)

    def create_cast_command(self, args: list[str]) -> BaseCommand:
        """Create CastCommand from arguments."""
        return self._utility.create_cast_command(args)

    def create_spell_command(self, args: list[str]) -> BaseCommand:
        """Create SpellCommand from arguments."""
        return self._utility.create_spell_command(args)

    def create_spells_command(self, args: list[str]) -> BaseCommand:
        """Create SpellsCommand from arguments."""
        return self._utility.create_spells_command(args)

    def create_learn_command(self, args: list[str]) -> BaseCommand:
        """Create LearnCommand from arguments."""
        return self._utility.create_learn_command(args)
