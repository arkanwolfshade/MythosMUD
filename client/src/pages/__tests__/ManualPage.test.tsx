import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { ManualPage } from '../ManualPage';

const hoisted = vi.hoisted(() => ({
  getTokenMock: vi.fn(),
  loggerErrorMock: vi.fn(),
}));

// Keep the real module: SafeHtml needs INCOMING_HTML_DOMPURIFY_CONFIG, so the sanitizer test runs the real config.
vi.mock('../../utils/security.js', async importOriginal => ({
  ...(await importOriginal<typeof import('../../utils/security.js')>()),
  secureTokenStorage: {
    getToken: () => hoisted.getTokenMock(),
  },
}));

vi.mock('../../utils/logger.js', () => ({
  logger: {
    error: hoisted.loggerErrorMock,
  },
}));

vi.mock('../../utils/config.js', () => ({
  API_V1_BASE: 'http://localhost:54768/v1',
}));

const manualBody = {
  commands: [
    {
      name: 'look',
      category: 'Exploration',
      summary: 'Examine your surroundings.',
      usage: ['look', 'look <target>'],
      arguments: [{ name: 'target', required: false, description: 'What to examine.' }],
      examples: [{ input: 'look lantern', note: 'Inspect the lantern.' }],
      see_also: ['local'],
      details_html: ['<p>The first step toward understanding.</p>'],
    },
    {
      name: 'local',
      category: 'Communication',
      summary: 'Speak to your sub-zone.',
      usage: ['local <message>', 'l <message>'],
      aliases: ['l'],
    },
  ],
  guides: [
    {
      id: 'lucidity',
      title: 'Lucidity',
      group: 'Core survival',
      summary: 'Guarding the mind.',
      see_also: ['look'],
      details_html: ['<p>The mind is a fragile vessel.</p>'],
    },
  ],
};

function mockJsonResponse(body: object, ok = true, status = 200): Response {
  return { ok, status, json: async () => body } as Response;
}

describe('ManualPage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    window.history.replaceState({}, '', '/manual');
    Element.prototype.scrollIntoView = vi.fn();
  });

  it('shows auth error when token is missing', async () => {
    hoisted.getTokenMock.mockReturnValue(null);

    render(<ManualPage />);

    expect(await screen.findByText('Not authenticated. Please log in first.')).toBeInTheDocument();
  });

  it('reports an unauthorised response as a login problem', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse({}, false, 401));

    render(<ManualPage />);

    expect(await screen.findByText('Not authenticated. Please log in first.')).toBeInTheDocument();
  });

  it('reports a failed connection', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockRejectedValueOnce(new Error('offline'));

    render(<ManualPage />);

    expect(await screen.findByText('Failed to connect to server.')).toBeInTheDocument();
    expect(hoisted.loggerErrorMock).toHaveBeenCalled();
  });

  it('requests the manual with the bearer token and renders commands and guides', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    const fetchSpy = vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(manualBody));

    render(<ManualPage />);

    expect(await screen.findByRole('heading', { name: 'LOOK' })).toBeInTheDocument();
    expect(fetchSpy).toHaveBeenCalledWith('http://localhost:54768/v1/api/help', {
      headers: { Authorization: 'Bearer token' },
    });
    expect(screen.getByText('look <target>')).toBeInTheDocument();
    expect(screen.getByText('Inspect the lantern.', { exact: false })).toBeInTheDocument();
    expect(screen.getByText('The first step toward understanding.')).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: /LOCAL/ })).toHaveTextContent('(also: l)');
    expect(screen.getByRole('heading', { name: /Lucidity/ })).toBeInTheDocument();
    expect(screen.getByText('The mind is a fragile vessel.')).toBeInTheDocument();
  });

  it('strips markup the sanitizer does not allow from the details', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    const hostile = {
      ...manualBody,
      commands: [
        {
          ...manualBody.commands[0],
          details_html: ['<p>Safe text</p><script>window.__pwned = true</script><img src=x onerror="alert(1)">'],
        },
      ],
    };
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(hostile));

    const { container } = render(<ManualPage />);

    expect(await screen.findByText('Safe text')).toBeInTheDocument();
    expect(container.querySelector('script')).toBeNull();
    expect(container.querySelector('img')).toBeNull();
  });

  it('filters by name, alias, or summary', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(manualBody));
    render(<ManualPage />);
    await screen.findByRole('heading', { name: 'LOOK' });
    const search = screen.getByLabelText('Search the archives');

    fireEvent.change(search, { target: { value: 'sub-zone' } });
    expect(screen.queryByRole('heading', { name: 'LOOK' })).not.toBeInTheDocument();
    expect(screen.getByRole('heading', { name: /LOCAL/ })).toBeInTheDocument();

    fireEvent.change(search, { target: { value: 'L' } });
    expect(screen.getByRole('heading', { name: /LOCAL/ })).toBeInTheDocument();

    fireEvent.change(search, { target: { value: 'zzz' } });
    expect(screen.getByText('Nothing in the archives matches that search.')).toBeInTheDocument();
  });

  it('links see-also topics and the contents to anchors', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(manualBody));

    render(<ManualPage />);
    await screen.findByRole('heading', { name: 'LOOK' });

    const localLinks = screen.getAllByRole('link', { name: 'local' });
    expect(localLinks.length).toBeGreaterThanOrEqual(2); // contents + the see-also under look
    for (const link of localLinks) expect(link).toHaveAttribute('href', '#local');
    expect(document.getElementById('look')).not.toBeNull();
    expect(document.getElementById('lucidity')).not.toBeNull();
  });

  it('takes focus on mount so the page scrolls with the keyboard straight away', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(manualBody));

    const { container } = render(<ManualPage />);
    await screen.findByRole('heading', { name: 'LOOK' });

    // The app shell clips the document, so this page is its own scroll container; a scroller only takes
    // PageUp/PageDown/Space/arrow keys once focused.
    expect(container.querySelector('.manual-page')).toHaveFocus();
  });

  it('scrolls to the topic named in the URL hash once loaded', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    window.history.replaceState({}, '', '/manual#local');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(manualBody));

    render(<ManualPage />);

    await waitFor(() => expect(Element.prototype.scrollIntoView).toHaveBeenCalled());
  });
});
