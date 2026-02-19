import { lazy, Suspense, useEffect, useRef, useState } from 'react';
import './App.css';
import {
  assertLoginResponse,
  assertServerCharacterResponseArray,
  isServerCharacterResponse,
  isServerCharacterResponseArray,
  type ServerCharacterResponse,
} from './utils/apiTypeGuards.js';
import { API_V1_BASE } from './utils/config.js';
import { getErrorMessage, isErrorResponse } from './utils/errorHandler.js';
import { logoutHandler } from './utils/logoutHandler.js';
import { memoryMonitor } from './utils/memoryMonitor.js';
import { inputSanitizer, secureTokenStorage } from './utils/security.js';

// Helper function to check if value is an object
function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

// Lazy load screen components for code splitting
// AI: Lazy loading reduces initial bundle size by ~30-50% and improves initial page load time
const EldritchEffectsDemo = lazy(() =>
  import('./components/EldritchEffectsDemo.jsx').then(m => ({ default: m.EldritchEffectsDemo }))
);
const GameClientV2Container = lazy(() =>
  import('./components/ui-v2/GameClientV2Container.jsx').then(m => ({ default: m.GameClientV2Container }))
);
const MotdInterstitialScreen = lazy(() =>
  import('./components/MotdInterstitialScreen.jsx').then(m => ({ default: m.MotdInterstitialScreen }))
);
const ProfessionSelectionScreen = lazy(() =>
  import('./components/ProfessionSelectionScreen.jsx').then(m => ({ default: m.ProfessionSelectionScreen }))
);
const StatsRollingScreen = lazy(() =>
  import('./components/StatsRollingScreen.jsx').then(m => ({ default: m.StatsRollingScreen }))
);
const CharacterSelectionScreen = lazy(() =>
  import('./components/CharacterSelectionScreen.jsx').then(m => ({ default: m.CharacterSelectionScreen }))
);
const SkillAssignmentScreen = lazy(() =>
  import('./components/SkillAssignmentScreen.jsx').then(m => ({ default: m.SkillAssignmentScreen }))
);
const CharacterNameScreen = lazy(() =>
  import('./components/CharacterNameScreen.jsx').then(m => ({ default: m.CharacterNameScreen }))
);

// Import types that are needed for props
import type { Profession } from './components/ProfessionCard.jsx';
import type { CharacterInfo } from './types/auth.js';

// Import the Stats interface from StatsRollingScreen
// Note: Server Stats model does NOT include 'wisdom' - it was removed/never existed
interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  size: number;
  intelligence: number;
  power: number;
  education: number;
  charisma: number;
  luck: number;
}

/** Plan 10.6: creation flow steps (stats → profession → skills → name). */
type CreationStep = 'stats' | 'profession' | 'skills' | 'name';

// ServerCharacterResponse is now imported from apiTypeGuards.ts

