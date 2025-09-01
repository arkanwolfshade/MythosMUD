import { determineMessageType, extractChannelFromMessage, isChatContent } from '../messageTypeUtils';

describe('messageTypeUtils', () => {
  describe('determineMessageType', () => {
    it('should categorize chat messages correctly', () => {
      const chatMessages = [
        '[Local] Player says: Hello there!',
        '[Global] Player whispers: Secret message',
        '[Say] Player shouts: Important announcement!',
        '[Local] Player emotes: waves hello',
        '[Tell] Player tells you: Private message',
      ];

      chatMessages.forEach(message => {
        const result = determineMessageType(message);
        expect(result.type).toBe('chat');
        expect(result.channel).toBeDefined();
      });
    });

    it('should categorize system messages correctly', () => {
      const systemMessages = [
        'Player has entered the game.',
        'Player has left the game.',
        'You are now in the Library.',
        'Exits: north, south, east, west',
        'You feel a sense of dread...',
        'The room is dark and foreboding.',
      ];

      systemMessages.forEach(message => {
        const result = determineMessageType(message);
        expect(result.type).toBe('system');
      });
    });

    it('should categorize command responses correctly', () => {
      const commandMessages = [
        'You look around the room.',
        'You examine the ancient tome.',
        'You search the area.',
        'You cast a spell.',
        'You move north.',
      ];

      commandMessages.forEach(message => {
        const result = determineMessageType(message);
        expect(result.type).toBe('command');
      });
    });

    it('should extract channel information from chat messages', () => {
      const testCases = [
        { message: '[Local] Player says: Hello', expected: 'local' },
        { message: '[Global] Player shouts: Announcement', expected: 'global' },
        { message: '[Say] Player whispers: Secret', expected: 'say' },
        { message: '[Tell] Player tells you: Private', expected: 'tell' },
      ];

      testCases.forEach(({ message, expected }) => {
        const result = determineMessageType(message);
        expect(result.channel).toBe(expected);
      });
    });

    it('should handle edge cases gracefully', () => {
      const edgeCases = [
        { message: '', expected: 'command' },
        { message: '   ', expected: 'command' },
        { message: '[Invalid] No verb', expected: 'command' },
        { message: 'Just some random text', expected: 'command' },
      ];

      edgeCases.forEach(({ message, expected }) => {
        const result = determineMessageType(message);
        expect(result.type).toBe(expected);
      });
    });
  });

  describe('extractChannelFromMessage', () => {
    it('should extract channel from bracketed messages', () => {
      const testCases = [
        { message: '[Local] Player says: Hello', expected: 'local' },
        { message: '[Global] Player shouts: Announcement', expected: 'global' },
        { message: '[Say] Player whispers: Secret', expected: 'say' },
        { message: '[Tell] Player tells you: Private', expected: 'tell' },
        { message: '[Custom] Player emotes: waves', expected: 'custom' },
      ];

      testCases.forEach(({ message, expected }) => {
        const result = extractChannelFromMessage(message);
        expect(result).toBe(expected);
      });
    });

    it('should return default channel for messages without brackets', () => {
      const messages = ['Player says: Hello', 'You are now in the room.', 'Just some text', ''];

      messages.forEach(message => {
        const result = extractChannelFromMessage(message);
        expect(result).toBe('local');
      });
    });

    it('should handle malformed brackets', () => {
      const malformedMessages = [
        '[Local Player says: Hello', // Missing closing bracket
        'Local] Player says: Hello', // Missing opening bracket
        '[] Player says: Hello', // Empty brackets
        '[ Local ] Player says: Hello', // Extra spaces
      ];

      malformedMessages.forEach(message => {
        const result = extractChannelFromMessage(message);
        expect(result).toBe('local');
      });
    });
  });

  describe('isChatContent', () => {
    it('should identify chat content correctly', () => {
      const chatContent = [
        '[Local] Player says: Hello',
        '[Global] Player whispers: Secret',
        '[Say] Player shouts: Announcement',
        '[Tell] Player tells you: Private',
        'Player says: Hello',
        'Player whispers: Secret',
        'Player shouts: Announcement',
        'Player emotes: waves',
      ];

      chatContent.forEach(message => {
        expect(isChatContent(message)).toBe(true);
      });
    });

    it('should identify non-chat content correctly', () => {
      const nonChatContent = [
        'You are now in the room.',
        'Player has entered the game.',
        'Exits: north, south',
        'You look around.',
        'You examine the object.',
        'You cast a spell.',
        'You move north.',
        '',
        '   ',
      ];

      nonChatContent.forEach(message => {
        expect(isChatContent(message)).toBe(false);
      });
    });

    it('should handle edge cases', () => {
      const edgeCases = [
        { message: 'says: but no player name', expected: true },
        { message: 'Player says', expected: true },
        { message: 'says Player: Hello', expected: false },
        { message: 'Player says Hello', expected: true },
      ];

      edgeCases.forEach(({ message, expected }) => {
        expect(isChatContent(message)).toBe(expected);
      });
    });
  });
});
