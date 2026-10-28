import React from 'react';

interface TerminalButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  onClick?: () => void;
  variant?: 'primary' | 'secondary' | 'danger' | 'warning' | 'success';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  className?: string;
  type?: 'button' | 'submit' | 'reset';
  fullWidth?: boolean;
}

export const TerminalButton = React.forwardRef<HTMLButtonElement, TerminalButtonProps>(
  (
    {
      children,
      onClick,
      variant = 'primary',
      size = 'md',
      disabled = false,
      className = '',
      type = 'button',
      fullWidth = false,
      ...rest
    },
    ref
  ) => {
    const baseClasses =
      'font-mono border rounded transition-eldritch duration-eldritch ease-eldritch focus:outline-hidden focus:ring-2 focus:ring-offset-2 focus:ring-offset-mythos-terminal-background';

    const variantClasses = {
      primary:
        'text-mythos-terminal-primary bg-mythos-terminal-surface border-mythos-terminal-primary hover:bg-mythos-terminal-primary hover:text-mythos-terminal-background hover:animate-eldritch-glow focus:ring-mythos-terminal-primary',
      secondary:
        'text-mythos-terminal-secondary bg-mythos-terminal-surface border-mythos-terminal-secondary hover:bg-mythos-terminal-secondary hover:text-mythos-terminal-background hover:animate-eldritch-pulse focus:ring-mythos-terminal-secondary',
      danger:
        'text-mythos-terminal-error bg-mythos-terminal-surface border-mythos-terminal-error hover:bg-mythos-terminal-error hover:text-mythos-terminal-background hover:animate-eldritch-glow focus:ring-mythos-terminal-error',
      warning:
        'text-mythos-terminal-warning bg-mythos-terminal-surface border-mythos-terminal-warning hover:bg-mythos-terminal-warning hover:text-mythos-terminal-background hover:animate-eldritch-pulse focus:ring-mythos-terminal-warning',
      success:
        'text-mythos-terminal-success bg-mythos-terminal-surface border-mythos-terminal-success hover:bg-mythos-terminal-success hover:text-mythos-terminal-background hover:animate-eldritch-glow focus:ring-mythos-terminal-success',
    };

    const sizeClasses = {
      sm: 'px-3 py-1 text-sm',
      md: 'px-4 py-2 text-base',
      lg: 'px-6 py-3 text-lg',
    };

    const disabledClasses = disabled
      ? 'opacity-50 cursor-not-allowed hover:bg-mythos-terminal-surface hover:text-mythos-terminal-text hover:animate-none'
      : 'cursor-pointer hover:animate-eldritch-scale';

    const widthClasses = fullWidth ? 'w-full' : '';

    const classes = [
      baseClasses,
      variantClasses[variant],
      sizeClasses[size],
      disabledClasses,
      widthClasses,
      className,
    ].join(' ');

    return (
      <button ref={ref} type={type} onClick={onClick} disabled={disabled} className={classes} {...rest}>
        {children}
      </button>
    );
  }
);

TerminalButton.displayName = 'TerminalButton';
