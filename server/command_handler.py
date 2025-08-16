import re

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .alias_storage import AliasStorage
from .auth.users import get_current_user
from .config_loader import get_config
from .game.chat_service import ChatService
from .game.movement_service import MovementService
from .logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/command", tags=["command"])


def get_username_from_user(user_obj):
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    else:
        raise ValueError("User object must have username attribute or key")


class CommandRequest(BaseModel):
    command: str


# Patterns to reject for command injection (expand as needed)
INJECTION_PATTERNS = [
    r"[;|&]",  # shell metacharacters
    r"\b(or|and)\b.*=",  # SQL injection
    r"__import__|eval|exec|system|os\.",  # Python injection
    r"%[a-zA-Z]",  # format string
]

# Commands that traditionally use slash prefix in modern interfaces
SLASH_COMMANDS = {"help", "who", "quit", "look", "go", "say", "me", "pose", "alias", "aliases", "unalias"}


def normalize_command(command: str) -> str:
    """
    Normalize command input by removing optional slash prefix.

    Supports both traditional MUD commands (go north) and modern slash commands (/go north).
    This allows for flexible command input while maintaining backward compatibility.

    Args:
        command: The raw command string from user input

    Returns:
        Normalized command string with slash prefix removed if present
    """
    if not command:
        return command

    # Remove leading slash if present
    if command.startswith("/"):
        normalized = command[1:].strip()
        logger.debug("Slash prefix removed from command", original=command, normalized=normalized)
        return normalized

    return command.strip()


def is_suspicious_input(command: str) -> bool:
    """Check if command contains suspicious patterns that might indicate injection attempts."""
    for pat in INJECTION_PATTERNS:
        if re.search(pat, command, re.IGNORECASE):
            logger.warning("Suspicious command pattern detected", pattern=pat, command=command)
            return True
    return False


def clean_command_input(command: str) -> str:
    """Clean and normalize command input by collapsing multiple spaces and stripping whitespace."""
    cleaned = re.sub(r"\s+", " ", command).strip()
    if cleaned != command:
        logger.debug("Command input cleaned", original=command, cleaned=cleaned)
    return cleaned


def _is_predefined_emote(command: str) -> bool:
    """
    Check if a command is a predefined emote alias.

    Args:
        command: The command to check

    Returns:
        True if the command is a predefined emote, False otherwise
    """
    try:
        from .game.emote_service import EmoteService

        emote_service = EmoteService()
        return emote_service.is_emote_alias(command)
    except Exception as e:
        logger.warning(f"Error checking predefined emote: {e}")
        return False


MAX_COMMAND_LENGTH = get_config().get("max_command_length", 1000)


