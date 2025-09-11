import { useEffect, useState } from 'react';
import './App.css';
import { EldritchEffectsDemo } from './components/EldritchEffectsDemo';
import { GameTerminalWithPanels } from './components/GameTerminalWithPanels';
import { StatsRollingScreen } from './components/StatsRollingScreen';
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

  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isRegistering, setIsRegistering] = useState(false);

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
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleStatsAccepted = (_stats: Stats) => {
    setHasCharacter(true);
    setCharacterName(playerName);
  };

  const handleStatsError = (error: string) => {
    setError(error);
    setIsAuthenticated(false);
    setAuthToken('');
    // Clear secure tokens
    secureTokenStorage.clearToken();
  };

  const toggleMode = () => {
    setIsRegistering(!isRegistering);
    setError(null);
    // Clear form fields when toggling between modes
    setPlayerName('');
    setPassword('');
    setInviteCode('');
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
                type="text"
                placeholder="Username"
                className="login-input"
                value={playerName}
                onChange={e => setPlayerName(e.target.value)}
              />
              <input
                type="password"
                placeholder="Password"
                className="login-input"
                value={password}
                onChange={e => setPassword(e.target.value)}
              />
              {isRegistering && (
                <input
                  type="text"
                  placeholder="Invite Code"
                  className="login-input"
                  value={inviteCode}
                  onChange={e => setInviteCode(e.target.value)}
                />
              )}
            </div>

            {error ? <div className="error-message">{error}</div> : null}

            <button
              className="login-button"
              onClick={isRegistering ? handleRegisterClick : handleLoginClick}
              disabled={isSubmitting}
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

  // If authenticated but no character, show stats rolling screen
  if (!hasCharacter) {
    return (
      <div className="App">
        <StatsRollingScreen
          characterName={playerName}
          onStatsAccepted={handleStatsAccepted}
          onError={handleStatsError}
          baseUrl="http://localhost:54731"
          authToken={authToken}
        />
      </div>
    );
  }

  // If authenticated and has character, show game terminal
  return (
    <div className="App">
      <GameTerminalWithPanels playerName={characterName} authToken={authToken} />
    </div>
  );
}

export default App;
