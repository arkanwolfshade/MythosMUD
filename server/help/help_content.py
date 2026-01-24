"""
Help content and command documentation for MythosMUD.

This module contains the comprehensive command documentation and
help system for the MythosMUD game.
"""

# pylint: disable=too-many-lines  # Reason: Help content requires extensive documentation strings for comprehensive command help system

from typing import Any, cast

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


# Command definitions for help system
COMMANDS: dict[str, dict[str, Any]] = {
    "look": {
        "category": "Exploration",
        "description": ("Examine your surroundings, look at players, items, containers, or peer in a direction"),
        "usage": "look [target] or /look [target]",
        "examples": [
            "look",
            "look north",
            "look player Armitage",
            "look item lantern",
            "look container backpack",
            "look in backpack",
            "look backpack-2",
        ],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>LOOK Command</h3>
<p>The ancient texts speak of observation as the first step toward understanding.
Use this command to examine your surroundings, inspect items, examine containers,
or peer into the unknown.</p>

<h4>Usage:</h4>
<ul>
<li><strong>look</strong> - Examine your current location</li>
<li><strong>look [direction]</strong> - Look in a specific direction (north, south, east, west, up, down)</li>
<li><strong>look player [name]</strong> - Look at another player</li>
<li><strong>look item [name]</strong> - Examine an item (in room, inventory, or equipped)</li>
<li><strong>look container [name]</strong> - Examine a container</li>
<li><strong>look in [container]</strong> - Look inside a container to see its contents</li>
<li><strong>look [name]-[number]</strong> or <strong>look [name] [number]</strong> - Target specific instance when multiple exist</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>look</li>
<li>look north</li>
<li>look player Armitage</li>
<li>look item lantern</li>
<li>look container backpack</li>
<li>look in backpack</li>
<li>look backpack-2</li>
<li>look lantern 1</li>
</ul>

<h4>Target Priority:</h4>
<p>When using ambiguous targets, the system resolves in this order:</p>
<ol>
<li>Players</li>
<li>NPCs</li>
<li>Items (room drops, inventory, equipped)</li>
<li>Containers (room containers, wearable containers)</li>
<li>Directions</li>
</ol>

<h4>Instance Targeting:</h4>
<p>When multiple items or containers match a name, use instance numbers:</p>
<ul>
<li><strong>look backpack-2</strong> - Look at the second backpack</li>
<li><strong>look lantern 1</strong> - Look at the first lantern</li>
</ul>

<h4>Container Inspection:</h4>
<p>To see the contents of a container, use the "in" keyword:</p>
<ul>
<li><strong>look in backpack</strong> - See what's inside your backpack</li>
<li><strong>look container chest</strong> - Examine a chest (shows capacity and lock status)</li>
</ul>

<p>As the Necronomicon suggests: "That which can be seen may yet remain unseen to the untrained eye."</p>
</div>
""",
    },
    "put": {
        "category": "Inventory",
        "description": "Put an item from your inventory into a container",
        "usage": "put <item> [in] <container> [quantity]",
        "examples": [
            "put lantern in backpack",
            "put lantern backpack",
            "put 1 in backpack",
            "put lantern in backpack 2",
        ],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>PUT Command</h3>
<p>Transfer items from your inventory into a container. The "in" keyword is optional,
making the command more natural to use.</p>

<h4>Usage:</h4>
<ul>
<li><strong>put &lt;item&gt; [in] &lt;container&gt; [quantity]</strong> - Put item into container</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>put lantern in backpack</li>
<li>put lantern backpack</li>
<li>put 1 in backpack</li>
<li>put lantern in backpack 2</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>The "in" keyword is optional - both "put lantern backpack" and "put lantern in backpack" work</li>
<li>You can use item names or inventory numbers</li>
<li>You can specify quantity to put only part of a stack</li>
<li>Container must be accessible (in room or equipped)</li>
<li>Container must have available capacity</li>
</ul>

<p>As noted in the restricted archives: "Proper storage of artifacts prevents dimensional contamination."</p>
</div>
""",
    },
    "get": {
        "category": "Inventory",
        "description": "Get an item from a container into your inventory",
        "usage": "get <item> [from] <container> [quantity]",
        "examples": [
            "get lantern from backpack",
            "get lantern backpack",
            "get 1 from backpack",
            "get lantern from backpack 2",
        ],
        "detailed_help": """
<div style="color: #8B4513;">
<h3>GET Command</h3>
<p>Transfer items from a container into your inventory. The "from" keyword is optional,
making the command more natural to use.</p>

<h4>Usage:</h4>
<ul>
<li><strong>get &lt;item&gt; [from] &lt;container&gt; [quantity]</strong> - Get item from container</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>get lantern from backpack</li>
<li>get lantern backpack</li>
<li>get 1 from backpack</li>
<li>get lantern from backpack 2</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>The "from" keyword is optional - both "get lantern backpack" and "get lantern from backpack" work</li>
<li>You can use item names or container item numbers</li>
<li>You can specify quantity to get only part of a stack</li>
<li>Container must be accessible (in room or equipped)</li>
<li>Your inventory must have available capacity</li>
</ul>

<p>As noted in the restricted archives: "Retrieval of stored artifacts requires careful handling."</p>
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
    "cast": {
        "category": "Magic",
        "description": "Cast a learned spell",
        "usage": "cast <spell_name> [target]",
        "examples": ["cast heal", "cast heal self", "cast fireball goblin"],
        "detailed_help": """
<div style="color: #9370DB;">
<h3>CAST Command</h3>
<p>Harness the eldritch forces that lie beyond the veil of reality. Casting spells requires
Magic Points (MP) and, for Mythos spells, lucidity. The forbidden knowledge exacts its price.</p>

<h4>Usage:</h4>
<ul>
<li><strong>cast [spell_name]</strong> - Cast a spell on yourself (self-target spells)</li>
<li><strong>cast [spell_name] [target]</strong> - Cast a spell on a specific target</li>
</ul>

<h4>Spell Casting:</h4>
<ul>
<li>You must have learned the spell first (use /learn or /teach)</li>
<li>Spells cost Magic Points (MP) to cast</li>
<li>Mythos spells also cost lucidity</li>
<li>Some spells require material components (consumed on cast)</li>
<li>Spells with casting times require you to wait - use /stop to interrupt</li>
</ul>

<h4>Combat Integration:</h4>
<ul>
<li>In combat, if no target is specified, the spell targets your combat opponent</li>
<li>Casting spells with casting times waits for your turn in combat</li>
<li>You can interrupt casting with /stop (may cost MP if LUCK check fails)</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>cast heal</li>
<li>cast heal self</li>
<li>cast fireball goblin</li>
<li>cast bless party</li>
</ul>

<h4>Mastery:</h4>
<p>Your mastery level affects spell effectiveness and success chance. Mastery increases
with successful casts. Use /spells to see your learned spells and mastery levels.</p>

<p>Warning: "That which calls upon the void may yet call back." - Prof. Armitage</p>
</div>
""",
    },
    "spells": {
        "category": "Magic",
        "description": "List all learned spells with mastery levels",
        "usage": "spells",
        "examples": ["spells"],
        "detailed_help": """
<div style="color: #9370DB;">
<h3>SPELLS Command</h3>
<p>Review your accumulated arcane knowledge. This command displays all spells you have
learned along with your current mastery level for each.</p>

<h4>Usage:</h4>
<ul>
<li><strong>spells</strong> - List all your learned spells with mastery percentages</li>
</ul>

<h4>Output Format:</h4>
<ul>
<li><strong>Spell Name - Mastery: XX%</strong> - Each learned spell with mastery level</li>
</ul>

<h4>Mastery Levels:</h4>
<ul>
<li>Mastery ranges from 0% to 100%</li>
<li>Mastery increases with successful spell casts</li>
<li>Higher mastery improves spell effectiveness and success chance</li>
<li>Use /spell [name] to see detailed spell information</li>
</ul>

<h4>Example:</h4>
<ul>
<li>spells</li>
</ul>

<h4>Learning Spells:</h4>
<p>Learn new spells using /learn or have another player teach you with /teach.
Some spells can be learned from spellbooks using /read.</p>

<p>As the Necronomicon warns: "Knowledge gained is knowledge that cannot be unlearned."</p>
</div>
""",
    },
    "spell": {
        "category": "Magic",
        "description": "Show detailed information about a specific spell",
        "usage": "spell <spell_name>",
        "examples": ["spell heal", "spell fireball"],
        "detailed_help": """
<div style="color: #9370DB;">
<h3>SPELL Command</h3>
<p>Examine the intricate details of a specific spell. This command reveals the spell's
costs, effects, requirements, and your current mastery level if you know it.</p>

<h4>Usage:</h4>
<ul>
<li><strong>spell [spell_name]</strong> - Show detailed information about a spell</li>
</ul>

<h4>Spell Information Displayed:</h4>
<ul>
<li><strong>Name</strong> - Spell name</li>
<li><strong>Description</strong> - What the spell does</li>
<li><strong>School</strong> - Spell school (mythos, clerical, elemental, other)</li>
<li><strong>MP Cost</strong> - Magic Points required to cast</li>
<li><strong>Lucidity Cost</strong> - Lucidity required (Mythos spells only)</li>
<li><strong>Corruption on Cast</strong> - Corruption gained (some Mythos spells)</li>
<li><strong>Casting Time</strong> - Time in seconds before spell completes</li>
<li><strong>Target Type</strong> - Who/what the spell can target</li>
<li><strong>Range</strong> - How far the spell can reach</li>
<li><strong>Effect</strong> - What effect the spell produces</li>
<li><strong>Required Materials</strong> - Material components needed (if any)</li>
<li><strong>Your Mastery</strong> - Your mastery level (if learned) or "Not learned"</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>spell heal</li>
<li>spell fireball</li>
<li>spell call_cthulhu</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>You can view spell information even if you haven't learned it</li>
<li>Use this to plan which spells to learn</li>
<li>Material components marked as "(consumed)" are used up when casting</li>
<li>Material components marked as "(reusable)" are not consumed</li>
</ul>

<p>Remember: "Understanding the cost of power is the first lesson in wielding it."</p>
</div>
""",
    },
    "learn": {
        "category": "Magic",
        "description": "Learn a new spell",
        "usage": "learn <spell_name>",
        "examples": ["learn heal", "learn fireball"],
        "detailed_help": """
<div style="color: #9370DB;">
<h3>LEARN Command</h3>
<p>Acquire new arcane knowledge. Learning spells requires access to the spell's secrets,
which may come from spellbooks, teachers, or other sources. Beware: some knowledge
comes with a price.</p>

<h4>Usage:</h4>
<ul>
<li><strong>learn [spell_name]</strong> - Learn a spell from available sources</li>
</ul>

<h4>Learning Methods:</h4>
<ul>
<li><strong>From Spellbooks</strong> - Use /read on a spellbook containing the spell</li>
<li><strong>From Teachers</strong> - Have another player use /teach to teach you</li>
<li><strong>Command Learning</strong> - Use /learn directly (may require special circumstances)</li>
</ul>

<h4>Learning Costs:</h4>
<ul>
<li>Mythos spells may apply corruption when learned</li>
<li>Some spells may have prerequisites (stats, other spells)</li>
<li>Once learned, spells start at 0% mastery</li>
<li>Practice casting to increase mastery</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>learn heal</li>
<li>learn fireball</li>
<li>learn bless</li>
</ul>

<h4>After Learning:</h4>
<ul>
<li>Use /spells to see your newly learned spell</li>
<li>Use /spell [name] to review spell details</li>
<li>Cast the spell to increase mastery</li>
</ul>

<p>Warning: "The price of forbidden knowledge is often paid in sanity." - Cultes des Goules</p>
</div>
""",
    },
    "teach": {
        "category": "Magic",
        "description": "Teach a spell to another player",
        "usage": "teach <player_name> <spell_name>",
        "examples": ["teach alice heal", "teach bob fireball"],
        "detailed_help": """
<div style="color: #9370DB;">
<h3>TEACH Command</h3>
<p>Share your arcane knowledge with fellow investigators. Teaching allows you to pass
on spells you have learned to other players who are present in your location.</p>

<h4>Usage:</h4>
<ul>
<li><strong>teach [player_name] [spell_name]</strong> - Teach a spell to another player</li>
</ul>

<h4>Requirements:</h4>
<ul>
<li>You must know the spell (have learned it yourself)</li>
<li>The target player must be in the same room as you</li>
<li>The target player must not already know the spell</li>
</ul>

<h4>Teaching Process:</h4>
<ul>
<li>Teaching shares your knowledge of the spell</li>
<li>The student starts with 0% mastery</li>
<li>If the spell applies corruption on learn, the student receives it</li>
<li>Both teacher and student see messages about the teaching</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>teach alice heal</li>
<li>teach bob fireball</li>
<li>teach charlie bless</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>You can only teach spells you have learned</li>
<li>The student can also use /learn if they have access to other sources</li>
<li>Teaching is a way to help new players learn useful spells</li>
</ul>

<p>As noted: "Knowledge shared multiplies the power of the arcane."</p>
</div>
""",
    },
    "stop": {
        "category": "Magic",
        "description": "Interrupt your current spell casting",
        "usage": "stop",
        "examples": ["stop"],
        "detailed_help": """
<div style="color: #9370DB;">
<h3>STOP Command</h3>
<p>Abandon your current spell casting attempt. Interrupting a spell mid-cast is dangerous
and may cost you Magic Points depending on your luck.</p>

<h4>Usage:</h4>
<ul>
<li><strong>stop</strong> - Interrupt your current spell casting</li>
</ul>

<h4>When to Use:</h4>
<ul>
<li>You're casting a spell with a casting time and want to cancel it</li>
<li>You need to change tactics during combat</li>
<li>You realize you're casting the wrong spell</li>
</ul>

<h4>Interruption Cost:</h4>
<ul>
<li>A LUCK check determines if you avoid MP loss</li>
<li>If LUCK check passes: No MP lost, casting stops safely</li>
<li>If LUCK check fails: You lose the spell's MP cost</li>
<li>Spell does not complete and has no effect</li>
</ul>

<h4>Examples:</h4>
<ul>
<li>stop</li>
</ul>

<h4>Notes:</h4>
<ul>
<li>Only works if you are currently casting a spell</li>
<li>Instant cast spells (0 casting time) cannot be interrupted</li>
<li>Material components already consumed are not refunded</li>
<li>Useful for canceling long casting times when needed</li>
</ul>

<p>Warning: "Interrupting the flow of eldritch power is not without risk."</p>
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
        return cast(str, command_info["detailed_help"])

    return f"""
<div style="color: #FF4500;">
<h3>Command Not Found</h3>
<p>The command '{command_name}' was not found. Use 'help' to see available commands.</p>
</div>
"""


def _get_general_help() -> str:
    """Get general help content with command categories."""
    # Group commands by category
    categories: dict[str, list[tuple[str, Any]]] = {}
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


def get_commands_by_category(category: str) -> list[tuple[str, dict[str, Any]]]:
    """Get all commands in a specific category."""
    commands = []
    for cmd_name, cmd_info in COMMANDS.items():
        if cmd_info["category"] == category:
            commands.append((cmd_name, cmd_info))
    return sorted(commands)