# Command definitions for help system
COMMANDS = {
    "look": {
        "category": "Exploration",
        "description": ("Examine your surroundings or look in a specific direction"),
        "usage": "look [direction] or /look [direction]",
        "examples": ["look", "look north", "look east", "/look", "/look north"],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>LOOK Command</h3>
<p>The ancient texts speak of observation as the first step toward understanding.
Use this command to examine your surroundings or peer into the unknown.</p>

<h4>Usage:</h4>
<ul>
<li><strong>look</strong> - Examine your current location</li>
<li><strong>look [direction]</strong> - Look in a specific direction (north, south, east, west)</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>look</li>
<li>look north</li>
<li>look east</li>
</ul>

<p>As the Necronomicon suggests: "That which can be seen may yet remain unseen to the untrained eye."</p>
</div>
""",
    },
    "go": {
        "category": "Movement",
        "description": "Move in a specific direction",
        "usage": "go <direction> or /go <direction>",
        "examples": ["go north", "go south", "go east", "go west", "/go north", "/go south"],
        "detailed_help": """
<div style="color: #2F4F4F;">
<h3>GO Command</h3>
<p>Traverse the non-Euclidean corridors of our world. Each step brings you closer
to revelations best left undiscovered.</p>

<h4>Usage:</h4>
<ul>
<li><strong>go [direction]</strong> or <strong>/go [direction]</strong> - Move in the specified direction</li>
</ul>

<h4>Available Directions:</h4>
<ul>
<li>north</li>
<li>south</li>
<li>east</li>
<li>west</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>go north</li>
<li>/go north</li>
<li>go south</li>
<li>/go south</li>
<li>go east</li>
<li>go west</li>
</ul>

<p>Remember: "The geometry of this place is not as it seems." - Prof. Armitage</p>
</div>
""",
    },
    "say": {
        "category": "Communication",
        "description": "Speak to other players in your current room",
        "usage": "say <message>",
        "examples": ["say Hello everyone!", "say What a strange place this is..."],
        "detailed_help": """
<div style="color: #006400;">
<h3>SAY Command</h3>
<p>Project your voice into the eldritch air, allowing your words to reach
the ears of those who share your current location. As the ancient texts
suggest, communication is the first step toward understanding.</p>

<h4>Usage:</h4>
<ul>
<li><strong>say [message]</strong> - Speak to players in your current room</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>say Hello everyone!</li>
<li>say What a strange place this is...</li>
<li>say Has anyone seen the professor?</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Only players in your current room will hear your message</li>
<li>Messages are limited to 500 characters</li>
<li>You cannot speak if you are muted in the say channel</li>
</ul>

<p>"Words have power in the right places, and the right places have power in words." - Prof. Armitage</p>
</div>
""",
    },
    "emote": {
        "category": "Communication",
        "description": "Perform an action or gesture visible to other players in your room",
        "usage": "emote <action>",
        "examples": ["emote adjusts his spectacles", "emote looks around nervously", "emote examines the ancient tome"],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>EMOTE Command</h3>
<p>Express yourself through actions and gestures, allowing others to witness
your physical presence in the eldritch realm. As the ancient texts suggest,
actions speak louder than words in the presence of forbidden knowledge.</p>

<h4>Usage:</h4>
<ul>
<li><strong>emote [action]</strong> - Perform an action visible to players in your room</li>
<li><strong>[predefined_emote]</strong> - Use a predefined emote (see list below)</li>
</ul>

<h4>Predefined Emotes:</h4>
<ul>
<li><strong>twibble</strong> - Twibble around aimlessly</li>
<li><strong>dance</strong> - Dance like no one is watching</li>
<li><strong>wave</strong> - Wave hello (aliases: hello, hi)</li>
<li><strong>bow</strong> - Bow respectfully (aliases: curtsey, curtsy)</li>
<li><strong>laugh</strong> - Laugh heartily (aliases: chuckle, giggle)</li>
<li><strong>sigh</strong> - Sigh deeply (aliases: exhale)</li>
<li><strong>stretch</strong> - Stretch your limbs (aliases: flex)</li>
<li><strong>yawn</strong> - Yawn widely (aliases: tire)</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>emote adjusts his spectacles</li>
<li>emote looks around nervously</li>
<li>emote examines the ancient tome</li>
<li>twibble</li>
<li>dance</li>
<li>wave</li>
<li>/bow</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Only players in your current room will see your emote</li>
<li>Emotes are limited to 200 characters</li>
<li>Use third person perspective (e.g., "adjusts" not "adjust")</li>
<li>You cannot emote if you are muted in the say channel</li>
<li>Predefined emotes can be used directly or with slash prefix (e.g., /twibble)</li>
</ul>

<p>"In the presence of the unknown, every gesture becomes a prayer." - Prof. Armitage</p>
</div>
""",
    },
    "me": {
        "category": "Communication",
        "description": "Describe an action you are performing (alternative to emote)",
        "usage": "me <action>",
        "examples": ["me adjusts his spectacles", "me looks around nervously", "me examines the ancient tome"],
        "detailed_help": """
<div style="color: #2F4F4F;">
<h3>ME Command</h3>
<p>Describe your actions in the third person, allowing others to witness
your presence and activities in the eldritch realm. This command is an
alternative to the emote command and works identically.</p>

<h4>Usage:</h4>
<ul>
<li><strong>me [action]</strong> - Describe an action you are performing</li>
<li><strong>me [predefined_emote]</strong> - Use a predefined emote (see emote help for list)</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>me adjusts his spectacles</li>
<li>me looks around nervously</li>
<li>me examines the ancient tome</li>
<li>me twibble</li>
<li>me dance</li>
<li>me wave</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Only players in your current room will see your action</li>
<li>Actions are limited to 200 characters</li>
<li>Use third person perspective (e.g., "adjusts" not "adjust")</li>
<li>You cannot use this command if you are muted in the say channel</li>
<li>This command works identically to the emote command</li>
</ul>

<p>"Every action in this realm leaves an echo in the fabric of reality." - Prof. Armitage</p>
</div>
""",
    },
    "pose": {
        "category": "Communication",
        "description": "Set or display your current pose/status",
        "usage": "pose [description]",
        "examples": ["pose", "pose stands with scholarly authority", "pose is deep in thought"],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>POSE Command</h3>
<p>Set your current pose or status, allowing others to see how you appear
in the eldritch realm. Your pose persists until changed and is visible
to anyone who looks at you or enters your room.</p>

<h4>Usage:</h4>
<ul>
<li><strong>pose</strong> - Display your current pose</li>
<li><strong>pose [description]</strong> - Set your pose to the specified description</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>pose</li>
<li>pose stands with scholarly authority</li>
<li>pose is deep in thought</li>
<li>pose appears to be studying ancient texts</li>
<li>pose looks ready for adventure</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Your pose is visible to all players in your room</li>
<li>Poses are limited to 100 characters</li>
<li>Your pose persists when you move between rooms</li>
<li>Use "pose" without arguments to see your current pose</li>
</ul>

<p>"In the realm of the unknown, one's stance reveals one's soul." - Prof. Armitage</p>
</div>
""",
    },
    "alias": {
        "category": "Aliases",
        "description": "Create or manage command aliases",
        "usage": "alias <name> <command>",
        "examples": ["alias l look", "alias n 'go north'", "alias l"],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>ALIAS Command</h3>
<p>Create shortcuts for commonly used commands, as documented in the restricted
archives of Miskatonic University. These eldritch shortcuts allow for more
efficient exploration of our realm.</p>

<h4>Usage:</h4>
<ul>
<li><strong>alias [name] [command]</strong> - Create or update an alias</li>
<li><strong>alias [name]</strong> - Show details of a specific alias</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>alias l look</li>
<li>alias n 'go north'</li>
<li>alias greet 'say Hello there!'</li>
<li>alias l</li>
</ul>

<h4>Rules:</h4>
<ul>
<li>Alias names must start with a letter</li>
<li>Only alphanumeric characters and underscores allowed</li>
<li>Maximum 50 aliases per player</li>
<li>Cannot alias reserved commands (alias, aliases, unalias, help)</li>
</ul>

<p>"Efficiency in command is the mark of a true scholar." - Prof. Armitage</p>
</div>
""",
    },
    "aliases": {
        "category": "Aliases",
        "description": "List all your command aliases",
        "usage": "aliases",
        "examples": ["aliases"],
        "detailed_help": """
<div style="color: #2F4F4F;">
<h3>ALIASES Command</h3>
<p>Display all your currently defined command aliases, as catalogued in the
forbidden archives of Miskatonic University.</p>

<h4>Usage:</h4>
<ul>
<li><strong>aliases</strong> - List all your aliases</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>aliases</li>
</ul>

<p>The list shows each alias name and its corresponding command, allowing you
to review your eldritch shortcuts at a glance.</p>

<p>"A well-organized mind is a prepared mind." - Miskatonic University Archives</p>
</div>
""",
    },
    "unalias": {
        "category": "Aliases",
        "description": "Remove a command alias",
        "usage": "unalias <name>",
        "examples": ["unalias l", "unalias n"],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>UNALIAS Command</h3>
<p>Remove unwanted command aliases from your collection, as documented in the
restricted archives. This allows you to clean up your command shortcuts.</p>

<h4>Usage:</h4>
<ul>
<li><strong>unalias [name]</strong> - Remove the specified alias</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>unalias l</li>
<li>unalias n</li>
<li>unalias greet</li>
</ul>

<h4>Note:</h4>
<p>This action cannot be undone. The alias will be permanently removed from
your collection.</p>

<p>"Sometimes the greatest wisdom lies in knowing what to remove." - Prof. Armitage</p>
</div>
""",
    },
    "help": {
        "category": "Information",
        "description": "Get help on commands and game features",
        "usage": "help [command] or /help [command]",
        "examples": ["help", "help look", "help go", "/help", "/help look"],
        "detailed_help": """
<div style="color: #2F4F4F;">
<h3>HELP Command</h3>
<p>Access the forbidden knowledge of Miskatonic University's command archives.
This command provides guidance on the eldritch incantations available to you.</p>

<h4>Usage:</h4>
<ul>
<li><strong>help</strong> or <strong>/help</strong> - Show all available commands</li>
<li><strong>help [command]</strong> or <strong>/help [command]</strong> - Get detailed help for a specific command</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>help</li>
<li>/help</li>
<li>help look</li>
<li>/help look</li>
<li>help go</li>
<li>help say</li>
</ul>

<h4>Command Conventions:</h4>
<p>MythosMUD supports both traditional MUD commands and modern slash commands:</p>
<ul>
<li><strong>Traditional:</strong> go north, look, say hello</li>
<li><strong>Modern:</strong> /go north, /look, /say hello</li>
</ul>

<p>"Knowledge is power, but some knowledge comes at a price." - Restricted Section</p>
</div>
""",
    },
    "mute": {
        "category": "User Management",
        "description": "Mute a specific player (you won't see their messages)",
        "usage": "mute <player_name> [duration_minutes] [reason]",
        "examples": ["mute Ithaqua", "mute Ithaqua 30", "mute Ithaqua 60 Being annoying"],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>MUTE Command</h3>
<p>Silence the voice of another player, as documented in the restricted
archives of Miskatonic University. This prevents you from seeing their
messages in the say channel.</p>

<h4>Usage:</h4>
<ul>
<li><strong>mute [player_name]</strong> - Mute a player permanently</li>
<li><strong>mute [player_name] [duration_minutes]</strong> - Mute for a specific duration</li>
<li><strong>mute [player_name] [duration_minutes] [reason]</strong> - Mute with reason</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>mute Ithaqua</li>
<li>mute Ithaqua 30</li>
<li>mute Ithaqua 60 Being annoying</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Only affects your view of the muted player's messages</li>
<li>Other players can still see the muted player's messages</li>
<li>Duration is in minutes (omit for permanent mute)</li>
<li>Admin players cannot be muted</li>
</ul>

<p>"Sometimes silence is the greatest weapon against chaos." - Prof. Armitage</p>
</div>
""",
    },
    "unmute": {
        "category": "User Management",
        "description": "Unmute a previously muted player",
        "usage": "unmute <player_name>",
        "examples": ["unmute Ithaqua"],
        "detailed_help": """
<div style="color: #006400;">
<h3>UNMUTE Command</h3>
<p>Restore the voice of a previously muted player, allowing you to once again
hear their eldritch utterances in the say channel.</p>

<h4>Usage:</h4>
<ul>
<li><strong>unmute [player_name]</strong> - Remove mute from a player</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>unmute Ithaqua</li>
<li>unmute Azathoth</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Only affects your view of the player's messages</li>
<li>If the player was muted by multiple people, you only unmute your own mute</li>
<li>You can only unmute players you personally muted</li>
</ul>

<p>"Redemption is always possible, even in the darkest corners." - Prof. Armitage</p>
</div>
""",
    },
    "mute_global": {
        "category": "User Management",
        "description": "Globally mute a player (they cannot use any chat channels)",
        "usage": "mute_global <player_name> [duration_minutes] [reason]",
        "examples": ["mute_global Ithaqua", "mute_global Ithaqua 120", "mute_global Ithaqua 60 Spamming"],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>MUTE_GLOBAL Command</h3>
<p>Apply a comprehensive silence to a player, preventing them from using any
chat channels. This is a powerful tool documented in the restricted archives
of Miskatonic University.</p>

<h4>Usage:</h4>
<ul>
<li><strong>mute_global [player_name]</strong> - Globally mute a player permanently</li>
<li><strong>mute_global [player_name] [duration_minutes]</strong> - Global mute for duration</li>
<li><strong>mute_global [player_name] [duration_minutes] [reason]</strong> - Global mute with reason</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>mute_global Ithaqua</li>
<li>mute_global Ithaqua 120</li>
<li>mute_global Ithaqua 60 Spamming</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Affects the player's ability to send messages in all channels</li>
<li>Other players cannot see messages from globally muted players</li>
<li>Duration is in minutes (omit for permanent mute)</li>
<li>Admin players cannot be globally muted</li>
<li>Use with caution - this is a powerful moderation tool</li>
</ul>

<p>"The power to silence must be wielded with wisdom and restraint." - Prof. Armitage</p>
</div>
""",
    },
    "unmute_global": {
        "category": "User Management",
        "description": "Remove global mute from a player",
        "usage": "unmute_global <player_name>",
        "examples": ["unmute_global Ithaqua"],
        "detailed_help": """
<div style="color: #006400;">
<h3>UNMUTE_GLOBAL Command</h3>
<p>Restore a player's ability to communicate across all channels, lifting
the comprehensive silence that was previously applied.</p>

<h4>Usage:</h4>
<ul>
<li><strong>unmute_global [player_name]</strong> - Remove global mute from a player</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>unmute_global Ithaqua</li>
<li>unmute_global Azathoth</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Restores the player's ability to send messages in all channels</li>
<li>You can only unmute players you personally globally muted</li>
<li>Use this command when you believe the player has learned their lesson</li>
</ul>

<p>"Redemption is the highest form of wisdom." - Prof. Armitage</p>
</div>
""",
    },
    "add_admin": {
        "category": "User Management",
        "description": "Grant admin privileges to a player",
        "usage": "add_admin <player_name>",
        "examples": ["add_admin Azathoth"],
        "detailed_help": """
<div style="color: #FFD700;">
<h3>ADD_ADMIN Command</h3>
<p>Grant administrative privileges to a player, as documented in the restricted
archives of Miskatonic University. Admin players are immune to mutes and
have access to powerful moderation tools.</p>

<h4>Usage:</h4>
<ul>
<li><strong>add_admin [player_name]</strong> - Grant admin status to a player</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>add_admin Azathoth</li>
<li>add_admin Ithaqua</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Admin players are immune to all types of mutes</li>
<li>Admin status is permanent until manually removed</li>
<li>Use this power wisely and only for trusted players</li>
<li>Admin players can help with moderation and community management</li>
</ul>

<p>"With great power comes great responsibility." - Prof. Armitage</p>
</div>
""",
    },
    "mutes": {
        "category": "User Management",
        "description": "Show your current mute status and who you have muted",
        "usage": "mutes",
        "examples": ["mutes"],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>MUTES Command</h3>
<p>Display your current mute status and list of players you have muted, as recorded
in the Miskatonic archives of player interactions.</p>

<h4>Usage:</h4>
<ul>
<li><strong>mutes</strong> - Show your mute status and muted players</li>
</ul>

<h4>What it shows:</h4>
<ul>
<li>Players you have muted (personal mutes)</li>
<li>Players you have globally muted</li>
<li>Your admin status</li>
<li>Mute durations and expiry times</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>mutes</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Personal mutes only affect your ability to see messages from that player</li>
<li>Global mutes prevent the player from sending messages to anyone</li>
<li>Admin players are immune to all types of mutes</li>
<li>Mute durations are shown in minutes remaining</li>
<li>For privacy and anti-harassment, you cannot see if others have muted you</li>
</ul>

<p>"Knowledge of one's own restrictions is the first step toward understanding." - Prof. Armitage</p>
</div>
""",
    },
}


