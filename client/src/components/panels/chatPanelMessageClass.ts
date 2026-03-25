/**
 * Tailwind class names for chat log rows (tags override messageType).
 * Kept separate from chatPanelRuntimeUtils to satisfy complexity tooling.
 */

const DEFAULT_MESSAGE_CLASS = 'text-mythos-terminal-text';

const MESSAGE_TYPE_TO_CLASS: Record<string, string> = {
  emote: 'text-mythos-terminal-primary italic',
  system: 'text-mythos-terminal-warning font-bold',
  error: 'text-mythos-terminal-error font-bold',
  whisper: 'text-mythos-terminal-secondary italic',
  party: 'text-mythos-terminal-primary',
  shout: 'text-mythos-terminal-warning font-bold',
};

const TAG_CLASS_PRIORITY: Array<{ tag: string; className: string }> = [
  { tag: 'hallucination', className: 'text-fuchsia-300 italic' },
  { tag: 'command-misfire', className: 'text-mythos-terminal-warning font-semibold' },
  { tag: 'rescue', className: 'text-mythos-terminal-primary font-semibold' },
];

function classNameFromTags(tags: string[] | undefined): string | undefined {
  if (!tags?.length) {
    return undefined;
  }
  for (const { tag, className } of TAG_CLASS_PRIORITY) {
    if (tags.includes(tag)) {
      return className;
    }
  }
  return undefined;
}

/** Minimal shape for styling; compatible with ChatPanelMessage. */
export function getChatPanelMessageClass(message: { tags?: string[]; messageType?: string }): string {
  const fromTags = classNameFromTags(message.tags);
  if (fromTags !== undefined) {
    return fromTags;
  }
  const byType = message.messageType ? MESSAGE_TYPE_TO_CLASS[message.messageType] : undefined;
  return byType ?? DEFAULT_MESSAGE_CLASS;
}
