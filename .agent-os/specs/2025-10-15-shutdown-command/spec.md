# Spec Requirements Document

> Spec: Admin Server Shutdown Command
> Created: 2025-10-15

## Overview

Implement an admin-only `/shutdown` command that gracefully shuts down the MythosMUD server with configurable countdown notifications to connected players. This feature enables administrators to perform planned maintenance and server restarts without data loss, providing clear communication to players about the impending shutdown.

## User Stories

### Server Administrator Planned Maintenance

As a server administrator, I want to gracefully shut down the server with advance notice to players, so that I can perform maintenance without disrupting gameplay or losing player data.

The admin issues `/shutdown 60` to initiate a 60-second countdown. All connected players receive periodic notifications via the Announcements channel (every 10 seconds above 10 seconds, then every second for the final 10 seconds). During the countdown, new players cannot log in. When the countdown reaches zero, the server persists all player data, despawns all NPCs, disconnects all players cleanly, shuts down services in proper order (NATS, WebSockets, background tasks), and exits gracefully. All shutdown actions are logged to the admin audit trail.

### Server Administrator Canceling Accidental Shutdown

As a server administrator, I want to cancel an accidental shutdown before it completes, so that I can prevent unnecessary disruption to players.

The admin accidentally issues `/shutdown 30` but immediately realizes the mistake. They issue `/shutdown cancel` within the countdown period. All players receive a notification that the scheduled shutdown has been cancelled, login restrictions are lifted, and normal gameplay resumes. The cancellation is logged to the admin audit trail.

### Non-Admin Player Attempting Shutdown

As a non-admin player, I should be prevented from using the `/shutdown` command, so that only authorized administrators can control server operations.

A regular player attempts to issue `/shutdown 10` or `/shutdown cancel`. The command is rejected with a thematic denial message indicating insufficient authorization. The rejection is not logged to avoid cluttering audit logs with routine permission denials.

## Spec Scope

1. **Shutdown Command** - Implement `/shutdown [seconds]` command with configurable countdown (default 10 seconds)
2. **Cancel Command** - Implement `/shutdown cancel` to abort ongoing shutdown countdown
3. **Player Notifications** - Send periodic countdown messages via Announcements channel with appropriate frequency
4. **Login Prevention** - Block new logins, MOTD progression, and character creation during countdown
5. **Graceful Shutdown Sequence** - Persist players, despawn NPCs, disconnect clients, stop services in correct order
6. **Admin Authorization** - Restrict command to players with `is_admin` flag set to true
7. **Audit Logging** - Log all shutdown/cancel actions via AdminActionsLogger

## Out of Scope

- Scheduling shutdowns for future times
- Different shutdown types (restart vs full shutdown)
- Configuring notification intervals
- Per-player shutdown notifications beyond Announcements channel
- Warning messages before countdown begins
- Shutdown reason parameters or additional flags
- Silent shutdowns without player notification
- Gradual feature degradation during countdown

## Expected Deliverable

1. Admin can execute `/shutdown 30` and observe countdown notifications at appropriate intervals (30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1) before server gracefully shuts down
2. Admin can execute `/shutdown cancel` during countdown and observe cancellation message followed by normal server operation
3. Non-admin player executing `/shutdown 10` receives thematic permission denial message
4. During shutdown countdown, new player login attempts are blocked with appropriate message
5. Admin actions log contains timestamped entries for shutdown initiations and cancellations with admin username
