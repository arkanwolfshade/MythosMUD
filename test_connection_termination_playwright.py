#!/usr/bin/env python3
"""
Playwright test to demonstrate connection termination behavior.
"""

import asyncio

from playwright.async_api import async_playwright


async def test_connection_termination_playwright():
    """Test connection termination using Playwright."""

    print("🧪 Testing Connection Termination with Playwright")
    print("=" * 50)

    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)

        try:
            # Create first context and page
            print("\n1. Creating first browser session...")
            context1 = await browser.new_context()
            page1 = await context1.new_page()

            # Navigate to the app
            await page1.goto("http://localhost:54731")
            print("   ✅ First session loaded")

            # Wait for the page to load
            await page1.wait_for_load_state("networkidle")

            # Check if we're on the login page
            login_form = page1.locator("form")
            if await login_form.count() > 0:
                print("   ✅ Login form found")

                # Fill in login details (we'll use a test user)
                await page1.fill('input[name="username"]', "Ithaqua")
                await page1.fill('input[name="password"]', "Cthulhu1")

                # Try to login
                await page1.click('button[type="submit"]')
                print("   ✅ Login attempt made")

                # Wait a moment for any response
                await page1.wait_for_timeout(2000)

                # Check if we got an error or success
                error_text = page1.locator(".error, .alert, [role='alert']")
                if await error_text.count() > 0:
                    error_content = await error_text.text_content()
                    print(f"   ⚠️  Login error: {error_content}")
                else:
                    print("   ✅ Login appears successful")

            # Create second context and page (simulating second login)
            print("\n2. Creating second browser session...")
            context2 = await browser.new_context()
            page2 = await context2.new_page()

            # Navigate to the app in second session
            await page2.goto("http://localhost:54731")
            print("   ✅ Second session loaded")

            # Wait for the page to load
            await page2.wait_for_load_state("networkidle")

            # Check if we're on the login page
            login_form2 = page2.locator("form")
            if await login_form2.count() > 0:
                print("   ✅ Login form found in second session")

                # Fill in login details
                await page2.fill('input[name="username"]', "Ithaqua")
                await page2.fill('input[name="password"]', "Cthulhu1")

                # Try to login
                await page2.click('button[type="submit"]')
                print("   ✅ Login attempt made in second session")

                # Wait a moment for any response
                await page2.wait_for_timeout(2000)

                # Check if we got an error or success
                error_text2 = page2.locator(".error, .alert, [role='alert']")
                if await error_text2.count() > 0:
                    error_content2 = await error_text2.text_content()
                    print(f"   ⚠️  Login error in second session: {error_content2}")
                else:
                    print("   ✅ Login appears successful in second session")

            # Wait a moment to see if first session is affected
            print("\n3. Checking for connection termination effects...")
            await page1.wait_for_timeout(3000)

            # Check if first session shows any disconnection messages
            disconnect_messages = page1.locator(
                "text=disconnect, text=connection lost, text=reconnect", case_sensitive=False
            )
            if await disconnect_messages.count() > 0:
                print("   ✅ First session shows disconnection message")
            else:
                print("   ℹ️  No disconnection message visible in first session")

            # Check if second session is working
            active_session = page2.locator("text=connected, text=online, text=game", case_sensitive=False)
            if await active_session.count() > 0:
                print("   ✅ Second session appears active")
            else:
                print("   ℹ️  Second session status unclear")

            # Take screenshots for comparison
            print("\n4. Taking screenshots for comparison...")
            await page1.screenshot(path="session1_final.png")
            await page2.screenshot(path="session2_final.png")
            print("   ✅ Screenshots saved: session1_final.png, session2_final.png")

            # Summary
            print("\n" + "=" * 50)
            print("✅ Playwright connection termination test completed!")
            print("\n📋 SUMMARY:")
            print("   • Created two browser sessions")
            print("   • Both attempted login")
            print("   • Checked for connection termination effects")
            print("   • Screenshots saved for manual inspection")
            print("\n🔍 Manual Verification:")
            print("   • Check session1_final.png for first session state")
            print("   • Check session2_final.png for second session state")
            print("   • Look for disconnection messages or errors")

        except Exception as e:
            print(f"❌ Test error: {e}")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(test_connection_termination_playwright())
