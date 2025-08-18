import React from 'react';

interface MythosPanelProps {
  children: React.ReactNode;
  title?: string;
  subtitle?: string;
  className?: string;
  variant?: 'default' | 'elevated' | 'outlined' | 'eldritch';
  size?: 'sm' | 'md' | 'lg';
  showEldritchBorder?: boolean;
}

export const MythosPanel: React.FC<MythosPanelProps> = ({
  children,
  title,
  subtitle,
  className = '',
  variant = 'default',
  size = 'md',
  showEldritchBorder = false,
}) => {
  const baseClasses = 'font-mono border rounded relative overflow-hidden';

  const variantClasses = {
    default: 'bg-mythos-terminal-surface border-gray-700 text-mythos-terminal-text',
    elevated:
      'bg-mythos-terminal-surface border-mythos-terminal-primary shadow-lg shadow-green-900/20 text-mythos-terminal-text',
    outlined: 'bg-transparent border-mythos-terminal-primary text-mythos-terminal-text',
    eldritch:
      'bg-mythos-terminal-surface border-mythos-terminal-primary text-mythos-terminal-text shadow-lg shadow-green-900/30',
  };

  const sizeClasses = {
    sm: 'p-3',
    md: 'p-4',
    lg: 'p-6',
  };

  const eldritchBorderClasses = showEldritchBorder
    ? 'before:absolute before:inset-0 before:border before:border-mythos-terminal-primary/30 before:rounded before:pointer-events-none before:animate-pulse'
    : '';

  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${eldritchBorderClasses} ${className}`;

  return (
    <div className={classes}>
      {/* Eldritch corner decorations for eldritch variant */}
      {variant === 'eldritch' && (
        <>
          <div className="absolute top-0 left-0 w-2 h-2 border-l-2 border-t-2 border-mythos-terminal-primary/50"></div>
          <div className="absolute top-0 right-0 w-2 h-2 border-r-2 border-t-2 border-mythos-terminal-primary/50"></div>
          <div className="absolute bottom-0 left-0 w-2 h-2 border-l-2 border-b-2 border-mythos-terminal-primary/50"></div>
          <div className="absolute bottom-0 right-0 w-2 h-2 border-r-2 border-b-2 border-mythos-terminal-primary/50"></div>
        </>
      )}

      {title && (
        <div
          className={`border-b border-gray-700 bg-mythos-terminal-background ${size === 'sm' ? 'px-2 py-1' : size === 'md' ? 'px-3 py-2' : 'px-4 py-3'}`}
        >
          <h3 className="text-mythos-terminal-primary font-bold text-sm">{title}</h3>
          {subtitle && <p className="text-mythos-terminal-text-secondary text-xs mt-1">{subtitle}</p>}
        </div>
      )}

      <div className={size === 'sm' ? 'p-2' : size === 'md' ? 'p-3' : 'p-4'}>{children}</div>
    </div>
  );
};
