import type { SkillsPayload } from './CharacterNameScreen.tsx';

export const OCCUPATION_VALUES = [70, 60, 60, 50, 50, 50, 40, 40, 40] as const;

export interface SkillCatalogEntry {
  id: number;
  key: string;
  name: string;
  description?: string;
  base_value: number;
  allow_at_creation: boolean;
  category?: string;
}

export interface SkillAssignmentScreenProps {
  baseUrl: string;
  authToken: string;
  onSkillsConfirmed: (payload: SkillsPayload) => void;
  onBack: () => void;
  onError: (error: string) => void;
}

export const MIN_TOUCH_TARGET_STYLE = { minHeight: 44 };

type SkillsLoadResult = { ok: true; skills: SkillCatalogEntry[] } | { ok: false; error: string; notify: boolean };

export async function loadSkillsCatalog(baseUrl: string, authToken: string): Promise<SkillsLoadResult> {
  try {
    const res = await fetch(`${baseUrl}/skills/`, {
      headers: { Authorization: `Bearer ${authToken}` },
    });
    if (!res.ok) {
      return { ok: false, error: `Failed to load skills (${res.status})`, notify: false };
    }

    const data = (await res.json()) as { skills?: SkillCatalogEntry[] };
    return { ok: true, skills: data.skills ?? [] };
  } catch (e) {
    const msg = e instanceof Error ? e.message : 'Failed to load skills';
    return { ok: false, error: msg, notify: true };
  }
}

export function renderLoadingState() {
  return (
    <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
      <p>Loading skill options...</p>
    </div>
  );
}

export function renderErrorState(error: string, onBack: () => void, onRetry?: () => void) {
  return (
    <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
      <p className="error-message" role="alert" aria-live="assertive">
        {error}
      </p>
      <div className="skill-actions">
        {onRetry && (
          <button type="button" onClick={onRetry} className="confirm-button">
            Retry
          </button>
        )}
        <button type="button" onClick={onBack} className="back-button">
          Back
        </button>
      </div>
    </div>
  );
}

export function renderSkillInstructions() {
  return (
    <div className="skill-instructions">
      <p>Complete both groups before continuing:</p>
      <ul>
        <li>Occupation skills: 1x70%, 2x60%, 3x50%, 3x40%</li>
        <li>Personal interest skills: choose 4 skills at base + 20%</li>
        <li>Cthulhu Mythos cannot be selected during creation</li>
      </ul>
    </div>
  );
}

export function renderOccupationSlots(
  selectableSkills: SkillCatalogEntry[],
  occupationSlots: (number | null)[],
  usedForOccupationDropdown: (excludeOccIndex: number) => Set<number>,
  setOccupationSlot: (index: number, skillId: number | null) => void
) {
  return OCCUPATION_VALUES.map((value, i) => {
    const used = usedForOccupationDropdown(i);
    const options = selectableSkills.filter(s => occupationSlots[i] === s.id || !used.has(s.id));
    return (
      <div key={i} className="slot-row">
        <label htmlFor={`occupation-slot-${i}`}>{`Occupation ${i + 1} (${value}%)`}</label>
        <select
          id={`occupation-slot-${i}`}
          aria-label={`Occupation skill ${i + 1} value ${value} percent`}
          value={occupationSlots[i] ?? ''}
          style={MIN_TOUCH_TARGET_STYLE}
          onChange={e => setOccupationSlot(i, e.target.value ? Number(e.target.value) : null)}
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
  });
}

export function renderPersonalInterestSlots(
  selectableSkills: SkillCatalogEntry[],
  personalInterest: (number | null)[],
  usedForPersonalDropdown: (excludePersIndex: number) => Set<number>,
  setPersonalSlot: (index: number, skillId: number | null) => void
) {
  return [0, 1, 2, 3].map(i => {
    const used = usedForPersonalDropdown(i);
    const options = selectableSkills.filter(s => personalInterest[i] === s.id || !used.has(s.id));
    return (
      <div key={i} className="slot-row">
        <label htmlFor={`personal-slot-${i}`}>{`Personal ${i + 1}`}</label>
        <select
          id={`personal-slot-${i}`}
          aria-label={`Personal interest slot ${i + 1}`}
          value={personalInterest[i] ?? ''}
          style={MIN_TOUCH_TARGET_STYLE}
          onChange={e => setPersonalSlot(i, e.target.value ? Number(e.target.value) : null)}
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
  });
}
