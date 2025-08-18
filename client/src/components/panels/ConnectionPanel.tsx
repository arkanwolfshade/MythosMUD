import React from 'react';

interface ConnectionPanelProps {
  placeholderText?: string;
}

export const ConnectionPanel: React.FC<ConnectionPanelProps> = ({
  placeholderText = 'Connection Panel (Coming Soon)',
}) => {
  return <div>{placeholderText}</div>;
};
