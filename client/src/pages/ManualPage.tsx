/**
 * Standalone Manual page.
 *
 * Opened from ESC Main Menu "Manual (New Tab)". Shows the command reference and concept guides from
 * GET /v1/api/help (filtered server-side by role), with a text filter and an anchor per topic
 * (e.g. /manual#look).
 */

import React, { useEffect, useMemo, useRef, useState } from 'react';
import { SafeHtml } from '../components/common/SafeHtml';
import { API_V1_BASE } from '../utils/config.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

interface ManualCommand {
  name: string;
  category: string;
  summary: string;
  usage: string[];
  aliases: string[];
  admin_only: boolean;
  arguments: { name: string; required: boolean; description: string }[];
  examples: { input: string; note?: string }[];
  see_also: string[];
  details_html: string[];
}

interface ManualGuide {
  id: string;
  title: string;
  group: string;
  summary: string;
  see_also: string[];
  details_html: string[];
}

interface ManualDocs {
  commands: ManualCommand[];
  guides: ManualGuide[];
}

const GUIDES_HEADING = 'Lore & Guidance';
const NOT_AUTHENTICATED = 'Not authenticated. Please log in first.';

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

function matches(query: string, ...fields: string[]): boolean {
  return fields.some(field => field.toLowerCase().includes(query));
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
    commands: docs.commands.filter(c => matches(query, c.name, c.summary, ...c.aliases)),
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

function Details({ lines }: { lines: string[] }) {
  if (lines.length === 0) return null;
  return <SafeHtml tag="div" className="help-entry" html={lines.join('\n')} />;
}

function SeeAlso({ topics }: { topics: string[] }) {
  if (topics.length === 0) return null;
  return (
    <p className="manual-seealso">
      <span className="help-subhead">See also: </span>
      <TopicLinks topics={topics} />
    </p>
  );
}

function Section({ title, items }: { title: string; items: React.ReactNode[] }) {
  if (items.length === 0) return null;
  return (
    <>
      <p className="help-subhead">{title}</p>
      <ul className="help-entry">{items}</ul>
    </>
  );
}

function CommandBody({ command }: { command: ManualCommand }) {
  return (
    <>
      <Section
        title="Usage"
        items={command.usage.map(usage => (
          <li key={usage}>
            <code>{usage}</code>
          </li>
        ))}
      />
      <Section
        title="Arguments"
        items={command.arguments.map(arg => (
          <li key={arg.name}>
            <code>{arg.name}</code> ({arg.required ? 'required' : 'optional'}) - {arg.description}
          </li>
        ))}
      />
      <Section
        title="Examples"
        items={command.examples.map(example => (
          <li key={example.input}>
            <code>{example.input}</code>
            {example.note ? ` - ${example.note}` : ''}
          </li>
        ))}
      />
    </>
  );
}

function CommandEntry({ command }: { command: ManualCommand }) {
  return (
    <article id={command.name} className="manual-entry scroll-mt-4">
      <h3 className="help-title font-bold">
        {command.name.toUpperCase()}
        {command.aliases.length > 0 && (
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
    <article id={guide.id} className="manual-entry scroll-mt-4">
      <h3 className="help-title font-bold">
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
    <nav aria-label="Contents" className="manual-contents">
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
          <h2 className="manual-heading font-bold border-b border-mythos-terminal-border">{category}</h2>
          {items.map(command => (
            <CommandEntry key={command.name} command={command} />
          ))}
        </section>
      ))}
      {docs.guides.length > 0 && (
        <section aria-label={GUIDES_HEADING}>
          <h2 className="manual-heading font-bold border-b border-mythos-terminal-border">{GUIDES_HEADING}</h2>
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
      <div className="manual-error text-center">
        <h1 className="font-bold text-mythos-terminal-error">Error</h1>
        <p>{error}</p>
        <button
          type="button"
          onClick={() => {
            window.location.href = '/';
          }}
          className="manual-button bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
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
  const pageRef = useRef<HTMLDivElement>(null);
  const visible = useMemo(() => (docs ? filterDocs(docs, query) : null), [docs, query]);

  // The app shell clips the document (html/body/#root are overflow: hidden), so this page scrolls itself. A scroll
  // container only takes PageUp/PageDown/Space/arrow keys once focused, so focus it as soon as the page mounts.
  useEffect(() => {
    pageRef.current?.focus({ preventScroll: true });
  }, []);

  useEffect(() => {
    if (!docs) return;
    const topic = decodeURIComponent(window.location.hash.slice(1));
    if (topic) document.getElementById(topic)?.scrollIntoView();
  }, [docs]);

  if (error && !docs) return <ManualError error={error} />;

  return (
    <div ref={pageRef} tabIndex={-1} className="manual-page bg-mythos-terminal-background text-mythos-terminal-text">
      <div className="manual-content">
        <h1 className="font-bold">Field Manual</h1>
        <p className="manual-intro text-mythos-terminal-text/70">
          Compiled for investigators by the Department of Occult Studies, Miskatonic University.
        </p>
        <label className="manual-search">
          <span>Search the archives</span>
          <input
            type="search"
            value={query}
            onChange={event => setQuery(event.target.value)}
            placeholder="a command, an alias, a topic"
            className="bg-mythos-terminal-background border border-mythos-terminal-border rounded"
          />
        </label>
        {visible ? <ManualBody docs={visible} /> : <p className="opacity-70">Consulting the archives...</p>}
      </div>
    </div>
  );
};
