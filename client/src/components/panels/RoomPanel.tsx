import React from 'react';

interface RoomPanelProps {
  placeholderText?: string;
}

export const RoomPanel: React.FC<RoomPanelProps> = ({ placeholderText = 'Room Panel (Coming Soon)' }) => {
  return <div>{placeholderText}</div>;
};
