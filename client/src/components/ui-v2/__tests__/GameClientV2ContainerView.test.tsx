import { fireEvent, render, screen } from '@testing-library/react';
import type { ReactNode } from 'react';
import { describe, expect, it, vi } from 'vitest';

import { GameClientV2ContainerView, type GameClientV2ContainerViewProps } from '../GameClientV2ContainerView';

vi.mock('../../utils/logger', () => ({
  logger: {
    downloadLogs: vi.fn(),
  },
}));

vi.mock('../GameClientV2', () => ({
  GameClientV2: ({ onMapClick }: { onMapClick: () => void }) => (
    <button onClick={onMapClick} type="button">
      OpenMap
    </button>
  ),
}));

vi.mock('../MainMenuModal', () => ({
  MainMenuModal: ({ onMapClick }: { onMapClick: () => void }) => (
    <button onClick={onMapClick} type="button">
      OpenMenuMap
    </button>
  ),
}));

vi.mock('../MapView', () => ({
  MapView: ({ isOpen }: { isOpen: boolean }) => (isOpen ? <div>MapOpen</div> : null),
}));

vi.mock('../DeathInterstitial', () => ({
  DeathInterstitial: () => null,
}));

vi.mock('../DeliriumInterstitial', () => ({
  DeliriumInterstitial: () => null,
}));

vi.mock('../ui/ModalContainer', () => ({
  ModalContainer: ({ children }: { children: ReactNode }) => <div>{children}</div>,
}));

vi.mock('../components/TabbedInterfaceOverlay', () => ({
  TabbedInterfaceOverlay: () => null,
}));

function makeProps(): GameClientV2ContainerViewProps {
  return {
    playerName: 'Test',
    authToken: 'token',
    isLoggingOut: false,
    gameState: {
      player: { id: 'p1', name: 'Player' },
      room: { id: 'room-1', plane: 'Prime', zone: 'Arkham', sub_zone: 'Docks' },
      messages: [],
      commandHistory: [],
      mythosTime: null,
      followingTarget: null,
      questLog: [],
      pendingFollowRequest: { request_id: 'follow-1', requestor_name: 'Cultist' },
      pendingPartyInvite: { invite_id: 'invite-1', inviter_name: 'Scholar' },
    },
    mythosTime: null,
    healthStatus: null,
    lucidityStatus: null,
    isMortallyWounded: false,
    isDead: false,
    deathLocation: '',
    isRespawning: false,
    isDelirious: false,
    deliriumLocation: '',
    isDeliriumRespawning: false,
    isMainMenuOpen: false,
    setIsMainMenuOpen: vi.fn(),
    showMap: false,
    setShowMap: vi.fn(),
    tabs: [],
    activeTabId: null,
    addTab: vi.fn(),
    closeTab: vi.fn(),
    setActiveTab: vi.fn(),
    clearedFollowRequestId: null,
    setClearedFollowRequestId: vi.fn(),
    clearedPartyInviteId: null,
    setClearedPartyInviteId: vi.fn(),
    setGameState: vi.fn(),
    clearPendingFollowRequest: vi.fn(),
    sendMessage: vi.fn(),
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    handleLogout: vi.fn(),
    handleCommandSubmit: vi.fn(),
    handleChatMessage: vi.fn(),
    handleClearMessages: vi.fn(),
    handleClearHistory: vi.fn(),
    handleRespawn: vi.fn(),
    handleDeliriumRespawn: vi.fn(),
    activeEffects: [],
  } as unknown as GameClientV2ContainerViewProps;
}

describe('GameClientV2ContainerView', () => {
  it('opens map in a tab when GameClientV2 requests map and room is available', () => {
    const props = makeProps();
    render(<GameClientV2ContainerView {...props} />);

    fireEvent.click(screen.getByRole('button', { name: 'OpenMap' }));

    expect(props.setShowMap).toHaveBeenCalledWith(true);
  });

  it('sends follow response from modal actions', () => {
    const props = makeProps();
    render(<GameClientV2ContainerView {...props} />);

    const accepts = screen.getAllByRole('button', { name: 'Accept' });
    const declines = screen.getAllByRole('button', { name: 'Decline' });
    fireEvent.click(accepts[0]);
    fireEvent.click(declines[0]);

    expect(props.sendMessage).toHaveBeenCalledWith('follow_response', { request_id: 'follow-1', accept: true });
    expect(props.sendMessage).toHaveBeenCalledWith('follow_response', { request_id: 'follow-1', accept: false });
  });
});
