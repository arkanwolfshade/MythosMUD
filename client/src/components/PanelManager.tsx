import React from 'react';

interface PanelManagerProps {
  children: React.ReactNode;
}

export const PanelManager: React.FC<PanelManagerProps> = ({ children }) => {
  return <div className="h-full w-full">{children}</div>;
};
