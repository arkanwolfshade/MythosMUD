/**
 * Security utilities for MythosMUD client
 * Provides secure token storage, session management, input sanitization, and CSRF protection
 */

import DOMPurify from 'dompurify';

interface Session {
  id: string;
  userId: string;
  expiresAt: number;
  onTimeout?: (sessionId: string) => void;
}

interface RefreshTokenResponse {
  access_token: string;
  expires_in: number;
  refresh_token?: string;
}

/**
 * Secure token storage using httpOnly cookies
 */
export const secureTokenStorage = {
  /**
   * Store authentication token in httpOnly cookie
   */
  setToken(token: string): void {
    // In a real implementation, this would be handled by the server
    // For client-side, we'll use a secure cookie approach
    const expires = new Date();
    expires.setTime(expires.getTime() + 24 * 60 * 60 * 1000); // 24 hours

    document.cookie = `authToken=${token}; expires=${expires.toUTCString()}; path=/; HttpOnly; Secure; SameSite=Strict`;
  },

  /**
   * Retrieve authentication token from cookie
   */
  getToken(): string | null {
    const cookies = document.cookie.split(';');
    const tokenCookie = cookies.find(cookie => cookie.trim().startsWith('authToken='));

    if (!tokenCookie) {
      return null;
    }

    return tokenCookie.split('=')[1] || null;
  },

  /**
   * Clear authentication token
   */
  clearToken(): void {
    document.cookie = 'authToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; HttpOnly; Secure; SameSite=Strict';
  },

  /**
   * Validate JWT token format
   */
  isValidToken(token: string): boolean {
    if (!token || typeof token !== 'string') {
      return false;
    }

    // Basic JWT format validation (3 parts separated by dots)
    const parts = token.split('.');
    return parts.length === 3;
  },

  /**
   * Check if token is expired
   */
  isTokenExpired(token: string): boolean {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      const currentTime = Math.floor(Date.now() / 1000);
      return payload.exp && payload.exp < currentTime;
    } catch {
      return true; // If we can't parse, consider it expired
    }
  },

  /**
   * Refresh token if needed
   */
  async refreshTokenIfNeeded(token: string): Promise<boolean> {
    if (!this.isValidToken(token) || !this.isTokenExpired(token)) {
      return true; // Token is valid, no refresh needed
    }

    try {
      const response = await fetch('/auth/refresh', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          refresh_token: this.getRefreshToken(),
        }),
      });

      if (!response.ok) {
        return false;
      }

      const data: RefreshTokenResponse = await response.json();

      if (data.access_token) {
        this.setToken(data.access_token);
        return true;
      }

      return false;
    } catch (error) {
      console.error('Token refresh failed:', error);
      return false;
    }
  },

  /**
   * Get refresh token (stored separately)
   */
  getRefreshToken(): string | null {
    const cookies = document.cookie.split(';');
    const refreshCookie = cookies.find(cookie => cookie.trim().startsWith('refreshToken='));

    if (!refreshCookie) {
      return null;
    }

    return refreshCookie.split('=')[1] || null;
  },

  /**
   * Set refresh token
   */
  setRefreshToken(token: string): void {
    const expires = new Date();
    expires.setTime(expires.getTime() + 7 * 24 * 60 * 60 * 1000); // 7 days

    document.cookie =
      `refreshToken=${token}; expires=${expires.toUTCString()}; ` + `path=/; HttpOnly; Secure; SameSite=Strict`;
  },

  /**
   * Clear refresh token
   */
  clearRefreshToken(): void {
    document.cookie = 'refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; HttpOnly; Secure; SameSite=Strict';
  },

  /**
   * Clear all tokens (both access and refresh)
   */
  clearAllTokens(): void {
    this.clearToken();
    this.clearRefreshToken();
  },
};

/**
 * Session management with timeout handling
 */
class SessionManager {
  private sessions: Map<string, Session> = new Map();
  private cleanupInterval: number | null = null;

  constructor() {
    // Start cleanup interval
    this.startCleanupInterval();
  }

  /**
   * Create a new session
   */
  createSession(userId: string, timeoutSeconds: number, onTimeout?: (sessionId: string) => void): string {
    const sessionId = this.generateSessionId();
    const expiresAt = Date.now() + timeoutSeconds * 1000;

    const session: Session = {
      id: sessionId,
      userId,
      expiresAt,
      onTimeout,
    };

    this.sessions.set(sessionId, session);

    return sessionId;
  }

  /**
   * Check if session is valid
   */
  isSessionValid(sessionId: string): boolean {
    const session = this.sessions.get(sessionId);
    if (!session) {
      return false;
    }

    return Date.now() < session.expiresAt;
  }

  /**
   * Refresh session timeout
   */
  refreshSession(sessionId: string, additionalSeconds: number = 3600): boolean {
    const session = this.sessions.get(sessionId);
    if (!session) {
      return false;
    }

    session.expiresAt = Date.now() + additionalSeconds * 1000;
    return true;
  }

