import React from 'react';

import type { HealthStatus } from '../../types/health';
import type { LucidityStatus } from '../../types/lucidity';
import { MinimapPanelSection } from './GameClientV2Minimap';
import { PanelContainer } from './PanelSystem/PanelContainer';
import type { PanelManagerContextValue } from './PanelSystem/PanelManagerContext';
import { CharacterInfoPanel } from './panels/CharacterInfoPanel';
import { CommandHistoryPanel } from './panels/CommandHistoryPanel';
import { CommandInputPanel } from './panels/CommandInputPanel';
import type { PanelState, Player, Room } from './types';
import { getCharacterInfoPanelOutlineClassName as getCharacterPanelOutlineClassName } from './utils/characterInfoPanelOutline';

export interface GameClientV2AuxiliaryPanelsProps {
  panelManager: Pick<
    PanelManagerContextValue,
    'updatePosition' | 'updateSize' | 'toggleMinimize' | 'toggleMaximize' | 'focusPanel'
  >;
  characterInfoPanel: PanelState | undefined;
  minimapPanel: PanelState | undefined;
  commandHistoryPanel: PanelState | undefined;
  commandInputPanel: PanelState | undefined;
  player: Player | null;
  derivedHealthStatus: HealthStatus | null;
  derivedLucidityStatus: LucidityStatus | null;
  room: Room | null;
  authToken: string;
  onMapClick?: () => void;
  commandHistory: string[];
  onClearHistory: () => void;
  onSelectCommand: (command: string) => void;
  onSendCommand: (command: string) => void;
  isConnected: boolean;
}

/** Character, minimap, command history/input (split out for Lizard max-lines-per-function). */
function renderCharacterInfoPanel(props: GameClientV2AuxiliaryPanelsProps): React.ReactNode {
  const { panelManager, characterInfoPanel, player, derivedHealthStatus, derivedLucidityStatus } = props;
  if (!characterInfoPanel || !characterInfoPanel.isVisible) return null;

  const characterPanelOutlineClassName = getCharacterPanelOutlineClassName(derivedHealthStatus, player);
  return (
    <PanelContainer
      id={characterInfoPanel.id}
      title={characterInfoPanel.title}
      position={characterInfoPanel.position}
      size={characterInfoPanel.size}
      zIndex={characterInfoPanel.zIndex}
      isMinimized={characterInfoPanel.isMinimized}
      isMaximized={characterInfoPanel.isMaximized}
      isVisible={characterInfoPanel.isVisible}
      minSize={characterInfoPanel.minSize}
      variant="default"
      className={characterPanelOutlineClassName}
      onPositionChange={panelManager.updatePosition}
      onSizeChange={panelManager.updateSize}
      onMinimize={panelManager.toggleMinimize}
      onMaximize={panelManager.toggleMaximize}
      onFocus={panelManager.focusPanel}
    >
      <CharacterInfoPanel player={player} healthStatus={derivedHealthStatus} lucidityStatus={derivedLucidityStatus} />
    </PanelContainer>
  );
}

function renderMinimapPanel(props: GameClientV2AuxiliaryPanelsProps): React.ReactNode {
  const { minimapPanel, room, authToken, onMapClick, panelManager } = props;
  if (!minimapPanel || !minimapPanel.isVisible) return null;

  return (
    <MinimapPanelSection
      minimapPanel={minimapPanel}
      room={room}
      authToken={authToken}
      onMapClick={onMapClick}
      updatePosition={panelManager.updatePosition}
      updateSize={panelManager.updateSize}
      toggleMinimize={panelManager.toggleMinimize}
      toggleMaximize={panelManager.toggleMaximize}
      focusPanel={panelManager.focusPanel}
    />
  );
}

function renderCommandHistoryPanel(props: GameClientV2AuxiliaryPanelsProps): React.ReactNode {
  const { commandHistoryPanel, panelManager, commandHistory, onClearHistory, onSelectCommand } = props;
  if (!commandHistoryPanel || !commandHistoryPanel.isVisible) return null;

  return (
    <PanelContainer
      id={commandHistoryPanel.id}
      title={commandHistoryPanel.title}
      position={commandHistoryPanel.position}
      size={commandHistoryPanel.size}
      zIndex={commandHistoryPanel.zIndex}
      isMinimized={commandHistoryPanel.isMinimized}
      isMaximized={commandHistoryPanel.isMaximized}
      isVisible={commandHistoryPanel.isVisible}
      minSize={commandHistoryPanel.minSize}
      variant="elevated"
      onPositionChange={panelManager.updatePosition}
      onSizeChange={panelManager.updateSize}
      onMinimize={panelManager.toggleMinimize}
      onMaximize={panelManager.toggleMaximize}
      onFocus={panelManager.focusPanel}
    >
      <CommandHistoryPanel
        commandHistory={commandHistory}
        onClearHistory={onClearHistory}
        onSelectCommand={onSelectCommand}
      />
    </PanelContainer>
  );
}

function renderCommandInputPanel(props: GameClientV2AuxiliaryPanelsProps): React.ReactNode {
  const { commandInputPanel, panelManager, onSendCommand, isConnected } = props;
  if (!commandInputPanel || !commandInputPanel.isVisible) return null;

  return (
    <PanelContainer
      id={commandInputPanel.id}
      title={commandInputPanel.title}
      position={commandInputPanel.position}
      size={commandInputPanel.size}
      zIndex={commandInputPanel.zIndex}
      isMinimized={commandInputPanel.isMinimized}
      isMaximized={commandInputPanel.isMaximized}
      isVisible={commandInputPanel.isVisible}
      minSize={commandInputPanel.minSize}
      variant="elevated"
      onPositionChange={panelManager.updatePosition}
      onSizeChange={panelManager.updateSize}
      onMinimize={panelManager.toggleMinimize}
      onMaximize={panelManager.toggleMaximize}
      onFocus={panelManager.focusPanel}
    >
      <CommandInputPanel onSendCommand={onSendCommand} disabled={!isConnected} isConnected={isConnected} />
    </PanelContainer>
  );
}

export const GameClientV2AuxiliaryPanels: React.FC<GameClientV2AuxiliaryPanelsProps> = props => (
  <>
    {renderCharacterInfoPanel(props)}
    {renderMinimapPanel(props)}
    {renderCommandHistoryPanel(props)}
    {renderCommandInputPanel(props)}
  </>
);
