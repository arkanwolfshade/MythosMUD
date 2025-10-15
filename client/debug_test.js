const { determineMessageType } = require('./src/utils/messageTypeUtils.ts');

const testMessages = [
  'Apple Lane - Residential Section A quiet residential street...',
  'You look around the room.',
  'Just some random text',
];

testMessages.forEach(msg => {
  const result = determineMessageType(msg);
  console.log(`Message: "${msg}" -> Type: ${result.type}`);
});
