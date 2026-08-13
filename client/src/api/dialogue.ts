/**
 * Admin dialogue API client for Content Tools (#583).
 */

import { getVersionedApiBaseUrl } from '../utils/config';

export interface DialogueOptionDto {
  label: string;
  next?: string | null;
}

export interface DialogueNodeDto {
  text: string;
  options: DialogueOptionDto[];
}

export interface DialogueTreeDto {
  start: string;
  nodes: Record<string, DialogueNodeDto>;
}

export interface DialogueDefinitionDto {
  id: string;
  definition: DialogueTreeDto;
  npc_definition_id: number | null;
  created_at?: string | null;
  updated_at?: string | null;
}

function buildHeaders(authToken?: string): HeadersInit {
  const headers: HeadersInit = { 'Content-Type': 'application/json' };
  if (authToken) {
    headers.Authorization = `Bearer ${authToken}`;
  }
  return headers;
}

function baseUrl(override?: string): string {
  const base = override && override.trim() !== '' ? override : getVersionedApiBaseUrl();
  return base.replace(/\/$/, '');
}

export async function listDialogueDefinitions(authToken: string, apiBase?: string): Promise<DialogueDefinitionDto[]> {
  const response = await fetch(`${baseUrl(apiBase)}/admin/dialogue/definitions`, {
    headers: buildHeaders(authToken),
  });
  if (!response.ok) {
    throw new Error(`Failed to list dialogues (${response.status})`);
  }
  return (await response.json()) as DialogueDefinitionDto[];
}

export async function upsertDialogueDefinition(
  authToken: string,
  dialogueId: string,
  body: { definition: DialogueTreeDto; npc_definition_id: number | null },
  apiBase?: string
): Promise<DialogueDefinitionDto> {
  const response = await fetch(`${baseUrl(apiBase)}/admin/dialogue/definitions/${encodeURIComponent(dialogueId)}`, {
    method: 'PUT',
    headers: buildHeaders(authToken),
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(`Failed to save dialogue (${response.status}): ${detail}`);
  }
  return (await response.json()) as DialogueDefinitionDto;
}

export async function deleteDialogueDefinition(authToken: string, dialogueId: string, apiBase?: string): Promise<void> {
  const response = await fetch(`${baseUrl(apiBase)}/admin/dialogue/definitions/${encodeURIComponent(dialogueId)}`, {
    method: 'DELETE',
    headers: buildHeaders(authToken),
  });
  if (!response.ok && response.status !== 204) {
    throw new Error(`Failed to delete dialogue (${response.status})`);
  }
}

function validateDialogueOption(
  nodeId: string,
  option: DialogueOptionDto,
  nodes: Record<string, DialogueNodeDto>
): string | null {
  if (!option.label?.trim()) {
    return `Node "${nodeId}" has an option without a label.`;
  }
  // null/undefined next ends the branch; "" is accidental input, not an end marker.
  if (option.next == null) {
    return null;
  }
  if (!option.next.trim()) {
    return `Node "${nodeId}" option "${option.label}" has an empty next (use null to end).`;
  }
  if (!(option.next in nodes)) {
    return `Node "${nodeId}" option "${option.label}" points to unknown next "${option.next}".`;
  }
  return null;
}

function validateDialogueNode(
  nodeId: string,
  node: DialogueNodeDto,
  nodes: Record<string, DialogueNodeDto>
): string | null {
  if (!node.text?.trim()) {
    return `Node "${nodeId}" needs text.`;
  }
  for (const option of node.options ?? []) {
    const optionError = validateDialogueOption(nodeId, option, nodes);
    if (optionError) {
      return optionError;
    }
  }
  return null;
}

/** Client-side tree sanity checks mirroring server nav-only rules. */
export function validateDialogueTreeClient(tree: DialogueTreeDto): string | null {
  if (!tree.start || !tree.nodes || Object.keys(tree.nodes).length === 0) {
    return 'Tree needs a start node and at least one node.';
  }
  if (!(tree.start in tree.nodes)) {
    return `Start node "${tree.start}" is missing from nodes.`;
  }
  for (const [nodeId, node] of Object.entries(tree.nodes)) {
    const error = validateDialogueNode(nodeId, node, tree.nodes);
    if (error) {
      return error;
    }
  }
  return null;
}
