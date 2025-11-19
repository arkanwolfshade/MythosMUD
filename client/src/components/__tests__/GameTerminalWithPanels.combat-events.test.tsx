/**
 * @jest-environment jsdom
 */

import '@testing-library/jest-dom';
import { render, screen, waitFor, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import { useGameConnection } from '../../hooks/useGameConnectionRefactored';
import { GameTerminalWithPanels } from '../GameTerminalWithPanels';

vi.mock('../../hooks/useGameConnectionRefactored');
const mockUseGameConnection = vi.mocked(useGameConnection);

vi.mock('../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
    debug: vi.fn(),
  },
}));

type MockGameEvent = {
  event_type: string;
  timestamp: string;
  sequence_number: number;
  data: Record<string, unknown>;
};

describe('GameTerminalWithPanels - Combat Events', () => {
  const defaultPlayerName = 'ArkanWolfshade';
  let eventCallback: ((event: MockGameEvent) => void) | null;

  const triggerEvent = (event: MockGameEvent) => {
    if (!eventCallback) {
      throw new Error('Event callback not registered');
    }
    eventCallback(event);
  };

  const renderTerminal = (playerName = defaultPlayerName) =>
    render(<GameTerminalWithPanels playerName={playerName} authToken="test-token" />);

  const findMessageContainer = (text: string) => {
    const messageContainers = screen.queryAllByTestId('chat-message');
    return messageContainers.find(container => within(container).queryByText(text));
  };

  const sendStatusUpdate = (playerName: string, options: { inCombat?: 'Yes' | 'No'; health?: string } = {}) => {
    const { inCombat = 'No', health = '100/100' } = options;
    const statusLines = [
      `Name: ${playerName}`,
      'Location: Arkham Sanitarium',
      `Health: ${health}`,
      'Sanity: 100/100',
      `In Combat: ${inCombat}`,
    ];

    triggerEvent({
      event_type: 'command_response',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        result: statusLines.join('\n'),
        is_html: false,
      },
    });
  };

  const getInfoValue = (label: string): HTMLElement => {
    // Special handling for Health - it's rendered by HealthMeter component
    if (label === 'Health:') {
      const healthMeter = screen.getByTestId('health-meter');
      const strongTag = healthMeter.querySelector('strong');
      if (strongTag) {
        // Return the strong tag element for health value
        return strongTag as HTMLElement;
      }
      // Fallback: look for "Health" text and find the meter container
      const labelNode = screen.getByText('Health');
      const container = labelNode.closest('[data-testid="health-meter"]');
      if (container) {
        const fallbackStrongTag = container.querySelector('strong');
        if (fallbackStrongTag) {
          return fallbackStrongTag as HTMLElement;
        }
      }
      // If we can't find the health meter, throw a descriptive error
      throw new Error(`Unable to find health meter element for label: ${label}`);
    }

    // For other labels (like "In Combat:"), use standard logic
    const labelNode = screen.getByText(label);
    const container = labelNode.closest('div');
    if (!container) {
      throw new Error(`Unable to find container for label: ${label}`);
    }
    const spans = container.querySelectorAll('span');
    if (spans.length === 0) {
      throw new Error(`No span elements found in container for label: ${label}`);
    }
    return spans[spans.length - 1] as HTMLElement;
  };

  beforeEach(() => {
    vi.clearAllMocks();
    eventCallback = null;

    mockUseGameConnection.mockImplementation(({ onEvent }) => {
      if (onEvent) {
        eventCallback = onEvent;
      }
      return {
        isConnected: true,
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        connect: vi.fn(),
        disconnect: vi.fn(),
        sendCommand: vi.fn(),
      } as unknown as ReturnType<typeof useGameConnection>;
    });
  });

  afterEach(() => {
    vi.restoreAllMocks();
    eventCallback = null;
  });

  it('does not mark observers as in combat when combat starts elsewhere', async () => {
    renderTerminal();
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(defaultPlayerName);
    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('No'));

    triggerEvent({
      event_type: 'combat_started',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        combat_id: 'combat-001',
        room_id: 'room-001',
        turn_order: ['uuid-ithaqua'],
        participants: {
          'uuid-ithaqua': { name: 'Ithaqua' },
        },
      },
    });

    await waitFor(() => expect(screen.getByText(/Combat has begun!/)).toBeInTheDocument());
    expect(getInfoValue('In Combat:')).toHaveTextContent('No');
  });

  it('marks the current player as in combat when they are a participant', async () => {
    renderTerminal();
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(defaultPlayerName);
    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('No'));

    triggerEvent({
      event_type: 'combat_started',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        combat_id: 'combat-002',
        room_id: 'room-002',
        turn_order: ['player-uuid'],
        participants: {
          'player-uuid': { name: defaultPlayerName },
        },
      },
    });

    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('Yes'));
  });

  it('clears combat state when the matching combat ends', async () => {
    renderTerminal();
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(defaultPlayerName);
    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('No'));

    triggerEvent({
      event_type: 'combat_started',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        combat_id: 'combat-003',
        room_id: 'room-003',
        turn_order: ['player-uuid'],
        participants: {
          'player-uuid': { name: defaultPlayerName },
        },
      },
    });

    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('Yes'));

    triggerEvent({
      event_type: 'combat_ended',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        combat_id: 'combat-003',
        room_id: 'room-003',
        reason: 'combat resolved',
        duration_seconds: 0,
      },
    });

    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('No'));
  });

  it('applies npc attacks only to the targeted player', async () => {
    renderTerminal();
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(defaultPlayerName, { inCombat: 'Yes' });
    await waitFor(() => expect(getInfoValue('Health:')).toHaveTextContent(/^100/));

    triggerEvent({
      event_type: 'npc_attacked',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        attacker_name: 'Sanitarium Patient',
        npc_name: defaultPlayerName,
        action_type: 'auto_attack',
        damage: 10,
        target_current_hp: 90,
        target_max_hp: 100,
      },
    });

    await waitFor(() => {
      expect(findMessageContainer('Sanitarium Patient attacks you for 10 damage! (90/100 HP)')).toBeDefined();
    });
    expect(getInfoValue('Health:')).toHaveTextContent(/^90/);
  });

  it('shows npc attacks against other players without altering local health', async () => {
    const otherPlayer = 'Ithaqua';
    renderTerminal(otherPlayer);
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(otherPlayer, { inCombat: 'No' });
    await waitFor(() => expect(getInfoValue('Health:')).toHaveTextContent(/^100/));

    triggerEvent({
      event_type: 'npc_attacked',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        attacker_name: 'Sanitarium Patient',
        npc_name: defaultPlayerName,
        action_type: 'auto_attack',
        damage: 10,
        target_current_hp: 90,
        target_max_hp: 100,
      },
    });

    await waitFor(() => {
      expect(
        findMessageContainer('Sanitarium Patient attacks ArkanWolfshade for 10 damage! (90/100 HP)')
      ).toBeDefined();
    });
    expect(getInfoValue('Health:')).toHaveTextContent(/^100/);
  });

  it('displays participant names in turn order instead of UUIDs', async () => {
    renderTerminal();
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(defaultPlayerName);
    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('No'));

    const playerUuid = '9bcee4bf-43dc-4860-885a-1be5356b5a24';
    const npcUuid = 'd839d857-1601-45dc-ac16-0960e034a52e';

    triggerEvent({
      event_type: 'combat_started',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        combat_id: 'combat-004',
        room_id: 'room-004',
        turn_order: [playerUuid, npcUuid],
        participants: {
          [playerUuid]: { name: 'ArkanWolfshade', hp: 100, max_hp: 100 },
          [npcUuid]: { name: 'Sanitarium Patient', hp: 50, max_hp: 50 },
        },
      },
    });

    // Verify message contains participant names, not UUIDs
    await waitFor(() => {
      const combatMessage = screen.getByText(/Combat has begun!/);
      expect(combatMessage).toBeInTheDocument();
      expect(combatMessage.textContent).toContain('ArkanWolfshade');
      expect(combatMessage.textContent).toContain('Sanitarium Patient');
      expect(combatMessage.textContent).not.toContain(playerUuid);
      expect(combatMessage.textContent).not.toContain(npcUuid);
    });
  });

  it('falls back to UUID if participant name is missing', async () => {
    renderTerminal();
    expect(eventCallback).not.toBeNull();

    sendStatusUpdate(defaultPlayerName);
    await waitFor(() => expect(getInfoValue('In Combat:')).toHaveTextContent('No'));

    const playerUuid = '9bcee4bf-43dc-4860-885a-1be5356b5a24';
    const unknownUuid = 'unknown-uuid-12345';

    triggerEvent({
      event_type: 'combat_started',
      timestamp: new Date().toISOString(),
      sequence_number: Date.now(),
      data: {
        combat_id: 'combat-005',
        room_id: 'room-005',
        turn_order: [playerUuid, unknownUuid],
        participants: {
          [playerUuid]: { name: 'ArkanWolfshade', hp: 100, max_hp: 100 },
          // Missing participant entry for unknownUuid
        },
      },
    });

    // Verify message shows name for found participant, UUID for missing one
    await waitFor(() => {
      const combatMessage = screen.getByText(/Combat has begun!/);
      expect(combatMessage).toBeInTheDocument();
      expect(combatMessage.textContent).toContain('ArkanWolfshade');
      expect(combatMessage.textContent).toContain(unknownUuid);
    });
  });
});
