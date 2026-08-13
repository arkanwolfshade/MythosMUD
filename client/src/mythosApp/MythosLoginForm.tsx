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

function LoginInputs({
  usernameInputRef,
  playerName,
  setPlayerName,
  password,
  setPassword,
  inviteCode,
  setInviteCode,
  isRegistering,
  handleKeyDown,
}: Pick<
  MythosLoginFormProps,
  | 'usernameInputRef'
  | 'playerName'
  | 'setPlayerName'
  | 'password'
  | 'setPassword'
  | 'inviteCode'
  | 'setInviteCode'
  | 'isRegistering'
  | 'handleKeyDown'
>) {
  return (
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
  );
}

function LoginActions({
  isRegistering,
  isSubmitting,
  handleLoginClick,
  handleRegisterClick,
  toggleMode,
  setShowDemo,
}: Pick<
  MythosLoginFormProps,
  'isRegistering' | 'isSubmitting' | 'handleLoginClick' | 'handleRegisterClick' | 'toggleMode' | 'setShowDemo'
>) {
  const submitLabel = isSubmitting ? (isRegistering ? 'Registering…' : 'Authenticating…') : 'Enter the Void';
  return (
    <>
      <button
        className="login-button"
        type="button"
        onClick={isRegistering ? handleRegisterClick : handleLoginClick}
        disabled={isSubmitting}
        data-testid="login-button"
      >
        {submitLabel}
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
    </>
  );
}

export function MythosLoginForm(props: MythosLoginFormProps) {
  const { error, isRegistering, isSubmitting } = props;

  return (
    <div className="login-container">
      <div className="login-form">
        <h1 className="login-title">MythosMUD</h1>
        <p className="login-subtitle">Enter the realm of eldritch knowledge</p>
        <LoginInputs {...props} />
        {error ? <div className="error-message">{error}</div> : null}
        <LoginActions
          isRegistering={isRegistering}
          isSubmitting={isSubmitting}
          handleLoginClick={props.handleLoginClick}
          handleRegisterClick={props.handleRegisterClick}
          toggleMode={props.toggleMode}
          setShowDemo={props.setShowDemo}
        />
      </div>
    </div>
  );
}
