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

// Chat patterns - messages that should appear in ChatPanel
const CHAT_PATTERNS: MessagePattern[] = [
  // Channel-specific chat messages with brackets
  {
    pattern: /^\[([^\]]+)\]\s+\w+\s+(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\s+you)?):/i,
    type: 'chat',
    channelExtractor: /^\[([^\]]+)\]/i,
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

// System patterns - game events and notifications
const SYSTEM_PATTERNS: MessagePattern[] = [
  { pattern: /has entered the game\.?$/i, type: 'system' },
  { pattern: /has left the game\.?$/i, type: 'system' },
  { pattern: /^You are now in /i, type: 'system' },
  { pattern: /^Exits?:/i, type: 'system' },
  { pattern: /^You feel /i, type: 'system' },
  { pattern: /^The room is /i, type: 'system' },
  { pattern: /^A /i, type: 'system' }, // Room descriptions often start with "A"
  { pattern: /^You see /i, type: 'system' },
  { pattern: /^You hear /i, type: 'system' },
  { pattern: /^You smell /i, type: 'system' },
  { pattern: /^You taste /i, type: 'system' },
  { pattern: /^You touch /i, type: 'system' },
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

  // Manual test of the specific pattern that should match
  const testPattern = /^\w+\s+(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\s+you)?):/i;
  const manualTest = testPattern.test(trimmedMessage);
  console.log(
    `🧪 MANUAL TEST: Pattern /^\\w+\\s+(say|says|whisper|whispers|shout|shouts|emote|emotes|tell|tells(?:\\s+you)?):/i against "${trimmedMessage}" = ${manualTest}`
  );

  // Test individual parts
  const wordMatch = /^\w+/.test(trimmedMessage);
  const spaceMatch = /^\w+\s+/.test(trimmedMessage);
  const sayMatch = /(say|says):/i.test(trimmedMessage);
  console.log(`🧪 COMPONENT TESTS: word=${wordMatch}, space=${spaceMatch}, say=${sayMatch}`);

  // Check chat patterns first (highest priority)
  for (const pattern of CHAT_PATTERNS) {
    console.log(`🔍 Testing pattern: ${pattern.pattern} against message: "${trimmedMessage}"`);
    const testResult = pattern.pattern.test(trimmedMessage);
    console.log(`🔍 Pattern test result: ${testResult}`);
    if (testResult) {
      console.log(`✅ Pattern matched! Type: ${pattern.type}`);
      const channel = pattern.channelExtractor ? extractChannelFromMessage(trimmedMessage) : undefined;

      return {
        type: pattern.type,
        channel,
      };
    }
  }

  // Check system patterns
  for (const pattern of SYSTEM_PATTERNS) {
    if (pattern.pattern.test(trimmedMessage)) {
      return {
        type: pattern.type,
      };
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

  // Intelligently determine channel based on message content
  const trimmedMessage = message.trim();

  // Check for specific chat verbs and map them to appropriate channels
  if (/\b(say|says)\b/i.test(trimmedMessage)) {
    return 'say';
  }
  if (/\b(whisper|whispers)\b/i.test(trimmedMessage)) {
    return 'whisper';
  }
  if (/\b(shout|shouts)\b/i.test(trimmedMessage)) {
    return 'global';
  }
  if (/\b(emote|emotes)\b/i.test(trimmedMessage)) {
    return 'say'; // Emotes are typically local to the room
  }
  if (/\b(tell|tells)\b/i.test(trimmedMessage)) {
    return 'whisper'; // Tell is typically a whisper
  }

  // Default to local channel for other messages
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

/**
 * Debug utility to log message categorization details
 *
 * @param message - The message being categorized
 * @param result - The categorization result
 */
export function debugMessageCategorization(message: string, result: MessageTypeResult): void {
  if (process.env.NODE_ENV === 'development') {
    console.log('🔍 Message Categorization Debug:', {
      message: message.substring(0, 100) + (message.length > 100 ? '...' : ''),
      result,
      timestamp: new Date().toISOString(),
    });
  }
}
