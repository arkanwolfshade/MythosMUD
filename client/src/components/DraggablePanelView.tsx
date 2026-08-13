import React from 'react';
import { DraggablePanelResizeHandles } from './DraggablePanelResizeHandles';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { TerminalButton } from './ui/TerminalButton';

const variantClasses = {
  default: 'text-mythos-terminal-text',
  eldritch:
    'text-mythos-terminal-text border-mythos-terminal-primary shadow-green-900/30 hover:shadow-green-900/50 hover:animate-eldritch-shadow',
  elevated:
    'text-mythos-terminal-text border-mythos-terminal-primary shadow-xl shadow-green-900/20 hover:shadow-2xl hover:shadow-green-900/30',
};

const headerClasses = {
  default: 'bg-mythos-terminal-background border-b border-mythos-terminal-border cursor-move select-none',
  eldritch:
    'bg-mythos-terminal-background border-b border-mythos-terminal-primary cursor-move select-none animate-eldritch-glow',
  elevated: 'bg-mythos-terminal-background border-b border-mythos-terminal-primary cursor-move select-none',
};

export interface DraggablePanelViewProps {
  children: React.ReactNode;
  title: string;
  className: string;
  variant: 'default' | 'eldritch' | 'elevated';
  zIndex: number;
  onClose?: () => void;
  onMinimize?: () => void;
  onMaximize?: () => void;
  isGridPositioned: boolean;
  position: { x: number; y: number };
  size: { width: number; height: number };
  isMinimized: boolean;
  headerHeight: number;
  panelRef: React.RefObject<HTMLDivElement | null>;
  headerRef: React.RefObject<HTMLDivElement | null>;
  contentRef: React.RefObject<HTMLDivElement | null>;
  handleMinimize: () => void;
  handleMouseDown: (e: React.MouseEvent, direction: string) => void;
  handleResizeHandleKeyDown: (direction: string, e: React.KeyboardEvent<HTMLButtonElement>) => void;
  handleHeaderMouseDown: (e: React.MouseEvent) => void;
}

export function DraggablePanelView(props: DraggablePanelViewProps): React.ReactElement {
  const {
    children,
    title,
    className,
    variant,
    zIndex,
    onClose,
    onMinimize,
    onMaximize,
    isGridPositioned,
    position,
    size,
    isMinimized,
    headerHeight,
    panelRef,
    headerRef,
    contentRef,
    handleMinimize,
    handleMouseDown,
    handleResizeHandleKeyDown,
    handleHeaderMouseDown,
  } = props;

  const baseClasses = isGridPositioned
    ? 'font-mono bg-mythos-terminal-surface border border-mythos-terminal-border rounded shadow-lg overflow-hidden transition-eldritch duration-eldritch ease-eldritch'
    : 'font-mono bg-mythos-terminal-surface border border-mythos-terminal-border rounded shadow-lg absolute overflow-hidden transition-eldritch duration-eldritch ease-eldritch relative';
  const classes = `draggable-panel ${baseClasses} ${variantClasses[variant]} ${className}`;
  const panelStyle: React.CSSProperties = isGridPositioned
    ? {
        position: 'relative',
        width: '100%',
        height: '100%',
        zIndex,
        left: 'auto',
        top: 'auto',
        right: 'auto',
        bottom: 'auto',
      }
    : {
        position: 'absolute',
        left: position.x,
        top: position.y,
        width: size.width,
        height: isMinimized ? 'auto' : size.height,
        zIndex,
      };

  return (
    <div ref={panelRef} className={classes} style={panelStyle}>
      <div
        ref={headerRef}
        role="button"
        tabIndex={0}
        className={`flex items-center justify-between px-3 py-2 ${headerClasses[variant]}`}
        onMouseDown={handleHeaderMouseDown}
        onKeyDown={e => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
          }
        }}
      >
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.panel} size={16} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">{title}</span>
        </div>
        <div className="flex items-center space-x-1">
          {onMinimize && (
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={handleMinimize}
              className="w-9 h-9 p-0 flex items-center justify-center hover:animate-eldritch-pulse"
            >
              <EldritchIcon name={MythosIcons.minimize} size={12} />
            </TerminalButton>
          )}
          {onMaximize && (
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={onMaximize}
              className="w-9 h-9 p-0 flex items-center justify-center hover:animate-eldritch-pulse"
            >
              <EldritchIcon name={MythosIcons.maximize} size={12} />
            </TerminalButton>
          )}
          {onClose && (
            <TerminalButton
              variant="danger"
              size="sm"
              onClick={onClose}
              className="w-9 h-9 p-0 flex items-center justify-center hover:animate-eldritch-glow"
            >
              <EldritchIcon name={MythosIcons.close} size={12} />
            </TerminalButton>
          )}
        </div>
      </div>
      {!isMinimized && (
        <div
          ref={contentRef}
          className="p-3 h-full overflow-auto relative bg-mythos-terminal-surface"
          style={{ height: `calc(100% - ${headerHeight}px)`, minHeight: '100px' }}
        >
          {children}
        </div>
      )}
      {!isMinimized && (
        <DraggablePanelResizeHandles onMouseDown={handleMouseDown} onResizeHandleKeyDown={handleResizeHandleKeyDown} />
      )}
    </div>
  );
}
