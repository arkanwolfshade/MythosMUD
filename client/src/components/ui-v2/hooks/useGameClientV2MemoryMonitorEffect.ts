// Memory monitor + container store subscriptions for GameClientV2Container.

import { useEffect } from 'react';

import { useContainerStore } from '../../../stores/containerStore';
import { useMemoryMonitor } from '../../../utils/memoryMonitor';

export function useGameClientV2MemoryMonitorEffect(): void {
  const { detector } = useMemoryMonitor('GameClientV2Container');

  void useContainerStore(s => s.openContainer);
  void useContainerStore(s => s.closeContainer);
  void useContainerStore(s => s.updateContainer);
  void useContainerStore(s => s.handleContainerDecayed);
  void useContainerStore(s => s.getContainer);
  void useContainerStore(s => s.isContainerOpen);

  useEffect(() => {
    detector.start();
    return () => detector.stop();
  }, [detector]);
}
