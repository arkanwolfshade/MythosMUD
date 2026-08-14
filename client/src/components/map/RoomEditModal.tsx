/**
 * Room Edit Modal component.
 */

import React from 'react';
import { RoomEditModalForm } from './RoomEditModalForm';
import { RoomEditModalTabs } from './RoomEditModalTabs';
import { useRoomEditModal, type RoomEditModalProps } from './useRoomEditModal';

export type { RoomEditModalProps } from './useRoomEditModal';

interface EnvironmentOption {
  value: string;
  label: string;
  description: string;
}

const ENVIRONMENT_OPTIONS: EnvironmentOption[] = [
  { value: '', label: 'Not Set', description: 'No specific environment type' },
  { value: 'indoors', label: 'Indoors', description: 'Enclosed interior space' },
  { value: 'outdoors', label: 'Outdoors', description: 'Open-air exterior space' },
  { value: 'underwater', label: 'Underwater', description: 'Submerged aquatic environment' },
  { value: 'intersection', label: 'Intersection', description: 'Street or path intersection' },
  { value: 'street_paved', label: 'Street (Paved)', description: 'Paved road or street' },
];

const RoomEditModalHeader = (props: { roomId: string; onClose: () => void }): React.ReactElement => (
  <div className="flex items-center justify-between p-6 border-b border-mythos-terminal-border bg-mythos-terminal-surface">
    <div>
      <h2 id="room-edit-title" className="text-2xl font-bold text-mythos-terminal-text">
        Edit Room
      </h2>
      <p className="text-sm text-mythos-terminal-text/60 mt-1 font-mono">{props.roomId}</p>
    </div>
    <button
      onClick={props.onClose}
      className="text-mythos-terminal-text hover:text-mythos-terminal-error text-3xl leading-none w-8 h-8 flex items-center justify-center rounded hover:bg-mythos-terminal-background transition-colors"
      aria-label="Close dialog"
      type="button"
    >
      ×
    </button>
  </div>
);

const RoomEditModalFooter = (props: {
  onClose: () => void;
  isFormValid: boolean;
  onSubmit: (e: React.FormEvent) => void;
}): React.ReactElement => (
  <>
    <div className="flex justify-end gap-3 p-6 border-t border-mythos-terminal-border bg-mythos-terminal-surface">
      <button
        type="button"
        onClick={props.onClose}
        className="px-4 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface transition-colors"
      >
        Cancel
      </button>
      <button
        type="submit"
        onClick={props.onSubmit}
        disabled={!props.isFormValid}
        className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        Update Room
      </button>
    </div>
    <div className="px-6 pb-4 text-xs text-mythos-terminal-text/50 text-center border-t border-mythos-terminal-border bg-mythos-terminal-surface">
      Press ESC to close
    </div>
  </>
);

const RoomEditModalContent = (props: {
  roomId: string;
  onClose: () => void;
  activeTab: 'basic' | 'location' | 'properties';
  onTabChange: (tab: 'basic' | 'location' | 'properties') => void;
  formProps: Omit<
    React.ComponentProps<typeof RoomEditModalForm>,
    'baseInputClasses' | 'baseTextAreaClasses' | 'baseMonoInputClasses'
  >;
  isFormValid: boolean;
  onSubmit: (e: React.FormEvent) => void;
}): React.ReactElement => {
  const baseInputClasses =
    'w-full px-3 py-2 bg-mythos-terminal-background border rounded text-mythos-terminal-text ' +
    'focus:outline-hidden focus:ring-2 focus:ring-mythos-terminal-primary focus:border-transparent';

  return (
    <div
      className="relative z-10 bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg w-full max-w-4xl max-h-modal overflow-hidden shadow-xl flex flex-col"
      role="dialog"
      aria-modal="true"
      aria-labelledby="room-edit-title"
    >
      <RoomEditModalHeader roomId={props.roomId} onClose={props.onClose} />
      <RoomEditModalTabs activeTab={props.activeTab} onTabChange={props.onTabChange} />
      <div className="flex-1 overflow-y-auto p-6">
        <RoomEditModalForm
          {...props.formProps}
          baseInputClasses={baseInputClasses}
          baseTextAreaClasses={`${baseInputClasses} resize-y font-mono text-sm`}
          baseMonoInputClasses={`${baseInputClasses} font-mono text-sm`}
        />
      </div>
      <RoomEditModalFooter onClose={props.onClose} isFormValid={props.isFormValid} onSubmit={props.onSubmit} />
    </div>
  );
};

function RoomEditModalShell(props: {
  roomId: string;
  onClose: () => void;
  activeTab: 'basic' | 'location' | 'properties';
  onTabChange: (tab: 'basic' | 'location' | 'properties') => void;
  formProps: Omit<
    React.ComponentProps<typeof RoomEditModalForm>,
    'baseInputClasses' | 'baseTextAreaClasses' | 'baseMonoInputClasses'
  >;
  isFormValid: boolean;
  onSubmit: (e: React.FormEvent) => void;
}): React.ReactElement {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-75 border-0 p-0"
        onClick={props.onClose}
        aria-label="Dismiss dialog (backdrop)"
      />
      <RoomEditModalContent {...props} />
    </div>
  );
}

export const RoomEditModal: React.FC<RoomEditModalProps> = props => {
  const vm = useRoomEditModal(props);
  if (!props.isOpen) return null;

  const selectedEnvironment = ENVIRONMENT_OPTIONS.find(opt => opt.value === vm.formData.environment);

  return (
    <RoomEditModalShell
      roomId={props.room.id}
      onClose={props.onClose}
      activeTab={vm.activeTab}
      onTabChange={vm.setActiveTab}
      isFormValid={vm.isFormValid}
      onSubmit={vm.handleSubmit}
      formProps={{
        activeTab: vm.activeTab,
        formData: vm.formData,
        errors: vm.errors,
        touched: vm.touched,
        environmentOptions: ENVIRONMENT_OPTIONS,
        selectedEnvironment,
        onFieldChange: vm.handleFieldChange,
        onFieldBlur: vm.handleFieldBlur,
        onSubmit: vm.handleSubmit,
      }}
    />
  );
};
