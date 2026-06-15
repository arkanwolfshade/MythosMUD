import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Keyboard Navigation', () => {
    it('should handle Enter key in login mode', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockLoginResponse([
            {
              player_id: 'char-1',
              name: 'testuser',
              profession_id: 1,
              profession_name: 'Professor',
              level: 1,
              created_at: new Date().toISOString(),
              last_active: new Date().toISOString(),
            },
          ])
        ),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });

      // Press Enter on password field
      fireEvent.keyDown(passwordInput, { key: 'Enter', code: 'Enter' });

      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(expect.stringContaining('/v1/auth/login'), expect.any(Object));
      });
    });

    it('should handle Enter key in registration mode with all fields filled', async () => {
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
              description: 'A wandering soul',
              flavor_text: 'You wander',
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

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });

      await waitFor(() => {
        expect(usernameInput).toHaveValue('newuser');
        expect(passwordInput).toHaveValue('newpass');
        expect(inviteInput).toHaveValue('INVITE123');
      });

      // Press Enter after React state has committed (avoids CI flake under concurrent rendering)
      fireEvent.keyDown(inviteInput, { key: 'Enter', code: 'Enter' });

      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(expect.stringContaining('/v1/auth/register'), expect.any(Object));
      });
    });

    it('should not submit in registration mode if invite code is missing', () => {
      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      // Don't fill invite code

      // Press Enter - should not submit
      fireEvent.keyDown(passwordInput, { key: 'Enter', code: 'Enter' });

      // Should not make any API calls
      expect(fetchSpy).not.toHaveBeenCalled();
    });

    it('should not submit if username or password is empty', () => {
      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      // Don't fill password

      // Press Enter - should not submit
      fireEvent.keyDown(usernameInput, { key: 'Enter', code: 'Enter' });

      // Should not make any API calls
      expect(fetchSpy).not.toHaveBeenCalled();
    });

    it('should ignore non-Enter keys', () => {
      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });

      // Press a different key
      fireEvent.keyDown(passwordInput, { key: 'a', code: 'KeyA' });

      // Should not make any API calls
      expect(fetchSpy).not.toHaveBeenCalled();
    });
  });
});
