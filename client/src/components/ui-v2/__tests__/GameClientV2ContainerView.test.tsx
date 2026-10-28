import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import type { ReactNode } from 'react';
import { describe, expect, it, vi } from 'vitest';

import { ContainerApiError } from '../../../api/containers';
import { GameClientV2ContainerView, type GameClientV2ContainerViewProps } from '../GameClientV2ContainerView';

vi.mock('../../utils/logger', () => ({
  logger: {
    downloadLogs: vi.fn(),
  },
}));

const openContainer = vi.hoisted(() => vi.fn());
vi.mock('../../../api/containers', async importOriginal => ({
  ...(await importOriginal<typeof import('../../../api/containers')>()),
  openContainer,
}));

vi.mock('../GameClientV2', () => ({
  GameClientV2: ({
    onMapClick,
    onOpenContainer,
  }: {
    onMapClick: () => void;
    onOpenContainer: (containerId: string) => void;
  }) => (
    <>
      <button onClick={onMapClick} type="button">
        OpenMap
      </button>
      <button onClick={() => onOpenContainer('chest-1')} type="button">
        OpenChest
      </button>
    </>
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

vi.mock('../primitives/ModalContainer', () => ({
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

  it('sends party invite responses from the second modal and dismisses it locally', () => {
    const props = makeProps();
    render(<GameClientV2ContainerView {...props} />);

    fireEvent.click(screen.getAllByRole('button', { name: 'Accept' })[1]);
    fireEvent.click(screen.getAllByRole('button', { name: 'Decline' })[1]);

    expect(props.sendMessage).toHaveBeenCalledWith('party_invite_response', { invite_id: 'invite-1', accept: true });
    expect(props.sendMessage).toHaveBeenCalledWith('party_invite_response', { invite_id: 'invite-1', accept: false });
    expect(props.setClearedPartyInviteId).toHaveBeenCalledWith('invite-1');
  });

  it('hides a request or invite the player already dismissed', () => {
    const props = { ...makeProps(), clearedFollowRequestId: 'follow-1', clearedPartyInviteId: 'invite-1' };
    render(<GameClientV2ContainerView {...props} />);

    expect(screen.queryByRole('button', { name: 'Accept' })).toBeNull();
  });

  it('shows the server refusal when a container will not open, and dismisses it', async () => {
    openContainer.mockRejectedValueOnce(new ContainerApiError('The chest is locked.', 403));
    render(<GameClientV2ContainerView {...makeProps()} />);

    fireEvent.click(screen.getByRole('button', { name: 'OpenChest' }));

    expect(await screen.findByRole('alert')).toHaveTextContent('The chest is locked.');
    expect(openContainer).toHaveBeenCalledWith('token', 'chest-1');
    fireEvent.click(screen.getByRole('button', { name: 'Dismiss' }));
    await waitFor(() => expect(screen.queryByRole('alert')).toBeNull());
  });

  it('falls back to a generic message for an unexpected container error', async () => {
    openContainer.mockRejectedValueOnce(new Error('network down'));
    render(<GameClientV2ContainerView {...makeProps()} />);

    fireEvent.click(screen.getByRole('button', { name: 'OpenChest' }));

    expect(await screen.findByRole('alert')).toHaveTextContent('Could not open that container.');
  });
});
