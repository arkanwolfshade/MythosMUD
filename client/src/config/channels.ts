import { Channel } from '../components/ui/ChannelSelector';
import { MythosIcons } from '../components/ui/EldritchIcon';

// Channel configuration for MythosMUD
// This defines all available chat channels with their properties
export const AVAILABLE_CHANNELS: Channel[] = [
  {
    id: 'say',
    name: 'Say',
    description: 'Speak to players in the same room',
    icon: MythosIcons.chat,
    color: 'text-mythos-terminal-text',
    shortcut: 'say',
  },
  {
    id: 'local',
    name: 'Local',
    description: 'Chat with players in the same sub-zone',
    icon: MythosIcons.local,
    color: 'text-mythos-terminal-primary',
    shortcut: 'l',
  },
  {
    id: 'global',
    name: 'Global',
    description: 'Chat with all players on the server',
    icon: MythosIcons.global,
    color: 'text-mythos-terminal-warning',
    shortcut: 'g',
  },
  {
    id: 'whisper',
    name: 'Whisper',
    description: 'Private message to a specific player',
    icon: MythosIcons.whisper,
    color: 'text-mythos-terminal-secondary',
    shortcut: 'w',
    disabled: true, // Not implemented yet
  },
  {
    id: 'system',
    name: 'System',
    description: 'System announcements and admin messages',
    icon: MythosIcons.system,
    color: 'text-mythos-terminal-error',
    shortcut: 'system',
    disabled: true, // Not implemented yet
  },
];

// Default channel to use when no channel is selected
export const DEFAULT_CHANNEL = 'say';

// Channel groups for organization
export const CHANNEL_GROUPS = {
  basic: ['say'],
  area: ['local'],
  server: ['global'],
  advanced: ['whisper', 'system'],
};

// Helper function to get channel by ID
export const getChannelById = (channelId: string): Channel | undefined => {
  return AVAILABLE_CHANNELS.find(channel => channel.id === channelId);
};

// Helper function to get enabled channels only
export const getEnabledChannels = (): Channel[] => {
  return AVAILABLE_CHANNELS.filter(channel => !channel.disabled);
};

// Helper function to get channel display name with prefix
export const getChannelDisplayName = (channelId: string): string => {
  const channel = getChannelById(channelId);
  if (!channel) return channelId;

  return channel.shortcut ? `/${channel.shortcut}` : channel.name;
};
