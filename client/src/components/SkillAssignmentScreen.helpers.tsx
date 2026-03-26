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
      <p>Loading skills catalog...</p>
    </div>
  );
}

export function renderErrorState(error: string, onBack: () => void) {
  return (
    <div className="skill-assignment-screen" data-testid="skill-assignment-screen">
      <p className="error-message">{error}</p>
      <button type="button" onClick={onBack} className="back-button">
        Back
      </button>
    </div>
  );
}
