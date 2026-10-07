import React, { useCallback, useState } from 'react';

import { ContainerApiError, openContainer } from '../../api/containers';
import { logger } from '../../utils/logger';
import { DeathInterstitial } from '../DeathInterstitial';
import { DeliriumInterstitial } from '../DeliriumInterstitial';
import { MainMenuModal } from '../MainMenuModal';
import { MapView } from '../MapView';
import { ContainerTransferModals } from './containers/ContainerTransferModal';
import { CorpseOverlay } from './containers/CorpseOverlay';
import { GameClientV2 } from './GameClientV2';
import { ModalContainer } from './primitives';
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

type PendingInviteModalsProps = Pick<
  GameClientV2ContainerViewProps,
  | 'clearedFollowRequestId'
  | 'setClearedFollowRequestId'
  | 'clearedPartyInviteId'
  | 'setClearedPartyInviteId'
  | 'sendMessage'
> & {
  pendingFollowRequest: GameClientV2ContainerViewProps['gameState']['pendingFollowRequest'];
  pendingPartyInvite: GameClientV2ContainerViewProps['gameState']['pendingPartyInvite'];
};

/**
 * The follow-request and party-invite prompts.
 *
 * clearedFollowRequestId/clearedPartyInviteId are UX-only local dismissal: the server never sends
 * a follow_request_cleared/party_invite_cleared event, so this state is not persisted across
 * reconnect (a stale pending request/invite will show its modal again after reconnect, which is
 * correct -- the server still considers it pending).
 */
function PendingInviteModals({
  pendingFollowRequest,
  pendingPartyInvite,
  clearedFollowRequestId,
  setClearedFollowRequestId,
  clearedPartyInviteId,
  setClearedPartyInviteId,
  sendMessage,
}: PendingInviteModalsProps) {
  const followRequest =
    pendingFollowRequest && clearedFollowRequestId !== pendingFollowRequest.request_id ? pendingFollowRequest : null;
  const partyInvite =
    pendingPartyInvite && clearedPartyInviteId !== pendingPartyInvite.invite_id ? pendingPartyInvite : null;

  const respondToFollow = (requestId: string, accept: boolean) => {
    setClearedFollowRequestId(requestId);
    sendMessage('follow_response', { request_id: requestId, accept });
  };
  const respondToParty = (inviteId: string, accept: boolean) => {
    setClearedPartyInviteId(inviteId);
    sendMessage('party_invite_response', { invite_id: inviteId, accept });
  };

  return (
    <>
      {followRequest && (
        <InviteModal
          title="Follow request"
          message={`${followRequest.requestor_name} wants to follow you.`}
          onDecline={() => respondToFollow(followRequest.request_id, false)}
          onAccept={() => respondToFollow(followRequest.request_id, true)}
        />
      )}
      {partyInvite && (
        <InviteModal
          title="Party invite"
          message={`${partyInvite.inviter_name} has invited you to join their party.`}
          onDecline={() => respondToParty(partyInvite.invite_id, false)}
          onAccept={() => respondToParty(partyInvite.invite_id, true)}
        />
      )}
    </>
  );
}

/** Opening a room container, and the error to show when the server refuses. */
function useOpenContainer(authToken: string) {
  const [containerOpenError, setContainerOpenError] = useState<string | null>(null);
  const handleOpenContainer = useCallback(
    (containerId: string) => {
      setContainerOpenError(null);
      openContainer(authToken, containerId).catch(e => {
        setContainerOpenError(e instanceof ContainerApiError ? e.message : 'Could not open that container.');
      });
    },
    [authToken]
  );
  const dismissContainerOpenError = useCallback(() => setContainerOpenError(null), []);
  return { containerOpenError, handleOpenContainer, dismissContainerOpenError };
}

function ContainerOpenErrorAlert({ message, onDismiss }: { message: string | null; onDismiss: () => void }) {
  if (!message) return null;
  return (
    <div
      role="alert"
      className="fixed bottom-4 left-4 z-[10000] max-w-sm rounded border border-mythos-terminal-error bg-mythos-terminal-background p-3 text-sm text-mythos-terminal-error shadow-xl"
    >
      {message}
      <button type="button" className="ml-2 underline" onClick={onDismiss} aria-label="Dismiss">
        Dismiss
      </button>
    </div>
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

  const { containerOpenError, handleOpenContainer, dismissContainerOpenError } = useOpenContainer(authToken);

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

  const containerClass = `game-terminal-container ${isDead ? 'dead' : ''}`;
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
          rescueStatus={gameState.rescueStatus ?? null}
          activeEffects={activeEffects}
          followingTarget={gameState.followingTarget ?? null}
          questLog={gameState.questLog ?? []}
          onSendCommand={handleCommandSubmit}
          onSendChatMessage={handleChatMessage}
          onClearMessages={handleClearMessages}
          onClearHistory={handleClearHistory}
          onDownloadLogs={() => logger.downloadLogs()}
          onMapClick={handleMapClickFromGame}
          playerInventory={gameState.playerInventory}
          playerEquipped={gameState.playerEquipped}
          roomContainers={gameState.roomContainers}
          onOpenContainer={handleOpenContainer}
        />
      )}

      <ContainerTransferModals
        openContainers={gameState.openContainers}
        playerInventory={gameState.playerInventory}
        authToken={authToken}
        onClose={() => {}}
      />
      <CorpseOverlay
        roomContainers={gameState.roomContainers}
        playerId={gameState.player?.id}
        onOpen={handleOpenContainer}
      />
      <ContainerOpenErrorAlert message={containerOpenError} onDismiss={dismissContainerOpenError} />

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

      <PendingInviteModals
        pendingFollowRequest={gameState.pendingFollowRequest}
        pendingPartyInvite={gameState.pendingPartyInvite}
        clearedFollowRequestId={clearedFollowRequestId}
        setClearedFollowRequestId={setClearedFollowRequestId}
        clearedPartyInviteId={clearedPartyInviteId}
        setClearedPartyInviteId={setClearedPartyInviteId}
        sendMessage={sendMessage}
      />

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
