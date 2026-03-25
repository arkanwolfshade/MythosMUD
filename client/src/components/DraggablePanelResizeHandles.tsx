import React from 'react';

interface DraggablePanelResizeHandlesProps {
  onMouseDown: (e: React.MouseEvent, direction: string) => void;
  onResizeHandleKeyDown: (direction: string, e: React.KeyboardEvent<HTMLButtonElement>) => void;
}

interface HandleConfig {
  direction: string;
  className: string;
  title: string;
  ariaLabel: string;
}

const HANDLE_CONFIGS: HandleConfig[] = [
  {
    direction: 'se',
    className: 'absolute top-0 right-0 w-3 h-3 cursor-se-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize',
    ariaLabel: 'Resize panel southeast',
  },
  {
    direction: 'sw',
    className: 'absolute bottom-0 left-0 w-3 h-3 cursor-sw-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize',
    ariaLabel: 'Resize panel southwest',
  },
  {
    direction: 'se',
    className: 'absolute bottom-0 right-0 w-3 h-3 cursor-se-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize',
    ariaLabel: 'Resize panel southeast',
  },
  {
    direction: 'nw',
    className: 'absolute top-0 left-0 w-3 h-3 cursor-nw-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize',
    ariaLabel: 'Resize panel northwest',
  },
  {
    direction: 'w',
    className:
      'absolute top-1/2 left-0 w-2 h-8 -translate-y-1/2 cursor-w-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize width',
    ariaLabel: 'Resize panel west edge',
  },
  {
    direction: 'e',
    className:
      'absolute top-1/2 right-0 w-2 h-8 -translate-y-1/2 cursor-e-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize width',
    ariaLabel: 'Resize panel east edge',
  },
  {
    direction: 'n',
    className:
      'absolute left-1/2 top-0 w-8 h-2 -translate-x-1/2 cursor-n-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize height',
    ariaLabel: 'Resize panel north edge',
  },
  {
    direction: 's',
    className:
      'absolute left-1/2 bottom-0 w-8 h-2 -translate-x-1/2 cursor-s-resize hover:bg-mythos-terminal-primary/30 z-10',
    title: 'Resize height',
    ariaLabel: 'Resize panel south edge',
  },
];

export const DraggablePanelResizeHandles: React.FC<DraggablePanelResizeHandlesProps> = ({
  onMouseDown,
  onResizeHandleKeyDown,
}) => {
  return (
    <>
      {HANDLE_CONFIGS.map(handle => (
        <button
          key={`${handle.direction}-${handle.className}`}
          type="button"
          className={handle.className}
          onMouseDown={e => {
            onMouseDown(e, handle.direction);
          }}
          onKeyDown={e => {
            onResizeHandleKeyDown(handle.direction, e);
          }}
          title={handle.title}
          aria-label={handle.ariaLabel}
        />
      ))}
    </>
  );
};
