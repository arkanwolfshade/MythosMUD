/**
 * Standalone Manual page.
 *
 * Opened from ESC Main Menu "Manual (New Tab)". Shows the command reference and concept guides from
 * GET /v1/api/help (filtered server-side by role), with a text filter and an anchor per topic
 * (e.g. /manual#look).
 */

import React, { useEffect, useMemo, useState } from 'react';
import { SafeHtml } from '../components/common/SafeHtml';
import { API_V1_BASE } from '../utils/config.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

interface ManualCommand {
  name: string;
  category: string;
  summary: string;
  usage: string[];
  aliases?: string[];
  admin_only?: boolean;
  arguments?: { name: string; required: boolean; description: string }[];
  examples?: { input: string; note?: string }[];
  see_also?: string[];
  details_html?: string[];
}

interface ManualGuide {
  id: string;
  title: string;
  group: string;
  summary: string;
  see_also?: string[];
  details_html?: string[];
}

interface ManualDocs {
  commands: ManualCommand[];
  guides: ManualGuide[];
}

const GUIDES_HEADING = 'Lore & Guidance';
const NOT_AUTHENTICATED = 'Not authenticated. Please log in first.';
const SUBHEAD_CLASS = 'help-subhead mt-3';

function useManualDocs() {
  const [docs, setDocs] = useState<ManualDocs | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const token = secureTokenStorage.getToken();
    if (!token) {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- auth gate before fetch
      setError(NOT_AUTHENTICATED);
      return;
    }
    let cancelled = false;
    const load = async () => {
      try {
        const response = await fetch(`${API_V1_BASE}/api/help`, { headers: { Authorization: `Bearer ${token}` } });
        if (cancelled) return;
        if (!response.ok) {
          setError(response.status === 401 ? NOT_AUTHENTICATED : 'Failed to load the manual.');
          return;
        }
        setDocs((await response.json()) as ManualDocs);
      } catch (err) {
        logger.error('ManualPage', 'Failed to fetch manual', { error: err });
        if (!cancelled) setError('Failed to connect to server.');
      }
    };
    void load();
    return () => {
      cancelled = true;
    };
  }, []);

  return { docs, error };
}

function matches(query: string, ...fields: (string | undefined)[]): boolean {
  return fields.some(field => field?.toLowerCase().includes(query));
}

function groupBy<T>(items: T[], key: (item: T) => string): [string, T[]][] {
  const groups = new Map<string, T[]>();
  for (const item of items) {
    const group = key(item);
    groups.set(group, [...(groups.get(group) ?? []), item]);
  }
  return [...groups];
}

function filterDocs(docs: ManualDocs, rawQuery: string): ManualDocs {
  const query = rawQuery.trim().toLowerCase();
  if (!query) return docs;
  return {
    commands: docs.commands.filter(c => matches(query, c.name, c.summary, ...(c.aliases ?? []))),
    guides: docs.guides.filter(g => matches(query, g.id, g.title, g.summary)),
  };
}

function TopicLinks({ topics }: { topics: string[] }) {
  return (
    <>
      {topics.map((topic, index) => (
        <React.Fragment key={topic}>
          {index > 0 && ', '}
          <a href={`#${topic}`} className="underline text-mythos-terminal-secondary">
            {topic}
          </a>
        </React.Fragment>
      ))}
    </>
  );
}

function Details({ lines }: { lines?: string[] }) {
  if (!lines || lines.length === 0) return null;
  return <SafeHtml tag="div" className="help-entry mt-2" html={lines.join('\n')} />;
}

function SeeAlso({ topics }: { topics?: string[] }) {
  if (!topics || topics.length === 0) return null;
  return (
    <p className="mt-3 text-sm">
      <span className="help-subhead">See also: </span>
      <TopicLinks topics={topics} />
    </p>
  );
}

function CommandBody({ command }: { command: ManualCommand }) {
  return (
    <>
      <p className="help-subhead mt-2">Usage</p>
      <ul className="help-entry">
        {command.usage.map(usage => (
          <li key={usage}>
            <code>{usage}</code>
          </li>
        ))}
      </ul>
      {command.arguments && command.arguments.length > 0 && (
        <>
          <p className={SUBHEAD_CLASS}>Arguments</p>
          <ul className="help-entry">
            {command.arguments.map(arg => (
              <li key={arg.name}>
                <code>{arg.name}</code> ({arg.required ? 'required' : 'optional'}) - {arg.description}
              </li>
            ))}
          </ul>
        </>
      )}
      {command.examples && command.examples.length > 0 && (
        <>
          <p className={SUBHEAD_CLASS}>Examples</p>
          <ul className="help-entry">
            {command.examples.map(example => (
              <li key={example.input}>
                <code>{example.input}</code>
                {example.note ? ` - ${example.note}` : ''}
              </li>
            ))}
          </ul>
        </>
      )}
    </>
  );
}

