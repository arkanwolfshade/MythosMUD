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

export const GameClientV2ContainerView: React.FC<GameClientV2ContainerViewProps> = props => {
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
      const room = gameState.room;
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
      setActiveTab(`map-${room.id}`);
    } else {
      setShowMap(true);
    }
  };

  const handleMainMenuMapClick = () => {
    if (gameState.room) {
      addTab({
        id: `map-${gameState.room.id}`,
        label: 'Map',
        content: (
          <MapView
            isOpen={true}
            onClose={() => closeTab(`map-${gameState.room?.id ?? ''}`)}
            currentRoom={gameState.room}
            authToken={authToken}
            hideHeader={true}
          />
        ),
        closable: true,
      });
    }
  };

  const declineFollow = () => {
    const reqId = gameState.pendingFollowRequest!.request_id;
    setClearedFollowRequestId(reqId);
    setGameState(prev => ({ ...prev, pendingFollowRequest: null }));
    clearPendingFollowRequest(reqId);
    sendMessage('follow_response', { request_id: reqId, accept: false });
  };
  const acceptFollow = () => {
    const reqId = gameState.pendingFollowRequest!.request_id;
    setClearedFollowRequestId(reqId);
    setGameState(prev => ({ ...prev, pendingFollowRequest: null }));
    clearPendingFollowRequest(reqId);
    sendMessage('follow_response', { request_id: reqId, accept: true });
  };
  const declineParty = () => {
    const inviteId = gameState.pendingPartyInvite!.invite_id;
    setClearedPartyInviteId(inviteId);
    setGameState(prev => ({ ...prev, pendingPartyInvite: null }));
    sendMessage('party_invite_response', { invite_id: inviteId, accept: false });
  };
  const acceptParty = () => {
    const inviteId = gameState.pendingPartyInvite!.invite_id;
    setClearedPartyInviteId(inviteId);
    setGameState(prev => ({ ...prev, pendingPartyInvite: null }));
    sendMessage('party_invite_response', { invite_id: inviteId, accept: true });
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
        <ModalContainer
          isOpen={true}
          onClose={declineFollow}
          title="Follow request"
          maxWidth="sm"
          showCloseButton={true}
          overlayZIndex={10000}
          position="center-no-backdrop"
          contentClassName="!bg-black border-2 border-mythos-terminal-primary shadow-2xl"
        >
          <div className="p-4 space-y-4">
            <p className="text-mythos-terminal-text font-medium">
              {gameState.pendingFollowRequest.requestor_name} wants to follow you.
            </p>
            <div className="flex gap-3 justify-end">
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                  text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={declineFollow}
              >
                Decline
              </button>
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                  text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={acceptFollow}
              >
                Accept
              </button>
            </div>
          </div>
        </ModalContainer>
      )}

      {showPartyModal && gameState.pendingPartyInvite && (
        <ModalContainer
          isOpen={true}
          onClose={declineParty}
          title="Party invite"
          maxWidth="sm"
          showCloseButton={true}
          overlayZIndex={10000}
          position="center-no-backdrop"
          contentClassName="!bg-black border-2 border-mythos-terminal-primary shadow-2xl"
        >
          <div className="p-4 space-y-4">
            <p className="text-mythos-terminal-text font-medium">
              {gameState.pendingPartyInvite.inviter_name} has invited you to join their party.
            </p>
            <div className="flex gap-3 justify-end">
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                    text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={declineParty}
              >
                Decline
              </button>
              <button
                type="button"
                className="px-3 py-1.5 rounded border border-mythos-terminal-border bg-mythos-terminal-surface
                    text-mythos-terminal-text hover:bg-mythos-terminal-border/30 font-medium"
                onClick={acceptParty}
              >
                Accept
              </button>
            </div>
          </div>
        </ModalContainer>
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
};
