import React from 'react';
import './DeathInterstitial.css';

interface DeathInterstitialProps {
  isVisible: boolean;
  deathLocation: string;
  onRespawn: () => void;
  isRespawning?: boolean;
}

export const DeathInterstitial: React.FC<DeathInterstitialProps> = ({
  isVisible,
  deathLocation,
  onRespawn,
  isRespawning = false,
}) => {
  if (!isVisible) {
    return null;
  }

  return (
    <div className="death-interstitial-overlay">
      <div className="death-interstitial-container">
        <div className="death-interstitial-content">
          <h1 className="death-title">THE THRESHOLD CROSSED</h1>

          <div className="death-narrative">
            <p>
              The darkness consumes you utterly, and for a timeless moment, you drift through the spaces between worlds.
              Whispers in languages older than humanity echo around you, speaking of things mortal minds were never
              meant to comprehend.
            </p>

            <p>
              But the threads binding you to the waking world are not yet severed. The sanitarium calls you back from
              the threshold of oblivion...
            </p>
          </div>

          <div className="death-location">
            <p className="death-location-label">You perished at:</p>
            <p className="death-location-name">{deathLocation || 'Unknown Location'}</p>
          </div>

          <button className="respawn-button" onClick={onRespawn} disabled={isRespawning}>
            {isRespawning ? 'Returning to the mortal realm...' : 'Rejoin the earthly plane'}
          </button>

          {isRespawning && (
            <div className="respawn-loading">
              <p>The veil between worlds parts...</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
