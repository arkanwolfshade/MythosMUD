"""
Help content and command documentation for MythosMUD.

This module contains the comprehensive command documentation and
help system for the MythosMUD game.
"""

from ..logging_config import get_logger

logger = get_logger(__name__)


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

<p>Note: Your words will be heard by all players currently in the same room.</p>
</div>
""",
    },
    "me": {
        "category": "Communication",
        "description": "Perform an action or emote",
        "usage": "me <action>",
        "examples": ["me adjusts spectacles", "me looks around nervously"],
        "detailed_help": """
<div style="color: #8B008B;">
<h3>ME Command</h3>
<p>Express yourself through actions and emotions. Let others see what you are doing
without speaking words.</p>

<h4>Usage:</h4>
<ul>
<li><strong>me [action]</strong> - Perform an action or emote</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>me adjusts spectacles</li>
<li>me looks around nervously</li>
<li>me examines the ancient tome</li>
<li>me shudders at the sight</li>
</ul>

<p>This command allows you to roleplay actions and emotions that other players can see.</p>
</div>
""",
    },
    "pose": {
        "category": "Communication",
        "description": "Set your character's pose or description",
        "usage": "pose <description>",
        "examples": ["pose is reading an ancient tome", "pose stands guard"],
        "detailed_help": """
<div style="color: #8B008B;">
<h3>POSE Command</h3>
<p>Set a persistent description of what your character is doing or how they appear.
This description will be visible to other players when they look at you.</p>

<h4>Usage:</h4>
<ul>
<li><strong>pose [description]</strong> - Set your character's pose</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>pose is reading an ancient tome</li>
<li>pose stands guard at the entrance</li>
<li>pose appears lost in thought</li>
</ul>

<p>Your pose will remain until you change it or log out.</p>
</div>
""",
    },
    "alias": {
        "category": "System",
        "description": "Create or view command aliases",
        "usage": "alias <name> <command> or alias <name>",
        "examples": ["alias n go north", "alias l look", "alias n"],
        "detailed_help": """
<div style="color: #FF8C00;">
<h3>ALIAS Command</h3>
<p>Create shortcuts for commonly used commands. Aliases allow you to define
your own command names for frequently used actions.</p>

<h4>Usage:</h4>
<ul>
<li><strong>alias [name] [command]</strong> - Create a new alias</li>
<li><strong>alias [name]</strong> - View an existing alias</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>alias n go north</li>
<li>alias l look</li>
<li>alias s say</li>
<li>alias n</li>
</ul>

<h4>Rules:</h4>
<ul>
<li>Alias names must start with a letter</li>
<li>Only alphanumeric characters and underscores allowed</li>
<li>Maximum 50 aliases per player</li>
<li>Cannot alias reserved commands</li>
</ul>

<p>After creating an alias, you can use the alias name as a command.</p>
</div>
""",
    },
    "aliases": {
        "category": "System",
        "description": "List all your aliases",
        "usage": "aliases",
        "examples": ["aliases"],
        "detailed_help": """
<div style="color: #FF8C00;">
<h3>ALIASES Command</h3>
<p>View all the aliases you have created for quick command access.</p>

<h4>Usage:</h4>
<ul>
<li><strong>aliases</strong> - List all your aliases</li>
</ul>

<h4>Example:</h4>
<ul>
<li>aliases</li>
</ul>

<p>This will show you all your current aliases and what commands they execute.</p>
</div>
""",
    },
    "unalias": {
        "category": "System",
        "description": "Remove a command alias",
        "usage": "unalias <name>",
        "examples": ["unalias n", "unalias l"],
        "detailed_help": """
<div style="color: #FF8C00;">
<h3>UNALIAS Command</h3>
<p>Remove an alias that you no longer need or want to change.</p>

<h4>Usage:</h4>
<ul>
<li><strong>unalias [name]</strong> - Remove the specified alias</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>unalias n</li>
<li>unalias l</li>
</ul>

