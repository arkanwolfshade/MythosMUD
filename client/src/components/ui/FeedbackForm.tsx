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

type FeedbackDraft = Omit<FeedbackData, 'userAgent' | 'timestamp'>;

const formSelectClasses =
  'w-full bg-mythos-terminal-surface border border-mythos-terminal-border rounded px-3 py-2 text-mythos-terminal-text-primary focus:outline-hidden focus:border-mythos-terminal-primary';
const formTextareaClasses = formSelectClasses + ' resize-y';
const labelClasses = 'block text-sm font-medium text-mythos-terminal-text-secondary mb-2';

const DEFAULT_FEEDBACK: FeedbackDraft = {
  type: 'general',
  title: '',
  description: '',
  priority: 'medium',
  component: 'all',
};

const TEMPLATES: Array<{ label: string; patch: Partial<FeedbackDraft> }> = [
  {
    label: 'Performance Issue',
    patch: {
      type: 'bug',
      title: 'Performance Issue',
      description: 'The component is running slowly or consuming too much memory.',
      priority: 'high',
    },
  },
  {
    label: 'Feature Request',
    patch: {
      type: 'feature',
      title: 'New Feature Request',
      description: 'I would like to see a new feature added to improve the user experience.',
      priority: 'medium',
    },
  },
  {
    label: 'UI/UX Improvement',
    patch: {
      type: 'improvement',
      title: 'UI/UX Improvement',
      description: 'The interface could be improved for better usability.',
      priority: 'low',
    },
  },
  {
    label: 'Bug Report',
    patch: {
      type: 'bug',
      title: 'Bug Report',
      description: 'I found a bug that needs to be fixed.',
      priority: 'high',
    },
  },
];

const SELECT_FIELDS: Array<{
  id: string;
  label: string;
  field: 'type' | 'component' | 'priority';
  options: Array<{ value: string; label: string }>;
}> = [
  {
    id: 'feedback-type',
    label: 'Feedback Type',
    field: 'type',
    options: [
      { value: 'general', label: 'General Feedback' },
      { value: 'bug', label: 'Bug Report' },
      { value: 'feature', label: 'Feature Request' },
      { value: 'improvement', label: 'Improvement Suggestion' },
    ],
  },
  {
    id: 'feedback-component',
    label: 'Related Component',
    field: 'component',
    options: [
      { value: 'all', label: 'All Components' },
      { value: 'chat', label: 'Chat Panel' },
      { value: 'game-log', label: 'Game Log Panel' },
      { value: 'commands', label: 'Commands Panel' },
    ],
  },
  {
    id: 'feedback-priority',
    label: 'Priority',
    field: 'priority',
    options: [
      { value: 'low', label: 'Low' },
      { value: 'medium', label: 'Medium' },
      { value: 'high', label: 'High' },
      { value: 'critical', label: 'Critical' },
    ],
  },
];

function FormSelectField({
  id,
  label,
  value,
  options,
  onChange,
}: {
  id: string;
  label: string;
  value: string;
  options: Array<{ value: string; label: string }>;
  onChange: (value: string) => void;
}) {
  return (
    <div>
      <label htmlFor={id} className={labelClasses}>
        {label}
      </label>
      <select
        id={id}
        value={value}
        onChange={e => {
          onChange(e.target.value);
        }}
        className={formSelectClasses}
      >
        {options.map(option => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}

function FeedbackFields({
  feedback,
  onChange,
}: {
  feedback: FeedbackDraft;
  onChange: (field: keyof FeedbackDraft, value: string) => void;
}) {
  return (
    <>
      {SELECT_FIELDS.map(({ id, label, field, options }) => (
        <FormSelectField
          key={id}
          id={id}
          label={label}
          value={feedback[field]}
          options={options}
          onChange={value => {
            onChange(field, value);
          }}
        />
      ))}
      <div>
        <label htmlFor="feedback-title" className={labelClasses}>
          Title *
        </label>
        <TerminalInput
          id="feedback-title"
          value={feedback.title}
          onChange={e => {
            onChange('title', e.target.value);
          }}
          placeholder="Brief description of your feedback"
          required
        />
      </div>
      <div>
        <label htmlFor="feedback-description" className={labelClasses}>
          Description *
        </label>
        <textarea
          id="feedback-description"
          value={feedback.description}
          onChange={e => {
            onChange('description', e.target.value);
          }}
          placeholder="Please provide detailed information about your feedback, including steps to reproduce if it's a bug report."
          required
          rows={6}
          className={formTextareaClasses}
        />
      </div>
    </>
  );
}

function QuickTemplates({ onApply }: { onApply: (patch: Partial<FeedbackDraft>) => void }) {
  return (
    <div>
      <p className={labelClasses}>Quick Templates</p>
      <div className="grid grid-cols-2 gap-2">
        {TEMPLATES.map(template => (
          <TerminalButton
            key={template.label}
            type="button"
            variant="secondary"
            size="sm"
            onClick={() => {
              onApply(template.patch);
            }}
          >
            {template.label}
          </TerminalButton>
        ))}
      </div>
    </div>
  );
}

export const FeedbackForm: React.FC<FeedbackFormProps> = ({ onSubmit, onCancel, isOpen }) => {
  const [feedback, setFeedback] = useState<FeedbackDraft>(DEFAULT_FEEDBACK);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      ...feedback,
      userAgent: navigator.userAgent,
      timestamp: new Date().toISOString(),
    });
    setFeedback(DEFAULT_FEEDBACK);
  };

  const handleChange = (field: keyof FeedbackDraft, value: string) => {
    setFeedback(prev => ({ ...prev, [field]: value }));
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
        <FeedbackFields feedback={feedback} onChange={handleChange} />
        <QuickTemplates
          onApply={patch => {
            setFeedback(prev => ({ ...prev, ...patch }));
          }}
        />
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