// Loading fallback component for lazy-loaded screens
// Defined at module level to prevent recreation on every render
const LoadingFallback = () => (
  <div className="App flex items-center justify-center min-h-screen bg-mythos-terminal-background">
    <div className="text-mythos-terminal-text font-mono">Loading...</div>
  </div>
);

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  // MULTI-CHARACTER: Replaced hasCharacter/characterName with characters array
  const [characters, setCharacters] = useState<CharacterInfo[]>([]);
  const [selectedCharacterName, setSelectedCharacterName] = useState<string>('');
  const [selectedCharacterId, setSelectedCharacterId] = useState<string>('');
  const [playerName, setPlayerName] = useState('');
  const [password, setPassword] = useState('');
  const [inviteCode, setInviteCode] = useState('');
  const [authToken, setAuthToken] = useState('');
  const [showDemo, setShowDemo] = useState(false); // Demo disabled for normal flow
  const [showMotd, setShowMotd] = useState(false); // Track MOTD display state
  // MULTI-CHARACTER: Character selection screen
  const [showCharacterSelection, setShowCharacterSelection] = useState(false);

  // Character creation flow state (plan 10.6: stats → profession → skills → name)
  const [creationStep, setCreationStep] = useState<CreationStep | null>(null);
  const [pendingStats, setPendingStats] = useState<Stats | null>(null);
  const [selectedProfession, setSelectedProfession] = useState<Profession | undefined>(undefined);
  const [pendingSkillsPayload, setPendingSkillsPayload] = useState<{
    occupation_slots: { skill_id: number; value: number }[];
    personal_interest: { skill_id: number }[];
  } | null>(null);

  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isRegistering, setIsRegistering] = useState(false);
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  // Initialize memory monitoring
  useEffect(() => {
    memoryMonitor.start();

    return () => {
      memoryMonitor.stop();
    };
  }, []);

  // Clear all stored authentication tokens on page load
  // CRITICAL: After server restart, all client authentications are void
  // Clients must reauthenticate on each page load to ensure tokens are validated
  // against the current server state
  //
  // NOTE: This clears tokens from storage, but tokens stored AFTER this mount
  // (i.e., during login in the same session) will remain valid for that session
  // NOTE: This only runs for the main app route, not for /map route
  // FIX: Use sessionStorage flag to prevent clearing tokens on component remount
  // (e.g., when Playwright switches tabs). Only clear on actual page load.

  // Dependencies intentionally omitted: API_V1_BASE and secureTokenStorage are stable module-level
  // references that never change. All setState functions are stable references from useState.
  // This effect should only run once on mount to check for existing authentication state.
  useEffect(() => {
    // Check if a valid token already exists before clearing
    // This prevents clearing tokens on component remount when user is already authenticated
    // Only clear tokens on fresh page load (no valid token exists)
    const existingToken = secureTokenStorage.getToken();
    const hasValidToken =
      existingToken &&
      secureTokenStorage.isValidToken(existingToken) &&
      !secureTokenStorage.isTokenExpired(existingToken);

    if (!hasValidToken) {
      // No valid token exists - clear all tokens (fresh page load or expired token)
      secureTokenStorage.clearAllTokens();

      // Also clear any auth state that might have been restored
      setAuthToken('');
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setShowMotd(false);
      setShowCharacterSelection(false);
    } else {
      // Valid token exists - restore authentication state (component remount scenario)
      // Restore token to state so defensive code can use it
      setAuthToken(existingToken);
      setIsAuthenticated(true);

      // Try to restore characters list from API to fully restore session state
      // This allows the component to properly render the game interface after remount
      fetch(`${API_V1_BASE}/api/players/characters`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${existingToken}`,
        },
      })
        .then(async response => {
          if (response.ok) {
            const rawData: unknown = await response.json();
            if (!isServerCharacterResponseArray(rawData)) {
              throw new Error('Invalid API response: expected ServerCharacterResponse[]');
            }
            return rawData;
          }
          // If 401, token is invalid - clear it
          if (response.status === 401) {
            secureTokenStorage.clearAllTokens();
            setIsAuthenticated(false);
            setAuthToken('');
          }
          return null;
        })
        .then(charactersList => {
          if (charactersList && charactersList.length > 0) {
            // Map server response to client interface
            // Server returns PlayerRead which has player_id as the ID field
            const mappedCharacters = charactersList.map(
              (c: ServerCharacterResponse): CharacterInfo => ({
                player_id: c.player_id || c.id || '',
                name: c.name,
                profession_id: c.profession_id,
                profession_name: c.profession_name,
                level: c.level,
                created_at: c.created_at,
                last_active: c.last_active,
              })
            );
            setCharacters(mappedCharacters);

            // If only one character, auto-select it (common case after remount)
            // BUT: Don't auto-select if we're in character creation flow
            const inCharacterCreation = creationStep !== null;

            if (mappedCharacters.length === 1 && !inCharacterCreation) {
              const singleChar = mappedCharacters[0];
              setSelectedCharacterId(singleChar.player_id);
              setSelectedCharacterName(singleChar.name);
              // Skip character selection and MOTD, go straight to game
              setShowCharacterSelection(false);
              setShowMotd(false);
            } else if (mappedCharacters.length > 1 && !inCharacterCreation) {
              // Multiple characters - show selection screen (only if not in character creation)
              setShowCharacterSelection(true);
            }
            // If in character creation, don't change the flow - let character creation continue
            return;
          } else if (charactersList && charactersList.length === 0) {
            // No characters - user needs to create one (plan 10.6: start at stats step)
            setCreationStep('stats');
            setShowCharacterSelection(false);
          }
        })
        .catch(error => {
          // If API call fails, token might be invalid - clear it
          console.warn('Failed to restore characters on remount:', error);
          secureTokenStorage.clearAllTokens();
          setIsAuthenticated(false);
          setAuthToken('');
        });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- Only run on mount; omit deps to prevent re-run on state changes
  }, []);

  const handleLoginClick = async () => {
    // Sanitize inputs
    const sanitizedUsername = inputSanitizer.sanitizeUsername(playerName);
    const sanitizedPassword = inputSanitizer.sanitizeCommand(password);

    if (!sanitizedUsername || !sanitizedPassword) {
      setError('Username and password are required');
      return;
    }
    setIsSubmitting(true);
    setError(null);
    try {
      const response = await fetch(`${API_V1_BASE}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: sanitizedUsername, password: sanitizedPassword }),
      });
      if (!response.ok) {
        let message = `Login failed (${response.status})`;
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            message = getErrorMessage(rawData);
          } else if (isObject(rawData)) {
            const data = rawData as Record<string, unknown>;
            message =
              typeof data.error === 'object' && data.error !== null && 'message' in data.error
                ? String((data.error as Record<string, unknown>).message)
                : typeof data.detail === 'string'
                  ? data.detail
                  : message;
          }
        } catch {
          // Ignore JSON parsing errors, use default message
        }
        throw new Error(message);
      }
      const rawData: unknown = await response.json();
      const data = assertLoginResponse(rawData, 'Invalid login response from server');

      const token = data.access_token;
      const refreshToken = data.refresh_token;

      // Store tokens securely with username-specific keys (prevents tab conflicts)
      secureTokenStorage.setToken(token, sanitizedUsername);
      if (refreshToken) {
        secureTokenStorage.setRefreshToken(refreshToken, sanitizedUsername);
      }

      setAuthToken(token);
      setIsAuthenticated(true);
      // MULTI-CHARACTER: Update to use characters array
      const charactersList = data.characters || [];
      // Map server response (id) to client interface (player_id)
      const mappedCharacters = charactersList.map(
        (c: ServerCharacterResponse): CharacterInfo => ({
          ...c,
          player_id: c.id || c.player_id || '', // Server returns 'id', client expects 'player_id'
        })
      );
      setCharacters(mappedCharacters);

      // For new users without characters, show profession selection
      if (charactersList.length === 0) {
        setCreationStep('stats');
        setShowCharacterSelection(false);
      } else {
        // For existing users with characters, show character selection screen
        setShowCharacterSelection(true);
        setCreationStep(null);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleRegisterClick = async () => {
    // Sanitize inputs
    const sanitizedUsername = inputSanitizer.sanitizeUsername(playerName);
    const sanitizedPassword = inputSanitizer.sanitizeCommand(password);
    const sanitizedInviteCode = inputSanitizer.sanitizeCommand(inviteCode);

    if (!sanitizedUsername || !sanitizedPassword || !sanitizedInviteCode) {
      setError('Username, password, and invite code are required');
      return;
    }
    setIsSubmitting(true);
    setError(null);
    try {
      const response = await fetch(`${API_V1_BASE}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: sanitizedUsername,
          password: sanitizedPassword,
          invite_code: sanitizedInviteCode,
        }),
      });
      if (!response.ok) {
        let message = `Registration failed (${response.status})`;
        try {
          const rawData: unknown = await response.json();

          if (isErrorResponse(rawData)) {
            message = getErrorMessage(rawData);
          } else if (isObject(rawData)) {
            const data = rawData as Record<string, unknown>;
            // Handle Pydantic validation errors (422) - check for detail array
            if (response.status === 422 && Array.isArray(data.detail)) {
              const validationErrors = data.detail as Array<Record<string, unknown>>;

              // Extract password-specific errors
              const passwordErrors = validationErrors.filter(err => {
                const loc = err.loc;
                if (Array.isArray(loc)) {
                  const fieldPath = loc.map(String).join('.').toLowerCase();
                  return fieldPath.includes('password');
                }
                return false;
              });

              if (passwordErrors.length > 0) {
                // Build user-friendly password error message with criteria
                const passwordMessages = passwordErrors.map(err => {
                  const msg = String(err.msg || err.message || 'Validation error');
                  // Extract specific password requirements from error messages
                  if (msg.includes('at least') || msg.includes('8 characters')) {
                    return 'Password must be at least 8 characters long';
                  }
                  if (msg.includes('exceed') || msg.includes('1024')) {
                    return 'Password must not exceed 1024 characters';
                  }
                  if (msg.includes('empty')) {
                    return 'Password cannot be empty';
                  }
                  return msg;
                });

                // Add password criteria summary
                message = `${passwordMessages.join('. ')}. Password requirements: at least 8 characters, maximum 1024 characters.`;
              } else {
                // Handle other validation errors
                const errorMessages = validationErrors
                  .map(err => {
                    const loc = err.loc ? (Array.isArray(err.loc) ? err.loc.join('.') : String(err.loc)) : '';
                    const msg = err.msg || err.message || 'Validation error';
                    // Convert field paths to user-friendly names
                    const fieldName = loc.split('.').pop()?.replace('_', ' ') || 'field';
                    return `${fieldName}: ${msg}`;
                  })
                  .join('; ');
                message = errorMessages || message;
              }
            } else if (response.status === 422 && typeof data.detail === 'string') {
              // Handle string detail (non-array 422 response)
              message = data.detail;
            } else {
              message =
                typeof data.error === 'object' && data.error !== null && 'message' in data.error
                  ? String((data.error as Record<string, unknown>).message)
                  : typeof data.detail === 'string'
                    ? data.detail
                    : message;
            }
          }
        } catch {
          // Ignore JSON parsing errors, use default message
        }
        throw new Error(message);
      }
      const rawData: unknown = await response.json();
      const data = assertLoginResponse(rawData, 'Invalid registration response from server');

      const token = data.access_token;
      const refreshToken = data.refresh_token;

      // Store tokens securely with username-specific keys (prevents tab conflicts)
      secureTokenStorage.setToken(token, sanitizedUsername);
      if (refreshToken) {
        secureTokenStorage.setRefreshToken(refreshToken, sanitizedUsername);
      }

      setAuthToken(token);
      setIsAuthenticated(true);
      // MULTI-CHARACTER: Update to use characters array
      const charactersList = data.characters || [];
      // Map server response (id) to client interface (player_id)
      const mappedCharacters = charactersList.map(
        (c: ServerCharacterResponse): CharacterInfo => ({
          ...c,
          player_id: c.id || c.player_id || '', // Server returns 'id', client expects 'player_id'
        })
      );
      setCharacters(mappedCharacters);

      // For new users without characters, show profession selection
      if (charactersList.length === 0) {
        setCreationStep('stats');
        setShowCharacterSelection(false);
      } else {
        // For existing users with characters, show character selection screen
        setShowCharacterSelection(true);
        setCreationStep(null);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleProfessionSelected = (profession: Profession) => {
    setSelectedProfession(profession);
    setCreationStep('skills');
  };

  const handleProfessionSelectionBack = () => {
    setCreationStep('stats');
  };

  const handleProfessionSelectionError = (error: string) => {
    // Check if error indicates server unavailability
    const errorLower = error.toLowerCase();
    const serverUnavailablePatterns = [
      'failed to fetch',
      'network error',
      'network request failed',
      'connection refused',
      'connection reset',
      'connection closed',
      'connection timeout',
      'server is unavailable',
      'service unavailable',
      'bad gateway',
      'gateway timeout',
    ];

    if (serverUnavailablePatterns.some(pattern => errorLower.includes(pattern))) {
      returnToLogin();
      return;
    }

    setError(error);
  };

  /** Plan 10.6: called when user accepts stats (stats step); advance to profession step. */
  const handleStatsAccepted = (stats: Stats) => {
    setPendingStats(stats);
    setCreationStep('profession');
  };

  /** Plan 10.6: called when CharacterNameScreen create-character succeeds; refresh list and exit creation. */
  const handleCreationComplete = async () => {
    try {
      const response = await fetch(`${API_V1_BASE}/api/players/characters`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (response.ok) {
        const rawData: unknown = await response.json();
        const charactersList = assertServerCharacterResponseArray(
          rawData,
          'Invalid API response: expected ServerCharacterResponse[]'
        );
        const mappedCharacters = charactersList.map(
          (c: ServerCharacterResponse): CharacterInfo => ({
            player_id: c.player_id || c.id || '',
            name: c.name,
            profession_id: c.profession_id,
            profession_name: c.profession_name,
            level: c.level,
            created_at: c.created_at,
            last_active: c.last_active,
          })
        );
        setCharacters(mappedCharacters);
        setPendingStats(null);
        setSelectedProfession(undefined);
        setPendingSkillsPayload(null);
        setCreationStep(null);
        setShowCharacterSelection(true);
      } else {
        // Check if server is unavailable
        if (isServerUnavailable(null, response)) {
          returnToLogin();
          return;
        }

        // Response was not OK - handle as error
        let errorMessage = 'Character created, but failed to refresh character list';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (isObject(rawData)) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        console.error('Failed to refresh characters list:', errorMessage);
        setError('Character created, but failed to refresh character list. Please refresh the page.');
        // Reset character creation state to allow retry
        setSelectedProfession(undefined);
        setCreationStep(null);
        setShowCharacterSelection(true);
        setShowCharacterSelection(false);
      }
    } catch (error) {
      // Check if error is due to server unavailability
      if (isServerUnavailable(error, null)) {
        returnToLogin();
        return;
      }

      // If refresh fails, log error and show error message
      // Don't proceed to character selection if we can't verify characters were created
      console.error('Failed to refresh characters list:', error);
      setError('Character created, but failed to refresh character list. Please refresh the page.');
      // Reset character creation state to allow retry
      setSelectedProfession(undefined);
      setCreationStep('stats');
      setShowCharacterSelection(false);
    }
  };

  const handleStatsError = (error: string) => {
    // Check if error indicates server unavailability
    const errorLower = error.toLowerCase();
    const serverUnavailablePatterns = [
      'failed to fetch',
      'network error',
      'network request failed',
      'connection refused',
      'connection reset',
      'connection closed',
      'connection timeout',
      'server is unavailable',
      'service unavailable',
      'bad gateway',
      'gateway timeout',
      'failed to connect to server',
    ];

    if (serverUnavailablePatterns.some(pattern => errorLower.includes(pattern))) {
      returnToLogin();
      return;
    }

    setError(error);
    // Don't clear authentication on stats error - allow user to retry
    // Reset character creation state
    setSelectedProfession(undefined);
    setCreationStep(null);
  };

  const handleStatsRollingBack = () => {
    setCreationStep(null);
    if (characters.length > 0) {
      setShowCharacterSelection(true);
    } else {
      returnToLogin();
    }
  };

  // Helper function to detect server unavailability
  const isServerUnavailable = (error: unknown, response: Response | null): boolean => {
    // Network errors (fetch throws, no response)
    if (!response) {
      return true;
    }

    // 5xx server errors indicate server unavailability
    if (response.status >= 500 && response.status < 600) {
      return true;
    }

    // Check for connection-related errors in error message
    if (error instanceof Error) {
      const errorMessage = error.message.toLowerCase();
      const connectionErrors = [
        'failed to fetch',
        'network error',
        'network request failed',
        'connection refused',
        'connection reset',
        'connection closed',
        'connection timeout',
        'err_connection_refused',
        'err_connection_reset',
        'err_connection_aborted',
      ];
      return connectionErrors.some(err => errorMessage.includes(err));
    }

    return false;
  };

  // Helper function to return to login screen
  const returnToLogin = () => {
    setIsAuthenticated(false);
    setCharacters([]);
    setSelectedCharacterName('');
    setSelectedCharacterId('');
    setShowCharacterSelection(false);
    setShowMotd(false);
    setCreationStep(null);
    setAuthToken('');
    secureTokenStorage.clearAllTokens();
    setError('Server is unavailable. Please try again later.');
  };

  // MULTI-CHARACTER: Character selection handler
  const handleCharacterSelected = async (characterId: string) => {
    try {
      const response = await fetch(`${API_V1_BASE}/api/players/select-character`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({ character_id: characterId }),
      });

      if (!response.ok) {
        // Check if server is unavailable
        if (isServerUnavailable(null, response)) {
          returnToLogin();
          return;
        }

        let errorMessage = 'Failed to select character';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (isObject(rawData)) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        setError(errorMessage);
        return;
      }

      const rawData: unknown = await response.json();
      // Character selection response may be a single character or a simple response
      // Validate as ServerCharacterResponse if possible, otherwise extract fields safely
      let selectedId = characterId;
      let selectedName = '';
      if (isServerCharacterResponse(rawData)) {
        selectedId = rawData.player_id || rawData.id || characterId;
        selectedName = rawData.name;
      } else if (isObject(rawData)) {
        const characterData = rawData as Record<string, unknown>;
        selectedId =
          (typeof characterData.id === 'string' ? characterData.id : null) ||
          (typeof characterData.player_id === 'string' ? characterData.player_id : null) ||
          characterId;
        selectedName = typeof characterData.name === 'string' ? characterData.name : '';
      }
      setSelectedCharacterName(selectedName);
      // Store the selected character ID for WebSocket connection
      setSelectedCharacterId(selectedId);
      setShowCharacterSelection(false);
      // Show MOTD screen after character selection
      setShowMotd(true);
    } catch (error) {
      // Check if error is due to server unavailability
      if (isServerUnavailable(error, null)) {
        returnToLogin();
        return;
      }

      const errorMessage = error instanceof Error ? error.message : 'Failed to select character';
      setError(errorMessage);
    }
  };

  // MULTI-CHARACTER: Character deletion handler
  const handleDeleteCharacter = async (characterId: string) => {
    try {
      const response = await fetch(`${API_V1_BASE}/api/players/characters/${characterId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        // Check if server is unavailable
        if (isServerUnavailable(null, response)) {
          returnToLogin();
          return;
        }

        let errorMessage = 'Failed to delete character';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (isObject(rawData)) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        throw new Error(errorMessage);
      }

      // Refresh characters list after deletion
      const charactersResponse = await fetch(`${API_V1_BASE}/api/players/characters`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (charactersResponse.ok) {
        const rawData: unknown = await charactersResponse.json();
        const charactersList = assertServerCharacterResponseArray(
          rawData,
          'Invalid API response: expected ServerCharacterResponse[]'
        );
        // Map server response (id) to client interface (player_id)
        const mappedCharacters = charactersList.map(
          (c: ServerCharacterResponse): CharacterInfo => ({
            player_id: c.player_id || c.id || '',
            name: c.name,
            profession_id: c.profession_id,
            profession_name: c.profession_name,
            level: c.level,
            created_at: c.created_at,
            last_active: c.last_active,
          })
        );
        setCharacters(mappedCharacters);

        // If last character was deleted, show profession selection screen for character creation
        if (mappedCharacters.length === 0) {
          setShowCharacterSelection(false);
          setCreationStep('stats');
          setSelectedProfession(undefined);
        }
      } else {
        // Check if server is unavailable
        if (isServerUnavailable(null, charactersResponse)) {
          returnToLogin();
          return;
        }

        // Character was deleted but refresh failed - log error and show message
        let errorMessage = 'Character deleted, but failed to refresh character list';
        try {
          const rawData: unknown = await charactersResponse.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (isObject(rawData)) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        console.error('Failed to refresh characters list after deletion:', errorMessage);
        setError(errorMessage);
        // Still throw to indicate partial failure; include response context as cause for diagnostics
        const deletionError = new Error(errorMessage);
        (deletionError as Error & { cause?: unknown }).cause = {
          status: response.status,
          statusText: response.statusText,
        };
        throw deletionError;
      }
    } catch (error) {
      // Check if error is due to server unavailability
      if (isServerUnavailable(error, null)) {
        returnToLogin();
        return;
      }

      const errorMessage = error instanceof Error ? error.message : 'Failed to delete character';
      // Preserve original error as cause so callers and logs can inspect root failure.
      const deletionError = new Error(errorMessage);
      (deletionError as Error & { cause?: unknown }).cause = error;
      throw deletionError;
    }
  };

  const handleCreateCharacter = () => {
    setPendingStats(null);
    setSelectedProfession(undefined);
    setPendingSkillsPayload(null);
    setCreationStep('stats');
    setShowCharacterSelection(false);
    setSelectedCharacterName('');
    setSelectedCharacterId('');
  };

  const handleMotdContinue = async () => {
    // The token should be in state from successful login (which also stored it in localStorage)
    // Since tokens are cleared on mount and login happens after mount, the token in state
    // is the source of truth for this session. We don't need to restore from storage
    // because storage was cleared on mount and then repopulated during login.
    if (!authToken) {
      // Token is missing from state - this should not happen if user just logged in successfully
      // If it does, redirect to login. This indicates a state loss issue that needs investigation.
      setError('Authentication token is missing. Please log in again.');
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setShowMotd(false);
      setShowCharacterSelection(false);
      return;
    }

    // Start login grace period when MOTD is dismissed
    if (selectedCharacterId) {
      try {
        const response = await fetch(`${API_V1_BASE}/api/players/${selectedCharacterId}/start-login-grace-period`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${authToken}`,
          },
        });

        if (!response.ok) {
          // Check if server is unavailable - if so, return to login
          if (isServerUnavailable(null, response)) {
            returnToLogin();
            return;
          }

          // Log error but don't block game entry - grace period is best effort
          try {
            const rawData: unknown = await response.json();
            if (isErrorResponse(rawData)) {
              console.warn('Failed to start login grace period:', getErrorMessage(rawData));
            } else if (isObject(rawData)) {
              const errorData = rawData as Record<string, unknown>;
              const detail = typeof errorData.detail === 'string' ? errorData.detail : 'Unknown error';
              console.warn('Failed to start login grace period:', detail);
            } else {
              console.warn('Failed to start login grace period: Unknown error');
            }
          } catch {
            console.warn('Failed to start login grace period: Unknown error');
          }
        }
      } catch (error) {
        // Check if error is due to server unavailability
        if (isServerUnavailable(error, null)) {
          returnToLogin();
          return;
        }

        // Log error but don't block game entry - grace period is best effort
        console.warn('Error starting login grace period:', error);
      }
    }

    // Proceed to game terminal - token is already in state and storage from login
    setShowMotd(false);
  };

  const handleMotdReturnToLogin = () => {
    // Clear all state and return to login
    setIsAuthenticated(false);
    setCharacters([]);
    setSelectedCharacterName('');
    setSelectedCharacterId('');
    setPlayerName('');
    setPassword('');
    setInviteCode('');
    setAuthToken('');
    setShowMotd(false);
    setShowCharacterSelection(false);
    secureTokenStorage.clearAllTokens();
    focusUsernameInput();
  };

  // Reference to store the disconnect callback from GameClientV2Container
  const disconnectCallbackRef = useRef<(() => void) | null>(null);

  // Reference to the username input for focus management
  const usernameInputRef = useRef<HTMLInputElement | null>(null);

  // Callback to register the disconnect function from GameClientV2Container
  const handleDisconnectCallback = (disconnectFn: () => void) => {
    disconnectCallbackRef.current = disconnectFn;
  };

  // Function to focus the username input for accessibility
  const focusUsernameInput = () => {
    // Use setTimeout to ensure the DOM has updated after state changes
    setTimeout(() => {
      if (usernameInputRef.current) {
        usernameInputRef.current.focus();
      }
    }, 0);
  };

  const handleLogout = async () => {
    if (isLoggingOut) return; // Prevent multiple logout attempts

    setIsLoggingOut(true);
    setError(null);

    // Helper function to clear all state
    const clearAllState = () => {
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setPlayerName('');
      setPassword('');
      setInviteCode('');
      setAuthToken('');
      setError(null);
      setShowCharacterSelection(false);
      secureTokenStorage.clearAllTokens();

      // Focus the username input for accessibility
      focusUsernameInput();
    };

    try {
      await logoutHandler({
        authToken,
        disconnect: () => {
          // Call the disconnect callback from GameClientV2Container
          if (disconnectCallbackRef.current) {
            disconnectCallbackRef.current();
          }
        },
        clearState: clearAllState,
        navigateToLogin: clearAllState,
        timeout: 5000,
      });
    } catch (error) {
      // Even if logout handler fails, we should still return to login
      console.error('Logout failed:', error);
      setError(error instanceof Error ? error.message : 'Logout failed');

      // Force return to login screen regardless of server response
      // Clear all state except the error message
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setPlayerName('');
      setPassword('');
      setInviteCode('');
      setAuthToken('');
      setShowCharacterSelection(false);
      secureTokenStorage.clearAllTokens();

      // Focus the username input for accessibility
      focusUsernameInput();
    } finally {
      setIsLoggingOut(false);
    }
  };

  const toggleMode = () => {
    setIsRegistering(!isRegistering);
    setError(null);
    // Clear form fields when toggling between modes
    setPlayerName('');
    setPassword('');
    setInviteCode('');
  };

  const handleKeyDown = (event: React.KeyboardEvent) => {
    if (event.key === 'Enter') {
      // Only trigger login/register if both username and password are filled
      if (playerName.trim() && password.trim()) {
        // For registration, also require invite code
        if (isRegistering && !inviteCode.trim()) {
          return;
        }
        // Trigger the appropriate action
        if (isRegistering) {
          void handleRegisterClick();
        } else {
          void handleLoginClick();
        }
      }
    }
  };

  if (showDemo) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <EldritchEffectsDemo
            onExit={() => {
              setShowDemo(false);
            }}
          />
        </Suspense>
      </div>
    );
  }

  if (!isAuthenticated) {
    return (
      <div className="App">
        <div className="login-container">
          <div className="login-form">
            <h1 className="login-title">MythosMUD</h1>
            <p className="login-subtitle">Enter the realm of eldritch knowledge</p>

            <div className="login-inputs">
              <input
                ref={usernameInputRef}
                type="text"
                placeholder="Username"
                className="login-input"
                value={playerName}
                onChange={e => {
                  setPlayerName(e.target.value);
                }}
                onKeyDown={handleKeyDown}
                data-testid="username-input"
              />
              <input
                type="password"
                placeholder="Password"
                className="login-input"
                value={password}
                onChange={e => {
                  setPassword(e.target.value);
                }}
                onKeyDown={handleKeyDown}
                data-testid="password-input"
              />
              {isRegistering && (
                <input
                  type="text"
                  placeholder="Invite Code"
                  className="login-input"
                  value={inviteCode}
                  onChange={e => {
                    setInviteCode(e.target.value);
                  }}
                  onKeyDown={handleKeyDown}
                />
              )}
            </div>

            {error ? <div className="error-message">{error}</div> : null}

            <button
              className="login-button"
              onClick={isRegistering ? handleRegisterClick : handleLoginClick}
              disabled={isSubmitting}
              data-testid="login-button"
            >
              {isSubmitting
                ? isRegistering
                  ? 'Registering…'
                  : 'Authenticating…'
                : isRegistering
                  ? 'Enter the Void'
                  : 'Enter the Void'}
            </button>

            <div className="mode-toggle">
              <button
                onClick={toggleMode}
                className="text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary transition-colors"
              >
                {isRegistering ? 'Already have an account? Login' : 'Need an account? Register'}
              </button>
            </div>

            <div className="demo-button">
              <button
                onClick={() => {
                  setShowDemo(true);
                }}
                className="text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary transition-colors"
              >
                View Eldritch Effects Demo
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // MULTI-CHARACTER: Show character selection screen if user has characters
  if (isAuthenticated && showCharacterSelection && characters.length > 0) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <CharacterSelectionScreen
            characters={characters}
            onCharacterSelected={handleCharacterSelected}
            onCreateCharacter={handleCreateCharacter}
            onDeleteCharacter={handleDeleteCharacter}
            onError={setError}
            baseUrl={API_V1_BASE}
            authToken={authToken}
          />
        </Suspense>
      </div>
    );
  }

  // Plan 10.6: character creation flow (stats -> profession -> skills -> name)
  if (isAuthenticated && creationStep !== null) {
    if (creationStep === 'stats') {
      return (
        <div className="App">
          <Suspense fallback={<LoadingFallback />}>
            <StatsRollingScreen
              onStatsAccepted={handleStatsAccepted}
              onError={handleStatsError}
              onBack={handleStatsRollingBack}
              baseUrl={API_V1_BASE}
              authToken={authToken}
            />
          </Suspense>
        </div>
      );
    }
    if (creationStep === 'profession') {
      return (
        <div className="App">
          <Suspense fallback={<LoadingFallback />}>
            <ProfessionSelectionScreen
              onProfessionSelected={handleProfessionSelected}
              onError={handleProfessionSelectionError}
              onBack={handleProfessionSelectionBack}
              baseUrl={API_V1_BASE}
              authToken={authToken}
            />
          </Suspense>
        </div>
      );
    }
    if (creationStep === 'skills') {
      return (
        <div className="App">
          <Suspense fallback={<LoadingFallback />}>
            <SkillAssignmentScreen
              baseUrl={API_V1_BASE}
              authToken={authToken}
              onSkillsConfirmed={payload => {
                setPendingSkillsPayload(payload);
                setCreationStep('name');
              }}
              onBack={() => {
                setCreationStep('profession');
              }}
              onError={handleStatsError}
            />
          </Suspense>
        </div>
      );
    }
    if (creationStep === 'name' && pendingStats && selectedProfession && pendingSkillsPayload) {
      return (
        <div className="App">
          <Suspense fallback={<LoadingFallback />}>
            <CharacterNameScreen
              stats={pendingStats}
              profession={selectedProfession}
              skillsPayload={pendingSkillsPayload}
              baseUrl={API_V1_BASE}
              authToken={authToken}
              onComplete={handleCreationComplete}
              onError={handleStatsError}
              onBack={() => {
                setCreationStep('skills');
              }}
            />
          </Suspense>
        </div>
      );
    }
    if (creationStep === 'name') {
      setCreationStep('skills');
      return null;
    }
  }

  if (showMotd) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <MotdInterstitialScreen onContinue={handleMotdContinue} onReturnToLogin={handleMotdReturnToLogin} />
        </Suspense>
      </div>
    );
  }

  // Ensure we have a valid token before rendering GameClientV2Container
  // Restore from secure storage if state was lost (defensive check)
  const finalAuthToken = authToken || secureTokenStorage.getToken() || '';

  // Defensive validation: If token is missing despite being authenticated, restore it or redirect
  if (!finalAuthToken) {
    // Token is missing - redirect to login
    // This should not happen in normal flow but protects against state loss
    setIsAuthenticated(false);
    setCharacters([]);
    setSelectedCharacterName('');
    setSelectedCharacterId('');
    setError('Session expired. Please log in again.');
    // The component will re-render and show login screen due to !isAuthenticated check above
    return null;
  }

  // Ensure token is in state if it was only in storage
  if (!authToken && finalAuthToken) {
    setAuthToken(finalAuthToken);
  }

  return (
    <div className="App">
      <Suspense fallback={<LoadingFallback />}>
        <GameClientV2Container
          playerName={selectedCharacterName || playerName}
          authToken={finalAuthToken}
          characterId={selectedCharacterId}
          onLogout={handleLogout}
          isLoggingOut={isLoggingOut}
          onDisconnect={handleDisconnectCallback}
        />
      </Suspense>
    </div>
  );
}

export { App };
