# Spec Summary (Lite)

Implement an admin-only `/shutdown` command that gracefully shuts down the MythosMUD server with configurable countdown notifications to connected players. The command provides countdown notifications via the Announcements channel, blocks new logins during countdown, and executes a proper shutdown sequence (persist players, despawn NPCs, disconnect clients, stop services) while logging all actions to the admin audit trail. Administrators can cancel ongoing shutdowns with `/shutdown cancel`.
