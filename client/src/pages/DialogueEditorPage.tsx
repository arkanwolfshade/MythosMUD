/**
 * Admin Content Tools — Dialogue form editor (#583).
 *
 * Form-based (not React Flow). Auth via localStorage token like MapPage.
 */

import { useCallback, useEffect, useState } from 'react';
import {
  deleteDialogueDefinition,
  listDialogueDefinitions,
  upsertDialogueDefinition,
  validateDialogueTreeClient,
  type DialogueDefinitionDto,
  type DialogueTreeDto,
} from '../api/dialogue';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

const EMPTY_TREE: DialogueTreeDto = {
  start: 'greeting',
  nodes: {
    greeting: {
      text: 'Hello, seeker.',
      options: [{ label: 'Farewell', next: null }],
    },
  },
};

export function DialogueEditorPage() {
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [items, setItems] = useState<DialogueDefinitionDto[]>([]);
  const [selectedId, setSelectedId] = useState('');
  const [dialogueId, setDialogueId] = useState('new_dialogue');
  const [npcDefinitionId, setNpcDefinitionId] = useState('');
  const [treeJson, setTreeJson] = useState(JSON.stringify(EMPTY_TREE, null, 2));
  const [status, setStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  const refresh = useCallback(async (token: string) => {
    const rows = await listDialogueDefinitions(token);
    setItems(rows);
  }, []);

  useEffect(() => {
    const token = secureTokenStorage.getToken();
    if (!token) {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- auth gate before fetch
      setError('Not authenticated. Please log in first.');
      setLoading(false);
      return;
    }
    setAuthToken(token);
    refresh(token)
      .catch(err => {
        logger.error('DialogueEditor', 'Failed to load dialogues', { error: err });
        setError(err instanceof Error ? err.message : 'Failed to load dialogues');
      })
      .finally(() => setLoading(false));
  }, [refresh]);

  const loadSelected = (id: string) => {
    setSelectedId(id);
    const row = items.find(item => item.id === id);
    if (!row) {
      return;
    }
    setDialogueId(row.id);
    setNpcDefinitionId(row.npc_definition_id != null ? String(row.npc_definition_id) : '');
    setTreeJson(JSON.stringify(row.definition, null, 2));
    setStatus(null);
    setError(null);
  };

  const onNew = () => {
    setSelectedId('');
    setDialogueId('new_dialogue');
    setNpcDefinitionId('');
    setTreeJson(JSON.stringify(EMPTY_TREE, null, 2));
    setStatus(null);
    setError(null);
  };

  const onSave = async () => {
    if (!authToken) {
      return;
    }
    setError(null);
    setStatus(null);
    let tree: DialogueTreeDto;
    try {
      tree = JSON.parse(treeJson) as DialogueTreeDto;
    } catch {
      setError('Definition JSON is invalid.');
      return;
    }
    const validationError = validateDialogueTreeClient(tree);
    if (validationError) {
      setError(validationError);
      return;
    }
    const npcId = npcDefinitionId.trim() === '' ? null : Number(npcDefinitionId);
    if (npcDefinitionId.trim() !== '' && Number.isNaN(npcId)) {
      setError('NPC definition id must be a number or empty.');
      return;
    }
    try {
      await upsertDialogueDefinition(authToken, dialogueId.trim(), {
        definition: tree,
        npc_definition_id: npcId,
      });
      setStatus(`Saved ${dialogueId.trim()}`);
      await refresh(authToken);
      setSelectedId(dialogueId.trim());
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Save failed');
    }
  };

  const onDelete = async () => {
    if (!authToken || !selectedId) {
      return;
    }
    try {
      const deletedId = selectedId;
      await deleteDialogueDefinition(authToken, deletedId);
      // onNew clears status; set Deleted after so role=status stays visible
      onNew();
      setStatus(`Deleted ${deletedId}`);
      await refresh(authToken);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Delete failed');
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text p-6">
        Loading Content Tools…
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text p-6">
      <header className="mb-6">
        <h1 className="text-2xl font-bold">Content Tools — Dialogue</h1>
        <p className="text-sm opacity-80 mt-1">
          Form editor for nav-only dialogue trees. Players use <code>talk</code> / <code>talk n</code>. Creator guide:{' '}
          <code>docs/runbooks/DIALOGUE_CONTENT_TOOLS.md</code>. Players: <code>help talk</code>.
        </p>
      </header>

      {error && (
        <div className="mb-4 border border-mythos-terminal-error text-mythos-terminal-error p-3 rounded" role="alert">
          {error}
        </div>
      )}
      {status && (
        <div className="mb-4 border border-mythos-terminal-primary p-3 rounded" role="status">
          {status}
        </div>
      )}

      <div className="grid gap-6 md:grid-cols-[240px_1fr]">
        <aside className="border border-mythos-terminal-border rounded p-3">
          <div className="flex items-center justify-between mb-2">
            <h2 className="font-semibold">Trees</h2>
            <button type="button" className="text-sm underline" onClick={onNew}>
              New
            </button>
          </div>
          <ul className="space-y-1 max-h-[70vh] overflow-auto">
            {items.map(item => (
              <li key={item.id}>
                <button
                  type="button"
                  className={`w-full text-left px-2 py-1 rounded ${
                    selectedId === item.id ? 'bg-mythos-terminal-primary text-white' : 'hover:bg-black/20'
                  }`}
                  onClick={() => loadSelected(item.id)}
                >
                  {item.id}
                </button>
              </li>
            ))}
            {items.length === 0 && <li className="opacity-60 text-sm">No dialogue trees yet.</li>}
          </ul>
        </aside>

        <section className="border border-mythos-terminal-border rounded p-4 space-y-3">
          <label className="block">
            <span className="text-sm">Dialogue id</span>
            <input
              className="mt-1 w-full bg-black/30 border border-mythos-terminal-border rounded px-2 py-1"
              value={dialogueId}
              onChange={e => setDialogueId(e.target.value)}
              data-testid="dialogue-id-input"
            />
          </label>
          <label className="block">
            <span className="text-sm">NPC definition id (optional)</span>
            <input
              className="mt-1 w-full bg-black/30 border border-mythos-terminal-border rounded px-2 py-1"
              value={npcDefinitionId}
              onChange={e => setNpcDefinitionId(e.target.value)}
              data-testid="dialogue-npc-id-input"
            />
          </label>
          <label className="block">
            <span className="text-sm">Definition JSON (start + nodes)</span>
            <textarea
              className="mt-1 w-full min-h-80 font-mono text-sm bg-black/30 border border-mythos-terminal-border rounded px-2 py-1"
              value={treeJson}
              onChange={e => setTreeJson(e.target.value)}
              data-testid="dialogue-tree-json"
            />
          </label>
          <div className="flex gap-3">
            <button
              type="button"
              className="px-4 py-2 bg-mythos-terminal-primary text-white rounded"
              onClick={() => void onSave()}
              data-testid="dialogue-save"
            >
              Save
            </button>
            <button
              type="button"
              className="px-4 py-2 border border-mythos-terminal-border rounded disabled:opacity-40"
              onClick={() => void onDelete()}
              disabled={!selectedId}
              data-testid="dialogue-delete"
            >
              Delete
            </button>
          </div>
        </section>
      </div>
    </div>
  );
}

export default DialogueEditorPage;
