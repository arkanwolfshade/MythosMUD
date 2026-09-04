import { useCallback, useEffect, useMemo, useState } from 'react';
import { logger } from '../utils/logger.js';
import type { OccupationSlotPayload, PersonalInterestPayload } from './CharacterNameScreen.tsx';
import {
  MIN_TOUCH_TARGET_STYLE,
  OCCUPATION_VALUES,
  loadSkillsCatalog,
  renderErrorState,
  renderLoadingState,
  renderOccupationSlots,
  renderPersonalInterestSlots,
  renderSkillInstructions,
  type SkillAssignmentScreenProps,
  type SkillCatalogEntry,
} from './SkillAssignmentScreen.helpers.tsx';

function useSkillCatalog(baseUrl: string, authToken: string, onError: (error: string) => void) {
  const [skills, setSkills] = useState<SkillCatalogEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadCatalog = useCallback(async () => {
    setLoading(true);
    setError(null);
    const result = await loadSkillsCatalog(baseUrl, authToken);
    if (result.ok) {
      setSkills(result.skills);
      return result.skills;
    }
    setError(result.error);
    if (result.notify) onError(result.error);
    return null;
  }, [authToken, baseUrl, onError]);

  useEffect(() => {
    let cancelled = false;
    void (async () => {
      const result = await loadSkillsCatalog(baseUrl, authToken);
      if (!cancelled) {
        if (result.ok) setSkills(result.skills);
        else {
          setError(result.error);
          if (result.notify) onError(result.error);
        }
        setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [baseUrl, authToken, onError]);

  return { skills, loading, error, loadCatalog };
}

function useSkillSlotPickers() {
  const [occupationSlots, setOccupationSlots] = useState<(number | null)[]>(OCCUPATION_VALUES.map(() => null));
  const [personalInterest, setPersonalInterest] = useState<(number | null)[]>([null, null, null, null]);

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

  return {
    occupationSlots,
    personalInterest,
    usedForOccupationDropdown,
    usedForPersonalDropdown,
    setOccupationSlot,
    setPersonalSlot,
    resetPersonalInterest: () => setPersonalInterest([null, null, null, null]),
  };
}

function useSkillAssignmentForm({
  baseUrl,
  authToken,
  onError,
}: Pick<SkillAssignmentScreenProps, 'baseUrl' | 'authToken' | 'onError'>) {
  const catalog = useSkillCatalog(baseUrl, authToken, onError);
  const slots = useSkillSlotPickers();
  const selectableSkills = useMemo(() => catalog.skills.filter(s => s.allow_at_creation), [catalog.skills]);

  const loadCatalog = useCallback(async () => {
    const loaded = await catalog.loadCatalog();
    if (loaded) slots.resetPersonalInterest();
  }, [catalog, slots]);

  return { ...catalog, ...slots, selectableSkills, loadCatalog };
}

export function SkillAssignmentScreen({
  baseUrl,
  authToken,
  onSkillsConfirmed,
  onBack,
  onError,
}: SkillAssignmentScreenProps) {
  const form = useSkillAssignmentForm({ baseUrl, authToken, onError });
  const {
    loading,
    error,
    loadCatalog,
    selectableSkills,
    occupationSlots,
    personalInterest,
    usedForOccupationDropdown,
    usedForPersonalDropdown,
    setOccupationSlot,
    setPersonalSlot,
  } = form;

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

  if (loading) return renderLoadingState();
  if (error) return renderErrorState(error, onBack, () => void loadCatalog());

  return (
    <SkillAssignmentForm
      selectableSkills={selectableSkills}
      occupationSlots={occupationSlots}
      personalInterest={personalInterest}
      usedForOccupationDropdown={usedForOccupationDropdown}
      usedForPersonalDropdown={usedForPersonalDropdown}
      setOccupationSlot={setOccupationSlot}
      setPersonalSlot={setPersonalSlot}
      onBack={onBack}
      onConfirm={handleConfirm}
      canConfirm={
        occupationSlots.every(s => s != null) && personalInterest.length === 4 && personalInterest.every(s => s != null)
      }
    />
  );
}

type SkillAssignmentFormProps = {
  selectableSkills: SkillCatalogEntry[];
  occupationSlots: (number | null)[];
  personalInterest: (number | null)[];
  usedForOccupationDropdown: (excludeOccIndex: number) => Set<number>;
  usedForPersonalDropdown: (excludePersIndex: number) => Set<number>;
  setOccupationSlot: (index: number, skillId: number | null) => void;
  setPersonalSlot: (index: number, skillId: number | null) => void;
  onBack: () => void;
  onConfirm: () => void;
  canConfirm: boolean;
};

// Single props arg keeps lizard parameter-count under the limit of 8.
function SkillAssignmentForm(props: SkillAssignmentFormProps) {
  const {
    selectableSkills,
    occupationSlots,
    personalInterest,
    usedForOccupationDropdown,
    usedForPersonalDropdown,
    setOccupationSlot,
    setPersonalSlot,
    onBack,
    onConfirm,
    canConfirm,
  } = props;

  return (
    <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
      <h2>Skill Allocation</h2>
      {renderSkillInstructions()}

      <section className="occupation-slots">
        <h3>Occupation skills</h3>
        {renderOccupationSlots(selectableSkills, occupationSlots, usedForOccupationDropdown, setOccupationSlot)}
      </section>

      <section className="personal-interest-slots">
        <h3>Personal interest (4 skills)</h3>
        {renderPersonalInterestSlots(selectableSkills, personalInterest, usedForPersonalDropdown, setPersonalSlot)}
      </section>

      <div className="skill-actions">
        <button type="button" onClick={onBack} className="back-button" style={MIN_TOUCH_TARGET_STYLE}>
          Back
        </button>
        <button
          type="button"
          onClick={onConfirm}
          disabled={!canConfirm}
          className="confirm-button"
          style={MIN_TOUCH_TARGET_STYLE}
        >
          Next: Name character
        </button>
      </div>
    </div>
  );
}
