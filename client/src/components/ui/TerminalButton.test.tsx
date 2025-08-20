import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { TerminalButton } from './TerminalButton';

describe('TerminalButton', () => {
  it('should render with default props', () => {
    render(<TerminalButton>Click me</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Click me' });
    expect(button).toBeInTheDocument();
    expect(button).toHaveClass(
      'bg-mythos-terminal-surface',
      'border-mythos-terminal-primary',
      'text-mythos-terminal-primary'
    );
  });

  it('should render with custom variant', () => {
    render(<TerminalButton variant="danger">Delete</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Delete' });
    expect(button).toHaveClass(
      'bg-mythos-terminal-surface',
      'border-mythos-terminal-error',
      'text-mythos-terminal-error'
    );
  });

  it('should render with warning variant', () => {
    render(<TerminalButton variant="warning">Warning</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Warning' });
    expect(button).toHaveClass(
      'bg-mythos-terminal-surface',
      'border-mythos-terminal-warning',
      'text-mythos-terminal-warning'
    );
  });

  it('should render with success variant', () => {
    render(<TerminalButton variant="success">Success</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Success' });
    expect(button).toHaveClass(
      'bg-mythos-terminal-surface',
      'border-mythos-terminal-success',
      'text-mythos-terminal-success'
    );
  });

  it('should render with secondary variant', () => {
    render(<TerminalButton variant="secondary">Secondary</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Secondary' });
    expect(button).toHaveClass('bg-mythos-terminal-surface', 'border-mythos-terminal-secondary');
  });

  it('should handle click events', () => {
    const handleClick = vi.fn();
    render(<TerminalButton onClick={handleClick}>Click me</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Click me' });
    fireEvent.click(button);

    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('should be disabled when disabled prop is true', () => {
    render(<TerminalButton disabled>Disabled</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Disabled' });
    expect(button).toBeDisabled();
    expect(button).toHaveClass('opacity-50', 'cursor-not-allowed');
  });

  it('should not call onClick when disabled', () => {
    const handleClick = vi.fn();
    render(
      <TerminalButton disabled onClick={handleClick}>
        Disabled
      </TerminalButton>
    );

    const button = screen.getByRole('button', { name: 'Disabled' });
    fireEvent.click(button);

    expect(handleClick).not.toHaveBeenCalled();
  });

  it('should apply custom className', () => {
    render(<TerminalButton className="custom-class">Custom</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Custom' });
    expect(button).toHaveClass('custom-class');
  });

  it('should render with different sizes', () => {
    const { rerender } = render(<TerminalButton size="sm">Small</TerminalButton>);
    expect(screen.getByRole('button')).toHaveClass('px-3', 'py-1', 'text-sm');

    rerender(<TerminalButton size="lg">Large</TerminalButton>);
    expect(screen.getByRole('button')).toHaveClass('px-6', 'py-3', 'text-lg');
  });

  it('should have proper base styling classes', () => {
    render(<TerminalButton>Styled</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Styled' });
    expect(button).toHaveClass(
      'font-mono',
      'border',
      'rounded',
      'transition-eldritch',
      'focus:outline-none',
      'focus:ring-2'
    );
  });

  it('should handle type prop', () => {
    render(<TerminalButton type="submit">Submit</TerminalButton>);

    const button = screen.getByRole('button', { name: 'Submit' });
    expect(button).toHaveAttribute('type', 'submit');
  });
});
