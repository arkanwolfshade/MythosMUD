// Client-side logging utility for MythosMUD
// Writes to both console and a log file for debugging

interface LogEntry {
  timestamp: string;
  level: 'DEBUG' | 'INFO' | 'WARN' | 'ERROR';
  component: string;
  message: string;
  data?: unknown;
}

// Extend Window interface for our custom properties
declare global {
  interface Window {
    mythosMudLogUrl?: string;
    mythosMudLogger?: ClientLogger;
  }
}

class ClientLogger {
  private logBuffer: LogEntry[] = [];
  private maxBufferSize = 1000;
  private isInitialized = false;

  constructor() {
    this.initializeLogging();
  }

  private initializeLogging() {
    if (this.isInitialized) return;

    // Create logs directory if it doesn't exist
    try {
      // Note: In browser environment, we can't create directories
      // But we can prepare for file download
      this.isInitialized = true;
    } catch (error) {
      console.error('Failed to initialize logging:', error);
    }

    // Set up periodic log flushing
    setInterval(() => {
      this.flushLogs();
    }, 5000); // Flush every 5 seconds

    // Set up beforeunload handler to flush logs
    window.addEventListener('beforeunload', () => {
      this.flushLogs();
    });

    this.info('Logger', 'Client logging initialized');
  }

  private createLogEntry(level: LogEntry['level'], component: string, message: string, data?: unknown): LogEntry {
    return {
      timestamp: new Date().toISOString(),
      level,
      component,
      message,
      data,
    };
  }

  private addToBuffer(entry: LogEntry) {
    this.logBuffer.push(entry);

    // Keep buffer size manageable
    if (this.logBuffer.length > this.maxBufferSize) {
      this.logBuffer = this.logBuffer.slice(-this.maxBufferSize / 2);
    }

    // Also log to console for immediate feedback
    const consoleMethod =
      entry.level === 'ERROR' ? 'error' : entry.level === 'WARN' ? 'warn' : entry.level === 'DEBUG' ? 'debug' : 'log';

    console[consoleMethod](
      `[${entry.timestamp}] [${entry.level}] [${entry.component}] ${entry.message}`,
      entry.data || ''
    );
  }

  debug(component: string, message: string, data?: unknown) {
    this.addToBuffer(this.createLogEntry('DEBUG', component, message, data));
  }

  info(component: string, message: string, data?: unknown) {
    this.addToBuffer(this.createLogEntry('INFO', component, message, data));
  }

  warn(component: string, message: string, data?: unknown) {
    this.addToBuffer(this.createLogEntry('WARN', component, message, data));
  }

  error(component: string, message: string, data?: unknown) {
    this.addToBuffer(this.createLogEntry('ERROR', component, message, data));
  }

  private flushLogs() {
    if (this.logBuffer.length === 0) return;

    try {
      const logContent = this.logBuffer
        .map(
          entry =>
            `${entry.timestamp} [${entry.level}] [${entry.component}] ${entry.message}${entry.data ? ` | Data: ${JSON.stringify(entry.data)}` : ''}`
        )
        .join('\n');

      // Create a blob and download link
      const blob = new Blob([logContent], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);

      // Store the URL for later download
      window.mythosMudLogUrl = url;

      // Clear the buffer after successful flush
      this.logBuffer = [];

      this.info('Logger', 'Logs flushed successfully');
    } catch (error) {
      console.error('Failed to flush logs:', error);
    }
  }

  // Method to manually download logs
  downloadLogs() {
    if (window.mythosMudLogUrl) {
      const link = document.createElement('a');
      link.href = window.mythosMudLogUrl;
      link.download = `mythosmud-client-${new Date().toISOString().replace(/[:.]/g, '-')}.log`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } else {
      this.warn('Logger', 'No logs available for download');
    }
  }

  // Method to get current log buffer (for debugging)
  getLogBuffer() {
    return [...this.logBuffer];
  }

  // Method to clear log buffer
  clearLogs() {
    this.logBuffer = [];
    this.info('Logger', 'Log buffer cleared');
  }
}

// Create singleton instance
export const logger = new ClientLogger();

// Export for global access (useful for debugging)
window.mythosMudLogger = logger;
