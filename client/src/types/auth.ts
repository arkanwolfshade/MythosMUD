/**
 * Authentication and character-related TypeScript types.
 *
 * MULTI-CHARACTER: Updated to support multiple characters per user.
 */

export interface CharacterInfo {
  player_id: string;
  name: string;
  profession_id: number;
  profession_name?: string;
  level: number;
  created_at: string;
  last_active: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  user_id: string;
  characters: CharacterInfo[];
  refresh_token?: string;
}
