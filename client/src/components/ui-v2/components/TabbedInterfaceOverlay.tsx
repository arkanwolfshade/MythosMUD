// Tabbed interface overlay component
// Extracted from GameClientV2Container to reduce complexity

import React from 'react';
import type { Tab } from '../TabbedInterface';

interface TabbedInterfaceOverlayProps {
  tabs: Tab[];
  activeTabId: string | null;
  setActiveTab: (id: string) => void;
  closeTab: (id: string) => void;
}

export const TabbedInterfaceOverlay: React.FC<TabbedInterfaceOverlayProps> = ({
  tabs,
  activeTabId,
  setActiveTab,
  closeTab,
}) => {
  if (tabs.length === 0) {
    return null;
  }

  return (
    <div className="fixed inset-0 z-9999 bg-mythos-terminal-background">
      <div className="flex flex-col h-full">
        {/* Tab Bar */}
        <div className="flex items-center border-b border-mythos-terminal-border bg-mythos-terminal-background overflow-x-auto">
          {tabs.map(tab => (
            <div
              key={tab.id}
              className={`
                flex items-center gap-2 px-4 py-2 border-r border-mythos-terminal-border
                cursor-pointer transition-colors
                ${
                  activeTabId === tab.id
                    ? 'bg-mythos-terminal-primary text-white'
                    : 'bg-mythos-terminal-background text-mythos-terminal-text hover:bg-mythos-terminal-border/50'
                }
              `}
              onClick={() => setActiveTab(tab.id)}
            >
              <span className="text-sm font-medium whitespace-nowrap">{tab.label}</span>
              {tab.closable !== false && (
                <button
                  onClick={e => {
                    e.stopPropagation();
                    closeTab(tab.id);
                  }}
                  className="ml-1 hover:bg-black/20 rounded p-0.5 transition-colors"
                  aria-label={`Close ${tab.label}`}
                >
                  ×
                </button>
              )}
            </div>
          ))}
        </div>
        {/* Tab Content */}
        <div className="flex-1 overflow-hidden">{tabs.find(tab => tab.id === activeTabId)?.content}</div>
      </div>
    </div>
  );
};
