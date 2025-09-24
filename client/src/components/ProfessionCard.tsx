import React from 'react';

export interface Profession {
  id: number;
  name: string;
  description: string;
  flavor_text: string;
  stat_requirements: Record<string, number>;
  mechanical_effects: Record<string, number>; // Game mechanics like bonuses (e.g., combat_bonus, social_bonus)
  is_available: boolean;
}

interface ProfessionCardProps {
  profession: Profession;
  isSelected: boolean;
  onSelect: (profession: Profession) => void;
}

export const ProfessionCard: React.FC<ProfessionCardProps> = ({ profession, isSelected, onSelect }) => {
  const handleClick = () => {
    onSelect(profession);
  };

  const handleKeyDown = (event: React.KeyboardEvent) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      onSelect(profession);
    }
  };

  const formatStatRequirements = (requirements: Record<string, number>): string => {
    if (!requirements || Object.keys(requirements).length === 0) {
      return 'No requirements';
    }

    const formattedRequirements = Object.entries(requirements)
      .map(([stat, value]) => `${stat.charAt(0).toUpperCase() + stat.slice(1)} ${value}`)
      .join(', ');

    return `Minimum: ${formattedRequirements}`;
  };

  const hasRequirements = profession.stat_requirements && Object.keys(profession.stat_requirements).length > 0;

  return (
    <div
      className={`profession-card ${isSelected ? 'selected' : ''}`}
      onClick={handleClick}
      onKeyDown={handleKeyDown}
      role="button"
      tabIndex={0}
      aria-pressed={isSelected}
      aria-label={`Select ${profession.name} profession`}
    >
      <div className="profession-header">
        <h3 className="profession-name">{profession.name}</h3>
      </div>

      <div className="profession-content">
        <p className="profession-description">{profession.description}</p>

        <p className="profession-flavor-text">{profession.flavor_text}</p>

        <div className="profession-requirements">
          <span className={`stat-requirements ${hasRequirements ? 'highlighted' : ''}`}>
            {formatStatRequirements(profession.stat_requirements)}
          </span>
        </div>
      </div>
    </div>
  );
};
