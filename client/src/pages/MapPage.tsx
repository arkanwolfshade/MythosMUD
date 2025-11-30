/**
 * Standalone Map Page component.
 *
 * This page can be opened in a new tab and will read the authentication token
 * from localStorage to maintain authentication across tabs.
 *
 * As documented in the Pnakotic Manuscripts, cross-dimensional navigation
 * requires careful preservation of authentication sigils across portal boundaries.
 */

import React, { useEffect, useState } from 'react';
import { RoomMapViewer } from '../components/map';
import { secureTokenStorage } from '../utils/security';
import { API_BASE_URL } from '../utils/config';
import { logger } from '../utils/logger';

interface RoomData {
  id: string;
  plane: string;
  zone: string;
  subZone?: string;
}

/**
 * Standalone map page that reads authentication from localStorage.
 */
export const MapPage: React.FC = () => {
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [currentRoom, setCurrentRoom] = useState<RoomData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  /**
   * Fetch the current room information from the API.
   */
  const fetchCurrentRoom = async (_token: string) => {
    try {
      // Try to get current room from game state API or player info
      // For now, we'll use a default or let the user select
      // The map viewer can work without a current room (it just won't highlight it)
      logger.info('MapPage', 'No current room specified, map will show all rooms');
      setCurrentRoom(null);
      setIsLoading(false);
    } catch (err) {
      logger.error('MapPage', 'Failed to fetch current room', { error: err });
      setError('Failed to load room information');
      setIsLoading(false);
    }
  };

  // Read auth token from localStorage on mount
  useEffect(() => {
    const initialize = () => {
      const token = secureTokenStorage.getToken();
      if (!token) {
        logger.warn('MapPage', 'No auth token found in localStorage');
        setError('Not authenticated. Please log in first.');
        setIsLoading(false);
        return;
      }

      setAuthToken(token);
      logger.info('MapPage', 'Auth token loaded from localStorage');

      // Try to get current room from URL parameters or localStorage
      const urlParams = new URLSearchParams(window.location.search);
      const roomId = urlParams.get('roomId');
      const plane = urlParams.get('plane');
      const zone = urlParams.get('zone');
      const subZone = urlParams.get('subZone');

      if (roomId && plane && zone) {
        setCurrentRoom({
          id: roomId,
          plane,
          zone,
          subZone: subZone || undefined,
        });
        setIsLoading(false);
      } else {
        // Try to fetch current room from API
        fetchCurrentRoom(token);
      }
    };

    // Defer initialization to avoid synchronous setState in effect
    queueMicrotask(initialize);
  }, []);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-mythos-terminal-primary mx-auto mb-4"></div>
          <p>Loading map...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
        <div className="text-center max-w-md p-6">
          <h1 className="text-2xl font-bold mb-4 text-mythos-terminal-error">Error</h1>
          <p className="mb-4">{error}</p>
          <button
            onClick={() => window.close()}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
          >
            Close
          </button>
        </div>
      </div>
    );
  }

  if (!authToken) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
        <div className="text-center max-w-md p-6">
          <h1 className="text-2xl font-bold mb-4">Authentication Required</h1>
          <p className="mb-4">Please log in to view the map.</p>
          <button
            onClick={() => (window.location.href = '/')}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
          >
            Go to Login
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen w-screen bg-mythos-terminal-background">
      <RoomMapViewer
        plane={currentRoom?.plane || 'earth'}
        zone={currentRoom?.zone || 'arkhamcity'}
        subZone={currentRoom?.subZone}
        currentRoomId={currentRoom?.id}
        authToken={authToken}
        baseUrl={API_BASE_URL}
      />
    </div>
  );
};
