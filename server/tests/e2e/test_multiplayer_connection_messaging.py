"""
End-to-End tests for multiplayer connection messaging.

This test suite uses browser automation to verify that players can see
each other's connection and disconnection messages in real-time.

REQUIRES: Backend server on port 54731, frontend server on port 5173
Run with: pytest -m e2e
"""

import asyncio
import os
import time

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright

# Mark as slow E2E test - requires running servers
pytestmark = [
    pytest.mark.slow,
    pytest.mark.e2e,
    pytest.mark.skip(reason="E2E tests require running servers. Run with: pytest -m e2e --runxfail")
]


@pytest_asyncio.fixture(scope="function")
async def browser_setup():
    """Set up browser for testing."""
    print("\n[E2E] Starting Playwright...")
    playwright = await async_playwright().start()
    # Run headless in CI environment or when no display is available
    headless = os.getenv("CI") == "true" or os.getenv("DISPLAY") is None
    print(f"[E2E] Launching browser (headless={headless})...")
    browser = await playwright.chromium.launch(
        headless=headless,
        args=["--no-sandbox", "--disable-setuid-sandbox"],
        timeout=30000,  # 30 second timeout
    )
    print("[E2E] Browser launched successfully")
    yield browser
    print("[E2E] Closing browser...")
    await browser.close()
    await playwright.stop()
    print("[E2E] Playwright stopped")


@pytest_asyncio.fixture
async def player_contexts(browser_setup):
    """Create two player browser contexts."""
    print("[FIXTURE] Creating player contexts...")
    contexts = []
    for i in range(2):
        print(f"[FIXTURE] Creating context {i + 1}...")
        context = await browser_setup.new_context()
        print(f"[FIXTURE] Creating page {i + 1}...")
        page = await context.new_page()
        contexts.append((context, page))
    print("[FIXTURE] Player contexts created successfully")
    yield contexts
    # Cleanup
    print("[FIXTURE] Cleaning up player contexts...")
    for context, _page in contexts:
        await context.close()
    print("[FIXTURE] Player contexts cleaned up")


async def login_and_dismiss_motd(page, username: str, password: str, player_label: str):
    """Helper function to login a player and dismiss the MOTD."""
    print(f"[HELPER] Logging in {player_label}...")
    await page.fill('input[placeholder="Username"]', username)
    await page.fill('input[placeholder="Password"]', password)
    await page.click('button:has-text("Enter the Void")')
    # Wait for MOTD to appear
    await page.wait_for_selector('button:has-text("Continue")', timeout=15000)
    print(f"[HELPER] {player_label} MOTD displayed - dismissing...")
    await page.click('button:has-text("Continue")')
    # Wait for game terminal to be visible
    await page.wait_for_selector(".game-terminal-container", timeout=5000)
    print(f"[HELPER] {player_label} successfully in game")


