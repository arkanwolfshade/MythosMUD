import { ALL_MESSAGES_CHANNEL, CHAT_CHANNEL_OPTIONS } from '../../config/channels';

const STANDALONE_COMMANDS = [
  'admin',
  'alias',
  'aliases',
  'attack',
  'emote',
  'go',
  'goto',
  'help',
  'hit',
  'inventory',
  'kick',
  'look',
  'logout',
  'me',
  'mute',
  'party',
  'pose',
  'punch',
  'quit',
  'smack',
  'status',
  'strike',
  'teleport',
  'thump',
  'unalias',
  'unmute',
  'w',
  'whisper',
  'who',
];

function prependChannelShortcut(command: string, effectiveChannel: string): string {
  const channel = CHAT_CHANNEL_OPTIONS.find(c => c.id === effectiveChannel);
  if (!channel?.shortcut) {
    return command;
  }
  const commandLower = command.toLowerCase();
  const alreadyHasChannelPrefix = commandLower.startsWith(`${channel.id} `) || commandLower === channel.id;
  return alreadyHasChannelPrefix ? command : `/${channel.shortcut} ${command}`;
}

function prependPartyPrefix(command: string): string {
  return command.toLowerCase().startsWith('party ') ? command : `party ${command}`;
}

function shouldPrependChannelShortcut(command: string, effectiveChannel: string, isStandalone: boolean): boolean {
  if (command.startsWith('/') || isStandalone) return false;
  return effectiveChannel !== 'say' && effectiveChannel !== 'local' && effectiveChannel !== 'party';
}

function applyChannelPrefix(command: string, effectiveChannel: string): string {
  const firstWord = command.split(/\s+/)[0].toLowerCase();
  const isStandalone = STANDALONE_COMMANDS.includes(firstWord);
  if (!shouldPrependChannelShortcut(command, effectiveChannel, isStandalone)) {
    return command;
  }
  return prependChannelShortcut(command, effectiveChannel);
}

export function prepareCommandForSubmit(commandInput: string, currentChannel: string): string {
  const command = commandInput.trim();
  const effectiveChannel = currentChannel === ALL_MESSAGES_CHANNEL.id ? 'say' : currentChannel;
  const withChannel = applyChannelPrefix(command, effectiveChannel);
  if (command.startsWith('/') || effectiveChannel !== 'party' || !withChannel) {
    return withChannel;
  }
  return prependPartyPrefix(withChannel);
}
