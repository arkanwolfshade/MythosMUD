/**
 * Environment-based debug logger for MythosMUD client
 * Provides controlled logging based on environment and configuration
 */

export type LogLevel = 'DEBUG' | 'INFO' | 'WARN' | 'ERROR';

interface LogConfig {
  level: LogLevel;
  enableConsole: boolean;
  enableFile: boolean;
}

interface LogEntry {
  timestamp: string;
  level: LogLevel;
  component: string;
  message: string;
  data?: unknown;
}

class DebugLogger {
  private config: LogConfig;
  private logBuffer: LogEntry[] = [];
  private maxBufferSize = 1000;

  constructor(component: string, config?: Partial<LogConfig>) {
    this.config = this.initializeConfig(config);
    this.component = component;
  }

  private component: string;

  private initializeConfig(userConfig?: Partial<LogConfig>): LogConfig {
    const defaultConfig: LogConfig = {
      level: this.getDefaultLogLevel(),
      enableConsole: true,
      enableFile: true,
    };

    return { ...defaultConfig, ...userConfig };
  }

  private getDefaultLogLevel(): LogLevel {
    // Check environment variables for log level
    const envLogLevel = import.meta.env.VITE_LOG_LEVEL as LogLevel;
    if (envLogLevel && ['DEBUG', 'INFO', 'WARN', 'ERROR'].includes(envLogLevel)) {
      return envLogLevel;
    }

    // Default based on environment
    if (import.meta.env.PROD) {
      return 'WARN';
    }

    return 'DEBUG';
  }

  private shouldLog(level: LogLevel): boolean {
    const levelPriority: Record<LogLevel, number> = {
      DEBUG: 0,
      INFO: 1,
      WARN: 2,
      ERROR: 3,
    };

    return levelPriority[level] >= levelPriority[this.config.level];
  }

  private createLogEntry(level: LogLevel, message: string, data?: unknown): LogEntry {
    return {
      timestamp: new Date().toISOString(),
      level,
      component: this.component,
      message,
      data,
    };
  }

  private addToBuffer(entry: LogEntry): void {
    this.logBuffer.push(entry);

    // Keep buffer size manageable
    if (this.logBuffer.length > this.maxBufferSize) {
      this.logBuffer = this.logBuffer.slice(-this.maxBufferSize / 2);
    }
  }

  private logToConsole(entry: LogEntry): void {
    if (!this.config.enableConsole) return;

    const consoleMethod = this.getConsoleMethod(entry.level);
    const formattedMessage = this.formatMessage(entry);

    console[consoleMethod](formattedMessage, entry.data || '');
  }

  private getConsoleMethod(level: LogLevel): 'debug' | 'log' | 'warn' | 'error' {
    switch (level) {
      case 'DEBUG':
        return 'debug';
      case 'INFO':
        return 'log';
      case 'WARN':
        return 'warn';
      case 'ERROR':
        return 'error';
      default:
        return 'log';
    }
  }

  private formatMessage(entry: LogEntry): string {
    return `[${entry.timestamp}] [${entry.level}] [${entry.component}] ${entry.message}`;
  }

  private log(level: LogLevel, message: string, data?: unknown): void {
    if (!this.shouldLog(level)) return;

    const entry = this.createLogEntry(level, message, data);

    this.addToBuffer(entry);
    this.logToConsole(entry);
  }

  // Public logging methods
  debug(message: string, data?: unknown): void {
    // In production builds, debug calls are removed at build time
    if (import.meta.env.PROD) {
      return;
    }
    this.log('DEBUG', message, data);
  }

  info(message: string, data?: unknown): void {
    this.log('INFO', message, data);
  }

  warn(message: string, data?: unknown): void {
    this.log('WARN', message, data);
  }

  error(message: string, data?: unknown): void {
    this.log('ERROR', message, data);
  }

  // Utility methods
  setLogLevel(level: LogLevel): void {
    this.config.level = level;
  }

  getLogLevel(): LogLevel {
    return this.config.level;
  }

  getLogBuffer(): LogEntry[] {
    return [...this.logBuffer];
  }

  clearLogs(): void {
    this.logBuffer = [];
  }

  // Method to get logs as formatted string
  getLogsAsString(): string {
    return this.logBuffer
      .map(entry => {
        const dataStr = entry.data ? ` | Data: ${JSON.stringify(entry.data)}` : '';
        return `${entry.timestamp} [${entry.level}] [${entry.component}] ${entry.message}${dataStr}`;
      })
      .join('\n');
  }

  // Method to download logs
  downloadLogs(): void {
    if (this.logBuffer.length === 0) {
      this.warn('No logs available for download');
      return;
    }

    try {
      const logContent = this.getLogsAsString();
      const blob = new Blob([logContent], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);

      const link = document.createElement('a');
      link.href = url;
      link.download = `mythosmud-${this.component}-${new Date().toISOString().replace(/[:.]/g, '-')}.log`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      URL.revokeObjectURL(url);
      this.info('Logs downloaded successfully');
    } catch (error) {
      this.error('Failed to download logs', { error: String(error) });
    }
  }
}

// Factory function to create logger instances
export function debugLogger(component: string, config?: Partial<LogConfig>): DebugLogger {
  return new DebugLogger(component, config);
}

// Export types for external use
export { DebugLogger };
export type { LogConfig, LogEntry, LogLevel };
