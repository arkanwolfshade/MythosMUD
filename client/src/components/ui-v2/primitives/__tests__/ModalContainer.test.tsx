/**
 * Tests for ModalContainer component.
 */

import { fireEvent, render, screen, within } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ModalContainer } from '../ModalContainer';

describe('ModalContainer', () => {
  it('should render nothing when closed', () => {
    const onClose = vi.fn();
    const { container } = render(
      <ModalContainer isOpen={false} onClose={onClose}>
        Content
      </ModalContainer>
    );

    expect(container).toBeEmptyDOMElement();
  });

  it('should render children when open', () => {
    const onClose = vi.fn();
    render(
      <ModalContainer isOpen onClose={onClose}>
        <div data-testid="modal-body">Modal content</div>
      </ModalContainer>
    );

    expect(screen.getByTestId('modal-body')).toBeInTheDocument();
  });

  it('should render the title when provided', () => {
    const onClose = vi.fn();
    render(
      <ModalContainer isOpen onClose={onClose} title="Settings">
        Content
      </ModalContainer>
    );

    expect(screen.getByText('Settings')).toBeInTheDocument();
  });

  it('should call onClose when the close button is clicked', () => {
    const onClose = vi.fn();
    render(
      <ModalContainer isOpen onClose={onClose} showCloseButton>
        Content
      </ModalContainer>
    );

    const dialog = screen.getByRole('dialog');
    fireEvent.click(within(dialog).getByLabelText('Close modal'));

    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should call onClose when the Escape key is pressed', () => {
    const onClose = vi.fn();
    render(
      <ModalContainer isOpen onClose={onClose}>
        Content
      </ModalContainer>
    );

    fireEvent.keyDown(document, { key: 'Escape' });

    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should not call onClose on Escape when closed', () => {
    const onClose = vi.fn();
    render(
      <ModalContainer isOpen={false} onClose={onClose}>
        Content
      </ModalContainer>
    );

    fireEvent.keyDown(document, { key: 'Escape' });

    expect(onClose).not.toHaveBeenCalled();
  });

  it('should render a dialog role with aria-modal for the default center position', () => {
    const onClose = vi.fn();
    render(
      <ModalContainer isOpen onClose={onClose} title="Dialog title">
        Content
      </ModalContainer>
    );

    const dialog = screen.getByRole('dialog');
    expect(dialog).toHaveAttribute('aria-modal', 'true');
  });

  it('should render the bottom-right floating shell for position="bottom-right"', () => {
    const onClose = vi.fn();
    const { container } = render(
      <ModalContainer isOpen onClose={onClose} position="bottom-right">
        Content
      </ModalContainer>
    );

    expect(container.querySelector('.fixed.bottom-4.right-4')).not.toBeNull();
  });
});
