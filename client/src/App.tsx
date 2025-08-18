import React, { useState } from 'react';
import './App.css';
import { GameTerminalWithPanels } from './components/GameTerminalWithPanels';
import { logger } from './utils/logger';

interface LoginFormData {
  username: string;
  password: string;
}

interface User {
  id: string;
  name: string;
  authToken: string;
}

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [user, setUser] = useState<User | null>(null);
  const [formData, setFormData] = useState<LoginFormData>({
    username: '',
    password: '',
  });

  const baseUrl = import.meta.env.VITE_API_URL || '/api';
  logger.info('App', 'Component initialized', { baseUrl });

  const handleInputChange = (field: keyof LoginFormData) => (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({
      ...prev,
      [field]: e.target.value,
    }));
    setError(null); // Clear error when user starts typing
  };

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      // For now, we'll simulate a successful login
      // In a real implementation, this would make an API call
      logger.info('App', 'Attempting login', { username: formData.username });

      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Simulate successful login
      const mockUser: User = {
        id: '1',
        name: formData.username,
        authToken: 'mock-auth-token-' + Date.now(),
      };

      setUser(mockUser);
      setIsAuthenticated(true);
      logger.info('App', 'Login successful', { userId: mockUser.id, username: mockUser.name });
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Login failed';
      setError(errorMessage);
      logger.error('App', 'Login failed', { error: errorMessage });
    } finally {
      setIsLoading(false);
    }
  };

  // const handleLogout = () => {
  //   setIsAuthenticated(false);
  //   setUser(null);
  //   setFormData({ username: '', password: '' });
  //   setError(null);
  //   logger.info('App', 'User logged out');
  // };

  // Show game interface if authenticated
  if (isAuthenticated && user) {
    return <GameTerminalWithPanels playerId={user.id} playerName={user.name} authToken={user.authToken} />;
  }

  // Show login screen
  return (
    <div className="app">
      <div className="login-container">
        <h1>MythosMUD</h1>
        <p className="subtitle">Enter the realm of forbidden knowledge</p>

        <form onSubmit={handleLogin} className="login-form">
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              id="username"
              type="text"
              value={formData.username}
              onChange={handleInputChange('username')}
              placeholder="Enter your username"
              required
              disabled={isLoading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              value={formData.password}
              onChange={handleInputChange('password')}
              placeholder="Enter your password"
              required
              disabled={isLoading}
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <button
            type="submit"
            className="login-button"
            disabled={isLoading || !formData.username || !formData.password}
          >
            {isLoading ? 'Connecting...' : 'Enter the Mythos'}
          </button>
        </form>

        <div className="form-footer">
          <p>Welcome to the eldritch realm of MythosMUD</p>
          <p>Where sanity is optional and knowledge is forbidden</p>
        </div>

        <div className="debug-container">
          <button
            className="debug-button"
            onClick={() => {
              setFormData({ username: 'testuser', password: 'testpass' });
            }}
          >
            Fill Test Credentials
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
