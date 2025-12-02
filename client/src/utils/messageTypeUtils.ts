/**
 * Message Type Utilities for Chat Panel Separation
 *
 * These utilities provide intelligent message categorization based on content analysis,
 * allowing proper routing of messages to the appropriate panels (ChatPanel vs GameLogPanel).
 *
 * Based on findings from "Pattern Recognition in Textual Communication Systems"
 * - Dr. Armitage, Miskatonic University, 1928
 */

export interface MessageTypeResult {
  type: 'chat' | 'command' | 'system';
  channel?: string;
}

/**
 * Message patterns for intelligent categorization
 * Each pattern includes a regex and the expected message type
 */
interface MessagePattern {
  pattern: RegExp;
  type: 'chat' | 'command' | 'system';
  channelExtractor?: RegExp;
}

const CARDINAL_REGEX = '(north|south|east|west|up|down|northeast|northwest|southeast|southwest)';
const TELEPORT_DEPARTURE_PATTERN = new RegExp(`^You teleport \\w+ to the ${CARDINAL_REGEX}\\.?$`, 'i');
const PLAYER_LEAVES_PATTERN = new RegExp(`^\\w+ leaves the room(?: heading ${CARDINAL_REGEX})?\\.?$`, 'i');
const PLAYER_ENTERS_PATTERN = new RegExp(`^\\w+ enters the room(?: from the ${CARDINAL_REGEX})?\\.?$`, 'i');
const PLAYER_TELEPORTED_PATTERN = new RegExp(`^You are teleported to the ${CARDINAL_REGEX} by \\w+\\.?$`, 'i');
const TELEPORT_EFFECT_VARIANTS = [
  'disappears in a ripple of distorted air',
  'arrives in a shimmer of eldritch energy',
  'vanishes in a flash of pale light',
  'appears beside you in a rush of displaced air',
].join('|');
const TELEPORT_EFFECT_PATTERN = new RegExp(`^\\w+ (${TELEPORT_EFFECT_VARIANTS})\\.?$`, 'i');

// Chat patterns - messages that should appear in ChatPanel
const CHAT_PATTERNS: MessagePattern[] = [
  // Channel-specific chat messages with brackets
  {
    pattern: /^\[([^\]]+)\]\s+\w+\s+(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\s+you)?):/i,
    type: 'chat',
    channelExtractor: /^\[([^\]]+)\]/i,
  },
  // Local channel messages: "You say locally:"
  {
    pattern: /^You say locally:/i,
    type: 'chat',
  },
  // Say channel messages: "You say:" (not "locally")
  {
    pattern: /^You say:(?! locally)/i, // Negative lookahead to exclude "You say locally:"
    type: 'chat',
  },
  // Whisper messages: "You whisper to PlayerName:" or "PlayerName whispers to you:"
  {
    pattern: /^(?:You whisper to \w+|\w+ whispers to you):/i,
    type: 'chat',
  },
  // Chat messages without brackets but with chat verbs
  {
    pattern: /^\w+\s+(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\s+you)?):/i,
    type: 'chat',
  },
  // Direct chat patterns - this should catch most chat content
  {
    pattern: /(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\s+you)?):/i,
    type: 'chat',
  },
  // Chat patterns without colons (for edge cases)
  {
    pattern: /^\w+\s+(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\s+you)?)(?:\s+|$)/i,
    type: 'chat',
  },
];

