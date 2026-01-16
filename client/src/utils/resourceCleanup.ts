import { useEffect, useMemo } from 'react';

interface CustomResource {
  cleanup: () => void;
  name?: string;
}

/**
 * Resource manager for tracking and cleaning up various types of resources
 * to prevent memory leaks in React components
 */
export class ResourceManager {
  private timers: Set<number> = new Set();
  private intervals: Set<number> = new Set();
  private webSockets: Set<WebSocket> = new Set();
  private customResources: Set<CustomResource> = new Set();

  /**
   * Register a timer for cleanup
   */
  registerTimer(timerId: number): void {
    this.timers.add(timerId);
  }

  /**
   * Register an interval for cleanup
   */
  registerInterval(intervalId: number): void {
    this.intervals.add(intervalId);
  }

  /**
   * Register a WebSocket connection for cleanup
   */
  registerWebSocket(websocket: WebSocket): void {
    this.webSockets.add(websocket);
  }

  /**
   * Register a custom resource for cleanup
   */
  registerCustomResource(resource: CustomResource): void {
    this.customResources.add(resource);
  }

  /**
   * Get all active timers
   */
  getActiveTimers(): number[] {
    return Array.from(this.timers);
  }

  /**
   * Get all active intervals
   */
  getActiveIntervals(): number[] {
    return Array.from(this.intervals);
  }

  /**
   * Get all active WebSocket connections
   */
  getActiveWebSockets(): WebSocket[] {
    return Array.from(this.webSockets);
  }

  /**
   * Get all active custom resources
   */
  getActiveCustomResources(): CustomResource[] {
    return Array.from(this.customResources);
  }

  /**
   * Get resource statistics
   */
  getResourceStats(): {
    timers: number;
    intervals: number;
    webSockets: number;
    customResources: number;
    total: number;
  } {
    return {
      timers: this.timers.size,
      intervals: this.intervals.size,
      webSockets: this.webSockets.size,
      customResources: this.customResources.size,
      total: this.timers.size + this.intervals.size + this.webSockets.size + this.customResources.size,
    };
  }

  /**
   * Clean up all registered resources
   */
  cleanup(): void {
    // Clear all timers
    this.timers.forEach(timerId => {
      clearTimeout(timerId);
    });
    this.timers.clear();

    // Clear all intervals
    this.intervals.forEach(intervalId => {
      clearInterval(intervalId);
    });
    this.intervals.clear();

    // Close all WebSocket connections
    this.webSockets.forEach(websocket => {
      if (websocket.readyState === WebSocket.OPEN || websocket.readyState === WebSocket.CONNECTING) {
        websocket.close();
      }
    });
    this.webSockets.clear();

    // Clean up custom resources
    this.customResources.forEach(resource => {
      try {
        if (typeof resource.cleanup === 'function') {
          resource.cleanup();
        }
      } catch (error) {
        console.error('Error cleaning up custom resource:', error);
      }
    });
    this.customResources.clear();
  }

  /**
   * Remove a specific timer from tracking
   */
  removeTimer(timerId: number): void {
    this.timers.delete(timerId);
  }

  /**
   * Remove a specific interval from tracking
   */
  removeInterval(intervalId: number): void {
    this.intervals.delete(intervalId);
  }

  /**
   * Remove a specific WebSocket from tracking
   */
  removeWebSocket(websocket: WebSocket): void {
    this.webSockets.delete(websocket);
  }

  /**
   * Remove a specific custom resource from tracking
   */
  removeCustomResource(resource: CustomResource): void {
    this.customResources.delete(resource);
  }
}

/**
 * React hook for managing resource cleanup
 * Automatically cleans up all registered resources when the component unmounts
 */
export const useResourceCleanup = (): ResourceManager => {
  // Use useMemo to create manager once and avoid ref access during render
  const resourceManager = useMemo(() => new ResourceManager(), []);

  // Cleanup on unmount
  useEffect(() => {
    // Periodic logging of resource stats (every 5 minutes in development)
    const logInterval = setInterval(
      () => {
        if (process.env.NODE_ENV === 'development') {
          const stats = resourceManager.getResourceStats();
          console.log('[ResourceManager] Periodic stats:', stats);
        }
      },
      5 * 60 * 1000
    ); // 5 minutes

    return () => {
      clearInterval(logInterval);
      resourceManager.cleanup();
    };
  }, [resourceManager]);

  return resourceManager;
};

/**
 * Utility function to create a cleanup function for timers
 */
export const createTimerCleanup = (resourceManager: ResourceManager) => {
  return {
    setTimeout: (callback: () => void, delay: number): number => {
      const timerId = window.setTimeout(callback, delay);
      resourceManager.registerTimer(timerId);
      return timerId;
    },
    setInterval: (callback: () => void, delay: number): number => {
      const intervalId = window.setInterval(callback, delay);
      resourceManager.registerInterval(intervalId);
      return intervalId;
    },
  };
};

/**
 * Utility function to create a cleanup function for WebSocket connections
 */
export const createWebSocketCleanup = (resourceManager: ResourceManager) => {
  return (url: string, protocols?: string | string[]): WebSocket => {
    const websocket = new WebSocket(url, protocols);
    resourceManager.registerWebSocket(websocket);
    return websocket;
  };
};

/**
 * Utility function to create a cleanup function for custom resources
 */
export const createCustomResourceCleanup = (resourceManager: ResourceManager) => {
  return (resource: CustomResource): void => {
    resourceManager.registerCustomResource(resource);
  };
};

export type { CustomResource };
