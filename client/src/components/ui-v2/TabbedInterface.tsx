/**
 * Tabbed Interface component.
 *
 * Provides a tabbed interface within the React app, similar to browser tabs.
 * Allows multiple views (like the map) to be open simultaneously.
 *
 * As documented in the Pnakotic Manuscripts, proper dimensional navigation
 * requires careful management of multiple viewing portals.
 */

import React, { useState, useCallback } from 'react';
import { X } from 'lucide-react';

export interface Tab {
  id: string;
  label: string;
  content: React.ReactNode;
  closable?: boolean;
}

export interface TabbedInterfaceProps {
  /** Initial tabs */
  initialTabs?: Tab[];
  /** Callback when tabs change */
  onTabsChange?: (tabs: Tab[]) => void;
  /** Whether to show the tab bar */
  showTabBar?: boolean;
}

/**
 * Tabbed Interface component for managing multiple views within the app.
 */
export const TabbedInterface: React.FC<TabbedInterfaceProps> = ({
  initialTabs = [],
  onTabsChange,
  showTabBar = true,
}) => {
  const [tabs, setTabs] = useState<Tab[]>(initialTabs);
  const [activeTabId, setActiveTabId] = useState<string | null>(initialTabs.length > 0 ? initialTabs[0].id : null);

  const addTab = useCallback(
    (tab: Tab) => {
      setTabs(prev => {
        const newTabs = [...prev, tab];
        onTabsChange?.(newTabs);
        return newTabs;
      });
      setActiveTabId(tab.id);
    },
    [onTabsChange]
  );

  const closeTab = useCallback(
    (tabId: string) => {
      setTabs(prev => {
        const newTabs = prev.filter(tab => tab.id !== tabId);
        onTabsChange?.(newTabs);

        // If we closed the active tab, switch to another tab
        if (activeTabId === tabId) {
          if (newTabs.length > 0) {
            setActiveTabId(newTabs[newTabs.length - 1].id);
          } else {
            setActiveTabId(null);
          }
        }

        return newTabs;
      });
    },
    [activeTabId, onTabsChange]
  );

  const setActiveTab = useCallback((tabId: string) => {
    setActiveTabId(tabId);
  }, []);

  const activeTab = tabs.find(tab => tab.id === activeTabId);

  // Expose methods via ref or context if needed
  React.useImperativeHandle(
    React.useRef(),
    () => ({
      addTab,
      closeTab,
      setActiveTab,
      tabs,
    }),
    [addTab, closeTab, setActiveTab, tabs]
  );

  return (
    <div className="flex flex-col h-full w-full bg-mythos-terminal-background">
      {showTabBar && tabs.length > 0 && (
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
                  <X size={14} />
                </button>
              )}
            </div>
          ))}
        </div>
      )}

      <div className="flex-1 overflow-hidden">
        {activeTab ? (
          <div className="h-full w-full">{activeTab.content}</div>
        ) : (
          <div className="flex items-center justify-center h-full text-mythos-terminal-text/50">No tabs open</div>
        )}
      </div>
    </div>
  );
};
