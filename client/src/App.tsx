import { useState } from 'react';
import './App.css';
import { EldritchEffectsDemo } from './components/EldritchEffectsDemo';
import { GameTerminalWithPanels } from './components/GameTerminalWithPanels';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [playerName, setPlayerName] = useState('');
  const [password, setPassword] = useState('');
  const [authToken, setAuthToken] = useState('');
  const [showDemo, setShowDemo] = useState(false); // Demo disabled for normal flow
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleLoginClick = async () => {
    if (!playerName || !password) {
      setError('Username and password are required');
      return;
    }
    setIsSubmitting(true);
    setError(null);
    try {
      const response = await fetch('/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: playerName, password }),
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
      if (!token) throw new Error('No access_token in response');
      setAuthToken(token);
      setIsAuthenticated(true);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  };

  // Demo mode for testing eldritch effects (disabled for normal flow)
  if (showDemo) {
    return (
      <div className="App">
        <div className="demo-controls fixed top-4 right-4 z-50">
          <button
            onClick={() => setShowDemo(false)}
            className="bg-mythos-terminal-primary text-black px-4 py-2 rounded font-mono hover:bg-green-400 transition-colors"
          >
            Exit Demo
          </button>
        </div>
        <EldritchEffectsDemo />
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
            </div>

            {error ? <div className="error-message">{error}</div> : null}

            <button className="login-button" onClick={handleLoginClick} disabled={isSubmitting}>
              {isSubmitting ? 'Authenticating…' : 'Enter the Void'}
            </button>

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

  return (
    <div className="App">
      <GameTerminalWithPanels playerName={playerName} authToken={authToken} />
    </div>
  );
}

export default App;
