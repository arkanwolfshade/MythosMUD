export const DEFAULT_COMMAND_HISTORY = [
  'look',
  'inventory',
  'get ancient tome',
  'read tome',
  'cast eldritch sight',
  'n',
  'look',
  'examine wall',
  'search for secret door',
  'whisper to Professor Armitage "The stars are right"',
  'shout "Beware the Yellow Sign!"',
  'flee',
  's',
  'look',
  'help',
  'who',
  'say "Has anyone seen the Necronomicon?"',
  'wear amulet',
  'cast protection spell',
  'attack cultist',
];

export const SAMPLE_COMMANDS = [
  'examine corpse',
  'cast detect magic',
  'search for clues',
  'whisper "The ritual begins"',
  'get ritual dagger',
  'read forbidden scroll',
  'cast summon horror',
  'flee in terror',
];

export const MYTHOS_COMMANDS = [
  'invoke Cthulhu',
  'read Necronomicon',
  'cast call of the void',
  'whisper to Yog-Sothoth',
  'perform eldritch ritual',
  'summon deep ones',
  'cast lucidity drain',
  'flee from madness',
];

export const MOVEMENT_COMMANDS = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'up', 'down'];

export const COMMAND_CATEGORIES = {
  Movement: MOVEMENT_COMMANDS,
  Combat: ['attack', 'defend', 'flee', 'cast', 'get', 'drop', 'wear', 'remove'],
  Communication: ['say', 'whisper', 'shout', 'tell', 'reply', 'emote'],
};

export const FEATURES = [
  ['search', 'Auto-suggestions:', 'Command completion as you type'],
  ['clock', 'History Navigation:', 'Use up/down arrows to browse past commands'],
  ['move', 'Quick Commands:', 'One-click access to common commands'],
  ['clear', 'History Management:', 'Clear command history with one click'],
  ['help', 'Help Integration:', 'Quick access to command help'],
  ['stats', 'Command Statistics:', 'Track your command usage'],
] as const;

export const SHORTCUTS = [
  ['up', 'Navigate up in command history'],
  ['down', 'Navigate down in command history'],
  ['Tab', 'Auto-complete command (future feature)'],
  ['Enter', 'Send command'],
  ['Ctrl+L', 'Clear input (future feature)'],
  ['Ctrl+R', 'Search history (future feature)'],
] as const;

export const EXAMPLES = {
  'Basic Commands': [
    ['look', 'Examine your surroundings'],
    ['inventory', 'Check your possessions'],
    ['help', 'Get command help'],
  ],
  Movement: [
    ['n', 'Move north'],
    ['s', 'Move south'],
    ['up', 'Climb up'],
  ],
  'Eldritch Commands': [
    ['cast eldritch sight', 'See the unseen'],
    ['read Necronomicon', 'Study forbidden lore'],
    ['invoke Cthulhu', 'Summon the Great Old One'],
  ],
} as const;
