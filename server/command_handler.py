import re

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .auth import get_current_user

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


@router.post("/", status_code=status.HTTP_200_OK)
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
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    # Handle help command first
    if cmd == "help":
        if len(args) > 1:
            return {"result": "Too many arguments. Usage: help [command]"}
        command_name = args[0] if args else None
        return {"result": get_help_content(command_name)}

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
