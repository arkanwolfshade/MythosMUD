import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Login Flow', () => {
    it('should show login form by default', () => {
      render(<App />);

      expect(screen.getByText('MythosMUD')).toBeInTheDocument();
      expect(screen.getByText('Enter the realm of eldritch knowledge')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
      expect(screen.getByText('Enter the Void')).toBeInTheDocument();
    });

    it('should handle login form input changes', () => {
      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });

      expect(usernameInput).toHaveValue('testuser');
      expect(passwordInput).toHaveValue('testpass');
    });

    it('should show error when login fields are empty', async () => {
      render(<App />);

      const loginButton = screen.getByText('Enter the Void');
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Username and password are required')).toBeInTheDocument();
      });
    });

    it('should handle successful login', async () => {
      const charList = [
        {
          player_id: 'char-1',
          name: 'testuser',
          profession_id: 1,
          profession_name: 'Professor',
          level: 1,
          created_at: new Date().toISOString(),
          last_active: new Date().toISOString(),
        },
      ];
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(createMockLoginResponse(charList)),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/v1/auth/login'),
          expect.objectContaining({
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: 'testuser', password: 'testpass' }),
          })
        );
      });

      await waitFor(
        () => {
          const heading = screen.queryByRole('heading', { name: /Select Your Character/i });
          const motd = screen.queryByRole('button', { name: /Enter the Realm/i });
          const game = screen.queryByTestId('game-terminal');
          expect(heading ?? motd ?? game).toBeTruthy();
        },
        { timeout: 3000 }
      );
    });

    it('should handle login failure', async () => {
      const mockResponse = {
        ok: false,
        status: 401,
        json: vi.fn().mockResolvedValue({ detail: 'Invalid credentials' }),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'wrongpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Invalid credentials')).toBeInTheDocument();
      });
    });

    it('should handle login with missing access token', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({}),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Invalid login response from server')).toBeInTheDocument();
      });
    });
  });
});
