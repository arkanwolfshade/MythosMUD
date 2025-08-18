import React from 'react';

interface TerminalInputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
  type?: 'text' | 'password' | 'email' | 'number';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
  onKeyDown?: (e: React.KeyboardEvent) => void;
  onFocus?: () => void;
  onBlur?: () => void;
}

export const TerminalInput: React.FC<TerminalInputProps> = ({
  value,
  onChange,
  placeholder = '',
  disabled = false,
  type = 'text',
  size = 'md',
  className = '',
  onKeyDown,
  onFocus,
  onBlur,
}) => {
  const baseClasses =
    'font-mono border transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-mythos-terminal-background bg-mythos-terminal-surface text-mythos-terminal-text border-gray-700 focus:border-mythos-terminal-primary focus:ring-mythos-terminal-primary';

  const sizeClasses = {
    sm: 'px-2 py-1 text-sm',
    md: 'px-3 py-2 text-base',
    lg: 'px-4 py-3 text-lg',
  };

  const disabledClasses = disabled ? 'bg-gray-800 text-gray-500 cursor-not-allowed' : '';

  const classes = `${baseClasses} ${sizeClasses[size]} ${disabledClasses} ${className}`;

  return (
    <input
      type={type}
      value={value}
      onChange={e => onChange(e.target.value)}
      placeholder={placeholder}
      disabled={disabled}
      className={classes}
      onKeyDown={onKeyDown}
      onFocus={onFocus}
      onBlur={onBlur}
    />
  );
};