class TestE2EMultiplayerConnectionMessaging:
    """End-to-End tests for multiplayer connection messaging."""

    @pytest.mark.asyncio
    @pytest.mark.e2e
    # @pytest.mark.skip(reason="E2E test requires running client and server - not suitable for CI")
    async def test_two_players_see_connection_messages(self, player_contexts):
        """Test that two players can see each other's connection messages."""
        print("\n[TEST] Starting test_two_players_see_connection_messages")
        # Get player contexts from fixture
        player1_context, player1_page = player_contexts[0]
        player2_context, player2_page = player_contexts[1]
        print("[TEST] Got player contexts from fixture")

        # Navigate both players to the game
        print("[TEST] Navigating Player 1 to http://localhost:5173...")
        await player1_page.goto("http://localhost:5173", timeout=10000)
        print("[TEST] Player 1 navigation complete")
        print("[TEST] Navigating Player 2 to http://localhost:5173...")
        await player2_page.goto("http://localhost:5173", timeout=10000)
        print("[TEST] Player 2 navigation complete")

        # Wait for pages to load
        print("[TEST] Waiting for network idle...")
        await player1_page.wait_for_load_state("networkidle", timeout=10000)
        await player2_page.wait_for_load_state("networkidle", timeout=10000)
        print("[TEST] Pages loaded")

        # Login both players (using documented E2E test credentials)
        await login_and_dismiss_motd(player1_page, "ArkanWolfshade", "Cthulhu1", "Player 1")
        await login_and_dismiss_motd(player2_page, "Ithaqua", "Cthulhu1", "Player 2")

        # Wait a moment for both players to be connected
        print("[TEST] Waiting for players to fully connect...")
        await asyncio.sleep(5)

        # Check that both players are in the same room initially
        # (This assumes the default starting room behavior)

        # Debug: Get all text content from player1's page to see what messages exist
        print("[TEST] Dumping Player 1 page content for debugging...")
        page_content = await player1_page.content()
        print(f"[TEST] Player 1 page length: {len(page_content)} characters")

        # Try to find message items
        message_items = await player1_page.query_selector_all(".message-item")
        print(f"[TEST] Found {len(message_items)} message items")
        if message_items:
            for i, item in enumerate(message_items[:5]):  # Show first 5
                text = await item.text_content()
                print(f"[TEST] Message {i + 1}: {text[:100] if text else 'None'}")
        else:
            print("[TEST] No message items found")
            # Take screenshot for debugging
            await player1_page.screenshot(path="test_after_motd_no_messages.png")

        # Verify Player 1 (who was already in the room) can see Player 2's connection
        # Look for a message containing "Ithaqua enters the room" (using partial text match)
        player2_entered_message = await player1_page.wait_for_selector("text=/Ithaqua enters the room/", timeout=10000)
        assert player2_entered_message is not None, "ArkanWolfshade should see Ithaqua's connection message"
        print("[TEST] ✅ Player 1 sees Player 2's entrance message")

        # Note: Player 2 won't see Player 1's entrance message because Player 1 was already
        # in the room when Player 2 arrived. This is correct multiplayer behavior.
        # Player 2 should see their own entrance confirmation message instead
        print("[TEST] ✅ Test completed successfully!")

    @pytest.mark.asyncio
    @pytest.mark.e2e
    # @pytest.mark.skip(reason="E2E test requires running client and server - not suitable for CI")
    async def test_player_disconnection_message(self, player_contexts):
        """Test that players see disconnection messages when someone leaves."""
        # Get player contexts from fixture
        player1_context, player1_page = player_contexts[0]
        player2_context, player2_page = player_contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173", timeout=10000)
        await player2_page.goto("http://localhost:5173", timeout=10000)

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle", timeout=10000)
        await player2_page.wait_for_load_state("networkidle", timeout=10000)

        # Login both players
        await login_and_dismiss_motd(player1_page, "ArkanWolfshade", "Cthulhu1", "Player 1")
        await login_and_dismiss_motd(player2_page, "Ithaqua", "Cthulhu1", "Player 2")

        # Wait for both players to be connected and see each other
        await asyncio.sleep(3)

        # Disconnect Player 2 by clicking logout
        logout_button = await player2_page.wait_for_selector('[data-testid="logout-button"]', timeout=5000)
        await logout_button.click()

        # Wait for disconnection
        await asyncio.sleep(2)

        # Verify Player 1 sees Player 2's disconnection message
        player2_left_message = await player1_page.wait_for_selector("text=/Ithaqua leaves the room/", timeout=10000)
        assert player2_left_message is not None, "ArkanWolfshade should see Ithaqua's disconnection message"

    @pytest.mark.asyncio
    @pytest.mark.e2e
    # @pytest.mark.skip(reason="E2E test requires running client and server - not suitable for CI")
    async def test_room_occupant_count_updates(self, player_contexts):
        """Test that room occupant counts update correctly."""
        # Get player contexts from fixture
        player1_context, player1_page = player_contexts[0]
        player2_context, player2_page = player_contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173", timeout=10000)
        await player2_page.goto("http://localhost:5173", timeout=10000)

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle", timeout=10000)
        await player2_page.wait_for_load_state("networkidle", timeout=10000)

        # Login Player 1 first
        await login_and_dismiss_motd(player1_page, "ArkanWolfshade", "Cthulhu1", "Player 1")

        # Check initial occupant count
        # Note: May include NPCs or other entities in the room
        await asyncio.sleep(1)
        occupant_count_1 = await player1_page.text_content('[data-testid="occupant-count"]')
        initial_count = int(occupant_count_1.strip("()"))
        print(f"[TEST] Initial occupant count: {initial_count}")
        assert initial_count >= 1, f"Occupant count should be at least 1 (the player), got: {occupant_count_1}"

        # Login Player 2
        await login_and_dismiss_motd(player2_page, "Ithaqua", "Cthulhu1", "Player 2")

        # Wait for both players to be connected
        await asyncio.sleep(2)

        # Check updated occupant count (should increase by 1)
        occupant_count_2 = await player1_page.text_content('[data-testid="occupant-count"]')
        final_count = int(occupant_count_2.strip("()"))
        print(f"[TEST] Occupant count after Player 2 joins: {final_count}")
        assert final_count == initial_count + 1, (
            f"Occupant count should increase by 1 (was {initial_count}, now {final_count})"
        )

        # Disconnect Player 2
        logout_button = await player2_page.wait_for_selector('[data-testid="logout-button"]', timeout=5000)
        await logout_button.click()
        await asyncio.sleep(2)

        # Check final occupant count (should decrease by 1)
        occupant_count_3 = await player1_page.text_content('[data-testid="occupant-count"]')
        logout_count = int(occupant_count_3.strip("()"))
        print(f"[TEST] Occupant count after Player 2 logout: {logout_count}")
        assert logout_count == initial_count, (
            f"Occupant count should return to initial ({initial_count}), got: {logout_count}"
        )

    @pytest.mark.asyncio
    @pytest.mark.e2e
    # @pytest.mark.skip(reason="E2E test requires running client and server - not suitable for CI")
    async def test_multiple_players_connection_messages(self, browser_setup):
        """Test connection messages with 2 players (max available test accounts)."""
        # Create 2 player contexts (limited by available test accounts)
        contexts = []
        pages = []
        for _i in range(2):
            context = await browser_setup.new_context()
            page = await context.new_page()
            contexts.append(context)
            pages.append(page)

        try:
            # Navigate all players to the game
            for page in pages:
                await page.goto("http://localhost:5173")
                await page.wait_for_load_state("networkidle")

            # Login all players (using documented E2E test credentials)
            test_users = ["ArkanWolfshade", "Ithaqua"]
            for i, page in enumerate(pages):
                player_id = test_users[i]
                await login_and_dismiss_motd(page, player_id, "Cthulhu1", f"Player {i + 1}")
                await asyncio.sleep(1)  # Stagger connections

            # Wait for all connections to stabilize
            await asyncio.sleep(3)

            # Check that the first player sees the second player's connection message
            # (Second player won't see first player's message since they arrived later)
            connection_message = await pages[0].wait_for_selector(
                f"text=/{test_users[1]} enters the room/", timeout=5000
            )
            assert connection_message is not None, f"{test_users[0]} should see {test_users[1]}'s connection"

            # Verify occupant count includes both players (may also include NPCs/other entities)
            occupant_count = await pages[0].text_content('[data-testid="occupant-count"]')
            count = int(occupant_count.strip("()"))
            assert count >= 2, f"Occupant count should be at least 2 (both players), got: {occupant_count}"

        finally:
            # Cleanup
            for context in contexts:
                await context.close()

    @pytest.mark.asyncio
    @pytest.mark.e2e
    # @pytest.mark.skip(reason="E2E test requires running client and server - not suitable for CI")
    async def test_connection_message_timing(self, player_contexts):
        """Test that connection messages appear in reasonable time."""
        # Get player contexts from fixture
        player1_context, player1_page = player_contexts[0]
        player2_context, player2_page = player_contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173", timeout=10000)
        await player2_page.goto("http://localhost:5173", timeout=10000)

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle", timeout=10000)
        await player2_page.wait_for_load_state("networkidle", timeout=10000)

        # Login Player 1
        await login_and_dismiss_motd(player1_page, "ArkanWolfshade", "Cthulhu1", "Player 1")

        # Record time when Player 2 starts connecting
        start_time = time.time()

        # Login Player 2
        await login_and_dismiss_motd(player2_page, "Ithaqua", "Cthulhu1", "Player 2")

        # Wait for connection message to appear
        await player1_page.wait_for_selector("text=/Ithaqua enters the room/", timeout=10000)

        # Record time when message appears
        end_time = time.time()

        # Verify message appeared within reasonable time (less than 5 seconds)
        message_delay = end_time - start_time
        assert message_delay < 5.0, f"Connection message took too long: {message_delay:.2f} seconds"
        assert message_delay > 0.1, f"Connection message appeared too quickly: {message_delay:.2f} seconds"
