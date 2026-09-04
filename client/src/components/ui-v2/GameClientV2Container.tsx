import React from 'react';

import { GameClientV2ContainerView } from './GameClientV2ContainerView';
import type { GameClientV2ContainerProps } from './hooks/useGameClientV2Container';
import { useGameClientV2Container } from './hooks/useGameClientV2Container';

// Container component that manages game state and renders GameClientV2
// Based on findings from "State Management Patterns" - Dr. Armitage, 1928
// Logic lives in useGameClientV2Container and GameClientV2ContainerView to keep cyclomatic complexity under limit.
export const GameClientV2Container: React.FC<GameClientV2ContainerProps> = props => {
  const state = useGameClientV2Container(props);
  return <GameClientV2ContainerView {...state} />;
};
