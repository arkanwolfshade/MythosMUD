import React from 'react';

interface PlayerPanelProps {
  placeholderText?: string;
}

export const PlayerPanel: React.FC<PlayerPanelProps> = ({ placeholderText = 'Player Panel (Coming Soon)' }) => {
  return <div>{placeholderText}</div>;
};
