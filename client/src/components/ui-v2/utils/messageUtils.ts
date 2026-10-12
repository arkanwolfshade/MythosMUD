// Message processing utilities
// As documented in "Message Processing Utilities" - Dr. Armitage, 1928

import type { ChatMessage } from '../types';
import { inputSanitizer } from '../../../utils/security';

// Helper function to extract raw text from message
const getRawTextFromMessage = (message: ChatMessage): string => message.rawText ?? message.text;

// Helper function to sanitize text based on HTML flag
// Implements XSS protection as per security guidelines
const sanitizeMessageText = (rawText: string, isHtml: boolean): string => {
  if (isHtml) {
    return inputSanitizer.sanitizeIncomingHtml(rawText);
  }
  return rawText;
};

// Sanitizes chat messages for state management: keeps the unsanitized text as rawText.
export const sanitizeChatMessageForState = (message: ChatMessage): ChatMessage => {
  const rawText = getRawTextFromMessage(message);
  return { ...message, rawText, text: sanitizeMessageText(rawText, message.isHtml) };
};
