// Message processing utilities
// As documented in "Message Processing Utilities" - Dr. Armitage, 1928

import type { ChatMessage } from '../types';
import { inputSanitizer } from '../../../utils/security';

// Helper function to extract raw text from message
const getRawTextFromMessage = (message: ChatMessage): string => {
  const messageWithRawText = message as ChatMessage & { rawText?: string };
  return messageWithRawText.rawText ?? message.text;
};

// Helper function to sanitize text based on HTML flag
// Implements XSS protection as per security guidelines
const sanitizeMessageText = (rawText: string, isHtml: boolean): string => {
  if (isHtml) {
    return inputSanitizer.sanitizeIncomingHtml(rawText);
  }
  return rawText;
};

// Helper function to extract message type with default fallback
const getMessageType = (message: ChatMessage): string => {
  return message.type ?? 'system';
};

// Helper function to extract channel with default fallback
const getMessageChannel = (message: ChatMessage): string => {
  const messageWithChannel = message as { channel?: string };
  return messageWithChannel.channel ?? 'system';
};

// Helper function to extract messageType with fallback to type
const getMessageTypeField = (message: ChatMessage, existingType: string): string => {
  const messageWithMessageType = message as { messageType?: string };
  return messageWithMessageType.messageType ?? (existingType as unknown as string);
};

// Helper function to extract message metadata (type, channel, messageType)
// Consolidates metadata extraction logic to reduce complexity
const getMessageMetadata = (message: ChatMessage): { type: string; channel: string; messageType: string } => {
  const existingType = getMessageType(message);
  const existingChannel = getMessageChannel(message);
  const messageType = getMessageTypeField(message, existingType);

  return {
    type: existingType,
    channel: existingChannel,
    messageType,
  };
};

// Sanitizes and normalizes chat messages for state management
// Reduces cyclomatic complexity by delegating to helper functions
export const sanitizeChatMessageForState = (message: ChatMessage): ChatMessage => {
  const rawText = getRawTextFromMessage(message);
  const sanitizedText = sanitizeMessageText(rawText, message.isHtml);
  const metadata = getMessageMetadata(message);

  return {
    ...message,
    type: metadata.type,
    messageType: metadata.messageType,
    channel: metadata.channel,
    rawText,
    text: sanitizedText,
  };
};
