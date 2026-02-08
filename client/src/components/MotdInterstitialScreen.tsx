import React from 'react';
import { MotdContent } from './MotdContent';

interface MotdInterstitialScreenProps {
  onContinue: () => void;
  onReturnToLogin: () => void;
}

/**
 * Interstitial MOTD screen that appears between authentication and the game terminal.
 * This replaces the modal overlay approach with a dedicated screen.
 */
export const MotdInterstitialScreen: React.FC<MotdInterstitialScreenProps> = ({ onContinue, onReturnToLogin }) => {
  return (
    <div className="h-screen min-h-screen w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono flex flex-col overflow-hidden">
      {/* Scrollable area so MOTD + buttons are always reachable without zooming */}
      <div className="flex-1 min-h-0 overflow-y-auto flex justify-center">
        <div className="w-full max-w-4xl p-8">
          {/* MOTD Content */}
          <div className="motd-content">
            <MotdContent />
          </div>

          {/* Action Buttons */}
          <div className="motd-actions mt-8 flex justify-center gap-4">
            <button
              onClick={onReturnToLogin}
              data-testid="motd-return-to-login"
              className="px-6 py-3 bg-mythos-terminal-surface border border-mythos-terminal-border text-mythos-terminal-text hover:bg-mythos-terminal-surface-hover transition-colors rounded"
              style={{
                background: 'linear-gradient(45deg, #d4af37, #b8941f)',
                color: '#0a0a0a',
                border: 'none',
                padding: '12px 30px',
                fontSize: '1.1em',
                fontWeight: 'bold',
                fontFamily: 'Courier New, monospace',
                borderRadius: '5px',
                cursor: 'pointer',
                transition: 'all 0.3s ease',
                textTransform: 'uppercase',
                letterSpacing: '1px',
                boxShadow: '0 4px 8px rgba(212, 175, 55, 0.3)',
              }}
            >
              Return to Login
            </button>
            <button
              onClick={onContinue}
              data-testid="motd-enter-realm"
              className="px-6 py-3 bg-mythos-terminal-primary text-black hover:bg-mythos-terminal-primary-hover transition-colors rounded font-semibold"
              style={{
                background: 'linear-gradient(45deg, #d4af37, #b8941f)',
                color: '#0a0a0a',
                border: 'none',
                padding: '12px 30px',
                fontSize: '1.1em',
                fontWeight: 'bold',
                fontFamily: 'Courier New, monospace',
                borderRadius: '5px',
                cursor: 'pointer',
                transition: 'all 0.3s ease',
                textTransform: 'uppercase',
                letterSpacing: '1px',
                boxShadow: '0 4px 8px rgba(212, 175, 55, 0.3)',
              }}
            >
              Enter the Realm
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
