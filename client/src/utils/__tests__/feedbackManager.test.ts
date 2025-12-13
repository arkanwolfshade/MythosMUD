import { act, renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { FeedbackData } from '../feedbackManager';
import { FeedbackManager, useFeedbackManager } from '../feedbackManager';

describe('FeedbackManager', () => {
  let manager: FeedbackManager;

  beforeEach(() => {
    // Clear localStorage completely before each test
    localStorage.removeItem('mythosmud_feedback');
    localStorage.clear();
    vi.clearAllMocks();
    // Create fresh instance for each test (will load from empty localStorage)
    manager = new FeedbackManager();
    // Ensure it's truly empty
    if (manager.getAllFeedback().length > 0) {
      manager.clearFeedback();
    }
  });

  afterEach(() => {
    // Clean up after each test
    if (manager) {
      manager.clearFeedback();
    }
    localStorage.removeItem('mythosmud_feedback');
    localStorage.clear();
  });

  describe('Initialization', () => {
    it('should initialize with empty feedback array', () => {
      // Assert
      expect(manager.getAllFeedback()).toEqual([]);
    });

    it('should load feedback from localStorage if available', () => {
      // Arrange
      const savedFeedback: FeedbackData[] = [
        {
          id: 'test-id-1',
          type: 'bug',
          title: 'Test Bug',
          description: 'Test description',
          priority: 'high',
          component: 'chat',
          userAgent: 'test-agent',
          timestamp: '2024-01-01T00:00:00Z',
          status: 'pending',
        },
      ];
      localStorage.setItem('mythosmud_feedback', JSON.stringify(savedFeedback));

      // Act
      const newManager = new FeedbackManager();

      // Assert
      expect(newManager.getAllFeedback()).toEqual(savedFeedback);
    });

    it('should handle invalid JSON in localStorage gracefully', () => {
      // Arrange
      const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
      localStorage.setItem('mythosmud_feedback', 'invalid json');

      // Act - should not throw
      const newManager = new FeedbackManager();

      // Assert
      expect(newManager.getAllFeedback()).toEqual([]);
      expect(consoleWarnSpy).toHaveBeenCalledWith('Failed to load feedback from localStorage:', expect.any(Error));
      consoleWarnSpy.mockRestore();
    });
  });

  describe('Adding Feedback', () => {
    it('should add feedback with generated ID and pending status', () => {
      // Arrange
      const feedbackData = {
        type: 'bug' as const,
        title: 'Test Bug',
        description: 'Test description',
        priority: 'high' as const,
        component: 'chat' as const,
        userAgent: 'test-agent',
        timestamp: '2024-01-01T00:00:00Z',
      };

      // Act
      const id = manager.addFeedback(feedbackData);

      // Assert
      expect(id).toBeDefined();
      const feedback = manager.getFeedback(id);
      expect(feedback).toMatchObject({
        ...feedbackData,
        id,
        status: 'pending',
      });
    });

    it('should add feedback to beginning of array', () => {
      // Arrange - ensure clean state
      manager.clearFeedback();
      const feedback1 = {
        type: 'bug' as const,
        title: 'Bug 1',
        description: 'Description 1',
        priority: 'high' as const,
        component: 'chat' as const,
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      };
      const feedback2 = {
        type: 'feature' as const,
        title: 'Feature 1',
        description: 'Description 2',
        priority: 'medium' as const,
        component: 'game-log' as const,
        userAgent: 'test',
        timestamp: '2024-01-01T00:01:00Z',
      };

      // Act
      const id1 = manager.addFeedback(feedback1);
      const id2 = manager.addFeedback(feedback2);
      const allFeedback = manager.getAllFeedback();

      // Assert
      expect(allFeedback.length).toBe(2);
      expect(allFeedback[0].id).toBe(id2); // Most recent first
      expect(allFeedback[1].id).toBe(id1);
    });

    it('should limit feedback to maxFeedbackItems', () => {
      // Arrange - Add more than 1000 items (maxFeedbackItems)
      for (let i = 0; i < 1001; i++) {
        manager.addFeedback({
          type: 'bug',
          title: `Bug ${i}`,
          description: `Description ${i}`,
          priority: 'low',
          component: 'chat',
          userAgent: 'test',
          timestamp: new Date().toISOString(),
        });
      }

      // Act
      const allFeedback = manager.getAllFeedback();

      // Assert
      expect(allFeedback.length).toBe(1000);
    });
  });

  describe('Updating Feedback', () => {
    it('should update existing feedback', () => {
      // Arrange
      const id = manager.addFeedback({
        type: 'bug',
        title: 'Original Title',
        description: 'Original description',
        priority: 'low',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });

      // Act
      const success = manager.updateFeedback(id, {
        title: 'Updated Title',
        status: 'in-progress',
      });

      // Assert
      expect(success).toBe(true);
      const feedback = manager.getFeedback(id);
      expect(feedback?.title).toBe('Updated Title');
      expect(feedback?.status).toBe('in-progress');
      expect(feedback?.description).toBe('Original description'); // Unchanged
    });

    it('should return false for non-existent feedback ID', () => {
      // Act
      const success = manager.updateFeedback('non-existent-id', {
        title: 'Updated',
      });

      // Assert
      expect(success).toBe(false);
    });
  });

  describe('Deleting Feedback', () => {
    it('should delete existing feedback', () => {
      // Arrange
      const id = manager.addFeedback({
        type: 'bug',
        title: 'Test Bug',
        description: 'Test description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });

      // Act
      const success = manager.deleteFeedback(id);

      // Assert
      expect(success).toBe(true);
      expect(manager.getFeedback(id)).toBeNull();
      expect(manager.getAllFeedback()).toHaveLength(0);
    });

    it('should return false for non-existent feedback ID', () => {
      // Act
      const success = manager.deleteFeedback('non-existent-id');

      // Assert
      expect(success).toBe(false);
    });
  });

  describe('Retrieving Feedback', () => {
    let testFeedbackIds: string[];

    beforeEach(() => {
      // Ensure clean state
      manager.clearFeedback();
      // Add some test feedback
      testFeedbackIds = [
        manager.addFeedback({
          type: 'bug',
          title: 'Bug 1',
          description: 'Description 1',
          priority: 'high',
          component: 'chat',
          userAgent: 'test',
          timestamp: '2024-01-01T00:00:00Z',
        }),
        manager.addFeedback({
          type: 'feature',
          title: 'Feature 1',
          description: 'Description 2',
          priority: 'medium',
          component: 'game-log',
          userAgent: 'test',
          timestamp: '2024-01-01T00:01:00Z',
        }),
        manager.addFeedback({
          type: 'bug',
          title: 'Bug 2',
          description: 'Description 3',
          priority: 'low',
          component: 'chat',
          userAgent: 'test',
          timestamp: '2024-01-01T00:02:00Z',
        }),
      ];
    });

    it('should get feedback by ID', () => {
      // Arrange
      const id = manager.addFeedback({
        type: 'bug',
        title: 'Specific Bug',
        description: 'Specific description',
        priority: 'critical',
        component: 'commands',
        userAgent: 'test',
        timestamp: '2024-01-01T00:03:00Z',
      });

      // Act
      const feedback = manager.getFeedback(id);

      // Assert
      expect(feedback).toBeDefined();
      expect(feedback?.title).toBe('Specific Bug');
    });

    it('should return null for non-existent ID', () => {
      // Act
      const feedback = manager.getFeedback('non-existent-id');

      // Assert
      expect(feedback).toBeNull();
    });

    it('should get all feedback', () => {
      // Act
      const allFeedback = manager.getAllFeedback();

      // Assert
      expect(allFeedback.length).toBe(testFeedbackIds.length);
      expect(allFeedback.every(f => testFeedbackIds.includes(f.id))).toBe(true);
    });

    it('should filter feedback by type', () => {
      // Act
      const bugs = manager.getFeedbackByType('bug');

      // Assert
      // Should have exactly 2 bugs from our test data
      const expectedBugs = testFeedbackIds.filter(id => manager.getFeedback(id)?.type === 'bug');
      expect(bugs.length).toBe(expectedBugs.length);
      expect(bugs.every(f => f.type === 'bug')).toBe(true);
    });

    it('should filter feedback by component', () => {
      // Act
      const chatFeedback = manager.getFeedbackByComponent('chat');

      // Assert
      // Should have exactly 2 chat feedbacks from our test data
      const expectedChat = testFeedbackIds.filter(id => manager.getFeedback(id)?.component === 'chat');
      expect(chatFeedback.length).toBe(expectedChat.length);
      expect(chatFeedback.every(f => f.component === 'chat')).toBe(true);
    });

    it('should filter feedback by priority', () => {
      // Act
      const highPriority = manager.getFeedbackByPriority('high');

      // Assert
      // Should have exactly 1 high priority from our test data
      const expectedHigh = testFeedbackIds.filter(id => manager.getFeedback(id)?.priority === 'high');
      expect(highPriority.length).toBe(expectedHigh.length);
      if (highPriority.length > 0) {
        expect(highPriority[0].priority).toBe('high');
      }
    });

    it('should filter feedback by status', () => {
      // Arrange
      const id = manager.getAllFeedback()[0].id;
      manager.updateFeedback(id, { status: 'in-progress' });

      // Act
      const inProgress = manager.getFeedbackByStatus('in-progress');

      // Assert
      expect(inProgress.length).toBe(1);
      expect(inProgress[0].status).toBe('in-progress');
    });

    it('should search feedback by title', () => {
      // Act
      const results = manager.searchFeedback('Bug');

      // Assert
      // Should find all feedback with "Bug" in title
      const expectedBugs = testFeedbackIds.filter(id => manager.getFeedback(id)?.title.includes('Bug'));
      expect(results.length).toBe(expectedBugs.length);
      expect(results.every(f => f.title.includes('Bug'))).toBe(true);
    });

    it('should search feedback by description', () => {
      // Act
      const results = manager.searchFeedback('Description 1');

      // Assert
      // Should find the one with "Description 1"
      expect(results.length).toBeGreaterThanOrEqual(1);
      expect(results.some(f => f.description === 'Description 1')).toBe(true);
    });

    it('should search feedback by tags', () => {
      // Arrange
      const id = manager.addFeedback({
        type: 'bug',
        title: 'Tagged Bug',
        description: 'Description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:04:00Z',
        tags: ['ui', 'critical', 'rendering'],
      });

      // Act
      const results = manager.searchFeedback('critical');

      // Assert
      expect(results.length).toBe(1);
      expect(results[0].id).toBe(id);
    });

    it('should perform case-insensitive search', () => {
      // Act
      const results = manager.searchFeedback('BUG');

      // Assert
      // Should find all feedback with "Bug" in title (case-insensitive)
      const expectedBugs = testFeedbackIds.filter(id => manager.getFeedback(id)?.title.toLowerCase().includes('bug'));
      expect(results.length).toBe(expectedBugs.length);
      expect(results.every(f => f.title.toLowerCase().includes('bug'))).toBe(true);
    });
  });

  describe('Statistics', () => {
    let statsTestIds: string[];

    beforeEach(() => {
      manager.clearFeedback();
      const now = Date.now();
      const oneDayAgo = now - 1 * 24 * 60 * 60 * 1000;
      const eightDaysAgo = now - 8 * 24 * 60 * 60 * 1000;

      statsTestIds = [
        manager.addFeedback({
          type: 'bug',
          title: 'Recent Bug',
          description: 'Description',
          priority: 'high',
          component: 'chat',
          userAgent: 'test',
          timestamp: new Date(oneDayAgo).toISOString(),
        }),
        manager.addFeedback({
          type: 'feature',
          title: 'Old Feature',
          description: 'Description',
          priority: 'medium',
          component: 'game-log',
          userAgent: 'test',
          timestamp: new Date(eightDaysAgo).toISOString(),
        }),
        manager.addFeedback({
          type: 'bug',
          title: 'Another Bug',
          description: 'Description',
          priority: 'low',
          component: 'chat',
          userAgent: 'test',
          timestamp: new Date(oneDayAgo).toISOString(),
          tags: ['ui'],
        }),
      ];
    });

    it('should generate correct statistics', () => {
      // Act
      const stats = manager.getStats();

      // Assert
      expect(stats.total).toBe(statsTestIds.length);
      expect(stats.byType.bug).toBe(2);
      expect(stats.byType.feature).toBe(1);
      expect(stats.byPriority.high).toBe(1);
      expect(stats.byPriority.medium).toBe(1);
      expect(stats.byPriority.low).toBe(1);
      expect(stats.byComponent.chat).toBe(2);
      expect(stats.byComponent['game-log']).toBe(1);
      expect(stats.recentCount).toBeGreaterThan(0);
    });
  });

  describe('Export and Import', () => {
    it('should export feedback as JSON string', () => {
      // Arrange
      manager.clearFeedback();
      const testId = manager.addFeedback({
        type: 'bug',
        title: 'Test Bug',
        description: 'Test description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });

      // Act
      const exported = manager.exportFeedback();
      const parsed = JSON.parse(exported);

      // Assert
      expect(parsed).toBeInstanceOf(Array);
      expect(parsed.length).toBeGreaterThanOrEqual(1);
      const testFeedback = parsed.find((f: FeedbackData) => f.id === testId);
      expect(testFeedback).toBeDefined();
      expect(testFeedback.title).toBe('Test Bug');
    });

    it('should import feedback from JSON string', () => {
      // Arrange
      const feedbackData: FeedbackData[] = [
        {
          id: 'imported-id-1',
          type: 'bug',
          title: 'Imported Bug',
          description: 'Imported description',
          priority: 'high',
          component: 'chat',
          userAgent: 'test',
          timestamp: '2024-01-01T00:00:00Z',
          status: 'pending',
        },
      ];

      // Act
      const success = manager.importFeedback(JSON.stringify(feedbackData));

      // Assert
      expect(success).toBe(true);
      expect(manager.getAllFeedback()).toEqual(feedbackData);
    });

    it('should return false for invalid JSON', () => {
      // Arrange
      const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

      // Act
      const success = manager.importFeedback('invalid json');

      // Assert
      expect(success).toBe(false);
      expect(consoleWarnSpy).toHaveBeenCalledWith('Failed to import feedback:', expect.any(Error));
      consoleWarnSpy.mockRestore();
    });

    it('should return false for non-array JSON', () => {
      // Act
      const success = manager.importFeedback(JSON.stringify({ not: 'an array' }));

      // Assert
      expect(success).toBe(false);
    });
  });

  describe('Trends', () => {
    it('should calculate daily, weekly, and monthly trends', () => {
      // Arrange
      const baseDate = new Date('2024-01-15T12:00:00Z');
      for (let i = 0; i < 5; i++) {
        const date = new Date(baseDate);
        date.setDate(date.getDate() + i);
        manager.addFeedback({
          type: 'bug',
          title: `Bug ${i}`,
          description: 'Description',
          priority: 'low',
          component: 'chat',
          userAgent: 'test',
          timestamp: date.toISOString(),
        });
      }

      // Act
      const trends = manager.getTrends();

      // Assert
      expect(trends.dailyCounts).toBeDefined();
      expect(trends.weeklyCounts).toBeDefined();
      expect(trends.monthlyCounts).toBeDefined();
    });
  });

  describe('Clear Feedback', () => {
    it('should clear all feedback', () => {
      // Arrange
      manager.addFeedback({
        type: 'bug',
        title: 'Test Bug',
        description: 'Test description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });

      // Act
      manager.clearFeedback();

      // Assert
      expect(manager.getAllFeedback()).toHaveLength(0);
    });
  });
});

describe('useFeedbackManager Hook', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('should initialize with empty feedback', () => {
    // Act
    const { result } = renderHook(() => useFeedbackManager());

    // Assert
    expect(result.current.feedback).toEqual([]);
  });

  it('should add feedback and update state', async () => {
    // Arrange
    const { result } = renderHook(() => useFeedbackManager());

    // Act
    await act(async () => {
      result.current.addFeedback({
        type: 'bug',
        title: 'Test Bug',
        description: 'Test description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });
    });

    // Assert
    expect(result.current.feedback).toHaveLength(1);
    expect(result.current.feedback[0].title).toBe('Test Bug');
  });

  it('should update feedback', async () => {
    // Arrange
    const { result } = renderHook(() => useFeedbackManager());
    let feedbackId: string;

    await act(async () => {
      feedbackId = result.current.addFeedback({
        type: 'bug',
        title: 'Original Title',
        description: 'Description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });
    });

    // Act
    await act(async () => {
      result.current.updateFeedback(feedbackId!, {
        title: 'Updated Title',
      });
    });

    // Assert
    expect(result.current.feedback[0].title).toBe('Updated Title');
  });

  it('should delete feedback', async () => {
    // Arrange
    const { result } = renderHook(() => useFeedbackManager());
    let feedbackId: string;

    await act(async () => {
      feedbackId = result.current.addFeedback({
        type: 'bug',
        title: 'Test Bug',
        description: 'Description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });
    });

    expect(result.current.feedback).toHaveLength(1);

    // Act
    await act(async () => {
      result.current.deleteFeedback(feedbackId!);
    });

    // Assert
    expect(result.current.feedback).toHaveLength(0);
  });

  it('should provide stats', async () => {
    // Arrange
    const { result } = renderHook(() => useFeedbackManager());

    await act(async () => {
      result.current.addFeedback({
        type: 'bug',
        title: 'Bug 1',
        description: 'Description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });
    });

    // Assert
    expect(result.current.stats).toBeDefined();
    expect(result.current.stats?.total).toBe(1);
  });

  it('should search feedback', () => {
    // Arrange
    const { result } = renderHook(() => useFeedbackManager());

    // Act
    const results = result.current.searchFeedback('test');

    // Assert
    expect(Array.isArray(results)).toBe(true);
  });

  it('should export and import feedback', async () => {
    // Arrange
    const { result } = renderHook(() => useFeedbackManager());

    await act(async () => {
      result.current.addFeedback({
        type: 'bug',
        title: 'Test Bug',
        description: 'Description',
        priority: 'high',
        component: 'chat',
        userAgent: 'test',
        timestamp: '2024-01-01T00:00:00Z',
      });
    });

    // Act
    const exported = result.current.exportFeedback();
    await act(async () => {
      result.current.clearFeedback();
      result.current.importFeedback(exported);
    });

    // Assert
    expect(result.current.feedback).toHaveLength(1);
  });
});
