import React from 'react';
import { useGameTerminal } from '../hooks/useGameTerminal';
import { GameTerminalPresentation } from './GameTerminalPresentation';

/**
 * Container component for GameTerminal.
 * This component handles all the business logic and state management,
 * while delegating the presentation to the GameTerminalPresentation component.
 *
 * This follows the Container/Presentational pattern, separating concerns
 * between data management and UI rendering.
 */
export const GameTerminalContainer: React.FC = () => {
  const gameTerminalState = useGameTerminal();

  return <GameTerminalPresentation {...gameTerminalState} />;
};
