import React from 'react';

interface TerminalButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
  type?: 'button' | 'submit' | 'reset';
}

export const TerminalButton: React.FC<TerminalButtonProps> = ({
  children,
  onClick,
  disabled = false,
  variant = 'primary',
  size = 'md',
  className = '',
  type = 'button',
}) => {
  const baseClasses =
    'font-mono border transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-mythos-terminal-background';

  const variantClasses = {
    primary:
      'bg-mythos-terminal-primary text-black border-mythos-terminal-primary hover:bg-green-400 hover:border-green-400 focus:ring-green-500 disabled:bg-gray-600 disabled:border-gray-600 disabled:text-gray-400',
    secondary:
      'bg-transparent text-mythos-terminal-primary border-mythos-terminal-primary hover:bg-mythos-terminal-primary hover:text-black focus:ring-green-500 disabled:border-gray-600 disabled:text-gray-400',
    danger:
      'bg-red-600 text-white border-red-600 hover:bg-red-700 hover:border-red-700 focus:ring-red-500 disabled:bg-gray-600 disabled:border-gray-600 disabled:text-gray-400',
  };

  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`;

  return (
    <button type={type} onClick={onClick} disabled={disabled} className={classes}>
      {children}
    </button>
  );
};