def get_help_content(command_name: str = None) -> str:
    """Generate help content for commands with Mythos theming."""
    if command_name:
        command_name = command_name.lower()
        if command_name not in COMMANDS:
            return f"""
<div style="color: #8B0000;">
<h3>Unknown Command: {command_name}</h3>
<p>The forbidden texts contain no mention of such a command.
Perhaps it exists in dimensions yet undiscovered, or perhaps it was never meant to be.</p>
<p>Use 'help' to see all available commands.</p>
</div>
"""

        return COMMANDS[command_name]["detailed_help"]

    # Generate categorized help
    categories = {}
    for cmd, info in COMMANDS.items():
        cat = info["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(cmd)

    help_html = """
<div style="color: #2F4F4F; font-family: 'Courier New', monospace;">
<h2 style="color: #8B0000; text-align: center; border-bottom: 2px solid #8B0000; padding-bottom: 10px;">
    📚 MYTHOSMUD COMMAND GRIMOIRE 📚
</h2>

<p style="text-align: center; font-style: italic; color: #8B4513;">
    "From the depths of the Miskatonic archives, these commands have been transcribed
    for the brave souls who dare to explore our realm of forbidden knowledge."
</p>

<div style="margin: 20px 0; padding: 15px; background-color: rgba(139, 69, 19, 0.1); border-left: 4px solid #8B4513;">
<p><strong>Usage:</strong> Type 'help [command]' for detailed information about any command.</p>
</div>
"""

    for category, commands in sorted(categories.items()):
        help_html += f"""
<div style="margin: 20px 0;">
<h3 style="color: #8B0000; border-bottom: 1px solid #8B0000; padding-bottom: 5px;">
    {category.upper()} COMMANDS
</h3>
<div style="margin-left: 20px;">
"""
        for cmd in sorted(commands):
            help_html += f'<p><strong style="color: #2F4F4F;">{cmd}</strong></p>'
        help_html += "</div></div>"

    help_html += """
<div style="margin-top: 30px; padding: 15px; background-color: rgba(139, 0, 0, 0.1); border: 1px solid #8B0000;">
<p style="text-align: center; font-style: italic; color: #8B0000;">
    "The stars are right, and the time is now. Venture forth, but remember:
    some knowledge is better left undiscovered."
</p>
</div>
</div>
"""

    return help_html


@router.post("", status_code=status.HTTP_200_OK)
async def handle_command(
    req: CommandRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    """Handle incoming command requests with comprehensive logging."""
    command_line = req.command

    # Check if user is authenticated
    if not current_user:
        raise HTTPException(status_code=401, detail="Authentication required")

    player_name = get_username_from_user(current_user)

    logger.info("Command received", player=player_name, command=command_line, length=len(command_line))

    if len(command_line) > MAX_COMMAND_LENGTH:
        logger.warning(
            "Command too long rejected",
            player=player_name,
            command=command_line,
            length=len(command_line),
            max_length=MAX_COMMAND_LENGTH,
        )
        raise HTTPException(
            status_code=400,
            detail=f"Command too long (max {MAX_COMMAND_LENGTH} characters)",
        )

    if is_suspicious_input(command_line):
        logger.warning("Suspicious command rejected", player=player_name, command=command_line)
        raise HTTPException(status_code=400, detail="Invalid characters or suspicious input detected")

    command_line = clean_command_input(command_line)
    if not command_line:
        logger.debug("Empty command after cleaning", player=player_name)
        return {"result": ""}

    # Normalize command by removing optional slash prefix
    command_line = normalize_command(command_line)
    if not command_line:
        logger.debug("Empty command after normalization", player=player_name)
        return {"result": ""}

    # Initialize alias storage
    try:
        alias_storage = AliasStorage()
        logger.debug("AliasStorage initialized successfully", player=player_name)
    except Exception as e:
        logger.error("Failed to initialize AliasStorage", player=player_name, error=str(e))
        # Continue without alias storage
        alias_storage = None

    # Check for alias expansion before command processing
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    logger.debug("Command parsed", player=player_name, command=cmd, args=args, original_command=command_line)

    # Handle alias management commands first (don't expand these)
    if cmd in ["alias", "aliases", "unalias"]:
        logger.debug("Processing alias management command", player=player_name, command=cmd)
        return await process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Check if this is an alias
    alias = alias_storage.get_alias(player_name, cmd)
    if alias:
        logger.debug("Alias found, expanding", player=player_name, alias_name=alias.name, original_command=cmd)
        # Expand the alias
        expanded_command = alias.get_expanded_command(args)
        # Recursively process the expanded command (with depth limit to prevent loops)
        result = await handle_expanded_command(
            expanded_command, current_user, request, alias_storage, player_name, depth=0, alias_chain=[]
        )
        # Add alias chain information to the result
        if "alias_chain" not in result:
            result["alias_chain"] = [{"original": cmd, "expanded": expanded_command, "alias_name": alias.name}]
        return result

    # Process command normally
    logger.debug("Processing standard command", player=player_name, command=cmd)
    return await process_command(cmd, args, current_user, request, alias_storage, player_name)


async def handle_expanded_command(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
    depth: int = 0,
    alias_chain: list[dict] = None,
) -> dict:
    """Handle command processing with alias expansion and loop detection."""
    logger.debug("Handling expanded command", player=player_name, command=command_line, depth=depth)

    # Prevent infinite loops
    if depth > 10:
        logger.error("Alias loop detected", player=player_name, depth=depth, command=command_line)
        return {"result": "Error: Alias loop detected. Maximum recursion depth exceeded."}

    # Initialize alias chain if not provided
    if alias_chain is None:
        alias_chain = []

    # Handle alias management commands first (don't expand these)
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in ["alias", "aliases", "unalias"]:
        logger.debug("Processing alias management command in expanded context", player=player_name, command=cmd)
        return await process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Check for alias expansion
    alias = alias_storage.get_alias(player_name, cmd)
    if alias:
        logger.debug("Alias expansion in recursive call", player=player_name, alias_name=alias.name, depth=depth)
        # Track alias usage for client display
        alias_info = {
            "original": cmd,
            "expanded": alias.get_expanded_command(args),
            "alias_name": alias.name,
        }
        alias_chain.append(alias_info)

        # Expand the alias and recurse
        expanded_command = alias.get_expanded_command(args)
        result = await handle_expanded_command(
            expanded_command, current_user, request, alias_storage, player_name, depth + 1, alias_chain
        )

        # Add alias chain to result if this is the top level
        if depth == 0 and alias_chain:
            result["alias_chain"] = alias_chain

        return result

    # Process command normally
    result = await process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Add alias chain to result if this is the top level
    if depth == 0 and alias_chain:
        result["alias_chain"] = alias_chain

    return result


async def process_command(
    cmd: str, args: list, current_user: dict, request: Request, alias_storage: AliasStorage, player_name: str
) -> dict:
    """Process a command with alias management support."""
    logger.debug("=== COMMAND HANDLER DEBUG: Processing command ===", player=player_name, command=cmd, args=args)

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    # Handle help command first
    if cmd == "help":
        logger.debug("Processing help command", player=player_name, args=args)
        if len(args) > 1:
            logger.warning("Help command with too many arguments", player=player_name, args=args)
            return {"result": "Too many arguments. Usage: help [command]"}
        command_name = args[0] if args else None
        return {"result": get_help_content(command_name)}

    # Handle alias management commands
    if cmd == "alias":
        logger.debug("Processing alias command", player=player_name, args=args)
        return handle_alias_command(args, alias_storage, player_name)

    if cmd == "aliases":
        logger.debug("Processing aliases command", player=player_name)
        return handle_aliases_command(alias_storage, player_name)

    if cmd == "unalias":
        logger.debug("Processing unalias command", player=player_name, args=args)
        return handle_unalias_command(args, alias_storage, player_name)

    if cmd == "look":
        logger.debug("Processing look command", player=player_name, args=args)
        if not persistence:
            logger.warning("Look command failed - no persistence layer", player=player_name)
            return {"result": "You see nothing special."}
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Look command failed - player not found", player=player_name)
            return {"result": "You see nothing special."}
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            logger.warning("Look command failed - room not found", player=player_name, room_id=room_id)
            return {"result": "You see nothing special."}
        if args:
            direction = args[0].lower()
            logger.debug("Looking in direction", player=player_name, direction=direction, room_id=room_id)
            exits = room.exits
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = persistence.get_room(target_room_id)
                if target_room:
                    name = target_room.name
                    desc = target_room.description
                    logger.debug(
                        "Looked at room in direction",
                        player=player_name,
                        direction=direction,
                        target_room_id=target_room_id,
                    )
                    return {"result": f"{name}\n{desc}"}
            logger.debug("No valid exit in direction", player=player_name, direction=direction, room_id=room_id)
            return {"result": "You see nothing special that way."}
        name = room.name
        desc = room.description
        exits = room.exits
        # Only include exits that have valid room IDs (not null)
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        logger.debug("Looked at current room", player=player_name, room_id=room_id, exits=valid_exits)
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}
    elif cmd == "go":
        logger.debug("Processing go command", player=player_name, args=args, args_length=len(args))
        if not persistence:
            logger.warning("Go command failed - no persistence layer", player=player_name)
            return {"result": "You can't go that way"}
        if not args:
            logger.warning(
                "Go command failed - no direction specified", player=player_name, args=args, args_type=type(args)
            )
            return {"result": "Go where? Usage: go <direction>"}
        direction = args[0].lower()
        logger.debug("Player attempting to move", player=player_name, direction=direction)
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Go command failed - player not found", player=player_name)
            return {"result": "You can't go that way"}
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            logger.warning("Go command failed - current room not found", player=player_name, room_id=room_id)
            return {"result": "You can't go that way"}
        exits = room.exits
        target_room_id = exits.get(direction)
        if not target_room_id:
            logger.debug("No exit in direction", player=player_name, direction=direction, room_id=room_id)
            return {"result": "You can't go that way"}
        target_room = persistence.get_room(target_room_id)
        if not target_room:
            logger.warning(
                "Go command failed - target room not found", player=player_name, target_room_id=target_room_id
            )
            return {"result": "You can't go that way"}

        # Use MovementService for atomic movement
        # Get the event bus from the app state if available
        event_bus = getattr(app.state, "event_bus", None) if app else None
        movement_service = MovementService(event_bus)
        success = movement_service.move_player(player.player_id, room_id, target_room_id)
        if not success:
            logger.warning("Movement failed", player=player_name, from_room=room_id, to_room=target_room_id)
            return {"result": "You can't go that way"}

        # Room ID is updated in the Player object via MovementService

        # Return room description
        name = target_room.name
        desc = target_room.description
        exits = target_room.exits
        # Only include exits that have valid room IDs (not null)
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}
    elif cmd == "say":
        logger.debug("=== COMMAND HANDLER DEBUG: Processing say command ===", player=player_name, args=args)

        if not persistence:
            logger.warning("Say command failed - no persistence layer", player=player_name)
            return {"result": "You cannot speak right now."}

        if not args:
            logger.warning("Say command failed - no message provided", player=player_name)
            return {"result": "Say what? Usage: say <message>"}

        message = " ".join(args).strip()
        if not message:
            return {"result": "You open your mouth, but no words come out."}

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Say command failed - player not found", player=player_name)
            return {"result": "You cannot speak right now."}

        # Initialize chat service
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Send the message
        logger.debug(
            "=== COMMAND HANDLER DEBUG: About to call chat_service.send_say_message ===",
            player_id=str(player.player_id),
            message=message,
        )
        result = await chat_service.send_say_message(str(player.player_id), message)
        logger.debug("=== COMMAND HANDLER DEBUG: chat_service.send_say_message completed ===", result=result)

        if result["success"]:
            # Format the message for display
            formatted_message = f"{player.name} says: {message}"
            logger.info("Say message sent successfully", player=player_name, message_length=len(message))
            return {"result": formatted_message}
        else:
            logger.warning("Say message failed", player=player_name, error=result.get("error"))
            return {"result": result.get("error", "You cannot speak right now.")}

    elif cmd in ["emote", "me"]:
        logger.debug("=== COMMAND HANDLER DEBUG: Processing emote command ===", player=player_name, args=args)

        if not persistence:
            logger.warning("Emote command failed - no persistence layer", player=player_name)
            return {"result": "You cannot emote right now."}

        if not args:
            logger.warning("Emote command failed - no action provided", player=player_name)
            return {"result": "Emote what? Usage: emote <action>"}

        action = " ".join(args).strip()
        if not action:
            return {"result": "You attempt to emote, but nothing happens."}

        if len(action) > 200:
            return {"result": "Emote too long (max 200 characters)"}

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Emote command failed - player not found", player=player_name)
            return {"result": "You cannot emote right now."}

        # Initialize chat service
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Send the emote message
        logger.debug(
            "=== COMMAND HANDLER DEBUG: About to call chat_service.send_emote_message ===",
            player_id=str(player.player_id),
            action=action,
        )
        result = await chat_service.send_emote_message(str(player.player_id), action)
        logger.debug("=== COMMAND HANDLER DEBUG: chat_service.send_emote_message completed ===", result=result)

        if result["success"]:
            # Format the message for display
            formatted_message = f"{player.name} {action}"
            logger.info("Emote message sent successfully", player=player_name, action_length=len(action))
            return {"result": formatted_message}
        else:
            logger.warning("Emote message failed", player=player_name, error=result.get("error"))
            return {"result": result.get("error", "You cannot emote right now.")}

    # Check for predefined emotes (like 'twibble', 'dance', etc.)
    elif _is_predefined_emote(cmd):
        logger.debug(
            "=== COMMAND HANDLER DEBUG: Processing predefined emote command ===", player=player_name, emote=cmd
        )

        if not persistence:
            logger.warning("Predefined emote command failed - no persistence layer", player=player_name)
            return {"result": "You cannot emote right now."}

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Predefined emote command failed - player not found", player=player_name)
            return {"result": "You cannot emote right now."}

        # Initialize chat service
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Send the predefined emote message
        logger.debug(
            "=== COMMAND HANDLER DEBUG: About to call chat_service.send_predefined_emote ===",
            player_id=str(player.player_id),
            emote_command=cmd,
        )
        result = await chat_service.send_predefined_emote(str(player.player_id), cmd)
        logger.debug("=== COMMAND HANDLER DEBUG: chat_service.send_predefined_emote completed ===", result=result)

        if result["success"]:
            # Return the self message for the player
            logger.info("Predefined emote message sent successfully", player=player_name, emote=cmd)
            return {"result": result["self_message"]}
        else:
            logger.warning("Predefined emote message failed", player=player_name, error=result.get("error"))
            return {"result": result.get("error", "You cannot emote right now.")}

    elif cmd == "pose":
        logger.debug("=== COMMAND HANDLER DEBUG: Processing pose command ===", player=player_name, args=args)

        if not persistence:
            logger.warning("Pose command failed - no persistence layer", player=player_name)
            return {"result": "You cannot pose right now."}

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Pose command failed - player not found", player=player_name)
            return {"result": "You cannot pose right now."}

        # Initialize chat service
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        if not args:
            # Display current pose
            current_pose = chat_service.get_player_pose(str(player.player_id))
            if current_pose:
                return {"result": f"Your current pose: {current_pose}"}
            else:
                return {"result": "You are not currently posing."}
        else:
            # Set new pose
            pose = " ".join(args).strip()
            if not pose:
                return {"result": "Pose what? Usage: pose [description]"}

            if len(pose) > 100:
                return {"result": "Pose too long (max 100 characters)"}

            # Send the pose message
            logger.debug(
                "=== COMMAND HANDLER DEBUG: About to call chat_service.set_player_pose ===",
                player_id=str(player.player_id),
                pose=pose,
            )
            result = await chat_service.set_player_pose(str(player.player_id), pose)
            logger.debug("=== COMMAND HANDLER DEBUG: chat_service.set_player_pose completed ===", result=result)

            if result["success"]:
                formatted_message = f"{player.name} {pose}"
                logger.info("Pose set successfully", player=player_name, pose_length=len(pose))
                return {"result": formatted_message}
            else:
                logger.warning("Pose set failed", player=player_name, error=result.get("error"))
                return {"result": result.get("error", "You cannot pose right now.")}

    # User management commands
    elif cmd == "mute":
        logger.debug("Processing mute command", player=player_name, args=args)
        if not args:
            return {"result": "Usage: mute <player_name> [duration_minutes] [reason]"}

        target_name = args[0]
        duration_minutes = None
        reason = ""

        if len(args) > 1:
            try:
                duration_minutes = int(args[1])
            except ValueError:
                # If second arg isn't a number, treat it as part of the reason
                reason = " ".join(args[1:])

        if len(args) > 2 and duration_minutes is not None:
            reason = " ".join(args[2:])

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "You cannot perform this action right now."}

        # Initialize services
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Resolve target player
        target_player = player_service.resolve_player_name(target_name)
        if not target_player:
            return {"result": f"Player '{target_name}' not found."}

        # Perform mute
        success = chat_service.mute_player(str(player.player_id), target_name)
        if success:
            duration_text = f" for {duration_minutes} minutes" if duration_minutes else " permanently"
            return {"result": f"You have muted {target_name}{duration_text}."}
        else:
            return {"result": f"Failed to mute {target_name}."}

    elif cmd == "unmute":
        logger.debug("Processing unmute command", player=player_name, args=args)
        if not args:
            return {"result": "Usage: unmute <player_name>"}

        target_name = args[0]

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "You cannot perform this action right now."}

        # Initialize services
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Resolve target player
        target_player = player_service.resolve_player_name(target_name)
        if not target_player:
            return {"result": f"Player '{target_name}' not found."}

        # Perform unmute
        success = chat_service.unmute_player(str(player.player_id), target_name)
        if success:
            return {"result": f"You have unmuted {target_name}."}
        else:
            return {"result": f"Failed to unmute {target_name}."}

    elif cmd == "mute_global":
        logger.debug("Processing mute_global command", player=player_name, args=args)
        if not args:
            return {"result": "Usage: mute_global <player_name> [duration_minutes] [reason]"}

        target_name = args[0]
        duration_minutes = None
        reason = ""

        if len(args) > 1:
            try:
                duration_minutes = int(args[1])
            except ValueError:
                # If second arg isn't a number, treat it as part of the reason
                reason = " ".join(args[1:])

        if len(args) > 2 and duration_minutes is not None:
            reason = " ".join(args[2:])

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "You cannot perform this action right now."}

        # Initialize services
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Resolve target player
        target_player = player_service.resolve_player_name(target_name)
        if not target_player:
            return {"result": f"Player '{target_name}' not found."}

        # Perform global mute
        success = chat_service.mute_global(str(player.player_id), target_name, duration_minutes, reason)
        if success:
            duration_text = f" for {duration_minutes} minutes" if duration_minutes else " permanently"
            return {"result": f"You have globally muted {target_name}{duration_text}."}
        else:
            return {"result": f"Failed to globally mute {target_name}."}

    elif cmd == "unmute_global":
        logger.debug("Processing unmute_global command", player=player_name, args=args)
        if not args:
            return {"result": "Usage: unmute_global <player_name>"}

        target_name = args[0]

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "You cannot perform this action right now."}

        # Initialize services
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Resolve target player
        target_player = player_service.resolve_player_name(target_name)
        if not target_player:
            return {"result": f"Player '{target_name}' not found."}

        # Perform global unmute
        success = chat_service.unmute_global(str(player.player_id), target_name)
        if success:
            return {"result": f"You have globally unmuted {target_name}."}
        else:
            return {"result": f"Failed to globally unmute {target_name}."}

    elif cmd == "add_admin":
        logger.debug("Processing add_admin command", player=player_name, args=args)
        if not args:
            return {"result": "Usage: add_admin <player_name>"}

        target_name = args[0]

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "You cannot perform this action right now."}

        # Initialize services
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Resolve target player
        target_player = player_service.resolve_player_name(target_name)
        if not target_player:
            return {"result": f"Player '{target_name}' not found."}

        # Add admin status
        success = chat_service.add_admin(target_player.id)
        if success:
            return {"result": f"You have added {target_name} as an admin."}
        else:
            return {"result": f"Failed to add {target_name} as admin."}

    elif cmd == "mutes":
        logger.debug("Processing mutes command", player=player_name, args=args)

        # Get player information
        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            return {"result": "You cannot perform this action right now."}

        # Initialize services
        from .game.player_service import PlayerService
        from .game.room_service import RoomService

        room_service = RoomService(persistence)
        player_service = PlayerService(persistence)
        chat_service = ChatService(persistence, room_service, player_service)

        # Get mute status
        mute_info = chat_service.get_mute_status(str(player.player_id))
        return {"result": mute_info}

    else:
        return {"result": f"Unknown command: {cmd}"}


