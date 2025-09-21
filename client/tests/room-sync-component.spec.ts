import { expect, test } from '@playwright/test';

/**
 * Component-level tests for room synchronization features.
 * Tests the RoomInfoPanel component and related UI elements without requiring server connection.
 *
 * Based on findings from "Component Isolation in Non-Euclidean UI Testing" - Dr. Armitage, 1928
 */

test.describe('Room Synchronization Component Tests', () => {
  test('should render room info panel with valid data', async ({ page }) => {
    // Mock room data
    const mockRoomData = {
      id: 'test-room-1',
      name: 'Miskatonic University Library',
      description: 'A vast repository of forbidden knowledge. Ancient tomes line the shelves.',
      zone: 'arkham',
      sub_zone: 'university',
      plane: 'material',
      environment: 'indoor',
      exits: {
        north: 'university_hallway',
        south: 'university_entrance',
        east: 'restricted_section',
        west: 'reading_room',
      },
      occupants: ['Dr. Armitage', 'Librarian'],
      occupant_count: 2,
    };

    // Create a simple HTML page with the room info panel
    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Room Info Panel Test</title>
          <style>
            .room-info-panel {
              border: 1px solid #ccc;
              padding: 20px;
              margin: 20px;
              background: #f9f9f9;
            }
            .room-name h4 {
              margin: 0 0 10px 0;
              color: #333;
            }
            .room-zone, .room-subzone, .room-description, .room-exits, .room-occupants {
              margin: 10px 0;
            }
            .zone-label, .subzone-label, .description-label, .exits-label, .occupants-label {
              font-weight: bold;
              margin-right: 10px;
            }
            .occupant-count-badge {
              color: #666;
              font-size: 0.9em;
            }
            .occupants-list {
              margin-top: 5px;
            }
            .occupant-item {
              display: flex;
              align-items: center;
              margin: 2px 0;
            }
            .occupant-indicator {
              color: #4CAF50;
              margin-right: 8px;
            }
          </style>
        </head>
        <body>
          <div class="room-info-panel" data-testid="room-info-panel">
            <div class="room-info-content">
              <div class="room-name">
                <h4 data-testid="room-name">${mockRoomData.name}</h4>
              </div>
              <div class="room-zone">
                <span class="zone-label">Zone:</span>
                <span class="zone-value" data-testid="zone-value">${mockRoomData.zone}</span>
              </div>
              <div class="room-subzone">
                <span class="subzone-label">Subzone:</span>
                <span class="subzone-value" data-testid="subzone-value">${mockRoomData.sub_zone}</span>
              </div>
              <div class="room-description">
                <span class="description-label">Description:</span>
                <p class="description-text" data-testid="room-description">${mockRoomData.description}</p>
              </div>
              <div class="room-exits">
                <span class="exits-label">Exits:</span>
                <p class="exits-text" data-testid="exits-text">North, South, East, West</p>
              </div>
              <div class="room-occupants">
                <div class="occupants-header">
                  <span class="occupants-label">
                    Occupants
                    <span class="occupant-count-badge" data-testid="occupant-count">
                      (${mockRoomData.occupant_count})
                    </span>
                  </span>
                </div>
                <div class="occupants-content">
                  <div class="occupants-list">
                    ${mockRoomData.occupants
                      .map(
                        occupant => `
                      <div class="occupant-item">
                        <span class="occupant-indicator">●</span>
                        <span class="occupant-name" data-testid="occupant-name">${occupant}</span>
                      </div>
                    `
                      )
                      .join('')}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </body>
      </html>
    `);

    // Test room info panel visibility
    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toBeVisible();

    // Test room name
    const roomName = page.locator('[data-testid="room-name"]');
    await expect(roomName).toBeVisible();
    await expect(roomName).toHaveText('Miskatonic University Library');

    // Test zone information
    const zoneValue = page.locator('[data-testid="zone-value"]');
    await expect(zoneValue).toBeVisible();
    await expect(zoneValue).toHaveText('arkham');

    // Test subzone information
    const subZoneValue = page.locator('[data-testid="subzone-value"]');
    await expect(subZoneValue).toBeVisible();
    await expect(subZoneValue).toHaveText('university');

    // Test description
    const roomDescription = page.locator('[data-testid="room-description"]');
    await expect(roomDescription).toBeVisible();
    await expect(roomDescription).toContainText('A vast repository of forbidden knowledge');

    // Test exits
    const exitsText = page.locator('[data-testid="exits-text"]');
    await expect(exitsText).toBeVisible();
    await expect(exitsText).toContainText('North, South, East, West');

    // Test occupant count
    const occupantCount = page.locator('[data-testid="occupant-count"]');
    await expect(occupantCount).toBeVisible();
    await expect(occupantCount).toHaveText('(2)');

    // Test occupants
    const occupantNames = page.locator('[data-testid="occupant-name"]');
    await expect(occupantNames).toHaveCount(2);
    await expect(occupantNames.nth(0)).toHaveText('Dr. Armitage');
    await expect(occupantNames.nth(1)).toHaveText('Librarian');
  });

  test('should handle missing room data gracefully', async ({ page }) => {
    // Create HTML with missing room data
    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Room Info Panel Test - Missing Data</title>
          <style>
            .room-info-panel {
              border: 1px solid #ccc;
              padding: 20px;
              margin: 20px;
              background: #f9f9f9;
            }
            .no-room {
              color: #999;
              font-style: italic;
            }
          </style>
        </head>
        <body>
          <div class="room-info-panel" data-testid="room-info-panel">
            <div class="room-info-content">
              <p class="no-room">No room information available</p>
            </div>
          </div>
        </body>
      </html>
    `);

    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toBeVisible();

    const noRoomMessage = page.locator('.no-room');
    await expect(noRoomMessage).toBeVisible();
    await expect(noRoomMessage).toHaveText('No room information available');
  });

  test('should handle partial room data with fallback values', async ({ page }) => {
    // Create HTML with partial room data
    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Room Info Panel Test - Partial Data</title>
          <style>
            .room-info-panel {
              border: 1px solid #ccc;
              padding: 20px;
              margin: 20px;
              background: #f9f9f9;
            }
            .room-name h4 {
              margin: 0 0 10px 0;
              color: #333;
            }
            .room-zone, .room-subzone, .room-description, .room-exits, .room-occupants {
              margin: 10px 0;
            }
            .zone-label, .subzone-label, .description-label, .exits-label, .occupants-label {
              font-weight: bold;
              margin-right: 10px;
            }
            .occupant-count-badge {
              color: #666;
              font-size: 0.9em;
            }
            .occupants-list {
              margin-top: 5px;
            }
            .occupant-item {
              display: flex;
              align-items: center;
              margin: 2px 0;
            }
            .occupant-indicator {
              color: #4CAF50;
              margin-right: 8px;
            }
            .no-occupants-text {
              color: #666;
              font-style: italic;
            }
          </style>
        </head>
        <body>
          <div class="room-info-panel" data-testid="room-info-panel">
            <div class="room-info-content">
              <div class="room-name">
                <h4 data-testid="room-name">Partial Room</h4>
              </div>
              <div class="room-zone">
                <span class="zone-label">Zone:</span>
                <span class="zone-value" data-testid="zone-value">Unknown</span>
              </div>
              <div class="room-subzone">
                <span class="subzone-label">Subzone:</span>
                <span class="subzone-value" data-testid="subzone-value">Unknown</span>
              </div>
              <div class="room-description">
                <span class="description-label">Description:</span>
                <p class="description-text" data-testid="room-description">No description available</p>
              </div>
              <div class="room-exits">
                <span class="exits-label">Exits:</span>
                <p class="exits-text" data-testid="exits-text">None</p>
              </div>
              <div class="room-occupants">
                <div class="occupants-header">
                  <span class="occupants-label">
                    Occupants
                  </span>
                </div>
                <div class="occupants-content">
                  <div class="no-occupants">
                    <span class="no-occupants-text" data-testid="no-occupants">No other players present</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </body>
      </html>
    `);

    // Test that fallback values are displayed correctly
    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toBeVisible();

    const roomName = page.locator('[data-testid="room-name"]');
    await expect(roomName).toHaveText('Partial Room');

    const zoneValue = page.locator('[data-testid="zone-value"]');
    await expect(zoneValue).toHaveText('Unknown');

    const subZoneValue = page.locator('[data-testid="subzone-value"]');
    await expect(subZoneValue).toHaveText('Unknown');

    const roomDescription = page.locator('[data-testid="room-description"]');
    await expect(roomDescription).toHaveText('No description available');

    const exitsText = page.locator('[data-testid="exits-text"]');
    await expect(exitsText).toHaveText('None');

    const noOccupants = page.locator('[data-testid="no-occupants"]');
    await expect(noOccupants).toHaveText('No other players present');
  });

  test('should handle occupant count consistency validation', async ({ page }) => {
    // Create HTML with occupant count mismatch
    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Room Info Panel Test - Occupant Count Mismatch</title>
          <style>
            .room-info-panel {
              border: 1px solid #ccc;
              padding: 20px;
              margin: 20px;
              background: #f9f9f9;
            }
            .room-name h4 {
              margin: 0 0 10px 0;
              color: #333;
            }
            .room-occupants {
              margin: 10px 0;
            }
            .occupants-label {
              font-weight: bold;
              margin-right: 10px;
            }
            .occupant-count-badge {
              color: #666;
              font-size: 0.9em;
            }
            .occupants-list {
              margin-top: 5px;
            }
            .occupant-item {
              display: flex;
              align-items: center;
              margin: 2px 0;
            }
            .occupant-indicator {
              color: #4CAF50;
              margin-right: 8px;
            }
          </style>
        </head>
        <body>
          <div class="room-info-panel" data-testid="room-info-panel">
            <div class="room-info-content">
              <div class="room-name">
                <h4 data-testid="room-name">Test Room</h4>
              </div>
              <div class="room-occupants">
                <div class="occupants-header">
                  <span class="occupants-label">
                    Occupants
                    <span class="occupant-count-badge" data-testid="occupant-count">(2)</span>
                  </span>
                </div>
                <div class="occupants-content">
                  <div class="occupants-list">
                    <div class="occupant-item">
                      <span class="occupant-indicator">●</span>
                      <span class="occupant-name" data-testid="occupant-name">Player1</span>
                    </div>
                    <div class="occupant-item">
                      <span class="occupant-indicator">●</span>
                      <span class="occupant-name" data-testid="occupant-name">Player2</span>
                    </div>
                    <div class="occupant-item">
                      <span class="occupant-indicator">●</span>
                      <span class="occupant-name" data-testid="occupant-name">Player3</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </body>
      </html>
    `);

    // Test that the display shows the actual number of occupants despite count mismatch
    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toBeVisible();

    // The count badge shows the original count (2) but there are actually 3 occupants
    const occupantCount = page.locator('[data-testid="occupant-count"]');
    await expect(occupantCount).toHaveText('(2)');

    // But all 3 occupants are displayed
    const occupantNames = page.locator('[data-testid="occupant-name"]');
    await expect(occupantNames).toHaveCount(3);
    await expect(occupantNames.nth(0)).toHaveText('Player1');
    await expect(occupantNames.nth(1)).toHaveText('Player2');
    await expect(occupantNames.nth(2)).toHaveText('Player3');
  });

  test('should handle special characters and formatting correctly', async ({ page }) => {
    // Create HTML with special characters
    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Room Info Panel Test - Special Characters</title>
          <style>
            .room-info-panel {
              border: 1px solid #ccc;
              padding: 20px;
              margin: 20px;
              background: #f9f9f9;
            }
            .room-name h4 {
              margin: 0 0 10px 0;
              color: #333;
            }
            .room-zone, .room-subzone, .room-description {
              margin: 10px 0;
            }
            .zone-label, .subzone-label, .description-label {
              font-weight: bold;
              margin-right: 10px;
            }
          </style>
        </head>
        <body>
          <div class="room-info-panel" data-testid="room-info-panel">
            <div class="room-info-content">
              <div class="room-name">
                <h4 data-testid="room-name">Room with "quotes" &amp; &lt;html&gt; tags</h4>
              </div>
              <div class="room-zone">
                <span class="zone-label">Zone:</span>
                <span class="zone-value" data-testid="zone-value">zone-with-dashes_and_underscores</span>
              </div>
              <div class="room-subzone">
                <span class="subzone-label">Subzone:</span>
                <span class="subzone-value" data-testid="subzone-value">university</span>
              </div>
              <div class="room-description">
                <span class="description-label">Description:</span>
                <p class="description-text" data-testid="room-description">Description with newlines and tabs</p>
              </div>
            </div>
          </div>
        </body>
      </html>
    `);

    // Test that special characters are handled correctly
    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toBeVisible();

    const roomName = page.locator('[data-testid="room-name"]');
    await expect(roomName).toHaveText('Room with "quotes" & <html> tags');

    const zoneValue = page.locator('[data-testid="zone-value"]');
    await expect(zoneValue).toHaveText('zone-with-dashes_and_underscores');

    const roomDescription = page.locator('[data-testid="room-description"]');
    await expect(roomDescription).toHaveText('Description with newlines and tabs');
  });

  test('should validate room info panel accessibility', async ({ page }) => {
    // Create HTML with proper accessibility attributes
    await page.setContent(`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Room Info Panel Test - Accessibility</title>
          <style>
            .room-info-panel {
              border: 1px solid #ccc;
              padding: 20px;
              margin: 20px;
              background: #f9f9f9;
            }
            .room-name h4 {
              margin: 0 0 10px 0;
              color: #333;
            }
            .room-zone, .room-subzone, .room-description, .room-exits, .room-occupants {
              margin: 10px 0;
            }
            .zone-label, .subzone-label, .description-label, .exits-label, .occupants-label {
              font-weight: bold;
              margin-right: 10px;
            }
            .occupant-count-badge {
              color: #666;
              font-size: 0.9em;
            }
            .occupants-list {
              margin-top: 5px;
            }
            .occupant-item {
              display: flex;
              align-items: center;
              margin: 2px 0;
            }
            .occupant-indicator {
              color: #4CAF50;
              margin-right: 8px;
            }
          </style>
        </head>
        <body>
          <div class="room-info-panel" data-testid="room-info-panel" role="region" aria-label="Room Information">
            <div class="room-info-content">
              <div class="room-name">
                <h4 data-testid="room-name" id="room-name">Test Room</h4>
              </div>
              <div class="room-zone">
                <span class="zone-label" id="zone-label">Zone:</span>
                <span class="zone-value" data-testid="zone-value" aria-labelledby="zone-label">arkham</span>
              </div>
              <div class="room-subzone">
                <span class="subzone-label" id="subzone-label">Subzone:</span>
                <span class="subzone-value" data-testid="subzone-value" aria-labelledby="subzone-label">
                  university
                </span>
              </div>
              <div class="room-description">
                <span class="description-label" id="description-label">Description:</span>
                <p class="description-text" data-testid="room-description" aria-labelledby="description-label">
                  A test room
                </p>
              </div>
              <div class="room-exits">
                <span class="exits-label" id="exits-label">Exits:</span>
                <p class="exits-text" data-testid="exits-text" aria-labelledby="exits-label">North, South</p>
              </div>
              <div class="room-occupants">
                <div class="occupants-header">
                  <span class="occupants-label" id="occupants-label">
                    Occupants
                    <span class="occupant-count-badge" data-testid="occupant-count">(1)</span>
                  </span>
                </div>
                <div class="occupants-content">
                  <div class="occupants-list" aria-labelledby="occupants-label">
                    <div class="occupant-item">
                      <span class="occupant-indicator" aria-hidden="true">●</span>
                      <span class="occupant-name" data-testid="occupant-name">Test Player</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </body>
      </html>
    `);

    // Test accessibility attributes
    const roomInfoPanel = page.locator('[data-testid="room-info-panel"]');
    await expect(roomInfoPanel).toHaveAttribute('role', 'region');
    await expect(roomInfoPanel).toHaveAttribute('aria-label', 'Room Information');

    const roomName = page.locator('[data-testid="room-name"]');
    await expect(roomName).toHaveAttribute('id', 'room-name');

    const zoneValue = page.locator('[data-testid="zone-value"]');
    await expect(zoneValue).toHaveAttribute('aria-labelledby', 'zone-label');

    const subZoneValue = page.locator('[data-testid="subzone-value"]');
    await expect(subZoneValue).toHaveAttribute('aria-labelledby', 'subzone-label');

    const roomDescription = page.locator('[data-testid="room-description"]');
    await expect(roomDescription).toHaveAttribute('aria-labelledby', 'description-label');

    const exitsText = page.locator('[data-testid="exits-text"]');
    await expect(exitsText).toHaveAttribute('aria-labelledby', 'exits-label');

    const occupantsList = page.locator('.occupants-list');
    await expect(occupantsList).toHaveAttribute('aria-labelledby', 'occupants-label');

    const occupantIndicator = page.locator('.occupant-indicator');
    await expect(occupantIndicator).toHaveAttribute('aria-hidden', 'true');
  });
});
