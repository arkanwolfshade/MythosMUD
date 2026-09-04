import React, { useState } from 'react';
import type { CharacterInfo } from '../types/auth.js';
import { logger } from '../utils/logger.js';
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

function formatCharacterDate(dateString: string) {
  try {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  } catch {
    return dateString;
  }
}

function EmptyCharacterSelection({ onCreateCharacter }: { onCreateCharacter: () => void }) {
  return (
    <div className="character-selection-screen">
      <div className="character-selection-container">
        <header className="character-selection-header">
          <h1>Welcome to MythosMUD</h1>
          <p className="character-instructions">Create your first character to begin your journey into the unknown.</p>
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

interface CharacterCardDeleteState {
  deleteConfirm: string | null;
  isDeleting: string | null;
  onDeleteClick: (characterId: string) => void;
  onDeleteConfirm: (characterId: string) => void;
  onDeleteCancel: () => void;
}

interface CharacterCardProps {
  character: CharacterInfo;
  deleteState: CharacterCardDeleteState;
  onSelect: (characterId: string) => void;
}

function CharacterCard({ character, deleteState, onSelect }: CharacterCardProps) {
  const { deleteConfirm, isDeleting, onDeleteClick, onDeleteConfirm, onDeleteCancel } = deleteState;
  return (
    <div className="character-card">
      <div className="character-info">
        <h3 className="character-name">{character.name}</h3>
        <div className="character-details">
          <span className="character-profession">
            {character.profession_name || `Profession ${character.profession_id}`}
          </span>
          <span className="character-level">Level {character.level}</span>
        </div>
        <div className="character-meta">
          <span className="character-created">Created: {formatCharacterDate(character.created_at)}</span>
          <span className="character-last-active">Last Active: {formatCharacterDate(character.last_active)}</span>
        </div>
      </div>
      <div className="character-actions">
        {deleteConfirm === character.player_id ? (
          <div className="delete-confirmation">
            <p>Are you sure you want to delete {character.name}?</p>
            <div className="delete-confirmation-buttons">
              <button
                onClick={() => onDeleteConfirm(character.player_id)}
                className="confirm-delete-button"
                disabled={isDeleting === character.player_id}
                type="button"
              >
                {isDeleting === character.player_id ? 'Deleting...' : 'Confirm Delete'}
              </button>
              <button onClick={onDeleteCancel} className="cancel-delete-button" type="button">
                Cancel
              </button>
            </div>
          </div>
        ) : (
          <>
            <button
              onClick={() => onSelect(character.player_id)}
              className="select-character-button primary"
              type="button"
              data-testid="select-character-button"
            >
              Select Character
            </button>
            <button
              onClick={() => onDeleteClick(character.player_id)}
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
  );
}

function CharacterSelectionList({
  characters,
  deleteState,
  onCharacterSelected,
  onCreateCharacter,
}: {
  characters: CharacterInfo[];
  deleteState: CharacterCardDeleteState;
  onCharacterSelected: (characterId: string) => void;
  onCreateCharacter: () => void;
}) {
  const canCreateCharacter = characters.length < 3;

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
            <CharacterCard
              key={character.player_id}
              character={character}
              deleteState={deleteState}
              onSelect={onCharacterSelected}
            />
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
}

export const CharacterSelectionScreen: React.FC<CharacterSelectionScreenProps> = props => {
  const { characters, onCharacterSelected, onCreateCharacter, onDeleteCharacter, onError } = props;
  const [isDeleting, setIsDeleting] = useState<string | null>(null);
  const [deleteConfirm, setDeleteConfirm] = useState<string | null>(null);

  const handleDeleteClick = (characterId: string) => {
    setDeleteConfirm(characterId);
  };

  const handleDeleteConfirm = async (characterId: string) => {
    try {
      setIsDeleting(characterId);
      // onDeleteCharacter (executeDeleteCharacterUi) already refetches and updates the
      // characters list on success; a second, redundant fetch here (whose result was
      // discarded anyway -- see prior comment) added a second, spurious source of delete
      // errors on top of a delete that had already succeeded. #777 follow-up.
      await onDeleteCharacter(characterId);
      setDeleteConfirm(null);
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

  const deleteState: CharacterCardDeleteState = {
    deleteConfirm,
    isDeleting,
    onDeleteClick: handleDeleteClick,
    onDeleteConfirm: handleDeleteConfirm,
    onDeleteCancel: handleDeleteCancel,
  };

  if (characters.length === 0) {
    return <EmptyCharacterSelection onCreateCharacter={onCreateCharacter} />;
  }

  return (
    <CharacterSelectionList
      characters={characters}
      deleteState={deleteState}
      onCharacterSelected={onCharacterSelected}
      onCreateCharacter={onCreateCharacter}
    />
  );
};
