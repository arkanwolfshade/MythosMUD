import type { KeyboardEvent, RefObject } from 'react';

export interface MythosLoginFormProps {
  usernameInputRef: RefObject<HTMLInputElement | null>;
  playerName: string;
  setPlayerName: (v: string) => void;
  password: string;
  setPassword: (v: string) => void;
  inviteCode: string;
  setInviteCode: (v: string) => void;
  isRegistering: boolean;
  error: string | null;
  isSubmitting: boolean;
  handleKeyDown: (event: KeyboardEvent) => void;
  handleLoginClick: () => Promise<void>;
  handleRegisterClick: () => Promise<void>;
  toggleMode: () => void;
  setShowDemo: (v: boolean) => void;
}

export function MythosLoginForm(props: MythosLoginFormProps) {
  const {
    usernameInputRef,
    playerName,
    setPlayerName,
    password,
    setPassword,
    inviteCode,
    setInviteCode,
    isRegistering,
    error,
    isSubmitting,
    handleKeyDown,
    handleLoginClick,
    handleRegisterClick,
    toggleMode,
    setShowDemo,
  } = props;

  return (
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
          type="button"
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
            type="button"
            onClick={toggleMode}
            className="text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary transition-colors"
          >
            {isRegistering ? 'Already have an account? Login' : 'Need an account? Register'}
          </button>
        </div>

        <div className="demo-button">
          <button
            type="button"
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
  );
}
