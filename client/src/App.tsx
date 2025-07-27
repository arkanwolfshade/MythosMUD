import { useState } from "react";
import "./App.css";
import { GameTerminal } from "./components/GameTerminal";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [playerId, setPlayerId] = useState("");
  const [authToken, setAuthToken] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [showRegistration, setShowRegistration] = useState(false);
  const [inviteCode, setInviteCode] = useState("");

  const baseUrl = import.meta.env.VITE_API_URL || "/api";

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError("");

    try {
      const response = await fetch(`${baseUrl}/auth/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setAuthToken(data.access_token);
        setPlayerId(username); // Use username as player ID since server doesn't return player_id
        setIsAuthenticated(true);
      } else {
        const errorData = await response.json();
        setError(errorData.detail || "Login failed");
      }
    } catch {
      setError("Failed to connect to server");
    } finally {
      setIsLoading(false);
    }
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setPlayerId("");
    setAuthToken("");
    setUsername("");
    setPassword("");
    setError("");
    setShowRegistration(false);
    setInviteCode("");
  };

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError("");

    try {
      const response = await fetch(`${baseUrl}/auth/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
          invite_code: inviteCode,
        }),
      });

      if (response.ok) {
        await response.json();
        setError("");
        setShowRegistration(false);
        setInviteCode("");
        // Show success message and switch to login
        alert("Registration successful! You may now log in.");
      } else {
        const errorData = await response.json();
        setError(errorData.detail || "Registration failed");
      }
    } catch {
      setError("Failed to connect to server");
    } finally {
      setIsLoading(false);
    }
  };

  if (isAuthenticated) {
    return (
      <div className="app">
        <header className="app-header">
          <h1>MythosMUD</h1>
          <button onClick={handleLogout} className="logout-button">
            Logout
          </button>
        </header>
        <GameTerminal playerId={playerId} authToken={authToken} />
      </div>
    );
  }

  return (
    <div className="app">
      <div className="login-container">
        <h1>MythosMUD</h1>
        <p className="subtitle">Enter the realm of forbidden knowledge...</p>

        {!showRegistration ? (
          <>
            <form onSubmit={handleLogin} className="login-form">
              <div className="form-group">
                <label htmlFor="username">Username:</label>
                <input
                  id="username"
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                  placeholder="Enter your username"
                />
              </div>

              <div className="form-group">
                <label htmlFor="password">Password:</label>
                <input
                  id="password"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  placeholder="Enter your password"
                />
              </div>

              {error && <div className="error-message">{error}</div>}

              <button type="submit" disabled={isLoading} className="login-button">
                {isLoading ? "Connecting..." : "Enter the MUD"}
              </button>
            </form>

            <div className="form-footer">
              <p>Don't have an account?</p>
              <button type="button" onClick={() => setShowRegistration(true)} className="secondary-button">
                Register with Invite Code
              </button>
            </div>
          </>
        ) : (
          <>
            <form onSubmit={handleRegister} className="login-form">
              <div className="form-group">
                <label htmlFor="reg-username">Username:</label>
                <input
                  id="reg-username"
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                  placeholder="Choose a username"
                />
              </div>

              <div className="form-group">
                <label htmlFor="reg-password">Password:</label>
                <input
                  id="reg-password"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  placeholder="Choose a password"
                />
              </div>

              <div className="form-group">
                <label htmlFor="invite-code">Invite Code:</label>
                <input
                  id="invite-code"
                  type="text"
                  value={inviteCode}
                  onChange={(e) => setInviteCode(e.target.value)}
                  required
                  placeholder="Enter your invite code"
                />
              </div>

              {error && <div className="error-message">{error}</div>}

              <button type="submit" disabled={isLoading} className="login-button">
                {isLoading ? "Creating Account..." : "Create Account"}
              </button>
            </form>

            <div className="form-footer">
              <p>Already have an account?</p>
              <button type="button" onClick={() => setShowRegistration(false)} className="secondary-button">
                Back to Login
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
