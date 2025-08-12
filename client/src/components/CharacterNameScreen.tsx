import React, { useState } from 'react';
import { logger } from '../utils/logger';
import './CharacterNameScreen.css';

interface CharacterNameScreenProps {
  onCharacterNameSubmitted: (characterName: string) => void;
  onError: (error: string) => void;
  baseUrl: string;
  authToken: string;
}

export const CharacterNameScreen: React.FC<CharacterNameScreenProps> = ({
  onCharacterNameSubmitted,
  onError,
  baseUrl,
  authToken,
}) => {
  const [characterName, setCharacterName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!characterName.trim()) {
      setError('Please enter a character name');
      return;
    }

    if (characterName.length < 2) {
      setError('Character name must be at least 2 characters long');
      return;
    }

    if (characterName.length > 20) {
      setError('Character name must be 20 characters or less');
      return;
    }

    // Basic validation for allowed characters
    const nameRegex = /^[a-zA-Z0-9\s\-_]+$/;
    if (!nameRegex.test(characterName)) {
      setError('Character name can only contain letters, numbers, spaces, hyphens, and underscores');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      // Check if character name is available
      const response = await fetch(`${baseUrl}/players/name/${encodeURIComponent(characterName)}`, {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (response.status === 404) {
        // Character name is available (404 means not found)
        logger.info('CharacterNameScreen', 'Character name is available', { characterName });
        onCharacterNameSubmitted(characterName.trim());
      } else if (response.status === 200) {
        // Character name already exists
        setError('This character name is already taken. Please choose a different name.');
        logger.warn('CharacterNameScreen', 'Character name already exists', { characterName });
      } else {
        // Other error
        const errorData = await response.json();
        const errorMessage = errorData.detail || 'Failed to validate character name';
        setError(errorMessage);
        logger.error('CharacterNameScreen', 'Failed to validate character name', { error: errorMessage });
      }
    } catch (error) {
      const errorMessage = 'Failed to connect to server';
      setError(errorMessage);
      onError(errorMessage);
      logger.error('CharacterNameScreen', 'Network error validating character name', {
        error: error instanceof Error ? error.message : String(error),
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="character-name-screen">
      <div className="character-name-header">
        <h2>Character Creation</h2>
        <p>Choose a name for your character</p>
      </div>

      <form onSubmit={handleSubmit} className="character-name-form">
        <div className="form-group">
          <label htmlFor="character-name">Character Name:</label>
          <input
            id="character-name"
            type="text"
            value={characterName}
            onChange={e => setCharacterName(e.target.value)}
            placeholder="Enter your character's name"
            required
            maxLength={20}
            disabled={isLoading}
            className="character-name-input"
          />
          <div className="input-help">
            <p>2-20 characters, letters, numbers, spaces, hyphens, and underscores only</p>
          </div>
        </div>

        {error && <div className="error-message">{error}</div>}

        <button type="submit" disabled={isLoading || !characterName.trim()} className="submit-button">
          {isLoading ? 'Validating...' : 'Continue to Stats'}
        </button>
      </form>

      <div className="character-name-info">
        <p>Your character name will be visible to other players in the game.</p>
        <p>Choose wisely - this name will represent you in the world of MythosMUD.</p>
      </div>
    </div>
  );
};
