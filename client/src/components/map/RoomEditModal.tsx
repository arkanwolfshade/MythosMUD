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

import React, { useState, useCallback, useEffect } from 'react';
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
        if (value.length > 100) {
          return 'Room name must be 100 characters or less';
        }
        break;
      case 'description':
        if (value.length > 5000) {
          return 'Description must be 5000 characters or less';
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

      // Validate on change
      const error = validateField(field, value);
      setErrors(prev => {
        if (error) {
          return { ...prev, [field]: error };
        } else {
          // eslint-disable-next-line @typescript-eslint/no-unused-vars
          const { [field]: _removed, ...rest } = prev;
          return rest;
        }
      });
    },
    [validateField]
  );

  // Handle form submission
  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();

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
        name: formData.name,
        description: formData.description,
        zone: formData.zone,
        subZone: formData.sub_zone,
        environment: formData.environment,
      };

      onUpdate(room.id, updates);
      onClose();
    },
    [formData, validateField, onUpdate, room.id, onClose]
  );

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="room-edit-title"
    >
      <div
        className="bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-3xl max-h-[90vh] overflow-y-auto shadow-xl"
        onClick={e => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <h2 id="room-edit-title" className="text-2xl font-bold text-mythos-terminal-text">
            Edit Room
          </h2>
          <button
            onClick={onClose}
            className="text-mythos-terminal-text hover:text-mythos-terminal-error text-2xl leading-none"
            aria-label="Close dialog"
          >
            ×
          </button>
        </div>

        {/* Room ID (read-only) */}
        <div className="mb-4">
          <label className="block text-sm font-medium text-mythos-terminal-text mb-2">Room ID:</label>
          <div className="px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text font-mono text-sm">
            {room.id}
          </div>
        </div>

        {/* Tabs */}
        <div className="flex gap-2 mb-6 border-b border-mythos-terminal-border">
          <button
            onClick={() => setActiveTab('basic')}
            className={`px-4 py-2 font-medium text-sm ${
              activeTab === 'basic'
                ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary'
                : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text'
            }`}
          >
            Basic Info
          </button>
          <button
            onClick={() => setActiveTab('location')}
            className={`px-4 py-2 font-medium text-sm ${
              activeTab === 'location'
                ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary'
                : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text'
            }`}
          >
            Location
          </button>
          <button
            onClick={() => setActiveTab('properties')}
            className={`px-4 py-2 font-medium text-sm ${
              activeTab === 'properties'
                ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary'
                : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text'
            }`}
          >
            Properties
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Basic Info Tab */}
          {activeTab === 'basic' && (
            <div className="space-y-4">
              {/* Name */}
              <div>
                <label htmlFor="room-name" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                  Name: <span className="text-mythos-terminal-error">*</span>
                </label>
                <input
                  id="room-name"
                  type="text"
                  value={formData.name}
                  onChange={e => handleFieldChange('name', e.target.value)}
                  required
                  className={`w-full px-3 py-2 bg-mythos-terminal-background border rounded text-mythos-terminal-text ${
                    errors.name ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
                  }`}
                />
                {errors.name && <p className="text-xs text-mythos-terminal-error mt-1">{errors.name}</p>}
              </div>

              {/* Description */}
              <div>
                <label htmlFor="room-description" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                  Description:
                </label>
                <textarea
                  id="room-description"
                  value={formData.description}
                  onChange={e => handleFieldChange('description', e.target.value)}
                  rows={6}
                  className={`w-full px-3 py-2 bg-mythos-terminal-background border rounded text-mythos-terminal-text ${
                    errors.description ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
                  }`}
                />
                {errors.description && <p className="text-xs text-mythos-terminal-error mt-1">{errors.description}</p>}
                <p className="text-xs text-mythos-terminal-text/50 mt-1">
                  {formData.description.length}/5000 characters
                </p>
              </div>
            </div>
          )}

          {/* Location Tab */}
          {activeTab === 'location' && (
            <div className="space-y-4">
              {/* Plane */}
              <div>
                <label htmlFor="room-plane" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                  Plane: <span className="text-mythos-terminal-error">*</span>
                </label>
                <input
                  id="room-plane"
                  type="text"
                  value={formData.plane}
                  onChange={e => handleFieldChange('plane', e.target.value)}
                  required
                  disabled
                  className="w-full px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text/50 font-mono text-sm disabled:opacity-50 disabled:cursor-not-allowed"
                />
                <p className="text-xs text-mythos-terminal-text/50 mt-1">
                  Plane cannot be changed. Delete and recreate the room to change the plane.
                </p>
              </div>

              {/* Zone */}
              <div>
                <label htmlFor="room-zone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                  Zone: <span className="text-mythos-terminal-error">*</span>
                </label>
                <input
                  id="room-zone"
                  type="text"
                  value={formData.zone}
                  onChange={e => handleFieldChange('zone', e.target.value)}
                  required
                  className={`w-full px-3 py-2 bg-mythos-terminal-background border rounded text-mythos-terminal-text ${
                    errors.zone ? 'border-mythos-terminal-error' : 'border-mythos-terminal-border'
                  }`}
                />
                {errors.zone && <p className="text-xs text-mythos-terminal-error mt-1">{errors.zone}</p>}
              </div>

              {/* Sub-zone */}
              <div>
                <label htmlFor="room-subzone" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                  Sub-zone:
                </label>
                <input
                  id="room-subzone"
                  type="text"
                  value={formData.sub_zone}
                  onChange={e => handleFieldChange('sub_zone', e.target.value)}
                  className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
                />
              </div>
            </div>
          )}

          {/* Properties Tab */}
          {activeTab === 'properties' && (
            <div className="space-y-4">
              {/* Environment */}
              <div>
                <label htmlFor="room-environment" className="block text-sm font-medium text-mythos-terminal-text mb-2">
                  Environment:
                </label>
                <select
                  id="room-environment"
                  value={formData.environment}
                  onChange={e => handleFieldChange('environment', e.target.value)}
                  className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
                >
                  <option value="">Select environment...</option>
                  <option value="indoors">Indoors</option>
                  <option value="outdoors">Outdoors</option>
                  <option value="intersection">Intersection</option>
                  <option value="underground">Underground</option>
                  <option value="water">Water</option>
                  <option value="air">Air</option>
                </select>
              </div>

              {/* TODO: Add more properties as needed */}
              <div className="text-sm text-mythos-terminal-text/50">
                Additional properties (exits, occupants, etc.) are managed separately.
              </div>
            </div>
          )}

          {/* Actions */}
          <div className="flex justify-end gap-3 pt-4 border-t border-mythos-terminal-border">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={Object.keys(errors).length > 0}
              className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Update Room
            </button>
          </div>
        </form>

        <div className="mt-4 text-xs text-mythos-terminal-text/50 text-center">Press ESC to close</div>
      </div>
    </div>
  );
};
