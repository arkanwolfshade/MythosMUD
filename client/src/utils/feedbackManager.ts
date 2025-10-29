import { useCallback, useEffect, useRef, useState } from 'react';

interface FeedbackData {
  id: string;
  type: 'bug' | 'feature' | 'improvement' | 'general';
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high' | 'critical';
  component: 'chat' | 'game-log' | 'commands' | 'all';
  userAgent: string;
  timestamp: string;
  status: 'pending' | 'reviewed' | 'in-progress' | 'resolved' | 'rejected';
  response?: string;
  tags?: string[];
}

interface FeedbackStats {
  total: number;
  byType: Record<string, number>;
  byPriority: Record<string, number>;
  byComponent: Record<string, number>;
  byStatus: Record<string, number>;
  recentCount: number;
}

class FeedbackManager {
  private feedback: FeedbackData[] = [];
  private storageKey = 'mythosmud_feedback';
  private maxFeedbackItems = 1000;

  constructor() {
    this.loadFeedback();
  }

  private generateId(): string {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  }

  private loadFeedback(): void {
    try {
      const stored = localStorage.getItem(this.storageKey);
      if (stored) {
        this.feedback = JSON.parse(stored);
      }
    } catch (error) {
      console.warn('Failed to load feedback from localStorage:', error);
      this.feedback = [];
    }
  }

  private saveFeedback(): void {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.feedback));
    } catch (error) {
      console.warn('Failed to save feedback to localStorage:', error);
    }
  }

  addFeedback(feedback: Omit<FeedbackData, 'id' | 'status'>): string {
    const newFeedback: FeedbackData = {
      ...feedback,
      id: this.generateId(),
      status: 'pending',
    };

    this.feedback.unshift(newFeedback); // Add to beginning

    // Keep only the most recent feedback items
    if (this.feedback.length > this.maxFeedbackItems) {
      this.feedback = this.feedback.slice(0, this.maxFeedbackItems);
    }

    this.saveFeedback();
    return newFeedback.id;
  }

  updateFeedback(id: string, updates: Partial<FeedbackData>): boolean {
    const index = this.feedback.findIndex(f => f.id === id);
    if (index === -1) return false;

    this.feedback[index] = { ...this.feedback[index], ...updates };
    this.saveFeedback();
    return true;
  }

  deleteFeedback(id: string): boolean {
    const index = this.feedback.findIndex(f => f.id === id);
    if (index === -1) return false;

    this.feedback.splice(index, 1);
    this.saveFeedback();
    return true;
  }

  getFeedback(id: string): FeedbackData | null {
    return this.feedback.find(f => f.id === id) || null;
  }

  getAllFeedback(): FeedbackData[] {
    return [...this.feedback];
  }

  getFeedbackByType(type: FeedbackData['type']): FeedbackData[] {
    return this.feedback.filter(f => f.type === type);
  }

  getFeedbackByComponent(component: FeedbackData['component']): FeedbackData[] {
    return this.feedback.filter(f => f.component === component);
  }

  getFeedbackByPriority(priority: FeedbackData['priority']): FeedbackData[] {
    return this.feedback.filter(f => f.priority === priority);
  }

  getFeedbackByStatus(status: FeedbackData['status']): FeedbackData[] {
    return this.feedback.filter(f => f.status === status);
  }

  searchFeedback(query: string): FeedbackData[] {
    const lowerQuery = query.toLowerCase();
    return this.feedback.filter(
      f =>
        f.title.toLowerCase().includes(lowerQuery) ||
        f.description.toLowerCase().includes(lowerQuery) ||
        f.tags?.some(tag => tag.toLowerCase().includes(lowerQuery))
    );
  }

  getStats(): FeedbackStats {
    const now = Date.now();
    const oneWeekAgo = now - 7 * 24 * 60 * 60 * 1000;

    const stats: FeedbackStats = {
      total: this.feedback.length,
      byType: {},
      byPriority: {},
      byComponent: {},
      byStatus: {},
      recentCount: this.feedback.filter(f => new Date(f.timestamp).getTime() > oneWeekAgo).length,
    };

    // Count by type
    this.feedback.forEach(f => {
      stats.byType[f.type] = (stats.byType[f.type] || 0) + 1;
    });

    // Count by priority
    this.feedback.forEach(f => {
      stats.byPriority[f.priority] = (stats.byPriority[f.priority] || 0) + 1;
    });

    // Count by component
    this.feedback.forEach(f => {
      stats.byComponent[f.component] = (stats.byComponent[f.component] || 0) + 1;
    });

    // Count by status
    this.feedback.forEach(f => {
      stats.byStatus[f.status] = (stats.byStatus[f.status] || 0) + 1;
    });

    return stats;
  }

  exportFeedback(): string {
    return JSON.stringify(this.feedback, null, 2);
  }

  importFeedback(data: string): boolean {
    try {
      const imported = JSON.parse(data);
      if (Array.isArray(imported)) {
        this.feedback = imported;
        this.saveFeedback();
        return true;
      }
      return false;
    } catch (error) {
      console.warn('Failed to import feedback:', error);
      return false;
    }
  }

  clearFeedback(): void {
    this.feedback = [];
    this.saveFeedback();
  }

  // Analytics methods
  getTrends(): {
    dailyCounts: Record<string, number>;
    weeklyCounts: Record<string, number>;
    monthlyCounts: Record<string, number>;
  } {
    const dailyCounts: Record<string, number> = {};
    const weeklyCounts: Record<string, number> = {};
    const monthlyCounts: Record<string, number> = {};

    this.feedback.forEach(f => {
      const date = new Date(f.timestamp);
      const dayKey = date.toISOString().split('T')[0];
      const weekKey = `${date.getFullYear()}-W${Math.ceil((date.getDate() + date.getDay()) / 7)}`;
      const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;

      dailyCounts[dayKey] = (dailyCounts[dayKey] || 0) + 1;
      weeklyCounts[weekKey] = (weeklyCounts[weekKey] || 0) + 1;
      monthlyCounts[monthKey] = (monthlyCounts[monthKey] || 0) + 1;
    });

    return { dailyCounts, weeklyCounts, monthlyCounts };
  }
}

