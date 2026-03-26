import { type Dispatch, type SetStateAction, useEffect, useState } from 'react';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

export interface RoomData {
  id: string;
  plane: string;
  zone: string;
  subZone?: string;
}

export interface MapPageState {
  authToken: string | null;
  currentRoom: RoomData | null;
  isLoading: boolean;
  error: string | null;
  editMode: boolean;
}

function parseMapRouteParams(search: string): { currentRoom: RoomData | null; editMode: boolean } {
  const urlParams = new URLSearchParams(search);
  const roomId = urlParams.get('roomId');
  const plane = urlParams.get('plane');
  const zone = urlParams.get('zone');
  const subZone = urlParams.get('subZone');
  const editMode = urlParams.get('edit') === 'true';

  const currentRoom =
    roomId && plane && zone
      ? {
          id: roomId,
          plane,
          zone,
          subZone: subZone || undefined,
        }
      : null;

  return { currentRoom, editMode };
}

async function fetchFallbackCurrentRoom(setState: Dispatch<SetStateAction<MapPageState>>): Promise<void> {
  try {
    logger.info('MapPage', 'No current room specified, map will show all rooms');
    setState(prev => ({ ...prev, currentRoom: null, isLoading: false }));
  } catch (err) {
    logger.error('MapPage', 'Failed to fetch current room', { error: err });
    setState(prev => ({ ...prev, error: 'Failed to load room information', isLoading: false }));
  }
}

export function useMapPageState(): MapPageState {
  const [state, setState] = useState<MapPageState>({
    authToken: null,
    currentRoom: null,
    isLoading: true,
    error: null,
    editMode: false,
  });

  useEffect(() => {
    const initialize = () => {
      const token = secureTokenStorage.getToken();
      if (!token) {
        logger.warn('MapPage', 'No auth token found in localStorage');
        setState(prev => ({ ...prev, error: 'Not authenticated. Please log in first.', isLoading: false }));
        return;
      }

      setState(prev => ({ ...prev, authToken: token }));
      logger.info('MapPage', 'Auth token loaded from localStorage');

      const parsed = parseMapRouteParams(window.location.search);
      if (parsed.currentRoom) {
        setState(prev => ({
          ...prev,
          currentRoom: parsed.currentRoom,
          editMode: parsed.editMode,
          isLoading: false,
        }));
      } else {
        setState(prev => ({ ...prev, editMode: parsed.editMode }));
        void fetchFallbackCurrentRoom(setState);
      }
    };

    queueMicrotask(initialize);
  }, []);

  return state;
}
