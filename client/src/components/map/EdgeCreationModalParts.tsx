import type { Node } from 'reactflow';
import type { EdgeValidationResult } from './hooks/useMapEditing';
import type { RoomNodeData } from './types';
import type { useEdgeCreationModal } from './useEdgeCreationModal';

interface EdgeModalValidationMessagesProps {
  validation: EdgeValidationResult;
}

function EdgeModalValidationMessages({ validation }: EdgeModalValidationMessagesProps) {
  return (
    <div className="space-y-2">
      {validation.errors.length > 0 ? (
        <EdgeModalMessageList title="Errors:" items={validation.errors} tone="error" />
      ) : null}
      {validation.warnings.length > 0 ? (
        <EdgeModalMessageList title="Warnings:" items={validation.warnings} tone="warning" />
      ) : null}
    </div>
  );
}

const EDGE_MODAL_MESSAGE_TONE_CLASSES: Record<'error' | 'warning', { box: string; heading: string; list: string }> = {
  error: {
    box: 'p-3 bg-mythos-terminal-error/20 border border-mythos-terminal-error rounded',
    heading: 'text-sm font-medium text-mythos-terminal-error mb-1',
    list: 'list-disc list-inside text-sm text-mythos-terminal-error space-y-1',
  },
  warning: {
    box: 'p-3 bg-yellow-900/20 border border-yellow-600 rounded',
    heading: 'text-sm font-medium text-yellow-400 mb-1',
    list: 'list-disc list-inside text-sm text-yellow-300 space-y-1',
  },
};

function EdgeModalMessageList({ title, items, tone }: { title: string; items: string[]; tone: 'error' | 'warning' }) {
  const styles = EDGE_MODAL_MESSAGE_TONE_CLASSES[tone];
  return (
    <div className={styles.box}>
      <div className={styles.heading}>{title}</div>
      <ul className={styles.list}>
        {items.map((msg, index) => (
          <li key={index}>{msg}</li>
        ))}
      </ul>
    </div>
  );
}

interface EdgeModalDirectionFieldsProps {
  direction: string;
  setDirection: (value: string) => void;
  effectiveDirections: string[];
}

function EdgeModalDirectionSelect(props: {
  direction: string;
  setDirection: (value: string) => void;
  effectiveDirections: string[];
}) {
  return (
    <select
      id="edge-direction-select"
      value={props.direction}
      onChange={e => props.setDirection(e.target.value)}
      required
      className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
    >
      <option value="">Select direction...</option>
      {props.effectiveDirections.map(dir => (
        <option key={dir} value={dir}>
          {dir}
        </option>
      ))}
    </select>
  );
}

function EdgeModalDirectionFields(props: EdgeModalDirectionFieldsProps) {
  return (
    <div>
      <label htmlFor="edge-direction-select" className="block text-sm font-medium text-mythos-terminal-text mb-2">
        Direction: <span className="text-mythos-terminal-error">*</span>
      </label>
      <EdgeModalDirectionSelect
        direction={props.direction}
        setDirection={props.setDirection}
        effectiveDirections={props.effectiveDirections}
      />
      {/* Free-text custom directions (e.g. "portal", "secret") are not offered here -- the
          exit-creation API (#627) only accepts the standard Direction enum. */}
    </div>
  );
}

const EDGE_EXIT_FLAGS = ['one_way', 'hidden', 'locked', 'no_pick', 'no_flee'] as const;

function EdgeModalTargetRoomField(props: {
  isEditMode: boolean;
  searchQuery: string;
  setSearchQuery: (value: string) => void;
  targetRoomId: string;
  setTargetRoomId: (value: string) => void;
  filteredNodes: Node<RoomNodeData>[];
}) {
  return (
    <div>
      <label htmlFor="target-room" className="block text-sm font-medium text-mythos-terminal-text mb-2">
        To Room: <span className="text-mythos-terminal-error">*</span>
      </label>
      <input
        id="target-room-search"
        type="text"
        value={props.searchQuery}
        onChange={e => props.setSearchQuery(e.target.value)}
        placeholder="Search rooms..."
        className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text mb-2"
      />
      <select
        id="target-room"
        value={props.targetRoomId}
        onChange={e => props.setTargetRoomId(e.target.value)}
        required
        disabled={props.isEditMode}
        className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <option value="">Select target room...</option>
        {props.filteredNodes.map(node => (
          <option key={node.id} value={node.id}>
            {node.data.name} ({node.id})
          </option>
        ))}
      </select>
      {props.isEditMode ? (
        <p className="text-xs text-mythos-terminal-text/50 mt-1">
          Target room cannot be changed. Delete and recreate the exit to change the target.
        </p>
      ) : null}
    </div>
  );
}