  /**
   * Remove session
   */
  removeSession(sessionId: string): boolean {
    return this.sessions.delete(sessionId);
  }

  /**
   * Clean up expired sessions
   */
  cleanupExpiredSessions(): void {
    const now = Date.now();

    for (const [sessionId, session] of this.sessions.entries()) {
      if (now >= session.expiresAt) {
        this.expireSession(sessionId);
      }
    }
  }

  /**
   * Expire a specific session
   */
  private expireSession(sessionId: string): void {
    const session = this.sessions.get(sessionId);
    if (session) {
      if (session.onTimeout) {
        session.onTimeout(sessionId);
      }
      this.sessions.delete(sessionId);
    }
  }

  /**
   * Generate unique session ID
   */
  private generateSessionId(): string {
    return 'session_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
  }

  /**
   * Start cleanup interval
   */
  private startCleanupInterval(): void {
    if (this.cleanupInterval) {
      clearInterval(this.cleanupInterval);
    }

    this.cleanupInterval = window.setInterval(() => {
      this.cleanupExpiredSessions();
    }, 60000); // Clean up every minute
  }

  /**
   * Stop cleanup interval
   */
  destroy(): void {
    if (this.cleanupInterval) {
      clearInterval(this.cleanupInterval);
      this.cleanupInterval = null;
    }
    this.sessions.clear();
  }
}

export const sessionManager = new SessionManager();

/**
 * Input sanitization utilities
 */
export const inputSanitizer = {
  /**
   * HTML sanitization using DOMPurify
   */
  sanitizeHtml(input: string): string {
    if (!input || typeof input !== 'string') {
      return '';
    }

    // Configure DOMPurify for MUD content - allow basic formatting but block dangerous elements
    const config = {
      ALLOWED_TAGS: ['b', 'i', 'u', 'em', 'strong', 'br', 'p', 'span', 'div'],
      ALLOWED_ATTR: ['class', 'style'],
      ALLOW_DATA_ATTR: false,
      ALLOW_UNKNOWN_PROTOCOLS: false,
    };

    return DOMPurify.sanitize(input, config);
  },

  /**
   * Sanitize user commands
   */
  sanitizeCommand(command: string): string {
    if (!command || typeof command !== 'string') {
      return '';
    }

    // Remove HTML tags and dangerous characters from commands
    return command
      .replace(/<[^>]*>/g, '')
      .replace(/[<>]/g, '')
      .replace(/javascript:/gi, '')
      .replace(/vbscript:/gi, '')
      .trim();
  },

  /**
   * Sanitize username input
   */
  sanitizeUsername(username: string): string {
    if (!username || typeof username !== 'string') {
      return '';
    }

    // Allow only alphanumeric characters, underscores, and hyphens
    return username.replace(/[^a-zA-Z0-9_-]/g, '').substring(0, 20);
  },

  /**
   * Sanitize chat message
   */
  sanitizeChatMessage(message: string): string {
    if (!message || typeof message !== 'string') {
      return '';
    }

    // Use DOMPurify for chat messages with more restrictive config
    const config = {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong'],
      ALLOWED_ATTR: [],
      ALLOW_DATA_ATTR: false,
      ALLOW_UNKNOWN_PROTOCOLS: false,
    };

    return DOMPurify.sanitize(message, config).substring(0, 500); // Limit message length
  },
};

/**
 * CSRF protection utilities
 */
class CSRFProtection {
  private tokens: Map<string, number> = new Map();
  private tokenExpiry: number = 3600000; // 1 hour default

  /**
   * Generate CSRF token
   */
  generateToken(expirySeconds: number = 3600): string {
    const token = this.generateRandomToken();
    const expiresAt = Date.now() + expirySeconds * 1000;

    this.tokens.set(token, expiresAt);

    // Clean up expired tokens
    this.cleanupExpiredTokens();

    return token;
  }

  /**
   * Validate CSRF token
   */
  validateToken(token: string): boolean {
    if (!token || typeof token !== 'string') {
      return false;
    }

    const expiresAt = this.tokens.get(token);
    if (!expiresAt) {
      return false;
    }

    if (Date.now() > expiresAt) {
      this.tokens.delete(token);
      return false;
    }

    return true;
  }

  /**
   * Add CSRF token to request headers
   */
  addTokenToHeaders(headers: Record<string, string> = {}): Record<string, string> {
    const token = this.generateToken();
    return {
      ...headers,
      'X-CSRF-Token': token,
    };
  }

  /**
   * Generate random token
   */
  private generateRandomToken(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
  }

  /**
   * Clean up expired tokens
   */
  private cleanupExpiredTokens(): void {
    const now = Date.now();

    for (const [token, expiresAt] of this.tokens.entries()) {
      if (now > expiresAt) {
        this.tokens.delete(token);
      }
    }
  }
}

export const csrfProtection = new CSRFProtection();
