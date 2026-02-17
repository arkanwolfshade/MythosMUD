import React, { useState } from 'react';
import { EldritchIcon, MythosIcons } from './EldritchIcon';
import { ModalContainer } from './ModalContainer';
import { TerminalButton } from './TerminalButton';
import { TerminalInput } from './TerminalInput';

interface FeedbackFormProps {
  onSubmit: (feedback: FeedbackData) => void;
  onCancel: () => void;
  isOpen: boolean;
}

interface FeedbackData {
  type: 'bug' | 'feature' | 'improvement' | 'general';
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high' | 'critical';
  component: 'chat' | 'game-log' | 'commands' | 'all';
  userAgent: string;
  timestamp: string;
}

const formSelectClasses =
  'w-full bg-mythos-terminal-surface border border-mythos-terminal-border rounded px-3 py-2 text-mythos-terminal-text-primary focus:outline-hidden focus:border-mythos-terminal-primary';
const formTextareaClasses = formSelectClasses + ' resize-y';

export const FeedbackForm: React.FC<FeedbackFormProps> = ({ onSubmit, onCancel, isOpen }) => {
  const [feedback, setFeedback] = useState<Omit<FeedbackData, 'userAgent' | 'timestamp'>>({
    type: 'general',
    title: '',
    description: '',
    priority: 'medium',
    component: 'all',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const feedbackData: FeedbackData = {
      ...feedback,
      userAgent: navigator.userAgent,
      timestamp: new Date().toISOString(),
    };

    onSubmit(feedbackData);

    // Reset form
    setFeedback({
      type: 'general',
      title: '',
      description: '',
      priority: 'medium',
      component: 'all',
    });
  };

  const handleChange = (field: keyof typeof feedback, value: string) => {
    setFeedback(prev => ({
      ...prev,
      [field]: value,
    }));
  };

  return (
    <ModalContainer
      isOpen={isOpen}
      onClose={onCancel}
      maxWidth="2xl"
      contentClassName="p-6"
      titleId="feedback-form-title"
    >
      <div className="flex items-center justify-between mb-4">
        <h2
          id="feedback-form-title"
          className="text-xl font-bold text-mythos-terminal-text-primary flex items-center gap-2"
        >
          <EldritchIcon name={MythosIcons.system} size={20} />
          Feedback & Suggestions
        </h2>
        <TerminalButton onClick={onCancel} variant="secondary" size="sm">
          ✕
        </TerminalButton>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        {/* Feedback Type */}
        <div>
          <label className="block text-sm font-medium text-mythos-terminal-text-secondary mb-2">Feedback Type</label>
          <select
            value={feedback.type}
            onChange={e => {
              handleChange('type', e.target.value);
            }}
            className={formSelectClasses}
          >
            <option value="general">General Feedback</option>
            <option value="bug">Bug Report</option>
            <option value="feature">Feature Request</option>
            <option value="improvement">Improvement Suggestion</option>
          </select>
        </div>

        {/* Component */}
        <div>
          <label className="block text-sm font-medium text-mythos-terminal-text-secondary mb-2">
            Related Component
          </label>
          <select
            value={feedback.component}
            onChange={e => {
              handleChange('component', e.target.value);
            }}
            className={formSelectClasses}
          >
            <option value="all">All Components</option>
            <option value="chat">Chat Panel</option>
            <option value="game-log">Game Log Panel</option>
            <option value="commands">Commands Panel</option>
          </select>
        </div>

        {/* Priority */}
        <div>
          <label className="block text-sm font-medium text-mythos-terminal-text-secondary mb-2">Priority</label>
          <select
            value={feedback.priority}
            onChange={e => {
              handleChange('priority', e.target.value);
            }}
            className={formSelectClasses}
          >
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
            <option value="critical">Critical</option>
          </select>
        </div>

        {/* Title */}
        <div>
          <label className="block text-sm font-medium text-mythos-terminal-text-secondary mb-2">Title *</label>
          <TerminalInput
            value={feedback.title}
            onChange={e => {
              handleChange('title', e.target.value);
            }}
            placeholder="Brief description of your feedback"
            required
          />
        </div>

        {/* Description */}
        <div>
          <label className="block text-sm font-medium text-mythos-terminal-text-secondary mb-2">Description *</label>
          <textarea
            value={feedback.description}
            onChange={e => {
              handleChange('description', e.target.value);
            }}
            placeholder="Please provide detailed information about your feedback, including steps to reproduce if it's a bug report."
            required
            rows={6}
            className={formTextareaClasses}
          />
        </div>

        {/* Quick Feedback Templates */}
        <div>
          <label className="block text-sm font-medium text-mythos-terminal-text-secondary mb-2">Quick Templates</label>
          <div className="grid grid-cols-2 gap-2">
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => {
                setFeedback(prev => ({
                  ...prev,
                  type: 'bug',
                  title: 'Performance Issue',
                  description: 'The component is running slowly or consuming too much memory.',
                  priority: 'high',
                }));
              }}
            >
              Performance Issue
            </TerminalButton>
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => {
                setFeedback(prev => ({
                  ...prev,
                  type: 'feature',
                  title: 'New Feature Request',
                  description: 'I would like to see a new feature added to improve the user experience.',
                  priority: 'medium',
                }));
              }}
            >
              Feature Request
            </TerminalButton>
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => {
                setFeedback(prev => ({
                  ...prev,
                  type: 'improvement',
                  title: 'UI/UX Improvement',
                  description: 'The interface could be improved for better usability.',
                  priority: 'low',
                }));
              }}
            >
              UI/UX Improvement
            </TerminalButton>
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => {
                setFeedback(prev => ({
                  ...prev,
                  type: 'bug',
                  title: 'Bug Report',
                  description: 'I found a bug that needs to be fixed.',
                  priority: 'high',
                }));
              }}
            >
              Bug Report
            </TerminalButton>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex justify-end gap-3 pt-4 border-t border-mythos-terminal-border">
          <TerminalButton type="button" variant="secondary" onClick={onCancel}>
            Cancel
          </TerminalButton>
          <TerminalButton type="submit" variant="primary">
            Submit Feedback
          </TerminalButton>
        </div>
      </form>
    </ModalContainer>
  );
};
