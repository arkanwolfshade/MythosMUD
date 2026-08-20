import React from 'react';

import { Z_INDEX_OVERLAY_TOP } from '../../constants/layout';
import { seedFrom } from '../../utils/directionHallucination';
import { AsciiMinimap } from '../map/AsciiMinimap';
import { MinimapPanelBackdrop } from './GameClientV2Minimap';
import { PanelContainer } from './PanelSystem/PanelContainer';
import type { PanelManagerContextValue } from './PanelSystem/PanelManagerContext';
import type { PanelState, Room } from './types';

export type MinimapPanelSectionProps = {
  minimapPanel: PanelState;
  room: Room | null;
  authToken: string;
  onMapClick?: () => void;
  /** #626: when set, replace the minimap with churning ASCII noise. */
  hallucinate?: boolean;
  /** Player id used to seed the noise alongside the room id. */
  playerId?: string;
} & Pick<
  PanelManagerContextValue,
  'updatePosition' | 'updateSize' | 'toggleMinimize' | 'toggleMaximize' | 'focusPanel'
>;

function MinimapInlineBody({
  room,
  authToken,
  onMapClick,
  hallucinate,
  playerId,
}: {
  room: Room | null;
  authToken: string;
  onMapClick?: () => void;
  hallucinate?: boolean;
  playerId?: string;
}) {
  if (!room?.id) {
    return (
      <button
        type="button"
        className="appearance-none w-full h-full min-h-15 flex items-center justify-center text-mythos-terminal-text/70 text-sm cursor-pointer bg-transparent rounded"
        onClick={onMapClick}
        title="Click to open map"
      >
        No location — click to open map
      </button>
    );
  }
  return (
    <>
      <div className="text-xs text-mythos-terminal-text/70 shrink-0 truncate" title={room.id}>
        {room.id}
      </div>
      <div className="flex-1 min-h-16 mt-1">
        <AsciiMinimap
          plane={room.plane ?? ''}
          zone={room.zone ?? ''}
          subZone={room.sub_zone}
          currentRoomId={room.id}
          authToken={authToken}
          size={5}
          variant="inline"
          onClick={onMapClick}
          hallucinate={Boolean(hallucinate && playerId)}
          seed={playerId ? seedFrom(room.id, playerId) : 0}
        />
      </div>
    </>
  );
}

/** Minimap backdrop + draggable panel (extracted to keep GameClientV2 under per-method line limits). */
export const MinimapPanelSection: React.FC<MinimapPanelSectionProps> = props => {
  const {
    minimapPanel,
    room,
    authToken,
    onMapClick,
    hallucinate,
    playerId,
    updatePosition,
    updateSize,
    toggleMinimize,
    toggleMaximize,
    focusPanel,
  } = props;

  return (
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
          className="min-h-25 h-full w-full flex flex-col bg-mythos-terminal-background"
          data-panel="minimap-content"
        >
          <div className="text-mythos-terminal-text/80 text-xs shrink-0 px-1 pb-1">Click map to open full view</div>
          <div className="w-full text-left flex-1 min-h-20 flex flex-col overflow-auto border border-mythos-terminal-border/50 rounded p-1.5 text-mythos-terminal-text bg-mythos-terminal-background">
            <MinimapInlineBody
              room={room}
              authToken={authToken}
              onMapClick={onMapClick}
              hallucinate={hallucinate}
              playerId={playerId}
            />
          </div>
        </div>
      </PanelContainer>
    </>
  );
};
