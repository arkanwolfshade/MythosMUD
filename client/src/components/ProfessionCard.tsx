import React from 'react';

export interface StatRequirement {
  stat: string;
  minimum: number;
}

export interface MechanicalEffect {
  effect_type: string;
  value: number | string;
  description?: string | null;
}

export interface Profession {
  id: number;
  name: string;
  description: string;
  flavor_text: string | null;
  stat_requirements: StatRequirement[];
  mechanical_effects: MechanicalEffect[];
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

  const formatStatRequirements = (requirements: StatRequirement[]): string => {
    if (!requirements || requirements.length === 0) {
      return 'No requirements';
    }

    const formattedRequirements = requirements
      .map(req => `${req.stat.charAt(0).toUpperCase() + req.stat.slice(1)} ${req.minimum}`)
      .join(', ');

    return `Minimum: ${formattedRequirements}`;
  };

  const hasRequirements = profession.stat_requirements && profession.stat_requirements.length > 0;

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

        {profession.flavor_text && <p className="profession-flavor-text">{profession.flavor_text}</p>}

        <div className="profession-requirements">
          <span className={`stat-requirements ${hasRequirements ? 'highlighted' : ''}`}>
            {formatStatRequirements(profession.stat_requirements)}
          </span>
        </div>
      </div>
    </div>
  );
};
