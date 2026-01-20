/**
 * Room Edit Modal component.
 *
 * Provides a form dialog for editing room properties including
 * name, description, zone, subzone, environment, and other schema properties.
 * Includes tabs/sections for different property groups and inline validation.
 *
 * As documented in the Pnakotic Manuscripts, proper management of
 * spatial entity properties is essential for maintaining the integrity
 * of our eldritch architecture.
 */

import React, { useCallback, useEffect, useState } from 'react';
import type { Room } from '../../stores/gameStore';
import type { RoomNodeData } from './types';

export interface RoomEditModalProps {
  /** Whether the modal is open */
  isOpen: boolean;
  /** Callback when modal should close */
  onClose: () => void;
  /** Room data to edit */
  room: Room;
  /** Callback when room should be updated */
  onUpdate: (roomId: string, updates: Partial<RoomNodeData>) => void;
}

/**
 * Environment option with description for the selector.
 */
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

/**
 * Room Edit Modal component.
 */
export const RoomEditModal: React.FC<RoomEditModalProps> = ({ isOpen, onClose, room, onUpdate }) => {
  const [activeTab, setActiveTab] = useState<'basic' | 'location' | 'properties'>('basic');
  const [formData, setFormData] = useState({
    name: room.name || '',
    description: room.description || '',
    plane: room.plane || '',
    zone: room.zone || '',
    sub_zone: room.sub_zone || '',
    environment: room.environment || '',
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});

  // Reset form when modal opens/closes or room changes
  useEffect(() => {
    if (isOpen && room) {
      setFormData({
        name: room.name || '',
        description: room.description || '',
        plane: room.plane || '',
        zone: room.zone || '',
        sub_zone: room.sub_zone || '',
        environment: room.environment || '',
      });
      setErrors({});
      setTouched({});
      setActiveTab('basic');
    }
  }, [isOpen, room]);

  // Handle ESC key
  useEffect(() => {
    if (!isOpen) return;

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isOpen, onClose]);

  // Prevent body scroll
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  // Validate form field
  const validateField = useCallback((field: string, value: string): string => {
    switch (field) {
      case 'name':
        if (!value.trim()) {
          return 'Room name is required';
        }
        if (value.length > 200) {
          return 'Room name must be 200 characters or less';
        }
        if (value.length < 1) {
          return 'Room name must be at least 1 character';
        }
        break;
      case 'description':
        if (value.length > 2000) {
          return 'Description must be 2000 characters or less';
        }
        if (value.trim().length > 0 && value.trim().length < 10) {
          return 'Description must be at least 10 characters if provided';
        }
        break;
      case 'plane':
        if (!value.trim()) {
          return 'Plane is required';
        }
        break;
      case 'zone':
        if (!value.trim()) {
          return 'Zone is required';
        }
        // Validate pattern: lowercase alphanumeric and underscores
        if (!/^[a-z0-9_]+$/.test(value)) {
          return 'Zone must contain only lowercase letters, numbers, and underscores';
        }
        break;
      case 'sub_zone':
        // Validate pattern if provided
        if (value.trim() && !/^[a-z0-9_]+$/.test(value)) {
          return 'Sub-zone must contain only lowercase letters, numbers, and underscores';
        }
        break;
      default:
        break;
    }
    return '';
  }, []);

  // Handle field change
  const handleFieldChange = useCallback(
    (field: keyof typeof formData, value: string) => {
      setFormData(prev => ({ ...prev, [field]: value }));
      setTouched(prev => ({ ...prev, [field]: true }));

      // Validate on change
      const error = validateField(field, value);
      setErrors(prev => {
        if (error) {
          return { ...prev, [field]: error };
        } else {
          // Destructuring removes field from errors object, _removed variable intentionally unused
          // eslint-disable-next-line @typescript-eslint/no-unused-vars
          const { [field]: _removed, ...rest } = prev;
          return rest;
        }
      });
    },
    [validateField]
  );

  // Handle field blur
  const handleFieldBlur = useCallback((field: keyof typeof formData) => {
    setTouched(prev => ({ ...prev, [field]: true }));
  }, []);

  // Handle form submission
  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();

      // Mark all fields as touched
      const allFields: Array<keyof typeof formData> = [
        'name',
        'description',
        'plane',
        'zone',
        'sub_zone',
        'environment',
      ];
      const newTouched: Record<string, boolean> = {};
      allFields.forEach(field => {
        newTouched[field] = true;
      });
      setTouched(newTouched);

      // Validate all fields
      const newErrors: Record<string, string> = {};
      Object.entries(formData).forEach(([field, value]) => {
        const error = validateField(field, value);
        if (error) {
          newErrors[field] = error;
        }
      });

      if (Object.keys(newErrors).length > 0) {
        setErrors(newErrors);
        return;
      }

      // Convert form data to room updates
      const updates: Partial<RoomNodeData> = {
        name: formData.name.trim(),
        description: formData.description.trim(),
        zone: formData.zone.trim(),
        subZone: formData.sub_zone.trim() || undefined,
        environment: formData.environment || undefined,
      };

      onUpdate(room.id, updates);
      onClose();
    },
    [formData, validateField, onUpdate, room.id, onClose]
  );

  // Check if form has errors
  const hasErrors = Object.keys(errors).length > 0;
  const isFormValid = !hasErrors;

  if (!isOpen) return null;

  const selectedEnvironment = ENVIRONMENT_OPTIONS.find(opt => opt.value === formData.environment);

  // Base input classes
  const baseInputClasses =
    'w-full px-3 py-2 bg-mythos-terminal-background border rounded text-mythos-terminal-text ' +
    'focus:outline-hidden focus:ring-2 focus:ring-mythos-terminal-primary focus:border-transparent';
  const baseTextAreaClasses = baseInputClasses + ' resize-y font-mono text-sm';
  const baseMonoInputClasses = baseInputClasses + ' font-mono text-sm';

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 p-4"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="room-edit-title"
    >
      <div
        className="bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg w-full max-w-4xl max-h-modal overflow-hidden shadow-xl flex flex-col"
        onClick={e => {
          e.stopPropagation();
        }}
      >
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-mythos-terminal-border bg-mythos-terminal-surface">
          <div>
            <h2 id="room-edit-title" className="text-2xl font-bold text-mythos-terminal-text">
              Edit Room
            </h2>
            <p className="text-sm text-mythos-terminal-text/60 mt-1 font-mono">{room.id}</p>
          </div>
          <button
            onClick={onClose}
            className="text-mythos-terminal-text hover:text-mythos-terminal-error text-3xl leading-none w-8 h-8 flex items-center justify-center rounded hover:bg-mythos-terminal-background transition-colors"
            aria-label="Close dialog"
            type="button"
          >
            ×
          </button>
        </div>

        {/* Tabs */}
        <div className="flex gap-1 px-6 pt-4 border-b border-mythos-terminal-border bg-mythos-terminal-surface">
          <button
            onClick={() => {
              setActiveTab('basic');
            }}
            type="button"
            className={`px-4 py-2 font-medium text-sm transition-colors rounded-t ${
              activeTab === 'basic'
                ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary bg-mythos-terminal-background'
                : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text hover:bg-mythos-terminal-background/50'
            }`}
            aria-selected={activeTab === 'basic'}
            role="tab"
          >
            Basic Info
          </button>
          <button
            onClick={() => {
              setActiveTab('location');
            }}
            type="button"
            className={`px-4 py-2 font-medium text-sm transition-colors rounded-t ${
              activeTab === 'location'
                ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary bg-mythos-terminal-background'
                : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text hover:bg-mythos-terminal-background/50'
            }`}
            aria-selected={activeTab === 'location'}
            role="tab"
          >
            Location
          </button>
          <button
            onClick={() => {
              setActiveTab('properties');
            }}
            type="button"
            className={`px-4 py-2 font-medium text-sm transition-colors rounded-t ${
              activeTab === 'properties'
                ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary bg-mythos-terminal-background'
                : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text hover:bg-mythos-terminal-background/50'
            }`}
            aria-selected={activeTab === 'properties'}
            role="tab"
          >
            Properties
          </button>
        </div>

        {/* Form Content - Scrollable */}
        <div className="flex-1 overflow-y-auto p-6">
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Basic Info Tab */}
            {activeTab === 'basic' && (
              <div className="space-y-6">
                {/* Name */}
                <div>
                  <label htmlFor="room-name" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                    Room Name <span className="text-mythos-terminal-error">*</span>
                  </label>
                  <input
                    id="room-name"
                    type="text"
                    value={formData.name}
                    onChange={e => {
                      handleFieldChange('name', e.target.value);
                    }}
                    onBlur={() => {
                      handleFieldBlur('name');
                    }}
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

                {/* Description */}
                <div>
                  <label
                    htmlFor="room-description"
                    className="block text-sm font-medium text-mythos-terminal-text mb-2"
                  >
                    Description
                  </label>
                  <textarea
                    id="room-description"
                    value={formData.description}
                    onChange={e => {
                      handleFieldChange('description', e.target.value);
                    }}
                    onBlur={() => {
                      handleFieldBlur('description');
                    }}
                    rows={8}
                    maxLength={2000}
                    className={`${baseTextAreaClasses} ${
                      errors.description && touched.description
                        ? 'border-mythos-terminal-error'
                        : 'border-mythos-terminal-border'
                    }`}
                    aria-invalid={errors.description && touched.description ? 'true' : 'false'}
                    aria-describedby={
                      errors.description && touched.description ? 'description-error' : 'description-help'
                    }
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
            )}

            {/* Location Tab */}
            {activeTab === 'location' && (
              <div className="space-y-6">
                {/* Plane */}
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

                {/* Zone */}
                <div>
                  <label htmlFor="room-zone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                    Zone <span className="text-mythos-terminal-error">*</span>
                  </label>
                  <input
                    id="room-zone"
                    type="text"
                    value={formData.zone}
                    onChange={e => {
                      handleFieldChange('zone', e.target.value.toLowerCase());
                    }}
                    onBlur={() => {
                      handleFieldBlur('zone');
                    }}
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

                {/* Sub-zone */}
                <div>
                  <label htmlFor="room-subzone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                    Sub-zone <span className="text-mythos-terminal-text/50 text-xs">(optional)</span>
                  </label>
                  <input
                    id="room-subzone"
                    type="text"
                    value={formData.sub_zone}
                    onChange={e => {
                      handleFieldChange('sub_zone', e.target.value.toLowerCase());
                    }}
                    onBlur={() => {
                      handleFieldBlur('sub_zone');
                    }}
                    pattern="^[a-z0-9_]*$"
                    className={`${baseMonoInputClasses} ${
                      errors.sub_zone && touched.sub_zone
                        ? 'border-mythos-terminal-error'
                        : 'border-mythos-terminal-border'
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
            )}

            {/* Properties Tab */}
            {activeTab === 'properties' && (
              <div className="space-y-6">
                {/* Environment */}
                <div>
                  <label
                    htmlFor="room-environment"
                    className="block text-sm font-medium text-mythos-terminal-text mb-2"
                  >
                    Environment Type
                  </label>
                  <select
                    id="room-environment"
                    value={formData.environment}
                    onChange={e => {
                      handleFieldChange('environment', e.target.value);
                    }}
                    className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text focus:outline-hidden focus:ring-2 focus:ring-mythos-terminal-primary focus:border-transparent"
                  >
                    {ENVIRONMENT_OPTIONS.map(option => (
                      <option key={option.value} value={option.value}>
                        {option.label}
                      </option>
                    ))}
                  </select>
                  {selectedEnvironment && selectedEnvironment.description && (
                    <p className="text-xs text-mythos-terminal-text/50 mt-1">{selectedEnvironment.description}</p>
                  )}
                </div>

                {/* Info message */}
                <div className="bg-mythos-terminal-surface border border-mythos-terminal-border rounded p-4">
                  <p className="text-sm text-mythos-terminal-text/70">
                    <strong className="text-mythos-terminal-text">Note:</strong> Additional properties such as exits,
                    occupants, and containers are managed separately through the map interface and room detail panels.
                  </p>
                </div>
              </div>
            )}
          </form>
        </div>

        {/* Actions Footer */}
        <div className="flex justify-end gap-3 p-6 border-t border-mythos-terminal-border bg-mythos-terminal-surface">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface transition-colors"
          >
            Cancel
          </button>
          <button
            type="submit"
            onClick={handleSubmit}
            disabled={!isFormValid}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            Update Room
          </button>
        </div>

        {/* Footer hint */}
        <div className="px-6 pb-4 text-xs text-mythos-terminal-text/50 text-center border-t border-mythos-terminal-border bg-mythos-terminal-surface">
          Press ESC to close
        </div>
      </div>
    </div>
  );
};
