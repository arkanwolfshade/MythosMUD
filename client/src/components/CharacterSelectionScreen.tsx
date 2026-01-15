import React, { useCallback, useState } from 'react';
import type { CharacterInfo } from '../types/auth';
import { isServerCharacterResponseArray } from '../utils/apiTypeGuards';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler';
import { logger } from '../utils/logger';
import './CharacterSelectionScreen.css';

interface CharacterSelectionScreenProps {
  characters: CharacterInfo[];
  onCharacterSelected: (characterId: string) => void;
  onCreateCharacter: () => void;
  onDeleteCharacter: (characterId: string) => Promise<void>;
  onError: (error: string) => void;
  baseUrl: string;
  authToken: string;
}

export const CharacterSelectionScreen: React.FC<CharacterSelectionScreenProps> = ({
  characters,
  onCharacterSelected,
  onCreateCharacter,
  onDeleteCharacter,
  onError,
  baseUrl,
  authToken,
}) => {
  const [isDeleting, setIsDeleting] = useState<string | null>(null);
  const [deleteConfirm, setDeleteConfirm] = useState<string | null>(null);

  const refreshCharacters = useCallback(async () => {
    try {
      const response = await fetch(`${baseUrl}/api/players/characters`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        let errorMessage = 'Failed to load characters';
        try {
          const rawData: unknown = await response.json();
          if (isErrorResponse(rawData)) {
            errorMessage = getErrorMessage(rawData);
          } else if (typeof rawData === 'object' && rawData !== null) {
            const errorData = rawData as Record<string, unknown>;
            errorMessage =
              typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail
                ? String((errorData.detail as Record<string, unknown>).message)
                : typeof errorData.detail === 'string'
                  ? errorData.detail
                  : errorMessage;
          }
        } catch {
          // Use default error message if JSON parsing fails
        }
        throw new Error(errorMessage);
      }

      const rawData: unknown = await response.json();
      if (!isServerCharacterResponseArray(rawData)) {
        throw new Error('Invalid API response: expected ServerCharacterResponse[]');
      }
      // Note: The parent component should update the characters prop
      // This is just for refreshing if needed
      logger.info('CharacterSelectionScreen', 'Characters refreshed', { count: rawData.length });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      logger.error('CharacterSelectionScreen', 'Failed to refresh characters', { error: errorMessage });
    }
  }, [baseUrl, authToken]);

  const handleDeleteClick = (characterId: string) => {
    setDeleteConfirm(characterId);
  };

  const handleDeleteConfirm = async (characterId: string) => {
    try {
      setIsDeleting(characterId);
      await onDeleteCharacter(characterId);
      setDeleteConfirm(null);
      // Refresh characters list after deletion
      await refreshCharacters();
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Failed to delete character';
      onError(errorMessage);
      logger.error('CharacterSelectionScreen', 'Failed to delete character', {
        characterId,
        error: errorMessage,
      });
    } finally {
      setIsDeleting(null);
    }
  };

  const handleDeleteCancel = () => {
    setDeleteConfirm(null);
  };

  const formatDate = (dateString: string) => {
    try {
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return dateString;
    }
  };

  const canCreateCharacter = characters.length < 3;

  if (characters.length === 0) {
    return (
      <div className="character-selection-screen">
        <div className="character-selection-container">
          <header className="character-selection-header">
            <h1>Welcome to MythosMUD</h1>
            <p className="character-instructions">
              Create your first character to begin your journey into the unknown.
            </p>
          </header>

          <div className="character-selection-actions">
            <button onClick={onCreateCharacter} className="create-character-button primary" type="button">
              Create Your First Character
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="character-selection-screen">
      <div className="character-selection-container">
        <header className="character-selection-header">
          <h1>Select Your Character</h1>
          <p className="character-instructions">
            Choose a character to play, or create a new one. You can have up to 3 active characters.
          </p>
        </header>

        <div className="characters-list">
          {characters.map(character => (
            <div key={character.player_id} className="character-card">
              <div className="character-info">
                <h3 className="character-name">{character.name}</h3>
                <div className="character-details">
                  <span className="character-profession">
                    {character.profession_name || `Profession ${character.profession_id}`}
                  </span>
                  <span className="character-level">Level {character.level}</span>
                </div>
                <div className="character-meta">
                  <span className="character-created">Created: {formatDate(character.created_at)}</span>
                  <span className="character-last-active">Last Active: {formatDate(character.last_active)}</span>
                </div>
              </div>

              <div className="character-actions">
                {deleteConfirm === character.player_id ? (
                  <div className="delete-confirmation">
                    <p>Are you sure you want to delete {character.name}?</p>
                    <div className="delete-confirmation-buttons">
                      <button
                        onClick={() => handleDeleteConfirm(character.player_id)}
                        className="confirm-delete-button"
                        disabled={isDeleting === character.player_id}
                        type="button"
                      >
                        {isDeleting === character.player_id ? 'Deleting...' : 'Confirm Delete'}
                      </button>
                      <button onClick={handleDeleteCancel} className="cancel-delete-button" type="button">
                        Cancel
                      </button>
                    </div>
                  </div>
                ) : (
                  <>
                    <button
                      onClick={() => onCharacterSelected(character.player_id)}
                      className="select-character-button primary"
                      type="button"
                    >
                      Select Character
                    </button>
                    <button
                      onClick={() => {
                        handleDeleteClick(character.player_id);
                      }}
                      className="delete-character-button"
                      disabled={isDeleting === character.player_id}
                      type="button"
                    >
                      Delete
                    </button>
                  </>
                )}
              </div>
            </div>
          ))}
        </div>

        <div className="character-selection-actions">
          {canCreateCharacter && (
            <button onClick={onCreateCharacter} className="create-character-button secondary" type="button">
              Create New Character ({characters.length}/3)
            </button>
          )}
          {!canCreateCharacter && (
            <p className="character-limit-message">You have reached the maximum number of characters (3).</p>
          )}
        </div>
      </div>
    </div>
  );
};
