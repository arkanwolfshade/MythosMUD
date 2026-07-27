# Client Lifecycle Metrics

> 40 nodes · cohesion 0.06

## Key Concepts

- **ResourceManager** (19 connections) — `client/src/utils/resourceCleanup.ts`
- **clientMetricsCollector.ts** (10 connections) — `client/src/utils/clientMetricsCollector.ts`
- **ClientMetricsCollector** (9 connections) — `client/src/utils/clientMetricsCollector.ts`
- **getClientMetricsCollector()** (6 connections) — `client/src/utils/clientMetricsCollector.ts`
- **useComponentLifecycleTracking.ts** (5 connections) — `client/src/hooks/useComponentLifecycleTracking.ts`
- **useStoreSubscriptionTracking.ts** (4 connections) — `client/src/hooks/useStoreSubscriptionTracking.ts`
- **useComponentLifecycleTracking.test.ts** (4 connections) — `client/src/hooks/__tests__/useComponentLifecycleTracking.test.ts`
- **useStoreSubscriptionTracking.test.ts** (4 connections) — `client/src/hooks/__tests__/useStoreSubscriptionTracking.test.ts`
- **useComponentLifecycleTracking()** (3 connections) — `client/src/hooks/useComponentLifecycleTracking.ts`
- **useStoreSubscriptionTracking()** (3 connections) — `client/src/hooks/useStoreSubscriptionTracking.ts`
- **clientMetricsCollector.test.ts** (2 connections) — `client/src/utils/__tests__/clientMetricsCollector.test.ts`
- **.getMetrics()** (2 connections) — `client/src/utils/clientMetricsCollector.ts`
- **.logMetrics()** (2 connections) — `client/src/utils/clientMetricsCollector.ts`
- **.setResourceManager()** (2 connections) — `client/src/utils/clientMetricsCollector.ts`
- **UseComponentLifecycleTrackingOptions** (1 connections) — `client/src/hooks/useComponentLifecycleTracking.ts`
- **trackComponentMount** (1 connections) — `client/src/hooks/__tests__/useComponentLifecycleTracking.test.ts`
- **trackComponentUnmount** (1 connections) — `client/src/hooks/__tests__/useComponentLifecycleTracking.test.ts`
- **trackStoreSubscription** (1 connections) — `client/src/hooks/__tests__/useStoreSubscriptionTracking.test.ts`
- **trackStoreUnsubscription** (1 connections) — `client/src/hooks/__tests__/useStoreSubscriptionTracking.test.ts`
- **ClientMetrics** (1 connections) — `client/src/utils/clientMetricsCollector.ts`
- **.trackComponentMount()** (1 connections) — `client/src/utils/clientMetricsCollector.ts`
- **.trackComponentUnmount()** (1 connections) — `client/src/utils/clientMetricsCollector.ts`
- **.trackStoreSubscription()** (1 connections) — `client/src/utils/clientMetricsCollector.ts`
- **.trackStoreUnsubscription()** (1 connections) — `client/src/utils/clientMetricsCollector.ts`
- **ComponentLifecycleMetrics** (1 connections) — `client/src/utils/clientMetricsCollector.ts`
- *... and 15 more nodes in this community*

## Relationships

- [[Connection State Hooks]] (3 shared connections)

## Source Files

- `client/src/hooks/__tests__/useComponentLifecycleTracking.test.ts`
- `client/src/hooks/__tests__/useStoreSubscriptionTracking.test.ts`
- `client/src/hooks/useComponentLifecycleTracking.ts`
- `client/src/hooks/useStoreSubscriptionTracking.ts`
- `client/src/utils/__tests__/clientMetricsCollector.test.ts`
- `client/src/utils/clientMetricsCollector.ts`
- `client/src/utils/resourceCleanup.ts`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
