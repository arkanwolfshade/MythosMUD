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
  overlayZIndex?: number;
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

function ModalContent(props: {
  title?: string;
  titleId?: string;
  showCloseButton: boolean;
  onClose: () => void;
  modalContentClasses: string;
  isNoBackdrop: boolean;
  children: React.ReactNode;
}): React.ReactElement {
  return (
    <div className={props.modalContentClasses} style={props.isNoBackdrop ? { pointerEvents: 'auto' } : undefined}>
      {(props.title || props.showCloseButton) && (
        <div className="flex items-center justify-between p-4 border-b border-mythos-terminal-border">
          {props.title && (
            <h2 id={props.titleId} className="text-xl font-bold text-mythos-terminal-text-primary">
              {props.title}
            </h2>
          )}
          {props.showCloseButton && (
            <button
              type="button"
              onClick={props.onClose}
              className="text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary focus:outline-hidden focus:ring-2 focus:ring-mythos-terminal-primary rounded p-1"
              aria-label="Close modal"
            >
              ✕
            </button>
          )}
        </div>
      )}
      {props.children}
    </div>
  );
}

function FloatingModalShell(props: {
  className: string;
  overlayZIndex: number;
  titleId?: string;
  content: React.ReactElement;
}): React.ReactElement {
  return (
    <div
      className={`fixed bottom-4 right-4 flex flex-col items-end ${props.className}`}
      style={{ zIndex: props.overlayZIndex }}
    >
      <div role="dialog" aria-modal="true" aria-labelledby={props.titleId} tabIndex={-1}>
        {props.content}
      </div>
    </div>
  );
}

function CenterNoBackdropShell(props: {
  className: string;
  overlayZIndex: number;
  titleId?: string;
  content: React.ReactElement;
}): React.ReactElement {
  return (
    <div
      className={`fixed inset-0 flex items-center justify-center pointer-events-none ${props.className}`}
      style={{ zIndex: props.overlayZIndex }}
    >
      <div
        className="pointer-events-auto"
        role="dialog"
        aria-modal="true"
        aria-labelledby={props.titleId}
        tabIndex={-1}
      >
        {props.content}
      </div>
    </div>
  );
}

function CenterModalShell(props: {
  className: string;
  overlayZIndex: number;
  titleId?: string;
  onClose: () => void;
  content: React.ReactElement;
}): React.ReactElement {
  return (
    <div
      className={`fixed inset-0 flex items-center justify-center ${props.className}`}
      style={{ zIndex: props.overlayZIndex }}
    >
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-50 border-0 p-0"
        onClick={props.onClose}
        aria-label="Close modal"
      />
      <div
        className="relative z-10 flex w-full max-w-full justify-center px-4"
        role="dialog"
        aria-modal="true"
        aria-labelledby={props.titleId}
        tabIndex={-1}
      >
        {props.content}
      </div>
    </div>
  );
}

function useModalEscapeKey(isOpen: boolean, onClose: () => void): void {
  useEffect(() => {
    if (!isOpen) return;
    const onDocumentKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('keydown', onDocumentKeyDown);
    return () => document.removeEventListener('keydown', onDocumentKeyDown);
  }, [isOpen, onClose]);
}

function renderOpenModal(props: {
  position: ModalContainerProps['position'];
  className: string;
  overlayZIndex: number;
  titleId?: string;
  onClose: () => void;
  content: React.ReactElement;
}): React.ReactElement {
  if (props.position === 'bottom-right') {
    return (
      <FloatingModalShell
        className={props.className}
        overlayZIndex={props.overlayZIndex}
        titleId={props.titleId}
        content={props.content}
      />
    );
  }
  if (props.position === 'center-no-backdrop') {
    return (
      <CenterNoBackdropShell
        className={props.className}
        overlayZIndex={props.overlayZIndex}
        titleId={props.titleId}
        content={props.content}
      />
    );
  }
  return (
    <CenterModalShell
      className={props.className}
      overlayZIndex={props.overlayZIndex}
      titleId={props.titleId}
      onClose={props.onClose}
      content={props.content}
    />
  );
}

export const ModalContainer: React.FC<ModalContainerProps> = props => {
  const {
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
  } = props;

  useModalEscapeKey(isOpen, onClose);
  if (!isOpen) return null;

  const modalContentClasses =
    `bg-mythos-terminal-background border border-mythos-terminal-border rounded-lg w-full ` +
    `${maxWidthClasses[maxWidth]} max-h-modal overflow-y-auto shadow-xl ${contentClassName}`;
  const content = (
    <ModalContent
      title={title}
      titleId={titleId}
      showCloseButton={showCloseButton}
      onClose={onClose}
      modalContentClasses={modalContentClasses}
      isNoBackdrop={position === 'center-no-backdrop'}
      children={children}
    />
  );

  return renderOpenModal({ position, className, overlayZIndex, titleId, onClose, content });
};

ModalContainer.displayName = 'ModalContainer';
