import { describe, it, expect } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import React from 'react';
import { useTabbedInterface } from '../useTabbedInterface';
import type { Tab } from '../TabbedInterface';

describe('useTabbedInterface', () => {
  const mockTab1: Tab = {
    id: 'tab1',
    label: 'Tab 1',
    content: React.createElement('div', null, 'Tab 1 Content'),
  };

  const mockTab2: Tab = {
    id: 'tab2',
    label: 'Tab 2',
    content: React.createElement('div', null, 'Tab 2 Content'),
  };

  const mockTab3: Tab = {
    id: 'tab3',
    label: 'Tab 3',
    content: React.createElement('div', null, 'Tab 3 Content'),
  };

  describe('initialization', () => {
    it('should initialize with empty tabs array', () => {
      const { result } = renderHook(() => useTabbedInterface());

      expect(result.current.tabs).toEqual([]);
      expect(result.current.activeTabId).toBeNull();
      expect(result.current.activeTab).toBeUndefined();
    });

    it('should initialize with provided tabs', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2]));

      expect(result.current.tabs).toHaveLength(2);
      expect(result.current.tabs[0].id).toBe('tab1');
      expect(result.current.tabs[1].id).toBe('tab2');
      expect(result.current.activeTabId).toBe('tab1');
      expect(result.current.activeTab).toEqual(mockTab1);
    });

    it('should set first tab as active when initialized with tabs', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2, mockTab3]));

      expect(result.current.activeTabId).toBe('tab1');
      expect(result.current.activeTab).toEqual(mockTab1);
    });
  });

  describe('addTab', () => {
    it('should add a new tab', () => {
      const { result } = renderHook(() => useTabbedInterface());

      act(() => {
        result.current.addTab(mockTab1);
      });

      expect(result.current.tabs).toHaveLength(1);
      expect(result.current.tabs[0]).toEqual(mockTab1);
      expect(result.current.activeTabId).toBe('tab1');
      expect(result.current.activeTab).toEqual(mockTab1);
    });

    it('should add multiple tabs', () => {
      const { result } = renderHook(() => useTabbedInterface());

      act(() => {
        result.current.addTab(mockTab1);
      });

      act(() => {
        result.current.addTab(mockTab2);
      });

      expect(result.current.tabs).toHaveLength(2);
      expect(result.current.tabs[0]).toEqual(mockTab1);
      expect(result.current.tabs[1]).toEqual(mockTab2);
      expect(result.current.activeTabId).toBe('tab2');
    });

    it('should switch to existing tab if tab with same id already exists', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1]));

      act(() => {
        result.current.setActiveTab('tab2');
      });

      act(() => {
        result.current.addTab(mockTab1); // Try to add tab1 again
      });

      expect(result.current.tabs).toHaveLength(1); // Should not add duplicate
      expect(result.current.activeTabId).toBe('tab1'); // Should switch to tab1
    });

    it('should set added tab as active', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1]));

      act(() => {
        result.current.addTab(mockTab2);
      });

      expect(result.current.activeTabId).toBe('tab2');
      expect(result.current.activeTab).toEqual(mockTab2);
    });
  });

  describe('closeTab', () => {
    it('should close a tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2]));

      act(() => {
        result.current.closeTab('tab2');
      });

      expect(result.current.tabs).toHaveLength(1);
      expect(result.current.tabs[0].id).toBe('tab1');
    });

    it('should switch to last tab when closing active tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2, mockTab3]));

      act(() => {
        result.current.setActiveTab('tab2');
      });

      act(() => {
        result.current.closeTab('tab2');
      });

      expect(result.current.tabs).toHaveLength(2);
      expect(result.current.activeTabId).toBe('tab3');
      expect(result.current.activeTab).toEqual(mockTab3);
    });

    it('should set activeTabId to null when closing last tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1]));

      act(() => {
        result.current.closeTab('tab1');
      });

      expect(result.current.tabs).toHaveLength(0);
      expect(result.current.activeTabId).toBeNull();
      expect(result.current.activeTab).toBeUndefined();
    });

    it('should not change active tab when closing non-active tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2, mockTab3]));

      act(() => {
        result.current.setActiveTab('tab2');
      });

      act(() => {
        result.current.closeTab('tab1');
      });

      expect(result.current.activeTabId).toBe('tab2');
      expect(result.current.activeTab).toEqual(mockTab2);
    });
  });

  describe('setActiveTab', () => {
    it('should set active tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2]));

      act(() => {
        result.current.setActiveTab('tab2');
      });

      expect(result.current.activeTabId).toBe('tab2');
      expect(result.current.activeTab).toEqual(mockTab2);
    });

    it('should update activeTab when setting active tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2, mockTab3]));

      act(() => {
        result.current.setActiveTab('tab3');
      });

      expect(result.current.activeTab).toEqual(mockTab3);
    });

    it('should handle setting active tab to non-existent tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1]));

      act(() => {
        result.current.setActiveTab('nonexistent');
      });

      expect(result.current.activeTabId).toBe('nonexistent');
      expect(result.current.activeTab).toBeUndefined();
    });
  });

  describe('activeTab', () => {
    it('should return undefined when no active tab', () => {
      const { result } = renderHook(() => useTabbedInterface());

      expect(result.current.activeTab).toBeUndefined();
    });

    it('should return correct active tab', () => {
      const { result } = renderHook(() => useTabbedInterface([mockTab1, mockTab2]));

      expect(result.current.activeTab).toEqual(mockTab1);

      act(() => {
        result.current.setActiveTab('tab2');
      });

      expect(result.current.activeTab).toEqual(mockTab2);
    });
  });
});
