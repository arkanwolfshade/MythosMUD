import { useState, useCallback } from 'react';
import type { Tab } from './TabbedInterface';

/**
 * Hook for managing tabs in a tabbed interface.
 */
export function useTabbedInterface(initialTabs: Tab[] = []) {
  const [tabs, setTabs] = useState<Tab[]>(initialTabs);
  const [activeTabId, setActiveTabId] = useState<string | null>(initialTabs.length > 0 ? initialTabs[0].id : null);

  const addTab = useCallback((tab: Tab) => {
    setTabs(prev => {
      // If tab already exists, just switch to it
      if (prev.some(t => t.id === tab.id)) {
        setActiveTabId(tab.id);
        return prev;
      }
      return [...prev, tab];
    });
    setActiveTabId(tab.id);
  }, []);

  const closeTab = useCallback(
    (tabId: string) => {
      setTabs(prev => {
        const newTabs = prev.filter(tab => tab.id !== tabId);
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
    [activeTabId]
  );

  const setActiveTab = useCallback((tabId: string) => {
    setActiveTabId(tabId);
  }, []);

  return {
    tabs,
    activeTabId,
    addTab,
    closeTab,
    setActiveTab,
    activeTab: tabs.find(tab => tab.id === activeTabId),
  };
}
