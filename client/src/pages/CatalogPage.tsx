/**
 * Standalone Item Catalog page.
 *
 * Opened from ESC Main Menu "Catalog (New Tab)". Lists item_prototypes via
 * GET /v1/api/item-catalog with type/namespace/search filters and pagination.
 */

import React, { useCallback, useEffect, useState } from 'react';
import { API_V1_BASE } from '../utils/config.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

interface CatalogPlayerItem {
  name: string;
  item_type: string;
  short_description: string;
}

interface CatalogAdminItem extends CatalogPlayerItem {
  prototype_id: string;
  long_description: string;
  weight: number;
  base_value: number;
  durability: number | null;
  flags: unknown[];
  wear_slots: unknown[];
  stacking_rules: Record<string, unknown>;
  usage_restrictions: Record<string, unknown>;
  effect_components: unknown[];
  metadata: Record<string, unknown>;
  tags: unknown[];
  created_at: string | null;
}

type CatalogItem = CatalogPlayerItem | CatalogAdminItem;

interface CatalogResponse {
  items: CatalogItem[];
  page: number;
  page_size: number;
  total: number;
  is_admin: boolean;
}

const INPUT_CLASS = 'mt-1 px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border rounded';
const BTN_CLASS = 'px-3 py-2 bg-mythos-terminal-primary text-white rounded disabled:opacity-40';

function isAdminItem(item: CatalogItem, isAdmin: boolean): item is CatalogAdminItem {
  return isAdmin && 'prototype_id' in item;
}

function formatCell(value: unknown): string {
  if (value == null) return '';
  if (typeof value !== 'object') return String(value);
  try {
    return JSON.stringify(value);
  } catch {
    return String(value);
  }
}

function buildCatalogUrl(page: number, itemType: string, namespace: string, search: string): string {
  const params = new URLSearchParams({ page: String(page), page_size: '25' });
  if (itemType.trim()) params.set('type', itemType.trim());
  if (namespace.trim()) params.set('namespace', namespace.trim());
  if (search.trim()) params.set('search', search.trim());
  return `${API_V1_BASE}/api/item-catalog/?${params.toString()}`;
}

function CatalogErrorView({ error, authToken }: { error: string; authToken: string | null }) {
  return (
    <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
      <div className="text-center max-w-md p-6">
        <h1 className="text-2xl font-bold mb-4 text-mythos-terminal-error">Error</h1>
        <p className="mb-4">{error}</p>
        <button
          type="button"
          onClick={() => {
            window.location.href = '/';
          }}
          className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
        >
          {authToken ? 'Back to Game' : 'Go to Login'}
        </button>
      </div>
    </div>
  );
}

function FilterField({
  label,
  value,
  onChange,
  placeholder,
  grow,
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  placeholder: string;
  grow?: boolean;
}) {
  return (
    <label className={`flex flex-col text-sm${grow ? ' grow min-w-48' : ''}`}>
      {label}
      <input className={INPUT_CLASS} value={value} onChange={e => onChange(e.target.value)} placeholder={placeholder} />
    </label>
  );
}

interface CatalogFilterFormProps {
  itemType: string;
  namespace: string;
  search: string;
  onItemTypeChange: (value: string) => void;
  onNamespaceChange: (value: string) => void;
  onSearchChange: (value: string) => void;
  onSubmit: () => void;
}

function CatalogFilterForm(props: CatalogFilterFormProps) {
  return (
    <form
      className="flex flex-wrap gap-2 mb-4 items-end"
      onSubmit={event => {
        event.preventDefault();
        props.onSubmit();
      }}
    >
      <FilterField label="Type" value={props.itemType} onChange={props.onItemTypeChange} placeholder="weapon" />
      <FilterField label="Namespace" value={props.namespace} onChange={props.onNamespaceChange} placeholder="core" />
      <FilterField label="Search" value={props.search} onChange={props.onSearchChange} placeholder="knife" grow />
      <button type="submit" className={`${BTN_CLASS} hover:bg-mythos-terminal-primary/80`}>
        Apply filters
      </button>
    </form>
  );
}

function AdminCells({ item }: { item: CatalogAdminItem }) {
  return (
    <>
      <td className="py-2 pr-3 align-top font-mono text-xs">{item.prototype_id}</td>
      <td className="py-2 pr-3 align-top">{item.weight}</td>
      <td className="py-2 pr-3 align-top">{item.base_value}</td>
      <td className="py-2 pr-3 align-top font-mono text-xs max-w-xs break-all">{formatCell(item.metadata)}</td>
      <td className="py-2 pr-3 align-top font-mono text-xs">{formatCell(item.tags)}</td>
    </>
  );
}

