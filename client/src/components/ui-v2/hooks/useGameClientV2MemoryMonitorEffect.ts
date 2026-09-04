// Memory monitor effect for GameClientV2Container.

import { useEffect } from 'react';

import { useMemoryMonitor } from '../../../utils/memoryMonitor';

export function useGameClientV2MemoryMonitorEffect(): void {
  const { detector } = useMemoryMonitor('GameClientV2Container');

  useEffect(() => {
    detector.start();
    return () => detector.stop();
  }, [detector]);
}
