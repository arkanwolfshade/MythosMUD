import { useCallback, useEffect, useRef } from 'react';

interface BatchedMessage {
  id: string;
  type: 'chat' | 'system' | 'error' | 'move';
  content: string;
  timestamp: number;
  metadata?: Record<string, unknown>;
}

interface BatchConfig {
  maxBatchSize: number;
  maxBatchDelay: number; // milliseconds
  maxBatchSizeBytes: number;
}

class MessageBatcher {
  private batch: BatchedMessage[] = [];
  private timer: NodeJS.Timeout | null = null;
  private config: BatchConfig;
  private onBatchReady: (messages: BatchedMessage[]) => void;

  constructor(onBatchReady: (messages: BatchedMessage[]) => void, config: Partial<BatchConfig> = {}) {
    this.onBatchReady = onBatchReady;
    this.config = {
      maxBatchSize: 10,
      maxBatchDelay: 100, // 100ms
      maxBatchSizeBytes: 1024 * 10, // 10KB
      ...config,
    };
  }

  addMessage(message: Omit<BatchedMessage, 'id' | 'timestamp'>): void {
    const batchedMessage: BatchedMessage = {
      ...message,
      id: this.generateId(),
      timestamp: Date.now(),
    };

    this.batch.push(batchedMessage);

    // Check if we should send the batch immediately
    if (this.shouldSendBatch()) {
      this.sendBatch();
    } else if (!this.timer) {
      // Start timer for delayed sending
      this.timer = setTimeout(() => {
        this.sendBatch();
      }, this.config.maxBatchDelay);
    }
  }

  private shouldSendBatch(): boolean {
    if (this.batch.length >= this.config.maxBatchSize) {
      return true;
    }

    // Check batch size in bytes
    const batchSizeBytes = this.getBatchSizeBytes();
    if (batchSizeBytes >= this.config.maxBatchSizeBytes) {
      return true;
    }

    return false;
  }

  private sendBatch(): void {
    if (this.batch.length === 0) return;

    // Clear timer
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = null;
    }

    // Send batch
    const messagesToSend = [...this.batch];
    this.batch = [];
    this.onBatchReady(messagesToSend);
  }

  private generateId(): string {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  // Force send current batch
  flush(): void {
    this.sendBatch();
  }

  // Get current batch size
  getBatchSize(): number {
    return this.batch.length;
  }

  // Get current batch size in bytes
  getBatchSizeBytes(): number {
    return this.batch.reduce((total, message) => {
      return total + JSON.stringify(message).length;
    }, 0);
  }

  // Clear current batch
  clear(): void {
    this.batch = [];
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = null;
    }
  }
}

// Hook for using message batcher in React components
export const useMessageBatcher = (
  onBatchReady: (messages: BatchedMessage[]) => void,
  config?: Partial<BatchConfig>
) => {
  const batcherRef = useRef<MessageBatcher | null>(null);

  if (!batcherRef.current) {
    batcherRef.current = new MessageBatcher(onBatchReady, config);
  }

  const addMessage = useCallback((message: Omit<BatchedMessage, 'id' | 'timestamp'>) => {
    batcherRef.current?.addMessage(message);
  }, []);

  const flush = useCallback(() => {
    batcherRef.current?.flush();
  }, []);

  const clear = useCallback(() => {
    batcherRef.current?.clear();
  }, []);

  const getBatchSize = useCallback(() => {
    return batcherRef.current?.getBatchSize() || 0;
  }, []);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      batcherRef.current?.flush();
    };
  }, []);

  return {
    addMessage,
    flush,
    clear,
    getBatchSize,
  };
};

export { MessageBatcher };
export type { BatchConfig, BatchedMessage };
