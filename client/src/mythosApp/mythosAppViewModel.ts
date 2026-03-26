import type { KeyboardEvent, RefObject } from 'react';
import type { Profession } from '../components/ProfessionCard.tsx';
import type { CharacterInfo } from '../types/auth.js';
import type { Stats } from '../hooks/useStatsRolling.js';
import type { CreationStep } from './creationTypes.js';

export interface MythosAppViewModel {
  showDemo: boolean;
  setShowDemo: (v: boolean) => void;
  isAuthenticated: boolean;
  characters: CharacterInfo[];
  showCharacterSelection: boolean;
  creationStep: CreationStep | null;
  pendingStats: Stats | null;
  selectedProfession: Profession | undefined;
  pendingSkillsPayload: {
    occupation_slots: { skill_id: number; value: number }[];
    personal_interest: { skill_id: number }[];
  } | null;
  showMotd: boolean;
  playerName: string;
  setPlayerName: (v: string) => void;
  password: string;
  setPassword: (v: string) => void;
  inviteCode: string;
  setInviteCode: (v: string) => void;
  error: string | null;
  isSubmitting: boolean;
  isRegistering: boolean;
  isLoggingOut: boolean;
  usernameInputRef: RefObject<HTMLInputElement | null>;
  authToken: string;
  selectedCharacterName: string;
  selectedCharacterId: string;
  handleLoginClick: () => Promise<void>;
  handleRegisterClick: () => Promise<void>;
  handleKeyDown: (event: KeyboardEvent) => void;
  toggleMode: () => void;
  handleCharacterSelected: (characterId: string) => Promise<void>;
  handleCreateCharacter: () => void;
  handleDeleteCharacter: (characterId: string) => Promise<void>;
  handleStatsAccepted: (stats: Stats) => void;
  handleStatsError: (error: string) => void;
  handleStatsRollingBack: () => void;
  handleProfessionSelected: (profession: Profession) => void;
  handleProfessionSelectionError: (error: string) => void;
  handleProfessionSelectionBack: () => void;
  handleCreationComplete: () => Promise<void>;
  handleMotdContinue: () => Promise<void>;
  handleMotdReturnToLogin: () => void;
  handleLogout: () => Promise<void>;
  handleDisconnectCallback: (disconnectFn: () => void) => void;
  setError: (v: string | null) => void;
  setCreationStep: (v: CreationStep | null) => void;
  setPendingSkillsPayload: (
    v: {
      occupation_slots: { skill_id: number; value: number }[];
      personal_interest: { skill_id: number }[];
    } | null
  ) => void;
  setAuthToken: (v: string) => void;
  setIsAuthenticated: (v: boolean) => void;
  setCharacters: (v: CharacterInfo[]) => void;
  setSelectedCharacterName: (v: string) => void;
  setSelectedCharacterId: (v: string) => void;
}
