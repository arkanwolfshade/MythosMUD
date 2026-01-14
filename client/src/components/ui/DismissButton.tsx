import React from 'react';

interface DismissButtonProps {
  onClick: () => void;
  variant?: 'primary' | 'error';
  className?: string;
  'aria-label'?: string;
  children?: React.ReactNode;
}

/**
 * Reusable dismiss button component with consistent styling.
 * Used in banners and modals for dismissing notifications.
 */
export const DismissButton: React.FC<DismissButtonProps> = ({
  onClick,
  variant = 'primary',
  className = '',
  'aria-label': ariaLabel = 'Dismiss',
  children = 'Dismiss',
}) => {
  const hoverColorClass =
    variant === 'error' ? 'hover:text-mythos-terminal-error' : 'hover:text-mythos-terminal-primary';

  const baseClasses =
    'rounded bg-transparent px-2 py-1 text-xs-3 uppercase tracking-wide text-mythos-terminal-text-secondary focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-mythos-terminal-primary/60';

  const classes = `${baseClasses} ${hoverColorClass} ${className}`;

  return (
    <button type="button" onClick={onClick} className={classes} aria-label={ariaLabel}>
      {children}
    </button>
  );
};

DismissButton.displayName = 'DismissButton';
