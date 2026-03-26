import { assertLoginResponse } from '../utils/apiTypeGuards.js';
import { API_V1_BASE } from '../utils/config.js';
import { inputSanitizer } from '../utils/security.js';
import { loginFailureMessage } from './loginFailureMessage.js';
import { registerFailureMessage } from './registerFailureMessage.js';

export interface SanitizedCredentials {
  username: string;
  password: string;
}

export function sanitizeLoginInputs(playerName: string, password: string): SanitizedCredentials | null {
  const sanitizedUsername = inputSanitizer.sanitizeUsername(playerName);
  const sanitizedPassword = inputSanitizer.sanitizeCommand(password);
  if (!sanitizedUsername || !sanitizedPassword) {
    return null;
  }
  return { username: sanitizedUsername, password: sanitizedPassword };
}

export function sanitizeRegisterInputs(
  playerName: string,
  password: string,
  inviteCode: string
): (SanitizedCredentials & { inviteCode: string }) | null {
  const sanitizedUsername = inputSanitizer.sanitizeUsername(playerName);
  const sanitizedPassword = inputSanitizer.sanitizeCommand(password);
  const sanitizedInviteCode = inputSanitizer.sanitizeCommand(inviteCode);
  if (!sanitizedUsername || !sanitizedPassword || !sanitizedInviteCode) {
    return null;
  }
  return { username: sanitizedUsername, password: sanitizedPassword, inviteCode: sanitizedInviteCode };
}

export async function submitLoginRequest(creds: SanitizedCredentials) {
  const response = await fetch(`${API_V1_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: creds.username, password: creds.password }),
  });
  if (!response.ok) {
    let message = `Login failed (${response.status})`;
    try {
      const rawData: unknown = await response.json();
      message = loginFailureMessage(rawData, message);
    } catch {
      // Ignore JSON parse errors
    }
    throw new Error(message);
  }
  const rawData: unknown = await response.json();
  return assertLoginResponse(rawData, 'Invalid login response from server');
}

export async function submitRegisterRequest(creds: SanitizedCredentials & { inviteCode: string }) {
  const response = await fetch(`${API_V1_BASE}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: creds.username,
      password: creds.password,
      invite_code: creds.inviteCode,
    }),
  });
  if (!response.ok) {
    let message = `Registration failed (${response.status})`;
    try {
      const rawData: unknown = await response.json();
      message = registerFailureMessage(response.status, rawData, message);
    } catch {
      // Ignore JSON parse errors
    }
    throw new Error(message);
  }
  const rawData: unknown = await response.json();
  return assertLoginResponse(rawData, 'Invalid registration response from server');
}

export type AuthSuccessPayload = Awaited<ReturnType<typeof submitLoginRequest>>;
