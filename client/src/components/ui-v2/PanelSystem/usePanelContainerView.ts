import type { ReactNode } from 'react';

import type { PanelPosition, PanelSize, PanelVariant } from '../types';
import type { PanelLayoutHandlers } from './panelLayoutTypes';
import { usePanelContainerLayout } from './usePanelContainerLayout';

export interface PanelContainerProps {
  id: string;
  title: string;
  children: ReactNode;
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
  /** Opaque background so panel stays readable over others (e.g. minimap popout). */
  opaque?: boolean;
  /** Minimum content height in px to avoid collapsed content. */
  minHeight?: number;
  onPositionChange: (id: string, position: PanelPosition) => void;
  onSizeChange: (id: string, size: PanelSize) => void;
  onMinimize: (id: string) => void;
  onMaximize: (id: string) => void;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
}

function resolveDisplaySize(isMaximized: boolean, layout: PanelLayoutHandlers): PanelSize {
  if (isMaximized && layout.maximizedSize) {
    return layout.maximizedSize;
  }
  return layout.effectiveSize;
}

function resolveDisplayPosition(
  isMaximized: boolean,
  layout: PanelLayoutHandlers,
  position: PanelPosition
): PanelPosition {
  if (isMaximized && layout.maximizedPosition) {
    return layout.maximizedPosition;
  }
  return position;
}

export function usePanelContainerView(props: PanelContainerProps) {
  const opaque = Boolean(props.opaque);
  const layout = usePanelContainerLayout({
    id: props.id,
    size: props.size,
    isMaximized: props.isMaximized,
    minHeight: props.minHeight,
    variant: props.variant || 'default',
    opaque,
    onPositionChange: props.onPositionChange,
    onSizeChange: props.onSizeChange,
    onMinimize: props.onMinimize,
    onMaximize: props.onMaximize,
    onClose: props.onClose,
    onFocus: props.onFocus,
  });

  return {
    ...props,
    minSize: props.minSize || { width: 200, height: 150 },
    className: props.className || '',
    opaque,
    layout,
    displaySize: resolveDisplaySize(props.isMaximized, layout),
    displayPosition: resolveDisplayPosition(props.isMaximized, layout, props.position),
  };
}
