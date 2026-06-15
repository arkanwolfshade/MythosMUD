import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Form State Management', () => {
    it('should clear form when toggling between login and register', () => {
      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      // Fill in form
      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });

      expect(usernameInput).toHaveValue('testuser');
      expect(passwordInput).toHaveValue('testpass');

      // Toggle to register
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      // Form should be cleared
      expect(usernameInput).toHaveValue('');
      expect(passwordInput).toHaveValue('');

      // Toggle back to login
      const toggleBackButton = screen.getByText('Already have an account? Login');
      fireEvent.click(toggleBackButton);

      // Form should still be cleared
      expect(usernameInput).toHaveValue('');
      expect(passwordInput).toHaveValue('');
    });

    it('should clear error when toggling modes', () => {
      render(<App />);

      // Trigger an error
      const loginButton = screen.getByText('Enter the Void');
      fireEvent.click(loginButton);

      expect(screen.getByText('Username and password are required')).toBeInTheDocument();

      // Toggle to register - error should be cleared
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      expect(screen.queryByText('Username and password are required')).not.toBeInTheDocument();
    });
  });
});
