import React from 'react';

import { Z_INDEX_OVERLAY_TOP } from '../../constants/layout';
import { AsciiMinimap } from '../map/AsciiMinimap';
import { PanelContainer } from './PanelSystem/PanelContainer';
import type { PanelManagerContextValue } from './PanelSystem/PanelManagerContext';
import type { PanelState, Room } from './types';

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

export type MinimapPanelSectionProps = {
  minimapPanel: PanelState;
  room: Room | null;
  authToken: string;
  onMapClick?: () => void;
} & Pick<
  PanelManagerContextValue,
  'updatePosition' | 'updateSize' | 'toggleMinimize' | 'toggleMaximize' | 'focusPanel'
>;

/** Minimap backdrop + draggable panel (extracted to keep GameClientV2 under per-method line limits). */
export const MinimapPanelSection: React.FC<MinimapPanelSectionProps> = ({
  minimapPanel,
  room,
  authToken,
  onMapClick,
  updatePosition,
  updateSize,
  toggleMinimize,
  toggleMaximize,
  focusPanel,
}) => (
  <>
    <MinimapPanelBackdrop panel={minimapPanel} />
    <PanelContainer
      id={minimapPanel.id}
      title={minimapPanel.title}
      position={minimapPanel.position}
      size={minimapPanel.size}
      zIndex={Z_INDEX_OVERLAY_TOP}
      isMinimized={minimapPanel.isMinimized}
      isMaximized={minimapPanel.isMaximized}
      isVisible={minimapPanel.isVisible}
      minSize={minimapPanel.minSize}
      opaque={minimapPanel.opaque}
      minHeight={minimapPanel.minHeight}
      variant="default"
      className="panel-minimap-opaque"
      onPositionChange={updatePosition}
      onSizeChange={updateSize}
      onMinimize={toggleMinimize}
      onMaximize={toggleMaximize}
      onFocus={focusPanel}
    >
      <div
        className="min-h-[100px] h-full w-full flex flex-col bg-mythos-terminal-background"
        data-panel="minimap-content"
      >
        <div className="text-mythos-terminal-text/80 text-xs shrink-0 px-1 pb-1">Click map to open full view</div>
        {/* Do not wrap AsciiMinimap in <button>: inline minimap already renders a <button> (valid HTML). */}
        <div className="w-full text-left flex-1 min-h-[80px] flex flex-col overflow-auto border border-mythos-terminal-border/50 rounded p-1.5 text-mythos-terminal-text bg-mythos-terminal-background">
          {room?.id ? (
            <>
              <div className="text-xs text-mythos-terminal-text/70 shrink-0 truncate" title={room.id}>
                {room.id}
              </div>
              <div className="flex-1 min-h-[64px] mt-1">
                <AsciiMinimap
                  plane={room.plane ?? ''}
                  zone={room.zone ?? ''}
                  subZone={room.sub_zone}
                  currentRoomId={room.id}
                  authToken={authToken}
                  size={5}
                  variant="inline"
                  onClick={onMapClick}
                />
              </div>
            </>
          ) : (
            <button
              type="button"
              className="appearance-none w-full h-full min-h-[60px] flex items-center justify-center text-mythos-terminal-text/70 text-sm cursor-pointer bg-transparent rounded"
              onClick={onMapClick}
              title="Click to open full map"
            >
              No location — click to open map
            </button>
          )}
        </div>
      </div>
    </PanelContainer>
  </>
);
