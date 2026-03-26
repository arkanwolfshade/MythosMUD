import { act, fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import { CharacterNameScreen } from '../components/CharacterNameScreen.tsx';
import {
  DEFAULT_ROLLED_STATS,
  createDefaultRollStatsFetchResponse,
  createMockLoginResponse,
  createMockProfessions,
  createMockSkills,
  fillSkillSlotsAndConfirm,
  registerTestUserFromLoginScreen,
  setupBasicMocks,
} from './professionSystemErrorHandling.test.helpers.ts';

// Mock fetch globally
const mockFetch = vi.fn();
globalThis.fetch = mockFetch as typeof fetch;

// Mock the logger
vi.mock('../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
    debug: vi.fn(),
    warn: vi.fn(),
  },
}));

// Mock secure token storage
vi.mock('../utils/security', () => ({
  secureTokenStorage: {
    getToken: vi.fn(() => null),
    setToken: vi.fn(),
    setRefreshToken: vi.fn(),
    clearAllTokens: vi.fn(),
    isValidToken: vi.fn(() => false),
    isTokenExpired: vi.fn(() => true),
  },
  inputSanitizer: {
    sanitizeUsername: vi.fn(val => val),
    sanitizeCommand: vi.fn(val => val),
  },
}));

describe('Profession System Error Handling and Edge Cases', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Profession Selection Error Handling', () => {
    it('should handle profession API failure gracefully', async () => {
      const statsResponse = createDefaultRollStatsFetchResponse();
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse);
        } else if (url.includes('/professions')) {
          return Promise.reject(new Error('Network error'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      // Plan 10.6: stats first; advance to profession so profession fetch runs and fails
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(
        () => {
          // When server unavailability is detected, the app returns to login screen
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 3000 }
      );
    });

    it('should handle empty profession list gracefully', async () => {
      const statsResponse = createDefaultRollStatsFetchResponse();
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ professions: [] }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      // Plan 10.6: stats first, then profession
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
    });

    it('should handle malformed profession data gracefully', async () => {
      const statsResponse = createDefaultRollStatsFetchResponse();
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue([
              {
                id: 0,
                name: 'Tramp',
                description: 'A wandering soul',
              },
            ]),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(() => {
        expect(screen.getByText('Error Loading Professions')).toBeInTheDocument();
        expect(screen.getByText(/Invalid API response: expected Profession\[\]/)).toBeInTheDocument();
      });
    });
  });

  describe('Stat Rolling Error Handling', () => {
    it('should handle stat rolling API failure gracefully', async () => {
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.reject(new Error('Stat rolling failed'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      // Plan 10.6: stats step loads and calls roll-stats on mount; when it fails we return to login
      await waitFor(
        () => {
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 5000 }
      );
    });

    it('should handle invalid profession ID in stat rolling', async () => {
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve({
            ok: false,
            status: 400,
            json: vi.fn().mockResolvedValue({
              detail: 'Invalid profession ID',
            }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      // When roll-stats returns 400, stats screen shows error view (no "Character Creation" header)
      await waitFor(() => {
        expect(screen.getByText('Invalid profession ID')).toBeInTheDocument();
      });
      expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
    });

    it('should handle malformed stat response gracefully', async () => {
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              profession_id: 0,
              meets_requirements: true,
            }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      await waitFor(
        () => {
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 5000 }
      );
    });
  });

  describe('Character Creation Error Handling', () => {
    beforeEach(() => {
      vi.stubGlobal('fetch', mockFetch);
    });

    it('should handle character creation API failure gracefully', async () => {
      setupBasicMocks(mockFetch);

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              professions: createMockProfessions(),
            }),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(createDefaultRollStatsFetchResponse());
        } else if (url.includes('/skills/')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ skills: createMockSkills() }),
          });
        } else if (url.includes('/players/create-character')) {
          return Promise.reject(new Error('Character creation failed'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);
      fireEvent.click(screen.getByText('Next'));

      await fillSkillSlotsAndConfirm();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
      });
      const nameInput = screen.getByPlaceholderText('Enter name');
      await act(async () => {
        fireEvent.change(nameInput, { target: { value: 'TestCharacter' } });
      });
      await act(async () => {
        fireEvent.click(screen.getByText('Create Character'));
      });

      await waitFor(
        () => {
          expect(document.querySelector('.App')).toBeInTheDocument();
        },
        { timeout: 2000 }
      );
    });

    // Isolated test: render CharacterNameScreen only and mock fetch so create-character returns 409.
    // Full App flow is not used so we avoid other fetches/navigation overriding the mock.
    it('should handle duplicate character name error', async () => {
      const createCharacterDetail = { detail: 'Character name already exists' };
      mockFetch.mockImplementation((input: string | URL | Request) => {
        const urlString =
          typeof input === 'string' ? input : input instanceof URL ? input.toString() : ((input as Request).url ?? '');
        if (urlString.includes('create-character')) {
          return Promise.resolve(
            new Response(JSON.stringify(createCharacterDetail), { status: 409, statusText: 'Conflict' })
          );
        }
        return Promise.reject(new Error('Unexpected request'));
      });

      const stats = { ...DEFAULT_ROLLED_STATS };
      const profession = {
        id: 1,
        name: 'Tramp',
        description: 'A wanderer',
        flavor_text: null,
        stat_requirements: [],
        mechanical_effects: [],
        is_available: true,
      };
      const skillsPayload = { occupation_slots: [], personal_interest: [] };
      const onComplete = vi.fn();
      const onError = vi.fn();
      const onBack = vi.fn();

      render(
        <CharacterNameScreen
          stats={stats}
          profession={profession}
          skillsPayload={skillsPayload}
          baseUrl="https://test.example/v1"
          authToken="test-token"
          onComplete={onComplete}
          onError={onError}
          onBack={onBack}
        />
      );

      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'TestCharacter' } });
      await act(async () => {
        fireEvent.click(screen.getByRole('button', { name: /Create Character/i }));
      });

      await waitFor(() => {
        expect(screen.getByText('Character name already exists')).toBeInTheDocument();
      });
      expect(onComplete).not.toHaveBeenCalled();
      expect(onError).toHaveBeenCalledWith('Character name already exists');
    });
  });

  describe('Edge Cases', () => {
    it('should handle rapid profession selection changes', async () => {
      setupBasicMocks(mockFetch);
      render(<App />);

      registerTestUserFromLoginScreen();

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');

      fireEvent.click(trampCard!);
      fireEvent.click(gutterRatCard!);
      fireEvent.click(trampCard!);
      fireEvent.click(gutterRatCard!);

      expect(screen.getByText('Next')).toBeInTheDocument();
    });

    it('should handle rapid stat rerolling', async () => {
      setupBasicMocks(mockFetch);
      render(<App />);

      registerTestUserFromLoginScreen();

      // Plan 10.6: stats first; wait for stats screen
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Rapidly click reroll button
      const rerollButton = screen.getByText('Reroll Stats');
      await act(async () => {
        fireEvent.click(rerollButton);
        fireEvent.click(rerollButton);
        fireEvent.click(rerollButton);
      });

      // Should handle rapid rerolling gracefully
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    it('should handle network timeout gracefully', async () => {
      // Mock network timeout
      mockFetch.mockImplementation(() => {
        return new Promise((_, reject) => {
          setTimeout(() => {
            reject(new Error('Network timeout'));
          }, 100);
        });
      });

      render(<App />);

      // Try to register
      registerTestUserFromLoginScreen();

      // Should handle timeout gracefully
      await waitFor(() => {
        expect(screen.getByText('Network timeout')).toBeInTheDocument();
      });
    });

    it('should handle concurrent API calls gracefully', async () => {
      setupBasicMocks(mockFetch);
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ professions: createMockProfessions() }),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(createDefaultRollStatsFetchResponse());
        } else if (url.includes('/skills/')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ skills: createMockSkills() }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      registerTestUserFromLoginScreen();

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);
      fireEvent.click(screen.getByText('Next'));

      await waitFor(() => {
        expect(screen.getByText('Skill Allocation')).toBeInTheDocument();
      });
    });
  });
});
