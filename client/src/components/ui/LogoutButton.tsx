import React, { useCallback, useEffect } from 'react';
import { EldritchIcon, MythosIcons } from './EldritchIcon';

interface LogoutButtonProps {
  onLogout: () => void;
  disabled?: boolean;
  isLoggingOut?: boolean;
  className?: string;
}

export const LogoutButton: React.FC<LogoutButtonProps> = ({
  onLogout,
  disabled = false,
  isLoggingOut = false,
  className = '',
}) => {
  const handleKeyDown = useCallback(
    (event: KeyboardEvent) => {
      // Check for Ctrl+Q shortcut
      if (event.ctrlKey && event.key.toLowerCase() === 'q') {
        event.preventDefault();
        if (!disabled && !isLoggingOut) {
          onLogout();
        }
      }
    },
    [onLogout, disabled, isLoggingOut]
  );

  // Set up global keyboard shortcut
  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleKeyDown]);

  const isDisabled = disabled || isLoggingOut;

  const baseClasses =
    'font-mono border rounded transition-eldritch duration-eldritch ease-eldritch focus:outline-hidden focus:ring-2 focus:ring-offset-2 focus:ring-offset-mythos-terminal-background';

  const variantClasses = isDisabled
    ? 'bg-mythos-terminal-surface border-mythos-terminal-error text-mythos-terminal-error opacity-50 cursor-not-allowed hover:bg-mythos-terminal-surface hover:text-mythos-terminal-error hover:animate-none'
    : 'bg-mythos-terminal-surface border-mythos-terminal-error text-mythos-terminal-error hover:bg-mythos-terminal-error hover:text-mythos-terminal-background hover:animate-eldritch-glow focus:ring-mythos-terminal-error cursor-pointer hover:animate-eldritch-scale';

  const sizeClasses = 'px-4 py-5 text-base min-h-touch';
  const widthClasses = 'w-full';

  const classes = [baseClasses, variantClasses, sizeClasses, widthClasses, className].join(' ');

  const handleClick = () => {
    if (!isDisabled) {
      onLogout();
    }
  };

  const handleKeyPress = (event: React.KeyboardEvent) => {
    if ((event.key === 'Enter' || event.key === ' ') && !isDisabled) {
      event.preventDefault();
      onLogout();
    }
  };

  return (
    <button
      type="button"
      onClick={handleClick}
      onKeyDown={handleKeyPress}
      disabled={isDisabled}
      className={classes}
      aria-label="Exit the realm and return to login screen"
      title="Exit the realm and return to login screen (Ctrl+Q)"
      data-testid="logout-button"
    >
      <div className="flex items-center justify-center gap-2">
        <EldritchIcon name={MythosIcons.portal} size={16} variant="error" />
        <span>{isLoggingOut ? 'Exiting...' : 'Exit the Realm'}</span>
      </div>
    </button>
  );
};