def handle_alias_command(args: list, alias_storage: AliasStorage, player_name: str) -> dict:
    """Handle the alias command for creating and viewing aliases."""
    logger.debug("Processing alias command", player=player_name, args=args)

    if not args:
        logger.warning("Alias command with no arguments", player=player_name)
        return {"result": "Usage: alias <name> <command> or alias <name> to view"}

    alias_name = args[0]

    # If only one argument, show the alias details
    if len(args) == 1:
        logger.debug("Viewing alias", player=player_name, alias_name=alias_name)
        alias = alias_storage.get_alias(player_name, alias_name)
        if alias:
            logger.debug("Alias found", player=player_name, alias_name=alias_name, command=alias.command)
            return {"result": f"Alias '{alias_name}' -> '{alias.command}'"}
        else:
            logger.debug("Alias not found", player=player_name, alias_name=alias_name)
            return {"result": f"No alias found with name '{alias_name}'"}

    # Create or update alias
    command = " ".join(args[1:])
    logger.debug("Creating/updating alias", player=player_name, alias_name=alias_name, command=command)

    # Validate alias name
    if not alias_storage.validate_alias_name(alias_name):
        logger.warning("Invalid alias name", player=player_name, alias_name=alias_name)
        return {
            "result": "Invalid alias name. Must start with a letter and contain only alphanumeric characters and underscores."
        }

    # Validate command
    if not alias_storage.validate_alias_command(command):
        logger.warning("Invalid alias command", player=player_name, alias_name=alias_name, command=command)
        return {"result": "Invalid command. Cannot alias reserved commands or empty commands."}

    # Check alias count limit
    if alias_storage.get_alias_count(player_name) >= 50:
        existing_alias = alias_storage.get_alias(player_name, alias_name)
        if not existing_alias:
            logger.warning(
                "Alias limit reached", player=player_name, alias_count=alias_storage.get_alias_count(player_name)
            )
            return {"result": "Maximum number of aliases (50) reached. Remove some aliases before creating new ones."}

    # Create the alias
    alias = alias_storage.create_alias(player_name, alias_name, command)
    if alias:
        logger.info("Alias created", player=player_name, alias_name=alias_name, command=command)
        return {"result": f"Alias '{alias_name}' created: '{command}'"}
    else:
        logger.error("Failed to create alias", player=player_name, alias_name=alias_name, command=command)
        return {"result": "Failed to create alias. Please check your input."}


