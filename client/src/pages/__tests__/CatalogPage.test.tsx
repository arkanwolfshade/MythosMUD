import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { CatalogPage } from '../CatalogPage';

const hoisted = vi.hoisted(() => ({
  getTokenMock: vi.fn(),
  loggerErrorMock: vi.fn(),
}));

vi.mock('../../utils/security.js', () => ({
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

const playerCatalogBody = {
  items: [{ name: 'Knife', item_type: 'weapon', short_description: 'A blade' }],
  page: 1,
  page_size: 25,
  total: 1,
  is_admin: false,
};

const emptyCatalogBody = {
  items: [],
  page: 1,
  page_size: 25,
  total: 0,
  is_admin: false,
};

const adminCatalogBody = {
  items: [
    {
      prototype_id: 'core.weapon.knife',
      name: 'Knife',
      item_type: 'weapon',
      short_description: 'A blade',
      weight: 0.5,
      base_value: 10,
      metadata: {
        weapon: { min_damage: 1, max_damage: 4, skill: 'melee' },
        catalog: { namespace: 'core' },
      },
      tags: ['melee', 'core'],
    },
  ],
  page: 1,
  page_size: 25,
  total: 1,
  is_admin: true,
};

function mockJsonResponse(body: object, ok = true, status = 200): Response {
  return {
    ok,
    status,
    json: async () => body,
  } as Response;
}

describe('CatalogPage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    window.history.replaceState({}, '', '/catalog');
  });

  it('shows auth error when token is missing', async () => {
    hoisted.getTokenMock.mockReturnValue(null);

    render(<CatalogPage />);

    expect(await screen.findByText('Not authenticated. Please log in first.')).toBeInTheDocument();
  });

  it('renders returned catalog rows', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(playerCatalogBody));

    render(<CatalogPage />);

    await waitFor(() => {
      expect(screen.getByText('Knife')).toBeInTheDocument();
      expect(screen.getByText('weapon')).toBeInTheDocument();
      expect(screen.getByText('A blade')).toBeInTheDocument();
    });
    expect(screen.getByText(/Showing 1-1 of 1/)).toBeInTheDocument();
  });

  it('renders empty-state when no prototypes match', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(emptyCatalogBody));

    render(<CatalogPage />);

    expect(await screen.findByText('No prototypes match.')).toBeInTheDocument();
    expect(screen.getByText(/Showing 0-0 of 0/)).toBeInTheDocument();
  });

  it('renders admin columns when is_admin is true', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse(adminCatalogBody));

    render(<CatalogPage />);

    expect(await screen.findByText('Prototype ID')).toBeInTheDocument();
    expect(screen.getByText('core.weapon.knife')).toBeInTheDocument();
    expect(screen.getByText('0.5')).toBeInTheDocument();
    expect(screen.getByText('10')).toBeInTheDocument();
    expect(screen.getByText('min_damage')).toBeInTheDocument();
    expect(screen.getByText('max_damage')).toBeInTheDocument();
    expect(screen.getByText('catalog')).toBeInTheDocument();
    expect(screen.getByText('namespace')).toBeInTheDocument();
    expect(screen.getByText('melee, core')).toBeInTheDocument();
    expect(screen.queryByText(/\{"weapon"/)).not.toBeInTheDocument();
  });

  it('shows load error when API returns non-ok', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce(mockJsonResponse({}, false, 500));

    render(<CatalogPage />);

    expect(await screen.findByText('Failed to load item catalog.')).toBeInTheDocument();
  });

  it('applies filters and refetches page 1', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    const fetchMock = vi.spyOn(global, 'fetch').mockResolvedValue(mockJsonResponse(playerCatalogBody));

    render(<CatalogPage />);
    await screen.findByText('Knife');

    fireEvent.change(screen.getByPlaceholderText('weapon'), { target: { value: 'weapon' } });
    fireEvent.change(screen.getByPlaceholderText('core'), { target: { value: 'core' } });
    fireEvent.change(screen.getByPlaceholderText('knife'), { target: { value: 'knife' } });
    fireEvent.click(screen.getByRole('button', { name: 'Apply filters' }));

    await waitFor(() => {
      expect(fetchMock.mock.calls.length).toBeGreaterThanOrEqual(2);
    });
    const lastUrl = String(fetchMock.mock.calls.at(-1)?.[0] ?? '');
    expect(lastUrl).toContain('type=weapon');
    expect(lastUrl).toContain('namespace=core');
    expect(lastUrl).toContain('search=knife');
    expect(lastUrl).toContain('page=1');
  });
});