<p>After removing an alias, you can create a new one with the same name if desired.</p>
</div>
""",
    },
    "help": {
        "category": "System",
        "description": "Get help on commands",
        "usage": "help [command]",
        "examples": ["help", "help look", "help go"],
        "detailed_help": """
<div style="color: #4169E1;">
<h3>HELP Command</h3>
<p>Access the ancient knowledge contained within these digital scrolls.
Learn about available commands and their proper usage.</p>

<h4>Usage:</h4>
<ul>
<li><strong>help</strong> - Show general help and command categories</li>
<li><strong>help [command]</strong> - Get detailed help for a specific command</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>help</li>
<li>help look</li>
<li>help go</li>
<li>help alias</li>
</ul>

<p>Use this command whenever you need guidance on how to use the game's features.</p>
</div>
""",
    },
    "npc": {
        "category": "Administration",
        "description": "NPC management commands (admin only)",
        "usage": "npc <subcommand> [arguments]",
        "examples": [
            "npc help",
            "npc list",
            "npc create TestNPC shopkeeper arkhamcity_downtown earth_arkhamcity_downtown_001",
        ],
        "detailed_help": """
<div style="color: #8B0000;">
<h3>NPC Admin Commands</h3>
<p>As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.</p>

<h4>Usage:</h4>
<ul>
<li><strong>npc help</strong> - Show NPC command help</li>
<li><strong>npc list</strong> - List all NPC definitions</li>
<li><strong>npc create &lt;name&gt; &lt;type&gt; &lt;sub_zone_id&gt; &lt;room_id&gt;</strong> - Create a new NPC definition</li>
<li><strong>npc edit &lt;id&gt; &lt;field&gt; &lt;value&gt;</strong> - Edit an NPC definition</li>
<li><strong>npc delete &lt;id&gt;</strong> - Delete an NPC definition</li>
<li><strong>npc spawn &lt;definition_id&gt; &lt;room_id&gt;</strong> - Spawn an NPC instance</li>
<li><strong>npc despawn &lt;npc_id&gt;</strong> - Despawn an NPC instance</li>
<li><strong>npc move &lt;npc_id&gt; &lt;room_id&gt;</strong> - Move an NPC instance</li>
<li><strong>npc stats &lt;npc_id&gt;</strong> - Get NPC instance stats</li>
<li><strong>npc population</strong> - Get NPC population statistics</li>
<li><strong>npc zone [zone_key]</strong> - Get NPC zone statistics</li>
<li><strong>npc status</strong> - Get NPC system status</li>
<li><strong>npc behavior &lt;npc_id&gt; &lt;behavior_type&gt;</strong> - Set NPC behavior type</li>
<li><strong>npc react &lt;npc_id&gt; &lt;reaction_type&gt;</strong> - Trigger NPC reaction</li>
<li><strong>npc stop &lt;npc_id&gt;</strong> - Stop NPC current behavior</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>npc help</li>
<li>npc list</li>
<li>npc create TestShopkeeper shopkeeper arkhamcity_downtown earth_arkhamcity_downtown_001</li>
<li>npc spawn 1 earth_arkhamcity_downtown_001</li>
<li>npc population</li>
<li>npc status</li>
<li>npc behavior npc_001 aggressive</li>
<li>npc react npc_001 greet</li>
<li>npc stop npc_001</li>
</ul>

<h4>NPC Types:</h4>
<ul>
<li>shopkeeper - Merchant NPCs</li>
<li>passive_mob - Non-aggressive creatures</li>
<li>aggressive_mob - Hostile creatures</li>
<li>quest_giver - Quest NPCs</li>
<li>merchant - Trading NPCs</li>
</ul>

<h4>Behavior Types:</h4>
<ul>
<li>passive - NPC remains non-aggressive</li>
<li>aggressive - NPC becomes hostile</li>
<li>defensive - NPC defends when attacked</li>
<li>wander - NPC moves randomly</li>
<li>patrol - NPC follows a patrol route</li>
<li>guard - NPC guards a specific area</li>
<li>idle - NPC remains stationary</li>
</ul>

