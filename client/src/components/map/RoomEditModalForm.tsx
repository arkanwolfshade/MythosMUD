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

function fieldBorderClass(hasError: boolean): string {
  return hasError ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border';
}

function FieldError({ id, message }: { id: string; message: string }): React.ReactElement {
  return (
    <p id={id} className="text-xs text-mythos-terminal-error mt-1" role="alert">
      {message}
    </p>
  );
}

function RoomEditNameField(props: RoomEditModalFormProps): React.ReactElement {
  const { formData, errors, touched, baseInputClasses, onFieldChange, onFieldBlur } = props;
  const showError = Boolean(errors.name && touched.name);
  return (
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
        className={`${baseInputClasses} ${fieldBorderClass(showError)}`}
        aria-invalid={showError ? 'true' : 'false'}
        aria-describedby={showError ? 'name-error' : 'name-help'}
      />
      {showError ? <FieldError id="name-error" message={errors.name} /> : null}
      <p id="name-help" className="text-xs text-mythos-terminal-text/50 mt-1">
        {formData.name.length}/200 characters
      </p>
    </div>
  );
}

function RoomEditDescriptionHint({ description }: { description: string }): React.ReactElement {
  const tooShort = description.trim().length > 0 && description.trim().length < 10;
  return (
    <p id="description-help" className="text-xs text-mythos-terminal-text/50 mt-1">
      {description.length}/2000 characters
      {tooShort ? <span className="text-mythos-terminal-warning ml-2">(minimum 10 characters recommended)</span> : null}
    </p>
  );
}

function RoomEditDescriptionField(props: RoomEditModalFormProps): React.ReactElement {
  const { formData, errors, touched, baseTextAreaClasses, onFieldChange, onFieldBlur } = props;
  const showError = Boolean(errors.description && touched.description);
  return (
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
        className={`${baseTextAreaClasses} ${fieldBorderClass(showError)}`}
        aria-invalid={showError ? 'true' : 'false'}
        aria-describedby={showError ? 'description-error' : 'description-help'}
      />
      {showError ? <FieldError id="description-error" message={errors.description} /> : null}
      <RoomEditDescriptionHint description={formData.description} />
    </div>
  );
}

function RoomEditPlaneField({ formData }: { formData: RoomEditFormData }): React.ReactElement {
  return (
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
  );
}

function RoomEditZoneField({ formData }: { formData: RoomEditFormData }): React.ReactElement {
  return (
    <div>
      <label htmlFor="room-zone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
        Zone
      </label>
      <input
        id="room-zone"
        type="text"
        value={formData.zone}
        disabled
        className="w-full px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text/50 font-mono text-sm disabled:opacity-50 disabled:cursor-not-allowed"
        aria-label="Zone identifier (read-only)"
      />
      <p className="text-xs text-mythos-terminal-text/50 mt-1">
        Zone cannot be changed here -- moving a room to another zone is a structural change, not a property edit. See
        #627.
      </p>
    </div>
  );
}

function RoomEditSubZoneField({ formData }: { formData: RoomEditFormData }): React.ReactElement {
  return (
    <div>
      <label htmlFor="room-subzone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
        Sub-zone
      </label>
      <input
        id="room-subzone"
        type="text"
        value={formData.sub_zone}
        disabled
        className="w-full px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text/50 font-mono text-sm disabled:opacity-50 disabled:cursor-not-allowed"
        aria-label="Sub-zone identifier (read-only)"
      />
      <p className="text-xs text-mythos-terminal-text/50 mt-1">
        Sub-zone cannot be changed here -- moving a room to another subzone is a structural change, not a property edit.
        See #627.
      </p>
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
      <RoomEditTabBody {...props} />
    </form>
  );
}

function RoomEditTabBody(props: RoomEditModalFormProps): React.ReactElement {
  if (props.activeTab === 'basic') {
    return (
      <div className="space-y-6">
        <RoomEditNameField {...props} />
        <RoomEditDescriptionField {...props} />
      </div>
    );
  }
  if (props.activeTab === 'location') {
    return (
      <div className="space-y-6">
        <RoomEditPlaneField formData={props.formData} />
        <RoomEditZoneField formData={props.formData} />
        <RoomEditSubZoneField formData={props.formData} />
      </div>
    );
  }
  if (props.activeTab === 'properties') return <RoomEditPropertiesTab {...props} />;
  const _exhaustive: never = props.activeTab;
  return _exhaustive;
}
