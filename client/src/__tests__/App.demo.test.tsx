import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { App } from '../App';
import { registerAppTestHooks } from './app.test.helpers';
import './app.test.mocks';

describe('App', () => {
  registerAppTestHooks();
  describe('Demo Mode', () => {
    it('should show demo mode when demo button is clicked', async () => {
      render(<App />);

      const demoButton = screen.getByText('View Eldritch Effects Demo');
      fireEvent.click(demoButton);

      // Wait for lazy-loaded component to render
      await waitFor(() => {
        expect(screen.getByTestId('eldritch-effects-demo')).toBeInTheDocument();
      });
      expect(screen.getByText('Exit Demo')).toBeInTheDocument();
    });

    it('should exit demo mode when exit button is clicked', async () => {
      render(<App />);

      // Enter demo mode
      const demoButton = screen.getByText('View Eldritch Effects Demo');
      fireEvent.click(demoButton);

      // Wait for lazy-loaded component to render
      await waitFor(() => {
        expect(screen.getByTestId('eldritch-effects-demo')).toBeInTheDocument();
      });

      // Exit demo mode
      const exitButton = screen.getByText('Exit Demo');
      fireEvent.click(exitButton);

      expect(screen.getByText('MythosMUD')).toBeInTheDocument();
      expect(screen.queryByTestId('eldritch-effects-demo')).not.toBeInTheDocument();
    });
  });
});
