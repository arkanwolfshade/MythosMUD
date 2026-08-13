import React from 'react';

export interface RoomEditFormData {
  name: string;
  description: string;
  plane: string;
  zone: string;
  sub_zone: string;
  environment: string;
}

interface EnvironmentOption {
  value: string;
  label: string;
  description: string;
}

export interface RoomEditModalFormProps {
  activeTab: 'basic' | 'location' | 'properties';
  formData: RoomEditFormData;
  errors: Record<string, string>;
  touched: Record<string, boolean>;
  baseInputClasses: string;
  baseTextAreaClasses: string;
  baseMonoInputClasses: string;
  environmentOptions: EnvironmentOption[];
  selectedEnvironment?: EnvironmentOption;
  onFieldChange: (field: keyof RoomEditFormData, value: string) => void;
  onFieldBlur: (field: keyof RoomEditFormData) => void;
  onSubmit: (e: React.FormEvent) => void;
}

function RoomEditBasicTab(props: RoomEditModalFormProps): React.ReactElement {
  const { formData, errors, touched, baseInputClasses, baseTextAreaClasses, onFieldChange, onFieldBlur } = props;
  return (
    <div className="space-y-6">
      <div>
        <label htmlFor="room-name" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Room Name <span className="text-mythos-terminal-error">*</span>
        </label>
        <input
          id="room-name"
          type="text"
          value={formData.name}
          onChange={e => onFieldChange('name', e.target.value)}
          onBlur={() => onFieldBlur('name')}
          required
          maxLength={200}
          className={`${baseInputClasses} ${
            errors.name && touched.name ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
          }`}
          aria-invalid={errors.name && touched.name ? 'true' : 'false'}
          aria-describedby={errors.name && touched.name ? 'name-error' : 'name-help'}
        />
        {errors.name && touched.name && (
          <p id="name-error" className="text-xs text-mythos-terminal-error mt-1" role="alert">
            {errors.name}
          </p>
        )}
        <p id="name-help" className="text-xs text-mythos-terminal-text/50 mt-1">
          {formData.name.length}/200 characters
        </p>
      </div>

      <div>
        <label htmlFor="room-description" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Description
        </label>
        <textarea
          id="room-description"
          value={formData.description}
          onChange={e => onFieldChange('description', e.target.value)}
          onBlur={() => onFieldBlur('description')}
          rows={8}
          maxLength={2000}
          className={`${baseTextAreaClasses} ${
            errors.description && touched.description ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
          }`}
          aria-invalid={errors.description && touched.description ? 'true' : 'false'}
          aria-describedby={errors.description && touched.description ? 'description-error' : 'description-help'}
        />
        {errors.description && touched.description && (
          <p id="description-error" className="text-xs text-mythos-terminal-error mt-1" role="alert">
            {errors.description}
          </p>
        )}
        <p id="description-help" className="text-xs text-mythos-terminal-text/50 mt-1">
          {formData.description.length}/2000 characters
          {formData.description.trim().length > 0 && formData.description.trim().length < 10 && (
            <span className="text-mythos-terminal-warning ml-2">(minimum 10 characters recommended)</span>
          )}
        </p>
      </div>
    </div>
  );
}

