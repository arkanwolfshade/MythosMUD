# AI Executor Quick Reference Card

## ⚡ Before You Start

```
Type this affirmation:
"I will execute [Scenario Name] exactly as written without modification, addition, or omission"
```

## ✅ The Seven Commandments

1. **READ COMPLETELY** - Read entire scenario before executing
2. **NO INTERPRETATION** - Execute exactly as written, character for character
3. **NO OPTIMIZATION** - Don't skip steps you think are unnecessary
4. **NO ENHANCEMENT** - Don't add steps you think would be helpful
5. **NO MODIFICATION** - Don't change commands you think could be improved
6. **ONE ATTEMPT** - Execute each step exactly once, then proceed
7. **STOP AT COMPLETION** - When you see "SCENARIO COMPLETE", stop immediately

## 🚫 Do NOT Do These Things

| ❌ NEVER                  | ✅ ALWAYS                        |
| ------------------------ | ------------------------------- |
| Retry empty results      | Accept first result and proceed |
| Skip "redundant" steps   | Execute every step              |
| Add debugging logs       | Use only provided logs          |
| Modify command syntax    | Use exact syntax from scenario  |
| Continue past completion | Stop at "SCENARIO COMPLETE"     |
| Add extra verification   | Execute only provided steps     |
| Reorder steps            | Follow numerical order          |
| Improve parameters       | Use exact parameters            |

## 🔍 When You See Empty Results

```javascript
const messages = await mcp_playwright_browser_evaluate({...});

if (messages.length === 0) {
    // ✅ CORRECT: Accept and proceed
    console.log('✅ No messages found - proceeding to next step');
    // Move to next step

    // ❌ WRONG: Do NOT retry!
    // const messages = await mcp_playwright_browser_evaluate({...}); // NO!
}
```

## 🎯 At Each Step

1. Read step completely
2. Execute commands exactly as written
3. Observe results (don't judge them)
4. Check completion checklist
5. Proceed to next step

## 🛑 When You See This Box

```
╔═══════════════════════════════════════════════════════════════╗
║              🎉 SCENARIO X COMPLETED 🎉                       ║
║                                                               ║
║  🛑 MANDATORY: STOP EXECUTION HERE                          ║
╚═══════════════════════════════════════════════════════════════╝
```

**ACTION**: Execute cleanup commands, then STOP. Do NOT continue to next scenario.

## 📝 Execution Pattern

```
FOR each step IN scenario:
    READ step completely
    EXECUTE commands exactly as written (no modifications)
    OBSERVE results (empty results are valid)
    CHECK completion checklist
    IF all checklist items complete:
        PROCEED to next step
    ELSE:
        DOCUMENT issue and STOP
    END IF
END FOR

WHEN you see "SCENARIO COMPLETE":
    EXECUTE cleanup
    STOP (do not continue to next scenario)
```

## ⚠️ Common Traps to Avoid

### Trap 1: "This step seems unnecessary"
**Thought**: "We already verified this in the previous step"
**Action**: Execute it anyway. It tests a different edge case.

### Trap 2: "Empty results must be wrong"
**Thought**: "Let me retry to get the messages"
**Action**: Empty results are often correct. Accept and proceed.

### Trap 3: "I should add some debug logging"
**Thought**: "Extra logs would help document what's happening"
**Action**: Use only the logs in the scenario. Adding logs changes timing.

### Trap 4: "This command syntax looks wrong"
**Thought**: "I should improve it to make it clearer"
**Action**: Use exact syntax. The system interprets it correctly.

### Trap 5: "One more verification wouldn't hurt"
**Thought**: "Let me check one more thing after completion"
**Action**: Stop immediately at completion. Extra checks change state.

## 🎓 The Golden Rule

> **If it's not explicitly written in the scenario file, DON'T DO IT.**

## 📞 When Something Goes Wrong

1. **DO NOT** try to fix it
2. **DO** document exactly what happened
3. **DO** note the step where it occurred
4. **DO** capture any error messages
5. **STOP** and report the issue

## 💪 Remember

- You are an **executor**, not an interpreter
- Your job is to **follow instructions**, not improve them
- **Exact execution** is more valuable than "optimized" execution
- **Consistency** matters more than cleverness
- When in doubt, **do exactly what the scenario says**

## 🔗 Full Documentation

For detailed explanations, see:
- `AI_EXECUTION_IMPROVEMENTS.md` - Complete improvement guide
- `EXECUTION_GUARDS.md` - Detailed failure patterns
- `SCENARIO_TEMPLATE.md` - Template with all improvements
- `MULTIPLAYER_TEST_RULES.md` - Master rules and prerequisites

---

**Keep this reference visible during scenario execution**

**Version**: 1.0
**Last Updated**: 2025-10-07