function CommandEntry({ command }: { command: ManualCommand }) {
  return (
    <article id={command.name} className="mb-6 scroll-mt-4">
      <h3 className="help-title text-lg font-bold">
        {command.name.toUpperCase()}
        {command.aliases && command.aliases.length > 0 && (
          <span className="help-aliases text-sm font-normal"> (also: {command.aliases.join(', ')})</span>
        )}
        {command.admin_only && <span className="help-aliases text-sm font-normal"> [admin]</span>}
      </h3>
      <p>{command.summary}</p>
      <CommandBody command={command} />
      <Details lines={command.details_html} />
      <SeeAlso topics={command.see_also} />
    </article>
  );
}

function GuideEntry({ guide }: { guide: ManualGuide }) {
  return (
    <article id={guide.id} className="mb-6 scroll-mt-4">
      <h3 className="help-title text-lg font-bold">
        {guide.title}
        <span className="help-aliases text-sm font-normal"> ({guide.group})</span>
      </h3>
      <p>{guide.summary}</p>
      <Details lines={guide.details_html} />
      <SeeAlso topics={guide.see_also} />
    </article>
  );
}

function Contents({ docs }: { docs: ManualDocs }) {
  const sections: [string, string[]][] = [
    ...groupBy(docs.commands, c => c.category).map(([category, items]): [string, string[]] => [
      category,
      items.map(c => c.name),
    ]),
    ...(docs.guides.length > 0 ? [[GUIDES_HEADING, docs.guides.map(g => g.id)] as [string, string[]]] : []),
  ];
  return (
    <nav aria-label="Contents" className="mb-8 text-sm space-y-2">
      {sections.map(([heading, topics]) => (
        <p key={heading}>
          <span className="help-subhead">{heading}: </span>
          <TopicLinks topics={topics} />
        </p>
      ))}
    </nav>
  );
}

function ManualBody({ docs }: { docs: ManualDocs }) {
  if (docs.commands.length === 0 && docs.guides.length === 0) {
    return <p className="opacity-70">Nothing in the archives matches that search.</p>;
  }
  return (
    <>
      <Contents docs={docs} />
      {groupBy(docs.commands, c => c.category).map(([category, items]) => (
        <section key={category} aria-label={category}>
          <h2 className="text-xl font-bold mb-3 border-b border-mythos-terminal-border">{category}</h2>
          {items.map(command => (
            <CommandEntry key={command.name} command={command} />
          ))}
        </section>
      ))}
      {docs.guides.length > 0 && (
        <section aria-label={GUIDES_HEADING}>
          <h2 className="text-xl font-bold mb-3 border-b border-mythos-terminal-border">{GUIDES_HEADING}</h2>
          {docs.guides.map(guide => (
            <GuideEntry key={guide.id} guide={guide} />
          ))}
        </section>
      )}
    </>
  );
}

function ManualError({ error }: { error: string }) {
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
          Go to Game
        </button>
      </div>
    </div>
  );
}

/**
 * Standalone manual page: token from localStorage; the server decides which commands this reader may see.
 */
export const ManualPage: React.FC = () => {
  const { docs, error } = useManualDocs();
  const [query, setQuery] = useState('');
  const visible = useMemo(() => (docs ? filterDocs(docs, query) : null), [docs, query]);

  useEffect(() => {
    if (!docs) return;
    const topic = decodeURIComponent(window.location.hash.slice(1));
    if (topic) document.getElementById(topic)?.scrollIntoView();
  }, [docs]);

  if (error && !docs) return <ManualError error={error} />;

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text p-4 sm:p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-2xl font-bold mb-1">Field Manual</h1>
        <p className="text-mythos-terminal-text/70 text-sm mb-4">
          Compiled for investigators by the Department of Occult Studies, Miskatonic University.
        </p>
        <label className="block mb-6">
          <span className="text-sm">Search the archives</span>
          <input
            type="search"
            value={query}
            onChange={event => setQuery(event.target.value)}
            placeholder="a command, an alias, a topic"
            className="mt-1 w-full px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border rounded"
          />
        </label>
        {visible ? <ManualBody docs={visible} /> : <p className="opacity-70">Consulting the archives...</p>}
      </div>
    </div>
  );
};