def handle_aliases_command(alias_storage: AliasStorage, player_name: str) -> dict:
    """Handle the aliases command for listing all aliases."""
    logger.debug("Listing aliases", player=player_name)
    aliases = alias_storage.get_player_aliases(player_name)

    if not aliases:
        logger.debug("No aliases found", player=player_name)
        return {"result": "You have no aliases defined."}

    # Format alias list
    alias_list = []
    for alias in aliases:
        alias_list.append(f"  {alias.name} -> {alias.command}")

    result = f"You have {len(aliases)} alias(es):\n" + "\n".join(alias_list)
    logger.debug("Aliases listed", player=player_name, alias_count=len(aliases))
    return {"result": result}


def handle_unalias_command(args: list, alias_storage: AliasStorage, player_name: str) -> dict:
    """Handle the unalias command for removing aliases."""
    logger.debug("Processing unalias command", player=player_name, args=args)

    if not args:
        logger.warning("Unalias command with no arguments", player=player_name)
        return {"result": "Usage: unalias <name>"}

    alias_name = args[0]
    logger.debug("Removing alias", player=player_name, alias_name=alias_name)

    # Check if alias exists
    existing_alias = alias_storage.get_alias(player_name, alias_name)
    if not existing_alias:
        logger.debug("Alias not found for removal", player=player_name, alias_name=alias_name)
        return {"result": f"No alias found with name '{alias_name}'"}

    # Remove the alias
    if alias_storage.remove_alias(player_name, alias_name):
        logger.info("Alias removed", player=player_name, alias_name=alias_name)
        return {"result": f"Alias '{alias_name}' removed."}
    else:
        logger.error("Failed to remove alias", player=player_name, alias_name=alias_name)
        return {"result": f"Failed to remove alias '{alias_name}'."}
