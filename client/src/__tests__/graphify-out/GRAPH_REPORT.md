# Graph Report - client\src\_\_tests\_\_ (2026-06-15)

## Corpus Check

- 21 files · ~16,257 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary

- 47 nodes · 94 edges · 14 communities (4 shown, 10 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness

- Built from commit: `0d6e19cc`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)

- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)

1. `createMockLoginResponse()` - 12 edges
2. `registerAppTestHooks()` - 11 edges
3. `fetchSpy` - 10 edges
4. `createMockProfessions()` - 5 edges
5. `setupBasicMocks()` - 5 edges
6. `createMockProfessionsFetchResponse()` - 4 edges
7. `createMockJsonResponse()` - 3 edges
8. `mockFetchForAuthAndProfessions()` - 3 edges
9. `createDefaultRollStatsResponseBody()` - 3 edges
10. `createDefaultRollStatsFetchResponse()` - 3 edges

## Surprising Connections (you probably didn't know these)

- `createMockProfessionsFetchResponse()` --calls--> `createMockProfessions()` [EXTRACTED]
  app.test.helpers.ts → professionSystemErrorHandling.test.helpers.ts

## Import Cycles

- None detected.

## Communities (14 total, 10 thin omitted)

### Community 2 - "Community 2"

Cohesion: 0.50
Nodes (3): DEFAULT_ROLLED_STATS, fillSkillSlotsAndConfirm(), mockFetch

### Community 3 - "Community 3"

Cohesion: 0.50
Nodes (3): createMockSkills(), FetchMock, registerTestUserFromLoginScreen()

### Community 6 - "Community 6"

Cohesion: 1.00
Nodes (3): createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions()

## Knowledge Gaps

- **10 isolated node(s):** `mockLogoutHandler`, `fetchSpy`, `fetchSpy`, `mockLogoutHandler`, `fetchSpy` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions

_Questions this graph is uniquely positioned to answer:_

- **Why does `createMockLoginResponse()` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 12`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Why does `createMockProfessions()` connect `Community 12` to `Community 0`, `Community 2`, `Community 3`, `Community 6`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Why does `registerAppTestHooks()` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **What connects `mockLogoutHandler`, `fetchSpy`, `fetchSpy` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
