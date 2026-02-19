/**
 * SkillAssignmentScreen: CoC-style skill allocation (plan 10.6 F4).
 * Nine occupation slots (70, 60, 60, 50, 50, 50, 40, 40, 40) and four personal interest (base+20).
 * Cthulhu Mythos disabled. On confirm passes payload to name step; no POST.
 */

import React, { useCallback, useEffect, useState } from 'react';
import { logger } from '../utils/logger.js';
import type { OccupationSlotPayload, PersonalInterestPayload, SkillsPayload } from './CharacterNameScreen.jsx';

const OCCUPATION_VALUES = [70, 60, 60, 50, 50, 50, 40, 40, 40] as const;

interface SkillCatalogEntry {
  id: number;
  key: string;
  name: string;
  description?: string;
  base_value: number;
  allow_at_creation: boolean;
  category?: string;
}

interface SkillAssignmentScreenProps {
  baseUrl: string;
  authToken: string;
  onSkillsConfirmed: (payload: SkillsPayload) => void;
  onBack: () => void;
  onError: (error: string) => void;
}

export const SkillAssignmentScreen: React.FC<SkillAssignmentScreenProps> = ({
  baseUrl,
  authToken,
  onSkillsConfirmed,
  onBack,
  onError,
}) => {
  const [skills, setSkills] = useState<SkillCatalogEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [occupationSlots, setOccupationSlots] = useState<(number | null)[]>(OCCUPATION_VALUES.map(() => null));
  const [personalInterest, setPersonalInterest] = useState<(number | null)[]>([]);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch(`${baseUrl}/skills/`, {
          headers: { Authorization: `Bearer ${authToken}` },
        });
        if (!res.ok) {
          const msg = `Failed to load skills (${res.status})`;
          if (!cancelled) setError(msg);
          return;
        }
        const data = (await res.json()) as { skills?: SkillCatalogEntry[] };
        const list = data.skills ?? [];
        if (!cancelled) {
          setSkills(list);
          setPersonalInterest([null, null, null, null]);
        }
      } catch (e) {
        const msg = e instanceof Error ? e.message : 'Failed to load skills';
        if (!cancelled) {
          setError(msg);
          onError(msg);
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [baseUrl, authToken, onError]);

  const selectableSkills = skills.filter(s => s.allow_at_creation);

  /** Skill IDs already used in other occupation slots or any personal interest (for occupation dropdown at excludeOccIndex). */
  const usedForOccupationDropdown = useCallback(
    (excludeOccIndex: number) => {
      const used = new Set<number>();
      occupationSlots.forEach((id, idx) => {
        if (idx !== excludeOccIndex && id != null) used.add(id);
      });
      personalInterest.forEach(id => {
        if (id != null) used.add(id);
      });
      return used;
    },
    [occupationSlots, personalInterest]
  );

  /** Skill IDs already used in any occupation slot or other personal slots (for personal dropdown at excludePersIndex). */
  const usedForPersonalDropdown = useCallback(
    (excludePersIndex: number) => {
      const used = new Set<number>();
      occupationSlots.forEach(id => {
        if (id != null) used.add(id);
      });
      personalInterest.forEach((id, idx) => {
        if (idx !== excludePersIndex && id != null) used.add(id);
      });
      return used;
    },
    [occupationSlots, personalInterest]
  );

  const setOccupationSlot = useCallback((index: number, skillId: number | null) => {
    setOccupationSlots(prev => {
      const next = [...prev];
      next[index] = skillId;
      return next;
    });
  }, []);

  const setPersonalSlot = useCallback((index: number, skillId: number | null) => {
    setPersonalInterest(prev => {
      const next = [...prev];
      next[index] = skillId;
      return next;
    });
  }, []);

  const handleConfirm = () => {
    const occ: OccupationSlotPayload[] = occupationSlots.map((skillId, i) => {
      if (skillId == null) throw new Error(`Occupation slot ${i + 1} must have a skill`);
      return { skill_id: skillId, value: OCCUPATION_VALUES[i] };
    });
    const pers: PersonalInterestPayload[] = personalInterest.map((skillId, i) => {
      if (skillId == null) throw new Error(`Personal interest ${i + 1} must have a skill`);
      return { skill_id: skillId };
    });
    logger.info('SkillAssignmentScreen', 'Skills confirmed', { occupationCount: 9, personalCount: 4 });
    onSkillsConfirmed({ occupation_slots: occ, personal_interest: pers });
  };

  const occupationComplete = occupationSlots.every(s => s != null);
  const personalComplete = personalInterest.length === 4 && personalInterest.every(s => s != null);
  const canConfirm = occupationComplete && personalComplete;

  if (loading) {
    return (
      <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
        <p>Loading skills catalog...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
        <p className="error-message">{error}</p>
        <button type="button" onClick={onBack} className="back-button">
          Back
        </button>
      </div>
    );
  }

  return (
    <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
      <h2>Skill Allocation</h2>
      <p className="skill-instructions">
        Assign nine occupation skills (one 70%, two 60%, three 50%, three 40%) and four personal interest skills (base +
        20% each). Cthulhu Mythos cannot be chosen here.
      </p>

      <section className="occupation-slots">
        <h3>Occupation skills</h3>
        {OCCUPATION_VALUES.map((value, i) => {
          const used = usedForOccupationDropdown(i);
          const options = selectableSkills.filter(s => occupationSlots[i] === s.id || !used.has(s.id));
          return (
            <div key={i} className="slot-row">
              <label>{value}%</label>
              <select
                value={occupationSlots[i] ?? ''}
                onChange={e => {
                  setOccupationSlot(i, e.target.value ? Number(e.target.value) : null);
                }}
              >
                <option value="">Select skill...</option>
                {options.map(s => (
                  <option key={s.id} value={s.id}>
                    {s.name} (base {s.base_value}%)
                  </option>
                ))}
              </select>
            </div>
          );
        })}
      </section>

      <section className="personal-interest-slots">
        <h3>Personal interest (4 skills)</h3>
        {[0, 1, 2, 3].map(i => {
          const used = usedForPersonalDropdown(i);
          const options = selectableSkills.filter(s => personalInterest[i] === s.id || !used.has(s.id));
          return (
            <div key={i} className="slot-row">
              <label>Personal {i + 1}</label>
              <select
                value={personalInterest[i] ?? ''}
                onChange={e => {
                  setPersonalSlot(i, e.target.value ? Number(e.target.value) : null);
                }}
              >
                <option value="">Select skill...</option>
                {options.map(s => (
                  <option key={s.id} value={s.id}>
                    {s.name} (base+20)
                  </option>
                ))}
              </select>
            </div>
          );
        })}
      </section>

      <div className="skill-actions">
        <button type="button" onClick={onBack} className="back-button">
          Back
        </button>
        <button type="button" onClick={handleConfirm} disabled={!canConfirm} className="confirm-button">
          Next: Name character
        </button>
      </div>
    </div>
  );
};
