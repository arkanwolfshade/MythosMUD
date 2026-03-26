import { API_V1_BASE } from '../utils/config.js';

export function postStartLoginGracePeriod(authToken: string, selectedCharacterId: string): Promise<Response> {
  return fetch(`${API_V1_BASE}/api/players/${selectedCharacterId}/start-login-grace-period`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${authToken}`,
    },
  });
}
