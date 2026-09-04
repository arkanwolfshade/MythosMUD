/**
 * Tests for MapControls component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { MapControls } from '../MapControls';

describe('MapControls', () => {
  const defaultProps = {
    searchQuery: '',
    onSearchChange: vi.fn(),
    plane: 'earth',
    zone: 'arkhamcity',
    subZone: undefined,
    onPlaneChange: vi.fn(),
    onZoneChange: vi.fn(),
    onSubZoneChange: vi.fn(),
    availablePlanes: ['earth'],
    availableZones: ['arkhamcity'],
    availableSubZones: [],
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render search input', () => {
    render(<MapControls {...defaultProps} />);

    const searchInput = screen.getByPlaceholderText('Search rooms...');
    expect(searchInput).toBeInTheDocument();
    expect(searchInput).toHaveValue('');
  });

  it('should call onSearchChange when search input changes', () => {
    const onSearchChange = vi.fn();
    render(<MapControls {...defaultProps} onSearchChange={onSearchChange} />);

    const searchInput = screen.getByPlaceholderText('Search rooms...');
    fireEvent.change(searchInput, { target: { value: 'test query' } });

    expect(onSearchChange).toHaveBeenCalledWith('test query');
  });

  it('should display current search query', () => {
    render(<MapControls {...defaultProps} searchQuery="test search" />);

    const searchInput = screen.getByPlaceholderText('Search rooms...');
    expect(searchInput).toHaveValue('test search');
  });

  it('should render plane filter when multiple planes available', () => {
    render(<MapControls {...defaultProps} availablePlanes={['earth', 'dream']} />);

    const planeSelect = screen.getByDisplayValue('earth');
    expect(planeSelect).toBeInTheDocument();
  });

  it('should not render plane filter when only one plane available', () => {
    render(<MapControls {...defaultProps} availablePlanes={['earth']} />);

    // Plane filter should not be rendered when only one option
    const selects = screen.queryAllByRole('combobox');
    const planeSelect = selects.find(select => (select as HTMLSelectElement).value === 'earth');
    expect(planeSelect).toBeUndefined();
  });

  it('should call onPlaneChange when plane filter changes', () => {
    const onPlaneChange = vi.fn();
    render(<MapControls {...defaultProps} availablePlanes={['earth', 'dream']} onPlaneChange={onPlaneChange} />);

    const planeSelect = screen.getByDisplayValue('earth');
    fireEvent.change(planeSelect, { target: { value: 'dream' } });

    expect(onPlaneChange).toHaveBeenCalledWith('dream');
  });

  it('should render zone filter when multiple zones available', () => {
    render(<MapControls {...defaultProps} availableZones={['arkhamcity', 'innsmouth']} />);

    const zoneSelect = screen.getByDisplayValue('arkhamcity');
    expect(zoneSelect).toBeInTheDocument();
  });

  it('should not render zone filter when only one zone available', () => {
    render(<MapControls {...defaultProps} availableZones={['arkhamcity']} />);

    // Zone filter should not be rendered when only one option
    const selects = screen.queryAllByRole('combobox');
    const zoneSelect = selects.find(select => (select as HTMLSelectElement).value === 'arkhamcity');
    expect(zoneSelect).toBeUndefined();
  });

  it('should call onZoneChange when zone filter changes', () => {
    const onZoneChange = vi.fn();
    render(<MapControls {...defaultProps} availableZones={['arkhamcity', 'innsmouth']} onZoneChange={onZoneChange} />);

    const zoneSelect = screen.getByDisplayValue('arkhamcity');
    fireEvent.change(zoneSelect, { target: { value: 'innsmouth' } });

    expect(onZoneChange).toHaveBeenCalledWith('innsmouth');
  });

  it('should render sub-zone filter when sub-zones available', () => {
    render(<MapControls {...defaultProps} availableSubZones={['campus', 'downtown']} />);

    const subZoneSelect = screen.getByDisplayValue('All Sub-zones');
    expect(subZoneSelect).toBeInTheDocument();
  });

  it('should not render sub-zone filter when no sub-zones available', () => {
    render(<MapControls {...defaultProps} availableSubZones={[]} />);

    const subZoneSelect = screen.queryByDisplayValue('All Sub-zones');
    expect(subZoneSelect).not.toBeInTheDocument();
  });

  it('should display current sub-zone when selected', () => {
    render(<MapControls {...defaultProps} subZone="campus" availableSubZones={['campus', 'downtown']} />);

    const subZoneSelect = screen.getByDisplayValue('campus');
    expect(subZoneSelect).toBeInTheDocument();
  });

  it('should call onSubZoneChange when sub-zone filter changes', () => {
    const onSubZoneChange = vi.fn();
    render(
      <MapControls {...defaultProps} availableSubZones={['campus', 'downtown']} onSubZoneChange={onSubZoneChange} />
    );

    const subZoneSelect = screen.getByDisplayValue('All Sub-zones');
    fireEvent.change(subZoneSelect, { target: { value: 'campus' } });

    expect(onSubZoneChange).toHaveBeenCalledWith('campus');
  });

  it('should call onSubZoneChange with undefined when "All Sub-zones" is selected', () => {
    const onSubZoneChange = vi.fn();
    render(
      <MapControls
        {...defaultProps}
        subZone="campus"
        availableSubZones={['campus', 'downtown']}
        onSubZoneChange={onSubZoneChange}
      />
    );

    const subZoneSelect = screen.getByDisplayValue('campus');
    fireEvent.change(subZoneSelect, { target: { value: '' } });

    expect(onSubZoneChange).toHaveBeenCalledWith(undefined);
  });

  it('should render reset view button when onResetView is provided', () => {
    const onResetView = vi.fn();
    render(<MapControls {...defaultProps} onResetView={onResetView} />);

    const resetButton = screen.getByText('Reset View');
    expect(resetButton).toBeInTheDocument();
  });

  it('should not render reset view button when onResetView is not provided', () => {
    render(<MapControls {...defaultProps} />);

    expect(screen.queryByText('Reset View')).not.toBeInTheDocument();
  });

  it('should call onResetView when reset button is clicked', () => {
    const onResetView = vi.fn();
    render(<MapControls {...defaultProps} onResetView={onResetView} />);

    const resetButton = screen.getByText('Reset View');
    fireEvent.click(resetButton);

    expect(onResetView).toHaveBeenCalledTimes(1);
  });

  it('should render all filters when multiple options available', () => {
    render(
      <MapControls
        {...defaultProps}
        availablePlanes={['earth', 'dream']}
        availableZones={['arkhamcity', 'innsmouth']}
        availableSubZones={['campus', 'downtown']}
        subZone="campus"
      />
    );

    expect(screen.getByDisplayValue('earth')).toBeInTheDocument();
    expect(screen.getByDisplayValue('arkhamcity')).toBeInTheDocument();
    expect(screen.getByDisplayValue('campus')).toBeInTheDocument();
  });

  it('should handle empty string subZone as undefined', () => {
    const onSubZoneChange = vi.fn();
    render(
      <MapControls {...defaultProps} subZone="" availableSubZones={['campus']} onSubZoneChange={onSubZoneChange} />
    );

    const subZoneSelect = screen.getByDisplayValue('All Sub-zones');
    expect(subZoneSelect).toBeInTheDocument();
  });

  it('should handle subZone change to empty string', () => {
    const onSubZoneChange = vi.fn();
    render(
      <MapControls
        {...defaultProps}
        subZone="campus"
        availableSubZones={['campus', 'downtown']}
        onSubZoneChange={onSubZoneChange}
      />
    );

    const subZoneSelect = screen.getByDisplayValue('campus');
    fireEvent.change(subZoneSelect, { target: { value: '' } });

    // Should call with undefined when empty string is selected (line 104 branch)
    expect(onSubZoneChange).toHaveBeenCalledWith(undefined);
  });

  it('should handle plane filter with single option (not rendered)', () => {
    render(<MapControls {...defaultProps} availablePlanes={['earth']} />);

    // Plane filter should not render when only one option (line 71 branch: length > 1 is false)
    const selects = screen.queryAllByRole('combobox');
    const hasPlaneSelect = selects.some(select => {
      const options = Array.from((select as HTMLSelectElement).options);
      return options.some(opt => opt.value === 'earth' && opt.text === 'earth');
    });
    expect(hasPlaneSelect).toBe(false);
  });

  it('should handle zone filter with single option (not rendered)', () => {
    render(<MapControls {...defaultProps} availableZones={['arkhamcity']} />);

    // Zone filter should not render when only one option (line 86 branch: length > 1 is false)
    const selects = screen.queryAllByRole('combobox');
    const hasZoneSelect = selects.some(select => {
      const options = Array.from((select as HTMLSelectElement).options);
      return options.some(opt => opt.value === 'arkhamcity' && opt.text === 'arkhamcity');
    });
    expect(hasZoneSelect).toBe(false);
  });

  it('should handle subZone filter with empty array (not rendered)', () => {
    render(<MapControls {...defaultProps} availableSubZones={[]} />);

    // Sub-zone filter should not render when array is empty (line 101 branch: length > 0 is false)
    expect(screen.queryByDisplayValue('All Sub-zones')).not.toBeInTheDocument();
  });

  it('should handle all filters hidden when single options', () => {
    render(
      <MapControls
        {...defaultProps}
        availablePlanes={['earth']}
        availableZones={['arkhamcity']}
        availableSubZones={[]}
      />
    );

    // Only search input should be visible, no filters
    expect(screen.getByPlaceholderText('Search rooms...')).toBeInTheDocument();
    const selects = screen.queryAllByRole('combobox');
    expect(selects.length).toBe(0);
  });

  it('should handle subZone with undefined value', () => {
    render(<MapControls {...defaultProps} subZone={undefined} availableSubZones={['campus', 'downtown']} />);

    // Should show "All Sub-zones" when subZone is undefined (line 103: subZone || '')
    const subZoneSelect = screen.getByDisplayValue('All Sub-zones');
    expect(subZoneSelect).toBeInTheDocument();
  });
});
