import re

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .alias_storage import AliasStorage
from .auth.users import get_current_user

router = APIRouter(prefix="/command", tags=["command"])


class CommandRequest(BaseModel):
    command: str


# Patterns to reject for command injection (expand as needed)
INJECTION_PATTERNS = [
    r"[;|&]",  # shell metacharacters
    r"\b(or|and)\b.*=",  # SQL injection
    r"__import__|eval|exec|system|os\.",  # Python injection
    r"%[a-zA-Z]",  # format string
]


def is_suspicious_input(command: str) -> bool:
    for pat in INJECTION_PATTERNS:
        if re.search(pat, command, re.IGNORECASE):
            return True
    return False


def clean_command_input(command: str) -> str:
    # Collapse multiple spaces, strip
    return re.sub(r"\s+", " ", command).strip()


MAX_COMMAND_LENGTH = 50


# Command definitions for help system
COMMANDS = {
    "look": {
        "category": "Exploration",
        "description": ("Examine your surroundings or look in a specific direction"),
        "usage": "look [direction]",
        "examples": ["look", "look north", "look east"],
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
        "usage": "go <direction>",
        "examples": ["go north", "go south", "go east", "go west"],
        "detailed_help": """
<div style="color: #2F4F4F;">
<h3>GO Command</h3>
<p>Traverse the non-Euclidean corridors of our world. Each step brings you closer
to revelations best left undiscovered.</p>

<h4>Usage:</h4>
<ul>
<li><strong>go [direction]</strong> - Move in the specified direction</li>
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
<li>go south</li>
<li>go east</li>
<li>go west</li>
</ul>

<p>Remember: "The geometry of this place is not as it seems." - Prof. Armitage</p>
</div>
""",
    },
    "say": {
        "category": "Communication",
        "description": "Speak to others in the same room",
        "usage": "say <message>",
        "examples": ["say Hello there!", "say What eldritch horrors await us?"],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>SAY Command</h3>
<p>Give voice to your thoughts, though beware what echoes back from the shadows.
Your words may attract attention from entities best left undisturbed.</p>

<h4>Usage:</h4>
<ul>
<li><strong>say [message]</strong> - Speak to others in your current location</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>say Hello there!</li>
<li>say What eldritch horrors await us?</li>
<li>say The stars are right...</li>
</ul>

<p>Warning: "Some things that speak should not be heard." - Miskatonic University Archives</p>
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
        "usage": "help [command]",
        "examples": ["help", "help look", "help go"],
        "detailed_help": """
<div style="color: #4B0082;">
<h3>HELP Command</h3>
<p>Seek knowledge from the ancient tomes of command lore. This command reveals
the secrets of interaction with our world.</p>

<h4>Usage:</h4>
<ul>
<li><strong>help</strong> - Show all available commands</li>
<li><strong>help [command]</strong> - Get detailed help for a specific command</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>help</li>
<li>help look</li>
<li>help go</li>
<li>help say</li>
</ul>

<p>"Knowledge is power, but some knowledge comes at a price." - Restricted Section</p>
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
def handle_command(
    req: CommandRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    command_line = req.command
    if len(command_line) > MAX_COMMAND_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Command too long (max {MAX_COMMAND_LENGTH} characters)",
        )
    if is_suspicious_input(command_line):
        raise HTTPException(status_code=400, detail="Invalid characters or suspicious input detected")
    command_line = clean_command_input(command_line)
    if not command_line:
        return {"result": ""}

    # Initialize alias storage
    alias_storage = AliasStorage()
    player_name = current_user["username"]

    # Check for alias expansion before command processing
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    # Handle alias management commands first (don't expand these)
    if cmd in ["alias", "aliases", "unalias"]:
        return process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Check if this is an alias
    alias = alias_storage.get_alias(player_name, cmd)
    if alias:
        # Expand the alias
        expanded_command = alias.get_expanded_command(args)
        # Recursively process the expanded command (with depth limit to prevent loops)
        result = handle_expanded_command(
            expanded_command, current_user, request, alias_storage, player_name, depth=0, alias_chain=[]
        )
        # Add alias chain information to the result
        if "alias_chain" not in result:
            result["alias_chain"] = [{"original": cmd, "expanded": expanded_command, "alias_name": alias.name}]
        return result

    # Process command normally
    return process_command(cmd, args, current_user, request, alias_storage, player_name)


def handle_expanded_command(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage,
    player_name: str,
    depth: int = 0,
    alias_chain: list[dict] = None,
) -> dict:
    """Handle command processing with alias expansion and loop detection."""
    # Prevent infinite loops
    if depth > 10:
        return {"result": "Error: Alias loop detected. Maximum recursion depth exceeded."}

    # Initialize alias chain if not provided
    if alias_chain is None:
        alias_chain = []

    # Handle alias management commands first (don't expand these)
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in ["alias", "aliases", "unalias"]:
        return process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Check for alias expansion
    alias = alias_storage.get_alias(player_name, cmd)
    if alias:
        # Track alias usage for client display
        alias_info = {
            "original": cmd,
            "expanded": alias.get_expanded_command(args),
            "alias_name": alias.name,
        }
        alias_chain.append(alias_info)

        # Expand the alias and recurse
        expanded_command = alias.get_expanded_command(args)
        result = handle_expanded_command(
            expanded_command, current_user, request, alias_storage, player_name, depth + 1, alias_chain
        )

        # Add alias chain to result if this is the top level
        if depth == 0 and alias_chain:
            result["alias_chain"] = alias_chain

        return result

    # Process command normally
    result = process_command(cmd, args, current_user, request, alias_storage, player_name)

    # Add alias chain to result if this is the top level
    if depth == 0 and alias_chain:
        result["alias_chain"] = alias_chain

    return result


def process_command(
    cmd: str, args: list, current_user: dict, request: Request, alias_storage: AliasStorage, player_name: str
) -> dict:
    """Process a command with alias management support."""
    app = request.app if request else None
    persistence = app.state.persistence if app else None

    # Handle help command first
    if cmd == "help":
        if len(args) > 1:
            return {"result": "Too many arguments. Usage: help [command]"}
        command_name = args[0] if args else None
        return {"result": get_help_content(command_name)}

    # Handle alias management commands
    if cmd == "alias":
        return handle_alias_command(args, alias_storage, player_name)

    if cmd == "aliases":
        return handle_aliases_command(alias_storage, player_name)

    if cmd == "unalias":
        return handle_unalias_command(args, alias_storage, player_name)

    if cmd == "look":
        if not persistence:
            return {"result": "You see nothing special."}
        player = persistence.get_player_by_name(current_user["username"])
        if not player:
            return {"result": "You see nothing special."}
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You see nothing special."}
        if args:
            direction = args[0].lower()
            exits = room.get("exits", {})
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = persistence.get_room(target_room_id)
                if target_room:
                    name = target_room.get("name", "")
                    desc = target_room.get("description", "You see nothing special.")
                    return {"result": f"{name}\n{desc}"}
            return {"result": "You see nothing special that way."}
        name = room.get("name", "")
        desc = room.get("description", "You see nothing special.")
        exits = room.get("exits", {})
        # Only include exits that have valid room IDs (not null)
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}
    elif cmd == "go":
        if not persistence:
            return {"result": "You can't go that way"}
        if not args:
            return {"result": "Go where? Usage: go <direction>"}
        direction = args[0].lower()
        player = persistence.get_player_by_name(current_user["username"])
        if not player:
            return {"result": "You can't go that way"}
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You can't go that way"}
        exits = room.get("exits", {})
        target_room_id = exits.get(direction)
        if not target_room_id:
            return {"result": "You can't go that way"}
        target_room = persistence.get_room(target_room_id)
        if not target_room:
            return {"result": "You can't go that way"}
        # Move the player: update and persist current_room_id
        player.current_room_id = target_room_id
        persistence.save_player(player)
        current_user["current_room_id"] = target_room_id
        name = target_room.get("name", "")
        desc = target_room.get("description", "You see nothing special.")
        exits = target_room.get("exits", {})
        # Only include exits that have valid room IDs (not null)
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}
    elif cmd == "say":
        message = " ".join(args).strip()
        if not message:
            return {"result": "You open your mouth, but no words come out"}
        return {"result": f"You say: {message}"}
    else:
        return {"result": f"Unknown command: {cmd}"}


def handle_alias_command(args: list, alias_storage: AliasStorage, player_name: str) -> dict:
    """Handle the alias command for creating and viewing aliases."""
    if not args:
        return {"result": "Usage: alias <name> <command> or alias <name> to view"}

    alias_name = args[0]

    # If only one argument, show the alias details
    if len(args) == 1:
        alias = alias_storage.get_alias(player_name, alias_name)
        if alias:
            return {"result": f"Alias '{alias_name}' -> '{alias.command}'"}
        else:
            return {"result": f"No alias found with name '{alias_name}'"}

    # Create or update alias
    command = " ".join(args[1:])

    # Validate alias name
    if not alias_storage.validate_alias_name(alias_name):
        return {
            "result": "Invalid alias name. Must start with a letter and contain only alphanumeric characters and underscores."
        }

    # Validate command
    if not alias_storage.validate_alias_command(command):
        return {"result": "Invalid command. Cannot alias reserved commands or empty commands."}

    # Check alias count limit
    if alias_storage.get_alias_count(player_name) >= 50:
        existing_alias = alias_storage.get_alias(player_name, alias_name)
        if not existing_alias:
            return {"result": "Maximum number of aliases (50) reached. Remove some aliases before creating new ones."}

    # Create the alias
    alias = alias_storage.create_alias(player_name, alias_name, command)
    if alias:
        return {"result": f"Alias '{alias_name}' created: '{command}'"}
    else:
        return {"result": "Failed to create alias. Please check your input."}


def handle_aliases_command(alias_storage: AliasStorage, player_name: str) -> dict:
    """Handle the aliases command for listing all aliases."""
    aliases = alias_storage.get_player_aliases(player_name)

    if not aliases:
        return {"result": "You have no aliases defined."}

    # Format alias list
    alias_list = []
    for alias in aliases:
        alias_list.append(f"  {alias.name} -> {alias.command}")

    result = f"You have {len(aliases)} alias(es):\n" + "\n".join(alias_list)
    return {"result": result}


def handle_unalias_command(args: list, alias_storage: AliasStorage, player_name: str) -> dict:
    """Handle the unalias command for removing aliases."""
    if not args:
        return {"result": "Usage: unalias <name>"}

    alias_name = args[0]

    # Check if alias exists
    existing_alias = alias_storage.get_alias(player_name, alias_name)
    if not existing_alias:
        return {"result": f"No alias found with name '{alias_name}'"}

    # Remove the alias
    if alias_storage.remove_alias(player_name, alias_name):
        return {"result": f"Alias '{alias_name}' removed."}
    else:
        return {"result": f"Failed to remove alias '{alias_name}'."}
