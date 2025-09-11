import { useEffect, useRef } from 'react';

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
  private eventSources: Set<EventSource> = new Set();
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
   * Register an EventSource connection for cleanup
   */
  registerEventSource(eventSource: EventSource): void {
    this.eventSources.add(eventSource);
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
   * Get all active EventSource connections
   */
  getActiveEventSources(): EventSource[] {
    return Array.from(this.eventSources);
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
    eventSources: number;
    customResources: number;
    total: number;
  } {
    return {
      timers: this.timers.size,
      intervals: this.intervals.size,
      webSockets: this.webSockets.size,
      eventSources: this.eventSources.size,
      customResources: this.customResources.size,
      total:
        this.timers.size +
        this.intervals.size +
        this.webSockets.size +
        this.eventSources.size +
        this.customResources.size,
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

    // Close all EventSource connections
    this.eventSources.forEach(eventSource => {
      if (eventSource.readyState === EventSource.OPEN || eventSource.readyState === EventSource.CONNECTING) {
        eventSource.close();
      }
    });
    this.eventSources.clear();

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
   * Remove a specific EventSource from tracking
   */
  removeEventSource(eventSource: EventSource): void {
    this.eventSources.delete(eventSource);
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
  const resourceManagerRef = useRef<ResourceManager | null>(null);

  // Create resource manager if it doesn't exist
  if (!resourceManagerRef.current) {
    resourceManagerRef.current = new ResourceManager();
  }

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      resourceManagerRef.current?.cleanup();
    };
  }, []);

  return resourceManagerRef.current;
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
 * Utility function to create a cleanup function for EventSource connections
 */
export const createEventSourceCleanup = (resourceManager: ResourceManager) => {
  return (url: string, eventSourceInitDict?: EventSourceInit): EventSource => {
    const eventSource = new EventSource(url, eventSourceInitDict);
    resourceManager.registerEventSource(eventSource);
    return eventSource;
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