function EdgeModalFlagsField(props: { flags: string[]; toggleFlag: (flag: string) => void }) {
  return (
    <div>
      <p className="block text-sm font-medium text-mythos-terminal-text mb-2">Exit Flags:</p>
      <div className="flex flex-wrap gap-2">
        {EDGE_EXIT_FLAGS.map(flag => (
          <label key={flag} className="flex items-center gap-2 cursor-pointer">
            <input
              type="checkbox"
              checked={props.flags.includes(flag)}
              onChange={() => props.toggleFlag(flag)}
              className="w-4 h-4"
            />
            <span className="text-sm text-mythos-terminal-text">{flag}</span>
          </label>
        ))}
      </div>
    </div>
  );
}

function EdgeModalFormActions(props: { onClose: () => void; canSubmit: boolean }) {
  return (
    <div className="flex justify-end gap-3 pt-4 border-t border-mythos-terminal-border">
      <button
        type="button"
        onClick={props.onClose}
        className="px-4 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface"
      >
        Cancel
      </button>
      <button
        type="submit"
        disabled={!props.canSubmit}
        className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        Create Exit
      </button>
    </div>
  );
}

interface EdgeCreationModalViewProps {
  onClose: () => void;
  sourceRoomId: string;
  validation: EdgeValidationResult | null;
  vm: ReturnType<typeof useEdgeCreationModal>;
}

function EdgeCreationModalForm(props: EdgeCreationModalViewProps) {
  const { onClose, validation, vm } = props;
  return (
    <form onSubmit={vm.handleSubmit} className="space-y-4">
      <EdgeModalTargetRoomField
        isEditMode={vm.isEditMode}
        searchQuery={vm.searchQuery}
        setSearchQuery={vm.setSearchQuery}
        targetRoomId={vm.targetRoomId}
        setTargetRoomId={vm.setTargetRoomId}
        filteredNodes={vm.filteredNodes}
      />
      <EdgeModalDirectionFields
        direction={vm.direction}
        setDirection={vm.setDirection}
        effectiveDirections={vm.effectiveDirections}
      />
      <EdgeModalFlagsField flags={vm.flags} toggleFlag={vm.toggleFlag} />
      <div>
        <label htmlFor="description" className="block text-sm font-medium text-mythos-terminal-text mb-2">
          Description (optional):
        </label>
        <textarea
          id="description"
          value={vm.description}
          onChange={e => vm.setDescription(e.target.value)}
          placeholder="Exit description..."
          rows={3}
          className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
        />
      </div>
      {validation ? <EdgeModalValidationMessages validation={validation} /> : null}
      <EdgeModalFormActions onClose={onClose} canSubmit={vm.canSubmit} />
    </form>
  );
}

export function EdgeCreationModalView(props: EdgeCreationModalViewProps) {
  const { onClose, sourceRoomId, vm } = props;
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-75 border-0 p-0"
        onClick={onClose}
        aria-label="Dismiss dialog (backdrop)"
      />
      <div
        className="relative z-10 bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-2xl max-h-modal overflow-y-auto shadow-xl"
        role="dialog"
        aria-modal="true"
        aria-labelledby="edge-creation-title"
      >
        <div className="flex items-center justify-between mb-6">
          <h2 id="edge-creation-title" className="text-2xl font-bold text-mythos-terminal-text">
            Create Exit
          </h2>
          <button
            onClick={onClose}
            className="text-mythos-terminal-text hover:text-mythos-terminal-error text-2xl leading-none"
            aria-label="Close dialog"
          >
            ×
          </button>
        </div>
        <div className="mb-4">
          <p className="block text-sm font-medium text-mythos-terminal-text mb-2">From Room:</p>
          <div className="px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text">
            {vm.sourceRoom?.data.name || sourceRoomId}
          </div>
        </div>
        <EdgeCreationModalForm {...props} />
        <div className="mt-4 text-xs text-mythos-terminal-text/50 text-center">Press ESC to close</div>
      </div>
    </div>
  );
}