<h4>Reaction Types:</h4>
<ul>
<li>greet - NPC greets players</li>
<li>attack - NPC attacks target</li>
<li>flee - NPC runs away</li>
<li>investigate - NPC investigates area</li>
<li>alert - NPC becomes alert</li>
<li>calm - NPC becomes calm</li>
<li>excited - NPC becomes excited</li>
<li>suspicious - NPC becomes suspicious</li>
</ul>

<p><strong>Note:</strong> These commands require admin privileges. Only administrators
can manage NPCs in the world.</p>
</div>
""",
    },
    "who": {
        "category": "Utility",
        "description": "List online players with their levels and locations",
        "usage": "who [name]",
        "examples": ["who", "who alice", "who al"],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>WHO Command</h3>
<p>Peer into the shadows to see which fellow investigators are currently active
in our realm. This command reveals the presence of other players, their levels,
and their current locations.</p>

<h4>Usage:</h4>
<ul>
<li><strong>who</strong> - List all online players with levels and locations</li>
<li><strong>who [name]</strong> - Search for specific players by name (case-insensitive partial matching)</li>
</ul>

<h4>Output Format:</h4>
<ul>
<li><strong>PlayerName [Level] - Zone: Sub-zone: Room</strong> - Regular player</li>
<li><strong>PlayerName [Level] [ADMIN] - Zone: Sub-zone: Room</strong> - Administrator</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>who</li>
<li>who alice</li>
<li>who al</li>
<li>who xyz</li>
</ul>

<h4>Sample Output:</h4>
<pre>
Online players (3): alice [5] - Arkham: City: Northside Intersection Derby High,
bob [3] - Arkham: City: Northside Room Derby St 001,
charlie [7] [ADMIN] - Arkham: City: Northside Room High Ln 002

Players matching 'al' (1): alice [5] - Arkham: City: Northside Intersection Derby High

No players found matching 'xyz'. Try 'who' to see all online players.
</pre>

<p>As the ancient texts suggest: "Knowledge of one's companions is the first step toward survival in the face of the unknown."</p>
</div>
""",
    },
}


def get_help_content(command_name: str | None = None) -> str:
    """
    Get help content for commands.

    Args:
        command_name: Optional specific command name to get help for

    Returns:
        str: HTML formatted help content
    """
    if command_name is None:
        # General help
        return _get_general_help()

    # Specific command help
    command_name = command_name.lower()
    if command_name in COMMANDS:
        command_info = COMMANDS[command_name]
        return command_info["detailed_help"]
    else:
        return f"""
<div style="color: #FF4500;">
<h3>Command Not Found</h3>
<p>The command '{command_name}' was not found. Use 'help' to see available commands.</p>
</div>
"""


def _get_general_help() -> str:
    """Get general help content with command categories."""
    # Group commands by category
    categories = {}
    for cmd_name, cmd_info in COMMANDS.items():
        category = cmd_info["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append((cmd_name, cmd_info))

    # Build help content
    help_content = """
<div style="color: #4169E1;">
<h2>MythosMUD Help System</h2>
<p>Welcome to the realm of forbidden knowledge. Here are the commands available to you:</p>
"""

    for category, commands in categories.items():
        help_content += f"""
<h3>{category} Commands</h3>
<ul>
"""
        for cmd_name, cmd_info in commands:
            help_content += f"<li><strong>{cmd_name}</strong> - {cmd_info['description']}</li>"

        help_content += "</ul>"

    help_content += """
<p>For detailed help on any command, use: <strong>help [command]</strong></p>
<p>Example: <strong>help look</strong></p>
</div>
"""

    return help_content


def get_command_categories() -> list[str]:
    """Get list of all command categories."""
    categories = set()
    for cmd_info in COMMANDS.values():
        categories.add(cmd_info["category"])
    return sorted(categories)


def get_commands_by_category(category: str) -> list[tuple[str, dict]]:
    """Get all commands in a specific category."""
    commands = []
    for cmd_name, cmd_info in COMMANDS.items():
        if cmd_info["category"] == category:
            commands.append((cmd_name, cmd_info))
    return sorted(commands)
