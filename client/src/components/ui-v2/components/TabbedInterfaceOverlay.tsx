// Tabbed interface overlay component
// Extracted from GameClientV2Container to reduce complexity

import React, { useRef } from 'react';
import { Z_INDEX_OVERLAY_TOP } from '../../../constants/layout';
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
  const rootRef = useRef<HTMLDivElement>(null);

  if (tabs.length === 0) {
    return null;
  }

  return (
    <div
      ref={rootRef}
      className="fixed inset-0 flex flex-col"
      style={{
        backgroundColor: '#0a0a0a',
        opacity: 1,
        zIndex: Z_INDEX_OVERLAY_TOP,
      }}
    >
      <div className="flex flex-col h-full flex-1 min-h-0">
        {/* Tab Bar */}
        <div
          className="flex items-center border-b border-mythos-terminal-border overflow-x-auto shrink-0"
          style={{ backgroundColor: '#0a0a0a' }}
        >
          {tabs.map(tab => (
            <div key={tab.id} className="flex items-stretch border-r border-mythos-terminal-border min-w-0">
              <button
                type="button"
                className={`
                  flex flex-1 items-center gap-2 px-4 py-2 min-w-0
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
              </button>
              {tab.closable !== false && (
                <button
                  type="button"
                  onClick={() => {
                    closeTab(tab.id);
                  }}
                  className="shrink-0 px-2 hover:bg-black/20 transition-colors self-stretch flex items-center"
                  aria-label={`Close ${tab.label}`}
                >
                  ×
                </button>
              )}
            </div>
          ))}
        </div>
        {/* Tab Content: opaque background so map popout does not show game UI through */}
        <div className="flex-1 overflow-hidden min-h-0" style={{ backgroundColor: '#0a0a0a' }}>
          {tabs.find(tab => tab.id === activeTabId)?.content}
        </div>
      </div>
    </div>
  );
};
