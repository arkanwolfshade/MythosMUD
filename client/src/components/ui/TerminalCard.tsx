import React from 'react';

interface TerminalCardProps {
  children: React.ReactNode;
  title?: string;
  className?: string;
  variant?: 'default' | 'elevated' | 'outlined';
}

export const TerminalCard: React.FC<TerminalCardProps> = ({ children, title, className = '', variant = 'default' }) => {
  const baseClasses = 'font-mono border rounded';

  const variantClasses = {
    default: 'bg-mythos-terminal-surface border-gray-700 text-mythos-terminal-text',
    elevated:
      'bg-mythos-terminal-surface border-mythos-terminal-primary shadow-lg shadow-green-900/20 text-mythos-terminal-text',
    outlined: 'bg-transparent border-mythos-terminal-primary text-mythos-terminal-text',
  };

  const classes = `${baseClasses} ${variantClasses[variant]} ${className}`;

  return (
    <div className={classes}>
      {title && (
        <div className="px-4 py-2 border-b border-gray-700 bg-mythos-terminal-background">
          <h3 className="text-mythos-terminal-primary font-bold">{title}</h3>
        </div>
      )}
      <div className="p-4">{children}</div>
    </div>
  );
};
