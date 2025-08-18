import React from 'react';

interface TerminalInputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  type?: string;
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  className?: string;
  onKeyDown?: (event: React.KeyboardEvent<HTMLInputElement>) => void;
  onFocus?: (event: React.FocusEvent<HTMLInputElement>) => void;
  onBlur?: (event: React.FocusEvent<HTMLInputElement>) => void;
  autoFocus?: boolean;
  required?: boolean;
  name?: string;
  id?: string;
}

export const TerminalInput: React.FC<TerminalInputProps> = ({
  value,
  onChange,
  placeholder,
  type = 'text',
  size = 'md',
  disabled = false,
  className = '',
  onKeyDown,
  onFocus,
  onBlur,
  autoFocus = false,
  required = false,
  name,
  id,
}) => {
  const baseClasses =
    'font-mono bg-mythos-terminal-surface border border-gray-700 text-mythos-terminal-text placeholder-mythos-terminal-text-secondary rounded transition-eldritch duration-eldritch ease-eldritch focus:outline-none focus:ring-2 focus:ring-mythos-terminal-primary focus:border-mythos-terminal-primary focus:animate-eldritch-border';

  const sizeClasses = {
    sm: 'px-2 py-1 text-sm',
    md: 'px-3 py-2 text-base',
    lg: 'px-4 py-3 text-lg',
  };

  const disabledClasses = disabled
    ? 'opacity-50 cursor-not-allowed bg-mythos-terminal-background'
    : 'cursor-text hover:border-mythos-terminal-primary/50';

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
      autoFocus={autoFocus}
      required={required}
      name={name}
      id={id}
    />
  );
};
