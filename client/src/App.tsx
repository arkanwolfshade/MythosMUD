import { lazy, Suspense, useEffect, useRef, useState } from 'react';
import './App.css';
import { API_BASE_URL } from './utils/config';
import { logoutHandler } from './utils/logoutHandler';
import { memoryMonitor } from './utils/memoryMonitor';
import { inputSanitizer, secureTokenStorage } from './utils/security';

// Lazy load screen components for code splitting
// AI: Lazy loading reduces initial bundle size by ~30-50% and improves initial page load time
const EldritchEffectsDemo = lazy(() =>
  import('./components/EldritchEffectsDemo').then(m => ({ default: m.EldritchEffectsDemo }))
);
const GameClientV2Container = lazy(() =>
  import('./components/ui-v2/GameClientV2Container').then(m => ({ default: m.GameClientV2Container }))
);
const MotdInterstitialScreen = lazy(() =>
  import('./components/MotdInterstitialScreen').then(m => ({ default: m.MotdInterstitialScreen }))
);
const ProfessionSelectionScreen = lazy(() =>
  import('./components/ProfessionSelectionScreen').then(m => ({ default: m.ProfessionSelectionScreen }))
);
const StatsRollingScreen = lazy(() =>
  import('./components/StatsRollingScreen').then(m => ({ default: m.StatsRollingScreen }))
);

// Import types that are needed for props
import type { Profession } from './components/ProfessionCard';

