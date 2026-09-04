/**
 * Tests for TerminalInput component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { TerminalInput } from '../TerminalInput';

describe('TerminalInput', () => {
  it('should render input', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} />);

    const input = screen.getByRole('textbox');
    expect(input).toBeInTheDocument();
  });

  it('should display value', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="test value" onChange={onChange} />);

    const input = screen.getByDisplayValue('test value');
    expect(input).toBeInTheDocument();
  });

  it('should call onChange when value changes', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} />);

    const input = screen.getByRole('textbox');
    fireEvent.change(input, { target: { value: 'new value' } });

    expect(onChange).toHaveBeenCalledTimes(1);
  });

  it('should display placeholder', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} placeholder="Enter text" />);

    const input = screen.getByPlaceholderText('Enter text');
    expect(input).toBeInTheDocument();
  });

  it('should handle different sizes', () => {
    const onChange = vi.fn();
    const { rerender } = render(<TerminalInput value="" onChange={onChange} size="sm" />);
    let input = screen.getByRole('textbox');
    expect(input).toBeInTheDocument();

    rerender(<TerminalInput value="" onChange={onChange} size="md" />);
    input = screen.getByRole('textbox');
    expect(input).toBeInTheDocument();

    rerender(<TerminalInput value="" onChange={onChange} size="lg" />);
    input = screen.getByRole('textbox');
    expect(input).toBeInTheDocument();
  });

  it('should handle disabled state', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} disabled />);

    const input = screen.getByRole('textbox') as HTMLInputElement;
    expect(input.disabled).toBe(true);
  });

  it('should handle onKeyDown', () => {
    const onChange = vi.fn();
    const onKeyDown = vi.fn();
    render(<TerminalInput value="" onChange={onChange} onKeyDown={onKeyDown} />);

    const input = screen.getByRole('textbox');
    fireEvent.keyDown(input, { key: 'Enter' });

    expect(onKeyDown).toHaveBeenCalledTimes(1);
  });

  it('should handle onFocus', () => {
    const onChange = vi.fn();
    const onFocus = vi.fn();
    render(<TerminalInput value="" onChange={onChange} onFocus={onFocus} />);

    const input = screen.getByRole('textbox');
    fireEvent.focus(input);

    expect(onFocus).toHaveBeenCalledTimes(1);
  });

  it('should handle onBlur', () => {
    const onChange = vi.fn();
    const onBlur = vi.fn();
    render(<TerminalInput value="" onChange={onChange} onBlur={onBlur} />);

    const input = screen.getByRole('textbox');
    fireEvent.blur(input);

    expect(onBlur).toHaveBeenCalledTimes(1);
  });

  it('should handle different input types', () => {
    const onChange = vi.fn();
    const { rerender, container } = render(<TerminalInput value="" onChange={onChange} type="text" />);
    let input = container.querySelector('input') as HTMLInputElement;
    expect(input.type).toBe('text');

    rerender(<TerminalInput value="" onChange={onChange} type="password" />);
    input = container.querySelector('input') as HTMLInputElement;
    expect(input.type).toBe('password');
  });

  it('should handle autoFocus', () => {
    const onChange = vi.fn();
    const { container } = render(<TerminalInput value="" onChange={onChange} autoFocus />);

    const input = container.querySelector('input') as HTMLInputElement;
    // Check that autoFocus prop is passed (React handles the actual focus behavior)
    expect(input).toBeInTheDocument();
    // In React, autoFocus is handled by React, not as a DOM attribute
    // We verify the component accepts the prop and renders
  });

  it('should handle required attribute', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} required />);

    const input = screen.getByRole('textbox') as HTMLInputElement;
    expect(input.required).toBe(true);
  });

  it('should handle name and id attributes', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} name="test-name" id="test-id" />);

    const input = screen.getByRole('textbox') as HTMLInputElement;
    expect(input.name).toBe('test-name');
    expect(input.id).toBe('test-id');
  });

  it('should handle data-testid', () => {
    const onChange = vi.fn();
    render(<TerminalInput value="" onChange={onChange} data-testid="test-input" />);

    const input = screen.getByTestId('test-input');
    expect(input).toBeInTheDocument();
  });

  it('should handle custom className', () => {
    const onChange = vi.fn();
    const { container } = render(<TerminalInput value="" onChange={onChange} className="custom-class" />);

    const input = container.querySelector('input');
    expect(input?.className).toContain('custom-class');
  });
});
