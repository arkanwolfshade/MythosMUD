import { useCallback, useEffect, useState } from 'react';
import type { Room } from '../../stores/gameStore';
import type { RoomNodeData } from './types';
import type { RoomEditFormData } from './RoomEditModalForm';

export interface RoomEditModalProps {
  isOpen: boolean;
  onClose: () => void;
  room: Room;
  onUpdate: (roomId: string, updates: Partial<RoomNodeData>) => void;
}

type EditableRoomField = keyof RoomEditFormData;

const toFormValue = (value: string | null | undefined): string => value ?? '';

const buildInitialFormData = (room: Room): RoomEditFormData => ({
  name: toFormValue(room.name),
  description: toFormValue(room.description),
  plane: toFormValue(room.plane),
  zone: toFormValue(room.zone),
  sub_zone: toFormValue(room.sub_zone),
  environment: toFormValue(room.environment),
});

const validateName = (value: string): string => {
  if (!value.trim()) return 'Room name is required';
  if (value.length > 200) return 'Room name must be 200 characters or less';
  if (value.length < 1) return 'Room name must be at least 1 character';
  return '';
};

const validateDescription = (value: string): string => {
  if (value.length > 2000) return 'Description must be 2000 characters or less';
  if (value.trim().length > 0 && value.trim().length < 10) {
    return 'Description must be at least 10 characters if provided';
  }
  return '';
};

const validatePlane = (value: string): string => (!value.trim() ? 'Plane is required' : '');

const validateZone = (value: string): string => {
  if (!value.trim()) return 'Zone is required';
  if (!/^[a-z0-9_]+$/.test(value)) {
    return 'Zone must contain only lowercase letters, numbers, and underscores';
  }
  return '';
};

const validateSubZone = (value: string): string =>
  value.trim() && !/^[a-z0-9_]+$/.test(value)
    ? 'Sub-zone must contain only lowercase letters, numbers, and underscores'
    : '';

const FIELD_VALIDATORS: Partial<Record<EditableRoomField, (value: string) => string>> = {
  name: validateName,
  description: validateDescription,
  plane: validatePlane,
  zone: validateZone,
  sub_zone: validateSubZone,
};

export function useRoomEditModal(props: RoomEditModalProps) {
  const { isOpen, onClose, room, onUpdate } = props;
  const [activeTab, setActiveTab] = useState<'basic' | 'location' | 'properties'>('basic');
  const [formData, setFormData] = useState<RoomEditFormData>(() => buildInitialFormData(room));
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});

  /* eslint-disable react-hooks/set-state-in-effect -- reset form when modal opens or room changes */
  useEffect(() => {
    if (isOpen && room) {
      setFormData(buildInitialFormData(room));
      setErrors({});
      setTouched({});
      setActiveTab('basic');
    }
  }, [isOpen, room]);
  /* eslint-enable react-hooks/set-state-in-effect */

  useEffect(() => {
    if (!isOpen) return;
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [isOpen, onClose]);

  useEffect(() => {
    document.body.style.overflow = isOpen ? 'hidden' : '';
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  const validateField = useCallback((field: string, value: string): string => {
    const typedField = field as EditableRoomField;
    const validator = FIELD_VALIDATORS[typedField];
    return validator ? validator(value) : '';
  }, []);

  const handleFieldChange = useCallback(
    (field: keyof RoomEditFormData, value: string) => {
      setFormData(prev => ({ ...prev, [field]: value }));
      setTouched(prev => ({ ...prev, [field]: true }));
      const error = validateField(field, value);
      setErrors(prev => {
        if (error) return { ...prev, [field]: error };
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        const { [field]: _removed, ...rest } = prev;
        return rest;
      });
    },
    [validateField]
  );

  const handleFieldBlur = useCallback((field: keyof RoomEditFormData) => {
    setTouched(prev => ({ ...prev, [field]: true }));
  }, []);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      const allFields: Array<keyof RoomEditFormData> = [
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

      const newErrors: Record<string, string> = {};
      Object.entries(formData).forEach(([field, value]) => {
        const error = validateField(field, value);
        if (error) newErrors[field] = error;
      });
      if (Object.keys(newErrors).length > 0) {
        setErrors(newErrors);
        return;
      }

      onUpdate(room.id, {
        name: formData.name.trim(),
        description: formData.description.trim(),
        zone: formData.zone.trim(),
        subZone: formData.sub_zone.trim() || undefined,
        // Empty string ("Not Set") is a deliberate clear, not "no change" -- do not coerce to
        // undefined here. undefined values are dropped by JSON.stringify, so an `|| undefined`
        // coercion would silently discard the user's intent to clear the environment. See #627.
        environment: formData.environment,
      });
      onClose();
    },
    [formData, validateField, onUpdate, room.id, onClose]
  );

  return {
    activeTab,
    setActiveTab,
    formData,
    errors,
    touched,
    handleFieldChange,
    handleFieldBlur,
    handleSubmit,
    isFormValid: Object.keys(errors).length === 0,
  };
}
