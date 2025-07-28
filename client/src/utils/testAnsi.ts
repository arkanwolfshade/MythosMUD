/**
 * Test file for ANSI to HTML converter
 */

import { ansiToHtml, ansiToHtmlWithBreaks } from "./ansiToHtml";

// Test ANSI codes
const testAnsi = "\x1b[33mYellow text\x1b[0m and \x1b[31mred text\x1b[0m";
const testMotd =
  "\x1b[33m\n                                     .....:::::::::::....\n                             ...::-=+*#*+=----------=++**=-...\x1b[0m";

console.log("Testing ANSI to HTML conversion...");
console.log("Original:", testAnsi);
console.log("Converted:", ansiToHtml(testAnsi));
console.log("With breaks:", ansiToHtmlWithBreaks(testMotd));

export { testAnsi, testMotd };
