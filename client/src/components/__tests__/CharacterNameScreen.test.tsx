import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { CharacterNameScreen } from '../CharacterNameScreen';
import type { Profession } from '../ProfessionCard';

const stats = {
  strength: 50,
  dexterity: 50,
  constitution: 50,
  size: 50,
  intelligence: 50,
  power: 50,
  education: 50,
  charisma: 50,
  luck: 50,
};

const profession: Profession = {
  id: 1,
  name: 'Antiquarian',
  description: 'Collector of strange things.',
  flavor_text: null,
  stat_requirements: [],
  mechanical_effects: [],
  is_available: true,
};

const SKIP_LABEL = /Skip the First Exposure tutorial/i;

function jsonResponse(body: unknown, ok = true): Response {
  return { ok, json: () => Promise.resolve(body) } as unknown as Response;
}

/** Fetch mock: `eligibility` answers the skip check; create-character always succeeds. */
function mockFetch(eligibility: () => Promise<Response>) {
  return vi.spyOn(global, 'fetch').mockImplementation((input: string | URL | Request) => {
    const url = String(input);
    if (url.includes('/players/characters/tutorial-skip')) return eligibility();
    if (url.includes('/players/create-character')) return Promise.resolve(jsonResponse({ player: {} }));
    return Promise.reject(new Error(`Unexpected URL ${url}`));
  });
}

function renderScreen() {
  const onComplete = vi.fn();
  render(
    <CharacterNameScreen
      stats={stats}
      profession={profession}
      skillsPayload={{ occupation_slots: [], personal_interest: [] }}
      baseUrl="http://test"
      authToken="token"
      onComplete={onComplete}
      onError={vi.fn()}
      onBack={vi.fn()}
    />
  );
  return { onComplete };
}

function createdBody(fetchSpy: ReturnType<typeof mockFetch>): Record<string, unknown> {
  const call = fetchSpy.mock.calls.find(([input]) => String(input).includes('/players/create-character'));
  expect(call).toBeDefined();
  const init = call?.[1];
  return JSON.parse(String(init?.body)) as Record<string, unknown>;
}

async function submitName(onComplete: ReturnType<typeof vi.fn>) {
  fireEvent.change(screen.getByLabelText('Character name'), { target: { value: 'Newcomer' } });
  fireEvent.click(screen.getByRole('button', { name: 'Create Character' }));
  await waitFor(() => {
    expect(onComplete).toHaveBeenCalled();
  });
}

describe('CharacterNameScreen: skipping First Exposure (#1081)', () => {
  let fetchSpy: ReturnType<typeof mockFetch>;

  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    fetchSpy.mockRestore();
  });

  it('offers no skip to an account that has not finished the tutorial, and takes the tutorial', async () => {
    fetchSpy = mockFetch(() => Promise.resolve(jsonResponse({ eligible: false })));
    const { onComplete } = renderScreen();

    await submitName(onComplete);

    expect(screen.queryByLabelText(SKIP_LABEL)).not.toBeInTheDocument();
    expect(createdBody(fetchSpy).start_in_tutorial).toBe(true);
  });

  it('offers the skip to an eligible account and sends it when ticked', async () => {
    fetchSpy = mockFetch(() => Promise.resolve(jsonResponse({ eligible: true })));
    const { onComplete } = renderScreen();

    const skip = await screen.findByLabelText(SKIP_LABEL);
    fireEvent.click(skip);
    await submitName(onComplete);

    expect(createdBody(fetchSpy).start_in_tutorial).toBe(false);
  });

  it('still takes the tutorial when an eligible account leaves the box unticked', async () => {
    fetchSpy = mockFetch(() => Promise.resolve(jsonResponse({ eligible: true })));
    const { onComplete } = renderScreen();

    await screen.findByLabelText(SKIP_LABEL);
    await submitName(onComplete);

    expect(createdBody(fetchSpy).start_in_tutorial).toBe(true);
  });

  it('hides the option when the eligibility check fails', async () => {
    fetchSpy = mockFetch(() => Promise.reject(new Error('network down')));
    const { onComplete } = renderScreen();

    await submitName(onComplete);

    expect(screen.queryByLabelText(SKIP_LABEL)).not.toBeInTheDocument();
    expect(createdBody(fetchSpy).start_in_tutorial).toBe(true);
  });
});
