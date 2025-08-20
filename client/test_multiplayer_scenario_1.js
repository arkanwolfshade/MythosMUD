const { chromium } = require('playwright');

async function testMultiplayerScenario1() {
  const browser = await chromium.launch({ headless: false });

  try {
    // Create two browser contexts for the two players
    const context1 = await browser.newContext();
    const context2 = await browser.newContext();

    const page1 = await context1.newPage();
    const page2 = await context2.newPage();

    console.log('🚀 Starting multiplayer scenario test...');

    // Step 1: AW enters the game
    console.log('1. AW entering the game...');
    await page1.goto('http://localhost:5173');
    await page1.waitForSelector('#username');
    await page1.fill('#username', 'ArkanWolfshade');
    await page1.fill('#password', 'Cthulhu1');
    await page1.click('button[type="submit"]');

    // Wait for connection and initial game state
    await page1.waitForSelector('.game-terminal', { timeout: 10000 });
    console.log('✅ AW successfully connected');

    // Step 2: Ithaqua enters the game
    console.log('2. Ithaqua entering the game...');
    await page2.goto('http://localhost:5173');
    await page2.waitForSelector('#username');
    await page2.fill('#username', 'Ithaqua');
    await page2.fill('#password', 'Cthulhu1');
    await page2.click('button[type="submit"]');

    // Wait for connection
    await page2.waitForSelector('.game-terminal', { timeout: 10000 });
    console.log('✅ Ithaqua successfully connected');

    // Step 3: Check if AW sees "Ithaqua has entered the game."
    console.log('3. Checking if AW sees Ithaqua entered message...');
    await page1.waitForTimeout(2000); // Wait for message to arrive

    const awMessages = await page1.$$eval('.message', elements => elements.map(el => el.textContent.trim()));

    const ithaquaEnteredMessage = awMessages.find(msg => msg.includes('Ithaqua has entered the game.'));

    if (ithaquaEnteredMessage) {
      console.log('✅ AW correctly sees: "Ithaqua has entered the game."');
    } else {
      console.log('❌ AW did NOT see "Ithaqua has entered the game."');
      console.log('AW messages:', awMessages);
    }

    // Step 4: Check if Ithaqua sees any enters/leaves messages
    console.log('4. Checking if Ithaqua sees any enters/leaves messages...');
    const ithaquaMessages = await page2.$$eval('.message', elements => elements.map(el => el.textContent.trim()));

    const unwantedMessages = ithaquaMessages.filter(
      msg =>
        msg.includes('enters the room') ||
        msg.includes('leaves the room') ||
        msg.includes('entered the game') ||
        msg.includes('left the game')
    );

    if (unwantedMessages.length === 0) {
      console.log('✅ Ithaqua correctly sees NO enters/leaves messages');
    } else {
      console.log('❌ Ithaqua incorrectly sees enters/leaves messages:', unwantedMessages);
    }

    // Step 5: Ithaqua leaves the game
    console.log('5. Ithaqua leaving the game...');
    await page2.close();
    await context2.close();
    console.log('✅ Ithaqua disconnected');

    // Step 6: Check if AW sees "Ithaqua has left the game."
    console.log('6. Checking if AW sees Ithaqua left message...');
    await page1.waitForTimeout(2000); // Wait for message to arrive

    const awMessagesAfter = await page1.$$eval('.message', elements => elements.map(el => el.textContent.trim()));

    const ithaquaLeftMessage = awMessagesAfter.find(msg => msg.includes('Ithaqua has left the game.'));

    if (ithaquaLeftMessage) {
      console.log('✅ AW correctly sees: "Ithaqua has left the game."');
    } else {
      console.log('❌ AW did NOT see "Ithaqua has left the game."');
      console.log('AW messages after disconnect:', awMessagesAfter);
    }

    console.log('\n🎯 Scenario 1 Test Results:');
    console.log('============================');
    console.log(`AW sees Ithaqua entered: ${ithaquaEnteredMessage ? '✅ PASS' : '❌ FAIL'}`);
    console.log(`Ithaqua sees no unwanted messages: ${unwantedMessages.length === 0 ? '✅ PASS' : '❌ FAIL'}`);
    console.log(`AW sees Ithaqua left: ${ithaquaLeftMessage ? '✅ PASS' : '❌ FAIL'}`);

    // Keep browser open for manual inspection
    console.log('\n🔍 Browser will remain open for 30 seconds for manual inspection...');
    await page1.waitForTimeout(30000);
  } catch (error) {
    console.error('❌ Test failed:', error);
  } finally {
    await browser.close();
  }
}

testMultiplayerScenario1();
