import React from 'react';
import type { PanelPosition, PanelSize, PanelVariant } from '../types';

export interface PanelContainerProps {
  id: string;
  title: string;
  children: React.ReactNode;
  position: PanelPosition;
  size: PanelSize;
  zIndex: number;
  isMinimized: boolean;
  isMaximized: boolean;
  isVisible: boolean;
  minSize?: PanelSize;
  maxSize?: PanelSize;
  variant?: PanelVariant;
  className?: string;
  opaque?: boolean;
  minHeight?: number;
  onPositionChange: (id: string, position: PanelPosition) => void;
  onSizeChange: (id: string, size: PanelSize) => void;
  onMinimize: (id: string) => void;
  onMaximize: (id: string) => void;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
}

/** Opaque fill behind panel chrome so backdrop art does not show through the face. */
export function PanelSolidUnderlay(): React.ReactElement {
  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
        zIndex: 0,
        pointerEvents: 'none',
        borderRadius: 'inherit',
      }}
      aria-hidden
    />
  );
}
