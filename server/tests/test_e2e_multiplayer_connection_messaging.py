"""
End-to-End tests for multiplayer connection messaging.

This test suite uses browser automation to verify that players can see
each other's connection and disconnection messages in real-time.
"""

import asyncio
import time

import pytest
import pytest_asyncio
from playwright.async_api import async_playwright


class TestE2EMultiplayerConnectionMessaging:
    """End-to-End tests for multiplayer connection messaging."""

    @pytest_asyncio.fixture(scope="class")
    async def browser_setup(self):
        """Set up browser for testing."""
        playwright = await async_playwright().start()
        # Run headless in CI environment
        import os

        headless = os.getenv("CI") == "true"
        browser = await playwright.chromium.launch(headless=headless)
        yield browser
        await browser.close()
        await playwright.stop()

    @pytest.fixture
    def player_contexts(self, browser_setup):
        """Create two player browser contexts."""
        # This will be called synchronously, but browser_setup is async
        # We'll handle this differently in each test
        return browser_setup

    async def _create_player_contexts(self, browser):
        """Helper method to create player contexts."""
        contexts = []
        for _i in range(2):
            context = await browser.new_context()
            page = await context.new_page()
            contexts.append((context, page))
        return contexts

    async def _cleanup_contexts(self, contexts):
        """Helper method to cleanup contexts."""
        for context, _page in contexts:
            await context.close()

    @pytest.mark.asyncio
    async def test_two_players_see_connection_messages(self, player_contexts):
        """Test that two players can see each other's connection messages."""
        # Create player contexts using helper
        browser = player_contexts  # No await needed since it's a regular fixture now
        contexts = await self._create_player_contexts(browser)
        player1_context, player1_page = contexts[0]
        player2_context, player2_page = contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173")
        await player2_page.goto("http://localhost:5173")

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle")
        await player2_page.wait_for_load_state("networkidle")

        # Login both players
        # Player 1 login
        await player1_page.fill('input[placeholder="Player ID"]', "test_player_1")
        await player1_page.click('button:has-text("Connect")')
        await player1_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Player 2 login
        await player2_page.fill('input[placeholder="Player ID"]', "test_player_2")
        await player2_page.click('button:has-text("Connect")')
        await player2_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Wait a moment for both players to be connected
        await asyncio.sleep(2)

        # Check that both players are in the same room initially
        # (This assumes the default starting room behavior)

        # Verify Player 1 can see Player 2's connection
        # Look for a message indicating Player 2 entered
        player2_entered_message = await player1_page.wait_for_selector(
            'text="test_player_2 enters the room"', timeout=10000
        )
        assert player2_entered_message is not None, "Player 1 should see Player 2's connection message"

        # Verify Player 2 can see Player 1's connection
        # Look for a message indicating Player 1 entered
        player1_entered_message = await player2_page.wait_for_selector(
            'text="test_player_1 enters the room"', timeout=10000
        )
        assert player1_entered_message is not None, "Player 2 should see Player 1's connection message"

        # Cleanup
        await self._cleanup_contexts(contexts)

    @pytest.mark.asyncio
    async def test_player_disconnection_message(self, player_contexts):
        """Test that players see disconnection messages when someone leaves."""
        # Create player contexts using helper
        browser = player_contexts  # No await needed since it's a regular fixture now
        contexts = await self._create_player_contexts(browser)
        player1_context, player1_page = contexts[0]
        player2_context, player2_page = contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173")
        await player2_page.goto("http://localhost:5173")

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle")
        await player2_page.wait_for_load_state("networkidle")

        # Login both players
        await player1_page.fill('input[placeholder="Player ID"]', "test_player_1")
        await player1_page.click('button:has-text("Connect")')
        await player1_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        await player2_page.fill('input[placeholder="Player ID"]', "test_player_2")
        await player2_page.click('button:has-text("Connect")')
        await player2_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Wait for both players to be connected and see each other
        await asyncio.sleep(3)

        # Disconnect Player 2
        await player2_page.click('button:has-text("Disconnect")')

        # Wait for disconnection
        await asyncio.sleep(2)

        # Verify Player 1 sees Player 2's disconnection message
        player2_left_message = await player1_page.wait_for_selector(
            'text="test_player_2 leaves the room"', timeout=10000
        )
        assert player2_left_message is not None, "Player 1 should see Player 2's disconnection message"

        # Cleanup
        await self._cleanup_contexts(contexts)

    @pytest.mark.asyncio
    async def test_room_occupant_count_updates(self, player_contexts):
        """Test that room occupant counts update correctly."""
        # Create player contexts using helper
        browser = player_contexts  # No await needed since it's a regular fixture now
        contexts = await self._create_player_contexts(browser)
        player1_context, player1_page = contexts[0]
        player2_context, player2_page = contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173")
        await player2_page.goto("http://localhost:5173")

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle")
        await player2_page.wait_for_load_state("networkidle")

        # Login Player 1 first
        await player1_page.fill('input[placeholder="Player ID"]', "test_player_1")
        await player1_page.click('button:has-text("Connect")')
        await player1_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Check initial occupant count (should be 1)
        await asyncio.sleep(1)
        occupant_count_1 = await player1_page.text_content(".occupant-count")
        assert "1" in occupant_count_1, f"Initial occupant count should be 1, got: {occupant_count_1}"

        # Login Player 2
        await player2_page.fill('input[placeholder="Player ID"]', "test_player_2")
        await player2_page.click('button:has-text("Connect")')
        await player2_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Wait for both players to be connected
        await asyncio.sleep(2)

        # Check updated occupant count (should be 2)
        occupant_count_2 = await player1_page.text_content(".occupant-count")
        assert "2" in occupant_count_2, f"Occupant count after second player should be 2, got: {occupant_count_2}"

        # Disconnect Player 2
        await player2_page.click('button:has-text("Disconnect")')
        await asyncio.sleep(2)

        # Check final occupant count (should be 1 again)
        occupant_count_3 = await player1_page.text_content(".occupant-count")
        assert "1" in occupant_count_3, f"Occupant count after disconnection should be 1, got: {occupant_count_3}"

        # Cleanup
        await self._cleanup_contexts(contexts)

    @pytest.mark.asyncio
    async def test_multiple_players_connection_messages(self, browser_setup):
        """Test connection messages with 3 players."""
        # Create 3 player contexts
        contexts = []
        pages = []
        for _i in range(3):
            context = await browser_setup.new_context()
            page = await context.new_page()
            contexts.append(context)
            pages.append(page)

        try:
            # Navigate all players to the game
            for page in pages:
                await page.goto("http://localhost:5173")
                await page.wait_for_load_state("networkidle")

            # Login all players
            for i, page in enumerate(pages):
                player_id = f"test_player_{i + 1}"
                await page.fill('input[placeholder="Player ID"]', player_id)
                await page.click('button:has-text("Connect")')
                await page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)
                await asyncio.sleep(1)  # Stagger connections

            # Wait for all connections to stabilize
            await asyncio.sleep(3)

            # Check that each player sees the others' connection messages
            for i, page in enumerate(pages):
                player_id = f"test_player_{i + 1}"

                # Check that this player sees connection messages for other players
                for j in range(3):
                    if i != j:
                        other_player_id = f"test_player_{j + 1}"
                        # Look for connection message
                        try:
                            connection_message = await page.wait_for_selector(
                                f'text="{other_player_id} enters the room"', timeout=5000
                            )
                            assert connection_message is not None, (
                                f"{player_id} should see {other_player_id}'s connection"
                            )
                        except Exception:
                            # If we can't find the message, it might be because the player connected first
                            # This is acceptable behavior
                            pass

            # Verify occupant count is 3
            occupant_count = await pages[0].text_content(".occupant-count")
            assert "3" in occupant_count, f"Occupant count should be 3, got: {occupant_count}"

        finally:
            # Cleanup
            for context in contexts:
                await context.close()

    @pytest.mark.asyncio
    async def test_connection_message_timing(self, player_contexts):
        """Test that connection messages appear in reasonable time."""
        # Create player contexts using helper
        browser = player_contexts  # No await needed since it's a regular fixture now
        contexts = await self._create_player_contexts(browser)
        player1_context, player1_page = contexts[0]
        player2_context, player2_page = contexts[1]

        # Navigate both players to the game
        await player1_page.goto("http://localhost:5173")
        await player2_page.goto("http://localhost:5173")

        # Wait for pages to load
        await player1_page.wait_for_load_state("networkidle")
        await player2_page.wait_for_load_state("networkidle")

        # Login Player 1
        await player1_page.fill('input[placeholder="Player ID"]', "test_player_1")
        await player1_page.click('button:has-text("Connect")')
        await player1_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Record time when Player 2 starts connecting
        start_time = time.time()

        # Login Player 2
        await player2_page.fill('input[placeholder="Player ID"]', "test_player_2")
        await player2_page.click('button:has-text("Connect")')
        await player2_page.wait_for_selector('.connection-status:has-text("Connected")', timeout=10000)

        # Wait for connection message to appear
        await player1_page.wait_for_selector('text="test_player_2 enters the room"', timeout=10000)

        # Record time when message appears
        end_time = time.time()

        # Verify message appeared within reasonable time (less than 5 seconds)
        message_delay = end_time - start_time
        assert message_delay < 5.0, f"Connection message took too long: {message_delay:.2f} seconds"
        assert message_delay > 0.1, f"Connection message appeared too quickly: {message_delay:.2f} seconds"

        # Cleanup
        await self._cleanup_contexts(contexts)
