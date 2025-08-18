import * as LucideIcons from 'lucide-react';
import React from 'react';

interface EldritchIconProps {
  name: keyof typeof LucideIcons;
  size?: number;
  className?: string;
  variant?: 'default' | 'primary' | 'secondary' | 'warning' | 'error' | 'success';
  animated?: boolean;
}

export const EldritchIcon: React.FC<EldritchIconProps> = ({
  name,
  size = 16,
  className = '',
  variant = 'default',
  animated = false,
}) => {
  const IconComponent = LucideIcons[name] as React.ComponentType<{ size?: number; className?: string }>;

  if (!IconComponent) {
    console.warn(`Icon "${name}" not found in Lucide React`);
    return null;
  }

  const variantClasses = {
    default: 'text-mythos-terminal-text',
    primary: 'text-mythos-terminal-primary',
    secondary: 'text-mythos-terminal-secondary',
    warning: 'text-mythos-terminal-warning',
    error: 'text-mythos-terminal-error',
    success: 'text-mythos-terminal-success',
  };

  const animationClasses = animated ? 'animate-pulse' : '';

  const classes = `${variantClasses[variant]} ${animationClasses} ${className}`;

  return <IconComponent size={size} className={classes} />;
};

// Predefined Mythos-themed icon mappings
export const MythosIcons = {
  // Connection and status
  connection: 'Wifi' as keyof typeof LucideIcons,
  disconnected: 'WifiOff' as keyof typeof LucideIcons,
  connecting: 'Loader2' as keyof typeof LucideIcons,

  // Navigation and movement
  move: 'Move' as keyof typeof LucideIcons,
  look: 'Eye' as keyof typeof LucideIcons,
  search: 'Search' as keyof typeof LucideIcons,

  // Communication
  chat: 'MessageCircle' as keyof typeof LucideIcons,
  whisper: 'MessageSquare' as keyof typeof LucideIcons,
  shout: 'Volume2' as keyof typeof LucideIcons,

  // Combat and actions
  attack: 'Sword' as keyof typeof LucideIcons,
  defend: 'Shield' as keyof typeof LucideIcons,
  cast: 'Zap' as keyof typeof LucideIcons,

  // Inventory and items
  inventory: 'Package' as keyof typeof LucideIcons,
  item: 'Box' as keyof typeof LucideIcons,
  gold: 'Coins' as keyof typeof LucideIcons,

  // Character and stats
  character: 'User' as keyof typeof LucideIcons,
  stats: 'BarChart3' as keyof typeof LucideIcons,
  health: 'Heart' as keyof typeof LucideIcons,
  sanity: 'Brain' as keyof typeof LucideIcons,

  // Environment
  room: 'Home' as keyof typeof LucideIcons,
  exit: 'ArrowRight' as keyof typeof LucideIcons,
  door: 'DoorOpen' as keyof typeof LucideIcons,

  // Eldritch and Mythos
  eldritch: 'Moon' as keyof typeof LucideIcons,
  forbidden: 'Lock' as keyof typeof LucideIcons,
  ancient: 'Clock' as keyof typeof LucideIcons,
  horror: 'Skull' as keyof typeof LucideIcons,

  // UI and controls
  close: 'X' as keyof typeof LucideIcons,
  minimize: 'Minus' as keyof typeof LucideIcons,
  maximize: 'Maximize' as keyof typeof LucideIcons,
  settings: 'Settings' as keyof typeof LucideIcons,
  help: 'HelpCircle' as keyof typeof LucideIcons,
  download: 'Download' as keyof typeof LucideIcons,
  clear: 'Trash2' as keyof typeof LucideIcons,

  // System
  error: 'AlertCircle' as keyof typeof LucideIcons,
  warning: 'AlertTriangle' as keyof typeof LucideIcons,
  success: 'CheckCircle' as keyof typeof LucideIcons,
  info: 'Info' as keyof typeof LucideIcons,
  clock: 'Clock' as keyof typeof LucideIcons,
} as const;
