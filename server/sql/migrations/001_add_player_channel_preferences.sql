-- Migration 001: Add player_channel_preferences table
-- Date: 2025-08-27
-- Description: Add table for storing player channel preferences for Advanced Chat Channels feature
-- Create player_channel_preferences table
CREATE TABLE IF NOT EXISTS player_channel_preferences (
    player_id TEXT PRIMARY KEY NOT NULL,
    default_channel TEXT NOT NULL DEFAULT 'local',
    muted_channels TEXT NOT NULL DEFAULT '[]',
    -- JSON array of muted channel names
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);
-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_player_channel_preferences_player_id ON player_channel_preferences(player_id);
CREATE INDEX IF NOT EXISTS idx_player_channel_preferences_default_channel ON player_channel_preferences(default_channel);
-- Create trigger to automatically update updated_at timestamp
CREATE TRIGGER IF NOT EXISTS update_player_channel_preferences_updated_at
AFTER
UPDATE ON player_channel_preferences FOR EACH ROW BEGIN
UPDATE player_channel_preferences
SET updated_at = CURRENT_TIMESTAMP
WHERE player_id = NEW.player_id;
END;
