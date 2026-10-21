/**
 * Tests for QuestLogPanel: a goal reads as its authored description, falling back to its target (#1102).
 */

import '@testing-library/jest-dom/vitest';
import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import type { QuestLogEntry } from '../../types';
import { QuestLogPanel } from '../QuestLogPanel';

const entry = (goals: QuestLogEntry['goals_with_progress']): QuestLogEntry => ({
  quest_id: 'first_exposure_dusk',
  name: 'first_exposure_dusk',
  title: 'Dusk',
  description: 'Find your feet.',
  goals_with_progress: goals,
  state: 'active',
});

describe('QuestLogPanel goals', () => {
  it('shows the authored description instead of the raw target', () => {
    render(
      <QuestLogPanel
        questLog={[entry([{ target: 'cmd_talk', description: 'Speak with the lamplighter', current: 0, required: 1 }])]}
      />
    );

    expect(screen.getByText('Speak with the lamplighter: 0/1')).toBeInTheDocument();
    expect(screen.queryByText(/cmd_talk/)).not.toBeInTheDocument();
  });

  it('falls back to the target when a goal has no description', () => {
    render(<QuestLogPanel questLog={[entry([{ target: 'cmd_talk', current: 0, required: 1 }])]} />);

    expect(screen.getByText('cmd_talk: 0/1')).toBeInTheDocument();
  });

  it('treats an empty description as none', () => {
    render(<QuestLogPanel questLog={[entry([{ target: 'cmd_look', description: '', current: 0, required: 1 }])]} />);

    expect(screen.getByText('cmd_look: 0/1')).toBeInTheDocument();
  });

  it('marks a finished goal done under its description', () => {
    render(
      <QuestLogPanel
        questLog={[entry([{ target: 'cmd_look', description: 'Look around', current: 1, required: 1, done: true }])]}
      />
    );

    expect(screen.getByText('Look around: done')).toBeInTheDocument();
  });
});