// Hook for using feedback manager in React components
export const useFeedbackManager = () => {
  const managerRef = useRef<FeedbackManager | null>(null);
  const [feedback, setFeedback] = useState<FeedbackData[]>([]);
  const [stats, setStats] = useState<FeedbackStats | null>(null);

  // Initialize ref only once using recommended pattern
  if (managerRef.current == null) {
    managerRef.current = new FeedbackManager();
  }

  const refreshFeedback = useCallback(() => {
    if (managerRef.current) {
      setFeedback(managerRef.current.getAllFeedback());
      setStats(managerRef.current.getStats());
    }
  }, []);

  useEffect(() => {
    refreshFeedback();
  }, [refreshFeedback]);

  const addFeedback = useCallback(
    (feedbackData: Omit<FeedbackData, 'id' | 'status'>) => {
      const id = managerRef.current!.addFeedback(feedbackData);
      refreshFeedback();
      return id;
    },
    [refreshFeedback]
  );

  const updateFeedback = useCallback(
    (id: string, updates: Partial<FeedbackData>) => {
      const success = managerRef.current!.updateFeedback(id, updates);
      if (success) {
        refreshFeedback();
      }
      return success;
    },
    [refreshFeedback]
  );

  const deleteFeedback = useCallback(
    (id: string) => {
      const success = managerRef.current!.deleteFeedback(id);
      if (success) {
        refreshFeedback();
      }
      return success;
    },
    [refreshFeedback]
  );

  const searchFeedback = useCallback((query: string) => {
    return managerRef.current!.searchFeedback(query);
  }, []);

  const getFeedbackByType = useCallback((type: FeedbackData['type']) => {
    return managerRef.current!.getFeedbackByType(type);
  }, []);

  const getFeedbackByComponent = useCallback((component: FeedbackData['component']) => {
    return managerRef.current!.getFeedbackByComponent(component);
  }, []);

  const exportFeedback = useCallback(() => {
    return managerRef.current!.exportFeedback();
  }, []);

  const importFeedback = useCallback(
    (data: string) => {
      const success = managerRef.current!.importFeedback(data);
      if (success) {
        refreshFeedback();
      }
      return success;
    },
    [refreshFeedback]
  );

  const clearFeedback = useCallback(() => {
    managerRef.current!.clearFeedback();
    refreshFeedback();
  }, [refreshFeedback]);

  return {
    feedback,
    stats,
    addFeedback,
    updateFeedback,
    deleteFeedback,
    searchFeedback,
    getFeedbackByType,
    getFeedbackByComponent,
    exportFeedback,
    importFeedback,
    clearFeedback,
    refreshFeedback,
  };
};

export { FeedbackManager };
export type { FeedbackData, FeedbackStats };
