import React, { useEffect } from 'react';

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
  useEffect(() => {
    if (!isOpen) {
      return;
    }
    const onDocumentKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    document.addEventListener('keydown', onDocumentKeyDown);
    return () => {
      document.removeEventListener('keydown', onDocumentKeyDown);
    };
  }, [isOpen, onClose]);

  if (!isOpen) {
    return null;
  }

  const modalContentClasses =
    `bg-mythos-terminal-background border border-mythos-terminal-border rounded-lg w-full ` +
    `${maxWidthClasses[maxWidth]} max-h-modal overflow-y-auto shadow-xl ${contentClassName}`;

  const isFloating = position === 'bottom-right';
  const isNoBackdrop = position === 'center-no-backdrop';

  const content = (
    <div className={modalContentClasses} style={isNoBackdrop ? { pointerEvents: 'auto' } : undefined}>
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
      <div className={`fixed bottom-4 right-4 flex flex-col items-end ${className}`} style={{ zIndex: overlayZIndex }}>
        <div role="dialog" aria-modal="true" aria-labelledby={titleId} tabIndex={-1}>
          {content}
        </div>
      </div>
    );
  }

  if (isNoBackdrop) {
    return (
      <div
        className={`fixed inset-0 flex items-center justify-center pointer-events-none ${className}`}
        style={{ zIndex: overlayZIndex }}
      >
        <div className="pointer-events-auto" role="dialog" aria-modal="true" aria-labelledby={titleId} tabIndex={-1}>
          {content}
        </div>
      </div>
    );
  }

  return (
    <div className={`fixed inset-0 flex items-center justify-center ${className}`} style={{ zIndex: overlayZIndex }}>
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-50 border-0 p-0"
        onClick={onClose}
        aria-label="Close modal"
      />
      <div
        className="relative z-10 flex w-full max-w-full justify-center px-4"
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        tabIndex={-1}
      >
        {content}
      </div>
    </div>
  );
};

ModalContainer.displayName = 'ModalContainer';
