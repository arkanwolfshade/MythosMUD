import React, { useState } from 'react';
import { logger } from '../utils/logger.js';
import { useProfessions } from '../hooks/useProfessions.js';
import { Profession, ProfessionCard } from './ProfessionCard.jsx';

interface ProfessionSelectionScreenProps {
  characterName?: string; // MULTI-CHARACTER: Made optional - character name is now entered later
  onProfessionSelected: (profession: Profession) => void;
  onError: (error: string) => void;
  onBack: () => void;
  baseUrl: string;
  authToken: string;
}

export const ProfessionSelectionScreen: React.FC<ProfessionSelectionScreenProps> = ({
  characterName,
  onProfessionSelected,
  onError,
  onBack,
  baseUrl,
  authToken,
}) => {
  const { professions, isLoading, error, fetchProfessions } = useProfessions({
    baseUrl,
    authToken,
    onError,
  });

  const [selectedProfession, setSelectedProfession] = useState<Profession | null>(null);

  const handleProfessionSelect = (profession: Profession) => {
    setSelectedProfession(profession);
    logger.info('ProfessionSelectionScreen', 'Profession selected', {
      professionId: profession.id,
      professionName: profession.name,
    });
  };

  const handleNext = () => {
    if (selectedProfession) {
      onProfessionSelected(selectedProfession);
    }
  };

  const handleBack = () => {
    onBack();
  };

  if (isLoading) {
    return (
      <div className="profession-selection-screen">
        <div className="loading-container">
          <h2>Loading professions...</h2>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="profession-selection-screen">
        <div className="error-container">
          <h2>Error Loading Professions</h2>
          <p className="error-message">{error}</p>
          <button onClick={fetchProfessions} className="retry-button">
            Retry
          </button>
          <button onClick={handleBack} className="back-button">
            Back
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="profession-selection-screen">
      <div className="profession-selection-container">
        <header className="profession-selection-header">
          <h1>Choose Your Profession</h1>
          {characterName && <p className="character-welcome">Welcome, {characterName}</p>}
          <p className="profession-instructions">
            Select a profession that defines your character's background and abilities. Each profession has different
            stat requirements and will influence your character's development.
          </p>
        </header>

        <div className="professions-grid">
          {professions.map(profession => (
            <ProfessionCard
              key={profession.id}
              profession={profession}
              isSelected={selectedProfession?.id === profession.id}
              onSelect={handleProfessionSelect}
            />
          ))}
        </div>

        <div className="profession-selection-actions">
          <button onClick={handleBack} className="back-button" type="button">
            Back
          </button>

          <button onClick={handleNext} className="next-button" disabled={!selectedProfession} type="button">
            Next
          </button>
        </div>
      </div>
    </div>
  );
};
