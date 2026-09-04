import React from 'react';
import './DeathInterstitial.css';

interface DeliriumInterstitialProps {
  isVisible: boolean;
  deliriumLocation: string;
  onRespawn: () => void;
  isRespawning?: boolean;
}

export const DeliriumInterstitial: React.FC<DeliriumInterstitialProps> = ({
  isVisible,
  deliriumLocation,
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
          <h1 className="death-title">THE MIND FRACTURES</h1>

          <div className="death-narrative">
            <p>
              Reality splinters around you. The boundaries between what is and what should not be dissolve into
              fragments of impossible geometry. Whispers from dimensions beyond comprehension echo through the cracks in
              your perception.
            </p>

            <p>
              Your grip on sanity has slipped beyond recovery. The Arkham Sanitarium offers a refuge—a place where the
              fractured mind can find temporary anchor in the mundane world...
            </p>
          </div>

          <div className="death-location">
            <p className="death-location-label">You lost your lucidity at:</p>
            <p className="death-location-name">{deliriumLocation || 'Unknown Location'}</p>
          </div>

          <button className="respawn-button" onClick={onRespawn} disabled={isRespawning}>
            {isRespawning ? 'Returning to the Sanitarium...' : 'Acknowledge your delirium'}
          </button>

          {isRespawning && (
            <div className="respawn-loading">
              <p>The orderlies guide you back to lucidity...</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
