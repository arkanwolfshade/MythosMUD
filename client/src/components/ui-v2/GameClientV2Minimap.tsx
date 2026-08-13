import React from 'react';

import type { PanelState } from './types';

const HEADER_HEIGHT_PX = 48;
const MINIMAP_BACKDROP_Z = 2147483646;

function minimapBackdropLayout(panel: PanelState): {
  pos: PanelState['position'];
  sz: PanelState['size'];
} {
  const isMax = panel.isMaximized;
  const pos = isMax ? { x: 0, y: HEADER_HEIGHT_PX } : panel.position;
  const sz = isMax
    ? {
        width: typeof window !== 'undefined' ? window.innerWidth : 800,
        height: (typeof window !== 'undefined' ? window.innerHeight : 600) - HEADER_HEIGHT_PX,
      }
    : panel.isMinimized
      ? { width: 200, height: 40 }
      : panel.size;
  return { pos, sz };
}

/** Opaque backdrop behind minimap popout (matches Rnd box, below panel z-index). */
export const MinimapPanelBackdrop: React.FC<{ panel: PanelState }> = ({ panel }) => {
  const { pos, sz } = minimapBackdropLayout(panel);
  return (
    <div
      aria-hidden
      className="pointer-events-none rounded border border-gray-700"
      style={{
        position: 'absolute',
        left: 0,
        top: 0,
        width: sz.width,
        height: sz.height,
        transform: `translate(${pos.x}px, ${pos.y}px)`,
        zIndex: MINIMAP_BACKDROP_Z,
        backgroundColor: '#0a0a0a',
      }}
    />
  );
};
