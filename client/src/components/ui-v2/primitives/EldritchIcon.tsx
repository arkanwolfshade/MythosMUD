import * as LucideIcons from 'lucide-react';
import React from 'react';

import { MythosIcons } from './MythosIcons';

// Re-export MythosIcons for backward compatibility
// Note: This maintains compatibility but the warning will persist
// Consider updating imports to use './MythosIcons' directly
export { MythosIcons };

// Map icon names to Lucide icon components
const iconMap: Record<keyof typeof MythosIcons, keyof typeof LucideIcons> = {
  // Core UI icons
  chat: 'MessageCircle',
  move: 'ArrowUp', // Fixed: Use 'ArrowUp' as a valid movement icon
  download: 'Download',
  clear: 'Trash2',
  connection: 'Wifi',
  minimize: 'Minus',
  maximize: 'Maximize',
  restore: 'Minimize2',
  close: 'X',
  clock: 'Clock',
  log: 'FileText',

  // Phase 4.1: New icons for eldritch effects demo
  lightbulb: 'Lightbulb',
  heart: 'Heart',
  sparkles: 'Sparkles',
  eye: 'Eye',
  eyeOff: 'EyeOff',
  star: 'Star',
  shadow: 'Moon',
  square: 'Square',
  play: 'Play',
  stop: 'Square',
  settings: 'Settings',
  panel: 'Layout',
  rotate: 'RotateCw',
  command: 'Square', // Added missing command icon mapping

  // Additional icons used throughout the codebase
  help: 'HelpCircle',
  stats: 'BarChart3',
  look: 'Eye',
  search: 'Search',
  inventory: 'Package',
  character: 'User',
  exit: 'ArrowRight',
  disconnected: 'WifiOff',
  connecting: 'Loader2',
  attack: 'Sword',
  room: 'Home',
  eldritch: 'Moon',
  horror: 'Skull',

  // Channel-specific icons
  global: 'Globe',
  local: 'MapPin',
  whisper: 'MessageSquare',
  system: 'Settings',
  users: 'Users',
  megaphone: 'Megaphone',

  // Logout button icon
  portal: 'CircleDot',
};

interface EldritchIconProps {
  name: keyof typeof MythosIcons;
  size?: number;
  className?: string;
  variant?: 'primary' | 'secondary' | 'warning' | 'error' | 'success';
}

export const EldritchIcon: React.FC<EldritchIconProps> = ({ name, size = 16, className = '', variant = 'primary' }) => {
  const iconKey = iconMap[name];
  const IconComponent = LucideIcons[iconKey] as React.ComponentType<{ size?: number; className?: string }>;

  const variantClasses = {
    primary: 'text-mythos-terminal-primary',
    secondary: 'text-mythos-terminal-secondary',
    warning: 'text-mythos-terminal-warning',
    error: 'text-mythos-terminal-error',
    success: 'text-mythos-terminal-success',
  };

  const classes = `${variantClasses[variant]} ${className}`;

  return <IconComponent size={size} className={classes} />;
};
