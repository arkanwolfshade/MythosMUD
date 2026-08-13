/**
 * Death-void detection from UI body text.
 * Location panel is authoritative; Game Info can retain stale void or foyer dumps.
 */
export function locationIndicatesDeathVoid(bodyText: string): boolean {
  const loc = bodyText.match(/Location\s*\n\s*([^\n]+)/i);
  if (!loc?.[1]) {
    return false;
  }
  return /Death\s*>\s*Void/i.test(loc[1].trim());
}

/** Error when a helper required a living player and found Death > Void. */
export function requiredAliveButDeadMessage(username: string): string {
  return (
    `Player ${username} is dead (Death > Void) but this step requires a living player. ` +
    `Either this test killed them and did not respawn, or the previous test did not clean up.`
  );
}
