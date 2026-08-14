import React from 'react';

import { logger } from '../../utils/logger';
import { DeathInterstitial } from '../DeathInterstitial';
import { DeliriumInterstitial } from '../DeliriumInterstitial';
import { MainMenuModal } from '../MainMenuModal';
import { MapView } from '../MapView';
import { ModalContainer } from '../ui/ModalContainer';
import { GameClientV2 } from './GameClientV2';
import { TabbedInterfaceOverlay } from './components/TabbedInterfaceOverlay';
import type { useGameClientV2Container } from './hooks/useGameClientV2Container';

export type GameClientV2ContainerViewProps = ReturnType<typeof useGameClientV2Container>;

function openMapTab(
  room: NonNullable<GameClientV2ContainerViewProps['gameState']['room']>,
  authToken: string,
  addTab: GameClientV2ContainerViewProps['addTab'],
  closeTab: GameClientV2ContainerViewProps['closeTab']
) {
  addTab({
    id: `map-${room.id}`,
    label: 'Map',
    content: (
      <MapView
        isOpen={true}
        onClose={() => closeTab(`map-${room.id}`)}
        currentRoom={room}
        authToken={authToken}
        hideHeader={true}
      />
    ),
    closable: true,
  });
}

function InviteModal({
  title,
  message,
  onDecline,
  onAccept,
}: {
  title: string;
  message: string;
  onDecline: () => void;
  onAccept: () => void;
}) {
  return (
    <ModalContainer
      isOpen={true}
      onClose={onDecline}
      title={title}
      maxWidth="sm"
      showCloseButton={true}
      overlayZIndex={10000}
      position="center-no-backdrop"
      contentClassName="!bg-black border-2 border-mythos-terminal-primary shadow-2xl"
    >
      <div className="p-4 space-y-4">
        <p className="text-mythos-terminal-text font-medium">{message}</p>
        <div className="flex gap-3 justify-end">
          <button
            type="button"
            className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
            onClick={onDecline}
          >
            Decline
          </button>
          <button
            type="button"
            className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
            onClick={onAccept}
          >
            Accept
          </button>
        </div>
      </div>
    </ModalContainer>
  );
}