function CatalogTable({ data }: { data: CatalogResponse }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-left text-sm border-collapse">
        <thead>
          <tr className="border-b border-mythos-terminal-border">
            <th className="py-2 pr-3">Name</th>
            <th className="py-2 pr-3">Type</th>
            <th className="py-2 pr-3">Short description</th>
            {data.is_admin ? (
              <>
                <th className="py-2 pr-3">Prototype ID</th>
                <th className="py-2 pr-3">Weight</th>
                <th className="py-2 pr-3">Value</th>
                <th className="py-2 pr-3">Metadata</th>
                <th className="py-2 pr-3">Tags</th>
              </>
            ) : null}
          </tr>
        </thead>
        <tbody>
          {data.items.map((item, index) => (
            <tr
              key={isAdminItem(item, data.is_admin) ? item.prototype_id : `${item.name}-${item.item_type}-${index}`}
              className="border-b border-mythos-terminal-border/40"
            >
              <td className="py-2 pr-3 align-top">{item.name}</td>
              <td className="py-2 pr-3 align-top">{item.item_type}</td>
              <td className="py-2 pr-3 align-top">{item.short_description}</td>
              {isAdminItem(item, data.is_admin) ? <AdminCells item={item} /> : null}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function CatalogPagination({
  page,
  totalPages,
  dataPage,
  onPrev,
  onNext,
}: {
  page: number;
  totalPages: number;
  dataPage: number;
  onPrev: () => void;
  onNext: () => void;
}) {
  return (
    <div className="flex gap-3 items-center mt-6">
      <button type="button" disabled={page <= 1} onClick={onPrev} className={BTN_CLASS}>
        Previous
      </button>
      <span className="text-sm">
        Page {dataPage} / {totalPages}
      </span>
      <button type="button" disabled={page >= totalPages} onClick={onNext} className={BTN_CLASS}>
        Next
      </button>
      <button
        type="button"
        onClick={() => {
          window.close();
        }}
        className={`ml-auto ${BTN_CLASS} hover:bg-mythos-terminal-primary/80`}
      >
        Close
      </button>
    </div>
  );
}

function CatalogResults({ data, isLoading }: { data: CatalogResponse | null; isLoading: boolean }) {
  if (isLoading && !data) return <p>Loading catalog...</p>;
  if (data && data.items.length === 0) {
    return <p className="text-mythos-terminal-text/70">No prototypes match.</p>;
  }
  return data ? <CatalogTable data={data} /> : null;
}

function catalogShowingLabel(data: CatalogResponse): string {
  const start = data.total > 0 ? (data.page - 1) * data.page_size + 1 : 0;
  const end = Math.min(data.page * data.page_size, data.total);
  return `Showing ${start}-${end} of ${data.total}; refine with filters`;
}

function catalogTotalPages(data: CatalogResponse): number {
  return Math.max(1, Math.ceil(data.total / data.page_size));
}

type CatalogPageState = ReturnType<typeof useCatalogPageState>;

function CatalogLoadedView({ s }: { s: CatalogPageState }) {
  const data = s.data;
  if (!data) {
    return (
      <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text p-6">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-2xl font-bold mb-2">Item Catalog</h1>
          <p className="text-mythos-terminal-text/70 text-sm mb-4">Loading catalog...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text p-6">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-2xl font-bold mb-2">Item Catalog</h1>
        <p className="text-mythos-terminal-text/70 text-sm mb-4">{catalogShowingLabel(data)}</p>
        <CatalogFilterForm
          itemType={s.itemType}
          namespace={s.namespace}
          search={s.search}
          onItemTypeChange={s.setItemType}
          onNamespaceChange={s.setNamespace}
          onSearchChange={s.setSearch}
          onSubmit={() => {
            s.setPage(1);
            if (s.authToken) void s.fetchCatalog(s.authToken, 1);
          }}
        />
        <CatalogResults data={data} isLoading={s.isLoading} />
        <CatalogPagination
          page={s.page}
          totalPages={catalogTotalPages(data)}
          dataPage={data.page}
          onPrev={() => s.setPage(p => Math.max(1, p - 1))}
          onNext={() => s.setPage(p => p + 1)}
        />
      </div>
    </div>
  );
}

function useCatalogPageState() {
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [itemType, setItemType] = useState('');
  const [namespace, setNamespace] = useState('');
  const [search, setSearch] = useState('');
  const [page, setPage] = useState(1);
  const [data, setData] = useState<CatalogResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchCatalog = useCallback(
    async (token: string, nextPage: number) => {
      setIsLoading(true);
      try {
        const response = await fetch(buildCatalogUrl(nextPage, itemType, namespace, search), {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (!response.ok) {
          setError(
            response.status === 401 ? 'Not authenticated. Please log in first.' : 'Failed to load item catalog.'
          );
          return;
        }
        setData((await response.json()) as CatalogResponse);
        setError(null);
      } catch (err) {
        logger.error('CatalogPage', 'Failed to fetch catalog', { error: err });
        setError('Failed to connect to server.');
      } finally {
        setIsLoading(false);
      }
    },
    [itemType, namespace, search]
  );

  useEffect(() => {
    const token = secureTokenStorage.getToken();
    if (!token) {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- auth gate before fetch
      setError('Not authenticated. Please log in first.');
      setIsLoading(false);
      return;
    }
    setAuthToken(token);
    void fetchCatalog(token, page);
  }, [fetchCatalog, page]);

  return {
    authToken,
    itemType,
    setItemType,
    namespace,
    setNamespace,
    search,
    setSearch,
    page,
    setPage,
    data,
    isLoading,
    error,
    fetchCatalog,
  };
}

/**
 * Standalone catalog page: token from localStorage; filters in query UI.
 */
export const CatalogPage: React.FC = () => {
  const s = useCatalogPageState();
  if (s.error && !s.data) {
    return <CatalogErrorView error={s.error} authToken={s.authToken} />;
  }
  return <CatalogLoadedView s={s} />;
};
