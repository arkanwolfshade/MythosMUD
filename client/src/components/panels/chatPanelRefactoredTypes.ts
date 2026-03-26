/**
 * Types for the refactored chat panel (split for Lizard NLOC/CCN limits).
 * Agent-readable: keep message shape aligned with game store chat payloads.
 */

export interface ChatPanelRefactoredMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}
