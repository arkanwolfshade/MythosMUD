import React, { useState } from 'react';
import type { Channel } from './ChannelSelector';
import {
  StyleGuideButtonsSection,
  StyleGuideCardsSection,
  StyleGuideColorsSection,
  StyleGuideCompoundSection,
  StyleGuideFormsSection,
  StyleGuideIconsSection,
  StyleGuideInputsSection,
  StyleGuideTypographySection,
} from './StyleGuideSections';

const MOCK_PLAYER = {
  id: 'player-1',
  name: 'TestPlayer',
  stats: {
    current_dp: 100,
    lucidity: 80,
    strength: 10,
    dexterity: 12,
    constitution: 14,
    intelligence: 16,
    wisdom: 13,
    charisma: 15,
    occult_knowledge: 5,
    fear: 2,
    corruption: 1,
    cult_affiliation: 0,
  },
  level: 5,
};

const STYLE_GUIDE_CHANNELS: Channel[] = [
  {
    id: 'local',
    name: 'Local',
    description: 'Chat with players in your current room',
    icon: 'local',
    color: '#10b981',
    shortcut: 'say',
  },
  {
    id: 'global',
    name: 'Global',
    description: 'Chat with all players across the game',
    icon: 'global',
    color: '#3b82f6',
    shortcut: 'chat',
  },
  {
    id: 'whisper',
    name: 'Whisper',
    description: 'Send a private message to a specific player',
    icon: 'whisper',
    color: '#8b5cf6',
    shortcut: 'whisper',
  },
];

/**
 * Style Guide Component
 *
 * This component demonstrates all available UI components and their variants.
 * It serves as both documentation and a testing ground for the design system.
 */
export const StyleGuide: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedChannel, setSelectedChannel] = useState('local');
  const [disabledInputValue, setDisabledInputValue] = useState('');
  const [errorInputValue, setErrorInputValue] = useState('');
  const [sizeSmValue, setSizeSmValue] = useState('');
  const [sizeMdValue, setSizeMdValue] = useState('');
  const [sizeLgValue, setSizeLgValue] = useState('');
  const [formInputValue, setFormInputValue] = useState('');

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-6">
      <div className="max-w-7xl mx-auto space-y-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-mythos-terminal-primary mb-2">MythosMUD UI Style Guide</h1>
          <p className="text-mythos-terminal-text-secondary">Comprehensive component library and design system</p>
        </div>
        <StyleGuideButtonsSection />
        <StyleGuideInputsSection
          inputs={{
            basic: { value: inputValue, setValue: setInputValue },
            disabled: { value: disabledInputValue, setValue: setDisabledInputValue },
            error: { value: errorInputValue, setValue: setErrorInputValue },
            sizeSm: { value: sizeSmValue, setValue: setSizeSmValue },
            sizeMd: { value: sizeMdValue, setValue: setSizeMdValue },
            sizeLg: { value: sizeLgValue, setValue: setSizeLgValue },
          }}
        />
        <StyleGuideCardsSection />
        <StyleGuideCompoundSection mockPlayer={MOCK_PLAYER} />
        <StyleGuideFormsSection
          channels={STYLE_GUIDE_CHANNELS}
          selectedChannel={selectedChannel}
          setSelectedChannel={setSelectedChannel}
          inputValue={inputValue}
          setInputValue={setInputValue}
          formInputValue={formInputValue}
          setFormInputValue={setFormInputValue}
        />
        <StyleGuideIconsSection />
        <StyleGuideColorsSection />
        <StyleGuideTypographySection />
      </div>
    </div>
  );
};
