import { useEffect, useLayoutEffect, useRef } from 'react';

function collectFocusableElements(container: HTMLElement): HTMLElement[] {
  const nodes = container.querySelectorAll<HTMLElement>(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  return Array.from(nodes).filter(el => {
    if (el.hasAttribute('disabled')) return false;
    if (el.getAttribute('aria-hidden') === 'true') return false;
    return true;
  });
}

export type ChatExportDialogProps = {
  visibleCount: number;
  exportFormat: string;
  isExporting: boolean;
  setExportFormat: (v: string) => void;
  onClose: () => void;
  onConfirmExport: () => void;
};

export function ChatExportDialog({
  visibleCount,
  exportFormat,
  isExporting,
  setExportFormat,
  onClose,
  onConfirmExport,
}: ChatExportDialogProps) {
  const panelRef = useRef<HTMLDivElement>(null);
  const previouslyFocusedRef = useRef<HTMLElement | null>(null);

  useLayoutEffect(() => {
    previouslyFocusedRef.current = document.activeElement as HTMLElement | null;
    const select = document.getElementById('chat-export-format') as HTMLSelectElement | null;
    select?.focus();
    return () => {
      previouslyFocusedRef.current?.focus?.();
    };
  }, []);

  useEffect(() => {
    const onDocKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && !isExporting) {
        e.preventDefault();
        onClose();
      }
    };
    document.addEventListener('keydown', onDocKeyDown);
    return () => {
      document.removeEventListener('keydown', onDocKeyDown);
    };
  }, [onClose, isExporting]);

  useEffect(() => {
    const panel = panelRef.current;
    if (!panel) return;

    const onPanelKeyDown = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;
      const els = collectFocusableElements(panel);
      if (els.length === 0) return;
      const first = els[0];
      const last = els[els.length - 1];
      const active = document.activeElement;
      if (e.shiftKey) {
        if (active === first) {
          e.preventDefault();
          last.focus();
        }
      } else if (active === last) {
        e.preventDefault();
        first.focus();
      }
    };
    panel.addEventListener('keydown', onPanelKeyDown);
    return () => {
      panel.removeEventListener('keydown', onPanelKeyDown);
    };
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <button
        type="button"
        tabIndex={-1}
        className="absolute inset-0 cursor-default border-0 bg-black/50 p-0"
        aria-label="Dismiss export dialog"
        disabled={isExporting}
        onMouseDown={() => {
          if (!isExporting) onClose();
        }}
      />
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="chat-export-title"
        className="relative z-10 mx-4 w-full max-w-md rounded-lg border border-mythos-terminal-primary bg-mythos-terminal-surface p-6"
      >
        <h3 id="chat-export-title" className="mb-4 text-lg font-bold text-mythos-terminal-primary">
          Export Chat Messages
        </h3>
        <div className="space-y-4">
          <div>
            <label htmlFor="chat-export-format" className="mb-2 block text-sm text-mythos-terminal-text-secondary">
              Export Format
            </label>
            <select
              id="chat-export-format"
              value={exportFormat}
              onChange={e => setExportFormat(e.target.value)}
              className="w-full rounded border border-gray-700 bg-mythos-terminal-background px-2 py-1 text-sm text-mythos-terminal-text"
              disabled={isExporting}
            >
              <option value="txt">Plain Text (.txt)</option>
              <option value="html">HTML (.html)</option>
              <option value="json">JSON (.json)</option>
              <option value="csv">CSV (.csv)</option>
            </select>
          </div>
          <div className="text-xs text-mythos-terminal-text-secondary">
            Exporting {visibleCount} message{visibleCount === 1 ? '' : 's'}
          </div>
          <div className="flex justify-end gap-2">
            <button
              onClick={onClose}
              disabled={isExporting}
              className="rounded border border-gray-700 bg-mythos-terminal-background px-4 py-2 text-sm hover:bg-mythos-terminal-surface disabled:opacity-50"
              type="button"
            >
              Cancel
            </button>
            <button
              onClick={onConfirmExport}
              disabled={isExporting || visibleCount === 0}
              className="rounded bg-mythos-terminal-primary px-4 py-2 text-sm font-bold text-black hover:bg-mythos-terminal-primary/80 disabled:opacity-50"
              type="button"
            >
              {isExporting ? 'Exporting...' : 'Export'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