function RoomEditLocationTab(props: RoomEditModalFormProps): React.ReactElement {
  const { formData, errors, touched, baseMonoInputClasses, onFieldChange, onFieldBlur } = props;
  return (
    <div className="space-y-6">
      <div>
        <label htmlFor="room-plane" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Plane <span className="text-mythos-terminal-error">*</span>
        </label>
        <input
          id="room-plane"
          type="text"
          value={formData.plane}
          disabled
          className="w-full px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text/50 font-mono text-sm disabled:opacity-50 disabled:cursor-not-allowed"
          aria-label="Plane identifier (read-only)"
        />
        <p className="text-xs text-mythos-terminal-text/50 mt-1">
          Plane cannot be changed. Delete and recreate the room to change the plane.
        </p>
      </div>

      <div>
        <label htmlFor="room-zone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Zone <span className="text-mythos-terminal-error">*</span>
        </label>
        <input
          id="room-zone"
          type="text"
          value={formData.zone}
          onChange={e => onFieldChange('zone', e.target.value.toLowerCase())}
          onBlur={() => onFieldBlur('zone')}
          required
          pattern="^[a-z0-9_]+$"
          className={`${baseMonoInputClasses} ${
            errors.zone && touched.zone ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
          }`}
          aria-invalid={errors.zone && touched.zone ? 'true' : 'false'}
          aria-describedby={errors.zone && touched.zone ? 'zone-error' : 'zone-help'}
        />
        {errors.zone && touched.zone && (
          <p id="zone-error" className="text-xs text-mythos-terminal-error mt-1" role="alert">
            {errors.zone}
          </p>
        )}
        <p id="zone-help" className="text-xs text-mythos-terminal-text/50 mt-1">
          Lowercase letters, numbers, and underscores only (e.g., arkham_square)
        </p>
      </div>

      <div>
        <label htmlFor="room-subzone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Sub-zone <span className="text-mythos-terminal-text/50 text-xs">(optional)</span>
        </label>
        <input
          id="room-subzone"
          type="text"
          value={formData.sub_zone}
          onChange={e => onFieldChange('sub_zone', e.target.value.toLowerCase())}
          onBlur={() => onFieldBlur('sub_zone')}
          pattern="^[a-z0-9_]*$"
          className={`${baseMonoInputClasses} ${
            errors.sub_zone && touched.sub_zone ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
          }`}
          aria-invalid={errors.sub_zone && touched.sub_zone ? 'true' : 'false'}
          aria-describedby={errors.sub_zone && touched.sub_zone ? 'subzone-error' : 'subzone-help'}
        />
        {errors.sub_zone && touched.sub_zone && (
          <p id="subzone-error" className="text-xs text-mythos-terminal-error mt-1" role="alert">
            {errors.sub_zone}
          </p>
        )}
        <p id="subzone-help" className="text-xs text-mythos-terminal-text/50 mt-1">
          Lowercase letters, numbers, and underscores only (e.g., main_street)
        </p>
      </div>
    </div>
  );
}

function RoomEditPropertiesTab(props: RoomEditModalFormProps): React.ReactElement {
  const { formData, environmentOptions, selectedEnvironment, onFieldChange } = props;
  return (
    <div className="space-y-6">
      <div>
        <label htmlFor="room-environment" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Environment Type
        </label>
        <select
          id="room-environment"
          value={formData.environment}
          onChange={e => onFieldChange('environment', e.target.value)}
          className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text focus:outline-hidden focus:ring-2 focus:ring-mythos-terminal-primary focus:border-transparent"
        >
          {environmentOptions.map(option => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        {selectedEnvironment && selectedEnvironment.description && (
          <p className="text-xs text-mythos-terminal-text/50 mt-1">{selectedEnvironment.description}</p>
        )}
      </div>
      <div className="bg-mythos-terminal-surface border border-mythos-terminal-border rounded p-4">
        <p className="text-sm text-mythos-terminal-text/70">
          <strong className="text-mythos-terminal-text">Note:</strong> Additional properties such as exits, occupants,
          and containers are managed separately through the map interface and room detail panels.
        </p>
      </div>
    </div>
  );
}

export function RoomEditModalForm(props: RoomEditModalFormProps): React.ReactElement {
  return (
    <form onSubmit={props.onSubmit} className="space-y-6">
      {props.activeTab === 'basic' && <RoomEditBasicTab {...props} />}
      {props.activeTab === 'location' && <RoomEditLocationTab {...props} />}
      {props.activeTab === 'properties' && <RoomEditPropertiesTab {...props} />}
    </form>
  );
}

export function RoomEditModalTabs(props: {
  activeTab: 'basic' | 'location' | 'properties';
  onTabChange: (tab: 'basic' | 'location' | 'properties') => void;
}): React.ReactElement {
  const tabClass = (tab: 'basic' | 'location' | 'properties') =>
    `px-4 py-2 font-medium text-sm transition-colors rounded-t ${
      props.activeTab === tab
        ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary bg-mythos-terminal-background'
        : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text hover:bg-mythos-terminal-background/50'
    }`;

  return (
    <div className="flex gap-1 px-6 pt-4 border-b border-mythos-terminal-border bg-mythos-terminal-surface">
      <button
        onClick={() => props.onTabChange('basic')}
        type="button"
        className={tabClass('basic')}
        aria-selected={props.activeTab === 'basic'}
        role="tab"
      >
        Basic Info
      </button>
      <button
        onClick={() => props.onTabChange('location')}
        type="button"
        className={tabClass('location')}
        aria-selected={props.activeTab === 'location'}
        role="tab"
      >
        Location
      </button>
      <button
        onClick={() => props.onTabChange('properties')}
        type="button"
        className={tabClass('properties')}
        aria-selected={props.activeTab === 'properties'}
        role="tab"
      >
        Properties
      </button>
    </div>
  );
}