function GameClientV2ContainerLayout(props: GameClientV2ContainerViewProps) {
  const {
    playerName,
    authToken,
    isLoggingOut,
    gameState,
    mythosTime,
    healthStatus,
    lucidityStatus,
    isMortallyWounded,
    isDead,
    deathLocation,
    isRespawning,
    isDelirious,
    deliriumLocation,
    isDeliriumRespawning,
    isMainMenuOpen,
    setIsMainMenuOpen,
    showMap,
    setShowMap,
    tabs,
    activeTabId,
    addTab,
    closeTab,
    setActiveTab,
    clearedFollowRequestId,
    setClearedFollowRequestId,
    clearedPartyInviteId,
    setClearedPartyInviteId,
    setGameState,
    clearPendingFollowRequest,
    sendMessage,
    isConnected,
    isConnecting,
    error,
    reconnectAttempts,
    handleLogout,
    handleCommandSubmit,
    handleChatMessage,
    handleClearMessages,
    handleClearHistory,
    handleRespawn,
    handleDeliriumRespawn,
    activeEffects,
  } = props;

  const handleMapClickFromGame = () => {
    if (tabs.length > 0 && gameState.room?.id) {
      openMapTab(gameState.room, authToken, addTab, closeTab);
      setActiveTab(`map-${gameState.room.id}`);
      return;
    }
    setShowMap(true);
  };

  const handleMainMenuMapClick = () => {
    if (gameState.room) openMapTab(gameState.room, authToken, addTab, closeTab);
  };

  const respondToFollow = (accept: boolean) => {
    const reqId = gameState.pendingFollowRequest!.request_id;
    setClearedFollowRequestId(reqId);
    setGameState(prev => ({ ...prev, pendingFollowRequest: null }));
    clearPendingFollowRequest(reqId);
    sendMessage('follow_response', { request_id: reqId, accept });
  };

  const respondToParty = (accept: boolean) => {
    const inviteId = gameState.pendingPartyInvite!.invite_id;
    setClearedPartyInviteId(inviteId);
    setGameState(prev => ({ ...prev, pendingPartyInvite: null }));
    sendMessage('party_invite_response', { invite_id: inviteId, accept });
  };

  const showFollowModal = Boolean(
    gameState.pendingFollowRequest && clearedFollowRequestId !== gameState.pendingFollowRequest.request_id
  );
  const showPartyModal = Boolean(
    gameState.pendingPartyInvite && clearedPartyInviteId !== gameState.pendingPartyInvite.invite_id
  );
  const containerClass = `game-terminal-container ${isMortallyWounded ? 'mortally-wounded' : ''} ${isDead ? 'dead' : ''}`;
  const currentRoomForMenu =
    gameState.room == null
      ? null
      : {
          id: gameState.room.id,
          plane: gameState.room.plane,
          zone: gameState.room.zone,
          subZone: gameState.room.sub_zone,
        };

  return (
    <div className={containerClass} data-game-container>
      {tabs.length === 0 && (
        <GameClientV2
          playerName={playerName}
          authToken={authToken}
          onLogout={handleLogout}
          isLoggingOut={isLoggingOut}
          player={gameState.player}
          room={gameState.room}
          messages={gameState.messages}
          commandHistory={gameState.commandHistory}
          isConnected={isConnected}
          isConnecting={isConnecting}
          error={error}
          reconnectAttempts={reconnectAttempts}
          mythosTime={gameState.mythosTime ?? mythosTime}
          healthStatus={healthStatus}
          lucidityStatus={lucidityStatus}
          activeEffects={activeEffects}
          followingTarget={gameState.followingTarget ?? null}
          questLog={gameState.questLog ?? []}
          onSendCommand={handleCommandSubmit}
          onSendChatMessage={handleChatMessage}
          onClearMessages={handleClearMessages}
          onClearHistory={handleClearHistory}
          onDownloadLogs={() => logger.downloadLogs()}
          onMapClick={handleMapClickFromGame}
        />
      )}

      <DeathInterstitial
        isVisible={isDead}
        deathLocation={deathLocation}
        onRespawn={handleRespawn}
        isRespawning={isRespawning}
      />
      <DeliriumInterstitial
        isVisible={isDelirious}
        deliriumLocation={deliriumLocation}
        onRespawn={handleDeliriumRespawn}
        isRespawning={isDeliriumRespawning}
      />

      {showFollowModal && gameState.pendingFollowRequest && (
        <InviteModal
          title="Follow request"
          message={`${gameState.pendingFollowRequest.requestor_name} wants to follow you.`}
          onDecline={() => respondToFollow(false)}
          onAccept={() => respondToFollow(true)}
        />
      )}

      {showPartyModal && gameState.pendingPartyInvite && (
        <InviteModal
          title="Party invite"
          message={`${gameState.pendingPartyInvite.inviter_name} has invited you to join their party.`}
          onDecline={() => respondToParty(false)}
          onAccept={() => respondToParty(true)}
        />
      )}

      <MainMenuModal
        isOpen={isMainMenuOpen}
        onClose={() => setIsMainMenuOpen(false)}
        onMapClick={handleMainMenuMapClick}
        onLogoutClick={handleLogout}
        currentRoom={currentRoomForMenu}
        openMapInNewTab={false}
        playerId={gameState.player?.id ?? null}
      />

      <TabbedInterfaceOverlay tabs={tabs} activeTabId={activeTabId} setActiveTab={setActiveTab} closeTab={closeTab} />

      <MapView
        isOpen={showMap && tabs.length === 0}
        onClose={() => setShowMap(false)}
        currentRoom={gameState.room}
        authToken={authToken}
      />
    </div>
  );
}

export const GameClientV2ContainerView: React.FC<GameClientV2ContainerViewProps> = props => (
  <GameClientV2ContainerLayout {...props} />
);
