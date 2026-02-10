import React from 'react';

interface ModalContainerProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
  title?: string;
  titleId?: string;
  maxWidth?: 'sm' | 'md' | 'lg' | 'xl' | '2xl' | '4xl';
  className?: string;
  contentClassName?: string;
  showCloseButton?: boolean;
  /** Z-index for overlay (default 50). Use 10000+ to appear above game panels (1000–1007). */
  overlayZIndex?: number;
  /**
   * 'center' = full-screen dimmed overlay + centered dialog;
   * 'center-no-backdrop' = centered dialog only, no overlay (game UI stays visible, dialog accepts clicks);
   * 'bottom-right' = floating card only.
   */
  position?: 'center' | 'center-no-backdrop' | 'bottom-right';
}

const maxWidthClasses = {
  sm: 'max-w-sm',
  md: 'max-w-md',
  lg: 'max-w-lg',
  xl: 'max-w-xl',
  '2xl': 'max-w-2xl',
  '4xl': 'max-w-4xl',
};

/**
 * Reusable modal container component with consistent styling and behavior.
 * Provides overlay, backdrop, and modal content structure.
 */
export const ModalContainer: React.FC<ModalContainerProps> = ({
  isOpen,
  onClose,
  children,
  title,
  titleId,
  maxWidth = '2xl',
  className = '',
  contentClassName = '',
  showCloseButton = false,
  overlayZIndex = 50,
  position = 'center',
}) => {
  if (!isOpen) return null;

  const handleBackdropClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLDivElement>) => {
    if (e.key === 'Escape') {
      onClose();
    }
  };

  const modalContentClasses =
    `bg-mythos-terminal-background border border-mythos-terminal-border rounded-lg w-full ` +
    `${maxWidthClasses[maxWidth]} max-h-modal overflow-y-auto shadow-xl ${contentClassName}`;

  const isFloating = position === 'bottom-right';
  const isNoBackdrop = position === 'center-no-backdrop';

  const content = (
    <div
      className={modalContentClasses}
      onClick={e => e.stopPropagation()}
      style={isNoBackdrop ? { pointerEvents: 'auto' } : undefined}
    >
      {(title || showCloseButton) && (
        <div className="flex items-center justify-between p-4 border-b border-mythos-terminal-border">
          {title && (
            <h2 id={titleId} className="text-xl font-bold text-mythos-terminal-text-primary">
              {title}
            </h2>
          )}
          {showCloseButton && (
            <button
              type="button"
              onClick={onClose}
              className="text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary focus:outline-hidden focus:ring-2 focus:ring-mythos-terminal-primary rounded p-1"
              aria-label="Close modal"
            >
              ✕
            </button>
          )}
        </div>
      )}
      {children}
    </div>
  );

  if (isFloating) {
    return (
      <div
        className={`fixed bottom-4 right-4 flex flex-col items-end ${className}`}
        style={{ zIndex: overlayZIndex }}
        onKeyDown={handleKeyDown}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
      >
        {content}
      </div>
    );
  }

  if (isNoBackdrop) {
    return (
      <div
        className={`fixed inset-0 flex items-center justify-center pointer-events-none ${className}`}
        style={{ zIndex: overlayZIndex }}
        onKeyDown={handleKeyDown}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
      >
        {content}
      </div>
    );
  }

  return (
    <div
      className={`fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 ${className}`}
      style={{ zIndex: overlayZIndex }}
      onClick={handleBackdropClick}
      onKeyDown={handleKeyDown}
      role="dialog"
      aria-modal="true"
      aria-labelledby={titleId}
    >
      {content}
    </div>
  );
};

ModalContainer.displayName = 'ModalContainer';
