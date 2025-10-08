import { useEffect, useRef, useState } from 'react';
import './App.css';
import { EldritchEffectsDemo } from './components/EldritchEffectsDemo';
import { GameTerminalWithPanels } from './components/GameTerminalWithPanels';
import { Profession, ProfessionSelectionScreen } from './components/ProfessionSelectionScreen';
import { StatsRollingScreen } from './components/StatsRollingScreen';
import { logoutHandler } from './utils/logoutHandler';
import { memoryMonitor } from './utils/memoryMonitor';
import { inputSanitizer, secureTokenStorage } from './utils/security';

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

  // Character creation flow state
  const [selectedProfession, setSelectedProfession] = useState<Profession | null>(null);
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
    setSelectedProfession(null);
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
    setSelectedProfession(null);
    setShowProfessionSelection(false);
  };

  const handleStatsError = (error: string) => {
    setError(error);
    setIsAuthenticated(false);
    setAuthToken('');
    // Clear secure tokens
    secureTokenStorage.clearAllTokens();
    // Reset character creation state
    setSelectedProfession(null);
    setShowProfessionSelection(false);
  };

  const handleStatsRollingBack = () => {
    setShowProfessionSelection(true);
  };

  // Reference to store the disconnect callback from GameTerminalWithPanels
  const disconnectCallbackRef = useRef<(() => void) | null>(null);

  // Reference to the username input for focus management
  const usernameInputRef = useRef<HTMLInputElement | null>(null);

  // Callback to register the disconnect function from GameTerminalWithPanels
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
          // Call the disconnect callback from GameTerminalWithPanels
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

  if (showDemo) {
    return (
      <div className="App">
        <EldritchEffectsDemo onExit={() => setShowDemo(false)} />
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
          <ProfessionSelectionScreen
            characterName={playerName}
            onProfessionSelected={handleProfessionSelected}
            onError={handleProfessionSelectionError}
            onBack={handleProfessionSelectionBack}
            baseUrl="http://localhost:54731"
            authToken={authToken}
          />
        </div>
      );
    }

    // Show stats rolling screen after profession selection
    return (
      <div className="App">
        <StatsRollingScreen
          characterName={playerName}
          onStatsAccepted={handleStatsAccepted}
          onError={handleStatsError}
          onBack={handleStatsRollingBack}
          baseUrl="http://localhost:54731"
          authToken={authToken}
          professionId={selectedProfession?.id}
          profession={selectedProfession}
        />
      </div>
    );
  }

  // If authenticated and has character, show game terminal
  return (
    <div className="App">
      <GameTerminalWithPanels
        playerName={characterName}
        authToken={authToken}
        onLogout={handleLogout}
        isLoggingOut={isLoggingOut}
        onDisconnect={handleDisconnectCallback}
      />
    </div>
  );
}

export default App;