// Import the Stats interface from StatsRollingScreen
interface Stats {
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;
}

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [hasCharacter, setHasCharacter] = useState(false);
  const [characterName, setCharacterName] = useState('');
  const [playerName, setPlayerName] = useState('');
  const [password, setPassword] = useState('');
  const [inviteCode, setInviteCode] = useState('');
  const [authToken, setAuthToken] = useState('');
  const [showDemo, setShowDemo] = useState(false); // Demo disabled for normal flow
  const [showMotd, setShowMotd] = useState(false); // Track MOTD display state

  // Character creation flow state
  const [selectedProfession, setSelectedProfession] = useState<Profession | undefined>(undefined);
  const [showProfessionSelection, setShowProfessionSelection] = useState(false);

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
  useEffect(() => {
    // Clear all stored tokens to force fresh authentication
    // This ensures that after server restart, clients cannot use stale tokens
    secureTokenStorage.clearAllTokens();

    // Also clear any auth state that might have been restored
    setAuthToken('');
    setIsAuthenticated(false);
    setHasCharacter(false);
    setCharacterName('');
    setShowMotd(false);
  }, []); // Only run on mount

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
      const response = await fetch('/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: sanitizedUsername, password: sanitizedPassword }),
      });
      if (!response.ok) {
        let message = `Login failed (${response.status})`;
        try {
          const data = await response.json();
          message = data?.error?.message || data?.detail || message;
        } catch {
          // Ignore JSON parsing errors, use default message
        }
        throw new Error(message);
      }
      const data = await response.json();
      const token = data?.access_token as string | undefined;
      const refreshToken = data?.refresh_token as string | undefined;

      if (!token) throw new Error('No access_token in response');

      // Store tokens securely
      secureTokenStorage.setToken(token);
      if (refreshToken) {
        secureTokenStorage.setRefreshToken(refreshToken);
      }

      setAuthToken(token);
      setIsAuthenticated(true);
      setHasCharacter(data?.has_character || false);
      setCharacterName(data?.character_name || '');

      // For new users without characters, show profession selection
      if (!data?.has_character) {
        setShowProfessionSelection(true);
      } else {
        // For existing users with characters, show MOTD screen
        setShowMotd(true);
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
      const response = await fetch('/auth/register', {
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
          const data = await response.json();
          message = data?.error?.message || data?.detail || message;
        } catch {
          // Ignore JSON parsing errors, use default message
        }
        throw new Error(message);
      }
      const data = await response.json();
      const token = data?.access_token as string | undefined;
      const refreshToken = data?.refresh_token as string | undefined;

      if (!token) throw new Error('No access_token in response');

      // Store tokens securely
      secureTokenStorage.setToken(token);
      if (refreshToken) {
        secureTokenStorage.setRefreshToken(refreshToken);
      }

      setAuthToken(token);
      setIsAuthenticated(true);
      setHasCharacter(data?.has_character || false);
      setCharacterName(data?.character_name || '');

      // For new users without characters, show profession selection
      if (!data?.has_character) {
        setShowProfessionSelection(true);
      } else {
        // For existing users with characters, show MOTD screen
        setShowMotd(true);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleProfessionSelected = (profession: Profession) => {
    setSelectedProfession(profession);
    setShowProfessionSelection(false);
  };

  const handleProfessionSelectionBack = () => {
    setShowProfessionSelection(false);
    setSelectedProfession(undefined);
    // Go back to login screen
    setIsAuthenticated(false);
    setHasCharacter(false);
    setCharacterName('');
    setPlayerName('');
    setPassword('');
    setInviteCode('');
    setAuthToken('');
  };

  const handleProfessionSelectionError = (error: string) => {
    setError(error);
  };

  const handleStatsAccepted = (_stats: Stats) => {
    setHasCharacter(true);
    setCharacterName(playerName);
    // Reset character creation state
    setSelectedProfession(undefined);
    setShowProfessionSelection(false);
    // Show MOTD screen after character creation
    setShowMotd(true);
  };

  const handleStatsError = (error: string) => {
    setError(error);
    setIsAuthenticated(false);
    setAuthToken('');
    // Clear secure tokens
    secureTokenStorage.clearAllTokens();
    // Reset character creation state
    setSelectedProfession(undefined);
    setShowProfessionSelection(false);
  };

  const handleStatsRollingBack = () => {
    setShowProfessionSelection(true);
  };

  const handleMotdContinue = () => {
    // The token should be in state from successful login (which also stored it in localStorage)
    // Since tokens are cleared on mount and login happens after mount, the token in state
    // is the source of truth for this session. We don't need to restore from storage
    // because storage was cleared on mount and then repopulated during login.
    if (!authToken) {
      // Token is missing from state - this should not happen if user just logged in successfully
      // If it does, redirect to login. This indicates a state loss issue that needs investigation.
      setError('Authentication token is missing. Please log in again.');
      setIsAuthenticated(false);
      setHasCharacter(false);
      setShowMotd(false);
      return;
    }

    // Proceed to game terminal - token is already in state and storage from login
    setShowMotd(false);
  };

  const handleMotdReturnToLogin = () => {
    // Clear all state and return to login
    setIsAuthenticated(false);
    setHasCharacter(false);
    setCharacterName('');
    setPlayerName('');
    setPassword('');
    setInviteCode('');
    setAuthToken('');
    setShowMotd(false);
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
      setHasCharacter(false);
      setCharacterName('');
      setPlayerName('');
      setPassword('');
      setInviteCode('');
      setAuthToken('');
      setError(null);
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
      setHasCharacter(false);
      setCharacterName('');
      setPlayerName('');
      setPassword('');
      setInviteCode('');
      setAuthToken('');
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
          handleRegisterClick();
        } else {
          handleLoginClick();
        }
      }
    }
  };

  // Loading fallback component for lazy-loaded screens
  const LoadingFallback = () => (
    <div className="App flex items-center justify-center min-h-screen bg-mythos-terminal-background">
      <div className="text-mythos-terminal-text font-mono">Loading...</div>
    </div>
  );

  if (showDemo) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <EldritchEffectsDemo onExit={() => setShowDemo(false)} />
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
                onChange={e => setPlayerName(e.target.value)}
                onKeyDown={handleKeyDown}
                data-testid="username-input"
              />
              <input
                type="password"
                placeholder="Password"
                className="login-input"
                value={password}
                onChange={e => setPassword(e.target.value)}
                onKeyDown={handleKeyDown}
                data-testid="password-input"
              />
              {isRegistering && (
                <input
                  type="text"
                  placeholder="Invite Code"
                  className="login-input"
                  value={inviteCode}
                  onChange={e => setInviteCode(e.target.value)}
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
                onClick={() => setShowDemo(true)}
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

  // If authenticated but no character, show character creation flow
  if (!hasCharacter) {
    // Show profession selection screen first
    if (showProfessionSelection) {
      return (
        <div className="App">
          <Suspense fallback={<LoadingFallback />}>
            <ProfessionSelectionScreen
              characterName={playerName}
              onProfessionSelected={handleProfessionSelected}
              onError={handleProfessionSelectionError}
              onBack={handleProfessionSelectionBack}
              baseUrl={API_BASE_URL}
              authToken={authToken}
            />
          </Suspense>
        </div>
      );
    }

    // Show stats rolling screen after profession selection
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <StatsRollingScreen
            characterName={playerName}
            onStatsAccepted={handleStatsAccepted}
            onError={handleStatsError}
            onBack={handleStatsRollingBack}
            baseUrl={API_BASE_URL}
            authToken={authToken}
            professionId={selectedProfession?.id}
            profession={selectedProfession as Profession | undefined}
          />
        </Suspense>
      </div>
    );
  }

  // If authenticated and has character, show MOTD screen or game terminal
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
    setHasCharacter(false);
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
          playerName={characterName || playerName}
          authToken={finalAuthToken}
          onLogout={handleLogout}
          isLoggingOut={isLoggingOut}
          onDisconnect={handleDisconnectCallback}
        />
      </Suspense>
    </div>
  );
}

export default App;
