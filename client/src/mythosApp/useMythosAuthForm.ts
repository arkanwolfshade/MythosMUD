import { useCallback } from 'react';
import {
  sanitizeLoginInputs,
  sanitizeRegisterInputs,
  submitLoginRequest,
  submitRegisterRequest,
} from './submitAuth.js';
import { persistTokensAndApplySession } from './applyAuthenticatedSession.js';
import type { AuthSessionSetters } from './applyAuthenticatedSession.js';

export function useMythosAuthForm(
  playerName: string,
  password: string,
  inviteCode: string,
  setError: (v: string | null) => void,
  setIsSubmitting: (v: boolean) => void,
  authSessionSetters: AuthSessionSetters
) {
  const handleLoginClick = useCallback(async () => {
    const creds = sanitizeLoginInputs(playerName, password);
    if (!creds) {
      setError('Username and password are required');
      return;
    }
    setIsSubmitting(true);
    setError(null);
    try {
      const data = await submitLoginRequest(creds);
      persistTokensAndApplySession(data, creds.username, authSessionSetters);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  }, [playerName, password, authSessionSetters, setError, setIsSubmitting]);

  const handleRegisterClick = useCallback(async () => {
    const creds = sanitizeRegisterInputs(playerName, password, inviteCode);
    if (!creds) {
      setError('Username, password, and invite code are required');
      return;
    }
    setIsSubmitting(true);
    setError(null);
    try {
      const data = await submitRegisterRequest(creds);
      persistTokensAndApplySession(data, creds.username, authSessionSetters);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setIsSubmitting(false);
    }
  }, [playerName, password, inviteCode, authSessionSetters, setError, setIsSubmitting]);

  return { handleLoginClick, handleRegisterClick };
}
