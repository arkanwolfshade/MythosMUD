import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Registration Flow', () => {
    it('should toggle to registration mode', () => {
      render(<App />);

      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      expect(screen.getByPlaceholderText('Invite Code')).toBeInTheDocument();
      expect(screen.getByText('Already have an account? Login')).toBeInTheDocument();
    });

    it('should handle registration form input changes', () => {
      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });

      expect(usernameInput).toHaveValue('newuser');
      expect(passwordInput).toHaveValue('newpass');
      expect(inviteInput).toHaveValue('INVITE123');
    });

    it('should show error when registration fields are empty', async () => {
      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const registerButton = screen.getByText('Enter the Void');
      fireEvent.click(registerButton);

      await waitFor(() => {
        expect(screen.getByText('Username, password, and invite code are required')).toBeInTheDocument();
      });
    });

    it('should handle successful registration', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
      };

      const mockProfessionsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: [
            {
              id: 0,
              name: 'Tramp',
              description: 'A wandering soul with no particular skills or connections.',
              flavor_text:
                'You have spent your days drifting from place to place, learning to survive on your wits alone.',
              stat_requirements: [],
              mechanical_effects: [],
              is_available: true,
            },
          ],
        }),
      };

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return Promise.resolve(mockResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/v1/auth/register'),
          expect.objectContaining({
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              username: 'newuser',
              password: 'newpass',
              invite_code: 'INVITE123',
            }),
          })
        );
      });

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
    });

    it('should handle registration failure', async () => {
      const mockResponse = {
        ok: false,
        status: 400,
        json: vi.fn().mockResolvedValue({ detail: 'Invalid invite code' }),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVALID' } });
      fireEvent.click(registerButton);

      await waitFor(() => {
        expect(screen.getByText('Invalid invite code')).toBeInTheDocument();
      });
    });
  });
});
