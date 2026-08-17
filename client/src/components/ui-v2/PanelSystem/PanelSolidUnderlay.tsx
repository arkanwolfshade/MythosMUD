/** Opaque fill behind panel chrome so backdrop art does not show through the face. */
export function PanelSolidUnderlay() {
  return (
    <div
      style={{
        position: 'absolute',
        inset: 0,
        backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
        zIndex: 0,
        pointerEvents: 'none',
        borderRadius: 'inherit',
      }}
      aria-hidden
    />
  );
}