// Error and command response patterns - should be displayed as command responses
const ERROR_PATTERNS: MessagePattern[] = [
  { pattern: /^Usage:/i, type: 'command' }, // Usage messages should appear as command responses
  { pattern: /^Error:/i, type: 'command' }, // Error messages should appear as command responses
  { pattern: /^You must /i, type: 'command' }, // Validation error messages
  { pattern: /^Invalid /i, type: 'command' }, // Invalid command/input messages
  { pattern: /^Cannot /i, type: 'command' }, // Cannot perform action messages
  { pattern: /^Failed /i, type: 'command' }, // Failed action messages
  { pattern: /not found|doesn't exist|does not exist/i, type: 'command' }, // Not found messages
];

// System patterns - game events and notifications
const SYSTEM_PATTERNS: MessagePattern[] = [
  { pattern: /has entered the game\.?$/i, type: 'system' },
  { pattern: /has left the game\.?$/i, type: 'system' },
  { pattern: /^You are now in /i, type: 'system' },
  // Movement messages - should appear in Game Info panel only
  { pattern: /^You move (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i, type: 'system' },
  { pattern: /^You go (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i, type: 'system' },
  { pattern: /^You walk (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i, type: 'system' },
  { pattern: /^You head (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i, type: 'system' },
  {
    pattern: /^You travel (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i,
    type: 'system',
  },
  {
    pattern: /^You cannot move (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i,
    type: 'system',
  },
  {
    pattern: /^You cannot go (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i,
    type: 'system',
  },
  // Teleportation and room transition messaging
  { pattern: TELEPORT_DEPARTURE_PATTERN, type: 'system' },
  { pattern: PLAYER_LEAVES_PATTERN, type: 'system' },
  { pattern: PLAYER_ENTERS_PATTERN, type: 'system' },
  { pattern: PLAYER_TELEPORTED_PATTERN, type: 'system' },
  { pattern: TELEPORT_EFFECT_PATTERN, type: 'system' },
  // NPC movement messages - should appear in Game Info panel
  {
    pattern: /^.+ (left|entered from) (north|south|east|west|up|down|northeast|northwest|southeast|southwest)\.?$/i,
    type: 'system',
  },
  { pattern: /^.+ appears\.?$/i, type: 'system' }, // NPC spawn messages
  { pattern: /^.+ leaves\.?$/i, type: 'system' }, // NPC departure messages
  // Combat messages - should appear in Game Log only
  { pattern: /^You (attack|punch|kick|strike|hit|smack|thump) /i, type: 'system' },
  // Room descriptions - MOST RELIABLE PATTERN: Contains "Exits:" anywhere in the message
  // This pattern catches ALL room descriptions regardless of how they start or what follows
  { pattern: /Exits?:/i, type: 'system' },
  // Who command responses - player listings and information
  { pattern: /^Online Players \(\d+\):/i, type: 'system' },
  { pattern: /^Players matching .+ \(\d+\):/i, type: 'system' },
  { pattern: /^No players are currently online\.?$/i, type: 'system' },
  { pattern: /^No players found\.?$/i, type: 'system' },
  { pattern: /^You feel /i, type: 'system' },
  { pattern: /^The room is /i, type: 'system' },
  // Room descriptions - comprehensive patterns
  { pattern: /^A section of /i, type: 'system' }, // "A section of High Lane..."
  { pattern: /^A narrow /i, type: 'system' }, // "A narrow alley..."
  { pattern: /^A small /i, type: 'system' }, // "A small garden..."
  { pattern: /^A large /i, type: 'system' }, // "A large hall..."
  { pattern: /^A /i, type: 'system' }, // Room descriptions often start with "A"
  // Location-based room descriptions
  { pattern: /^Apple Lane /i, type: 'system' }, // "Apple Lane - Residential Section..."
  { pattern: /^Apple and Derby /i, type: 'system' }, // "Apple and Derby Intersection..."
  { pattern: /^High Lane /i, type: 'system' }, // "High Lane - Near Derby Intersection..."
  { pattern: /^Derby Street /i, type: 'system' }, // "Derby Street..."
  // Specific room name patterns only - avoid overly broad patterns
  { pattern: /^[A-Z][a-z]+ [A-Z][a-z]+ - [A-Z][a-z]+ [A-Z][a-z]+/i, type: 'system' }, // "Apple Lane - Residential Section"
  { pattern: /^[A-Z][a-z]+ and [A-Z][a-z]+ [A-Z][a-z]+/i, type: 'system' }, // "Apple and Derby Intersection"
  // Specific "You" patterns for system messages only
  { pattern: /^You feel /i, type: 'system' }, // Keep this one - it's about environmental effects
  { pattern: /^You are now in /i, type: 'system' }, // Keep this one - it's about location changes
  { pattern: /^The /i, type: 'system' }, // Room descriptions often start with "The"
  { pattern: /^It is /i, type: 'system' },
  { pattern: /^There is /i, type: 'system' },
  { pattern: /^There are /i, type: 'system' },
];

/**
 * Determines the message type and extracts channel information based on content analysis
 *
 * @param message - The message text to analyze
 * @returns MessageTypeResult with type and optional channel
 */
export function determineMessageType(message: string): MessageTypeResult {
  // Handle empty or whitespace-only messages
  if (!message || !message.trim()) {
    return { type: 'command' };
  }

  const trimmedMessage = message.trim();

  // Check chat patterns first (highest priority)
  for (const pattern of CHAT_PATTERNS) {
    if (pattern.pattern.test(trimmedMessage)) {
      let channel: string | undefined;

      // Special handling for specific patterns
      if (/^You say locally:/i.test(trimmedMessage)) {
        channel = 'local';
      } else if (/^You say:(?! locally)/i.test(trimmedMessage)) {
        channel = 'say'; // "You say:" without "locally" goes to say channel
      } else if (/^(?:You whisper to \w+|\w+ whispers to you):/i.test(trimmedMessage)) {
        channel = 'whisper';
      } else {
        channel = pattern.channelExtractor ? extractChannelFromMessage(trimmedMessage) : undefined;
      }

      return { type: pattern.type, channel };
    }
  }

  // Check error patterns (second priority)
  for (const pattern of ERROR_PATTERNS) {
    if (pattern.pattern.test(trimmedMessage)) {
      return { type: pattern.type };
    }
  }

  // Check system patterns
  for (const pattern of SYSTEM_PATTERNS) {
    if (pattern.pattern.test(trimmedMessage)) {
      return { type: pattern.type };
    }
  }

  // Default to command response
  return { type: 'command' };
}

/**
 * Extracts channel information from message text
 *
 * @param message - The message text to extract channel from
 * @returns The channel name in lowercase, or 'local' as default
 */
export function extractChannelFromMessage(message: string): string {
  if (!message || !message.trim()) {
    return 'local';
  }

  // Look for channel in brackets at the start of the message
  const channelMatch = message.match(/^\[([^\]]+)\]/i);
  if (channelMatch && channelMatch[1]) {
    return channelMatch[1].toLowerCase().trim();
  }

  // For messages without explicit channel brackets, default to 'local'
  // This ensures consistent behavior for all non-bracketed messages
  return 'local';
}

/**
 * Determines if a message contains chat content
 *
 * @param text - The message text to check
 * @returns True if the message contains chat content
 */
export function isChatContent(text: string): boolean {
  if (!text || !text.trim()) {
    return false;
  }

  const trimmedText = text.trim();

  // Check for chat patterns
  for (const pattern of CHAT_PATTERNS) {
    if (pattern.pattern.test(trimmedText)) {
      return true;
    }
  }

  return false;
}
