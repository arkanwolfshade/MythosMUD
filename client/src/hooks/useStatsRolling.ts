/**
 * useStatsRolling: fetches and rerolls character stats for the stats-rolling screen.
 */

import { useCallback, useEffect, useState } from 'react';
import type { Profession } from '../components/ProfessionCard.tsx';
import { performStatsRoll, useRerollCooldownTimer } from './useStatsRollingActions';

export interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  size: number;
  intelligence: number;
  power: number;
  education: number;
  charisma: number;
  luck: number;
}

export interface UseStatsRollingOptions {
  baseUrl: string;
  authToken: string;
  professionId?: number;
  profession?: Profession | null;
  onError?: (error: string) => void;
  rollOnMount?: boolean;
}

export interface UseStatsRollingResult {
  currentStats: Stats | null;
  isLoading: boolean;
  isRerolling: boolean;
  error: string;
  rerollCooldown: number;
  timeoutMessage: string;
  rollStats: () => Promise<void>;
  rerollStats: () => Promise<void>;
  setError: (error: string) => void;
}

export function useStatsRolling(options: UseStatsRollingOptions): UseStatsRollingResult {
  const { baseUrl, authToken, professionId, profession, onError, rollOnMount = true } = options;
  const [currentStats, setCurrentStats] = useState<Stats | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isRerolling, setIsRerolling] = useState(false);
  const [rerollCooldown, setRerollCooldown] = useState(0);
  const [error, setErrorState] = useState('');
  const [timeoutMessage, setTimeoutMessage] = useState('');

  const performRoll = useCallback(
    async (isReroll: boolean) =>
      performStatsRoll({
        isReroll,
        baseUrl,
        authToken,
        professionId,
        profession,
        onError,
        setCurrentStats,
        setIsLoading,
        setIsRerolling,
        setRerollCooldown,
        setErrorState,
        setTimeoutMessage,
      }),
    [authToken, baseUrl, professionId, profession, onError]
  );

  const rollStats = useCallback(() => performRoll(false), [performRoll]);
  const rerollStats = useCallback(() => performRoll(true), [performRoll]);

  useEffect(() => {
    if (rollOnMount && authToken) void rollStats();
  }, [authToken, rollStats, professionId, rollOnMount]);

  useRerollCooldownTimer(rerollCooldown, setRerollCooldown);

  return {
    currentStats,
    isLoading,
    isRerolling,
    error,
    rerollCooldown,
    timeoutMessage,
    rollStats,
    rerollStats,
    setError: setErrorState,
  };
}
