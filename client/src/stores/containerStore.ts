/**
 * Container store for unified container system.
 *
 * As documented in the restricted archives of Miskatonic University, container
 * state management requires careful orchestration to ensure proper handling
 * of investigator artifacts across environmental props, wearable gear, and corpses.
 *
 * **Zustand Store Usage Patterns:**
 *
 * **CORRECT Usage Examples:**
 *
 * ```tsx
 * // ✅ GOOD: Accessing state directly with shallow comparison
 * import { shallow } from 'zustand/shallow';
 *
 * function ContainerComponent({ containerId }: { containerId: string }) {
 *   const openContainers = useContainerStore(state => state.openContainers, shallow);
 *   const container = useMemo(() => openContainers[containerId] || null, [openContainers, containerId]);
 *   return <div>{container?.items.length} items</div>;
 * }
 *
 * // ✅ GOOD: Using selectors for specific fields
 * function ContainerList() {
 *   const selectedContainerId = useContainerStore(state => state.selectedContainerId);
 *   const selectContainer = useContainerStore(state => state.selectContainer);
 *   return <div>Selected: {selectedContainerId}</div>;
 * }
 * ```
 *
 * **INCORRECT Usage Examples (Anti-patterns):**
 *
 * ```tsx
 * // ❌ BAD: Calling selector functions inside selectors
 * function MyComponent({ containerId }: { containerId: string }) {
 *   const container = useContainerStore(state => state.getContainer(containerId)); // Don't do this!
 *   // Instead, use: const openContainers = useContainerStore(state => state.openContainers, shallow);
 *   // Then: const container = useMemo(() => openContainers[containerId] || null, [openContainers, containerId]);
 * }
 *
 * // ❌ BAD: Subscribing to entire store
 * function MyComponent() {
 *   const containerState = useContainerStore(); // Don't do this!
 *   return <div>{containerState.selectedContainerId}</div>;
 * }
 * ```
 *
 * **Note on Selector Functions:**
 * - Selector functions like `getContainer()`, `getMutationToken()`, `isContainerOpen()`, etc.
 *   are kept for backward compatibility but should NOT be called inside component selectors.
 * - Instead, access the underlying state directly
 *   (e.g., use `openContainers[containerId]` instead of `getContainer(containerId)`).
 * - Use `useMemo` to compute derived values from the state.
 */

import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

// Container types matching server-side definitions
export type ContainerSourceType = 'environment' | 'equipment' | 'corpse';
export type ContainerLockState = 'unlocked' | 'locked' | 'sealed';

/** Weapon stats when item is a weapon (from prototype metadata.weapon). */
export interface WeaponStats {
  min_damage: number;
  max_damage: number;
  modifier?: number;
  damage_types?: string[];
  magical?: boolean;
}

export interface InventoryStack {
  item_instance_id: string;
  prototype_id: string;
  item_id: string;
  item_name: string;
  slot_type: string;
  quantity: number;
  metadata?: Record<string, unknown>;
  /** Weapon stats when present (e.g. 1d4+0 slashing, piercing). */
  weapon?: WeaponStats;
  flags?: string[];
  origin?: Record<string, unknown>;
  created_at?: string;
  inner_container?: {
    capacity_slots: number;
    items: InventoryStack[];
    lock_state?: string;
    allowed_roles?: string[];
  };
}

export interface ContainerComponent {
  container_id: string;
  source_type: ContainerSourceType;
  owner_id?: string;
  room_id?: string;
  entity_id?: string;
  lock_state: ContainerLockState;
  capacity_slots: number;
  weight_limit?: number;
  decay_at?: string;
  allowed_roles: string[];
  items: InventoryStack[];
  metadata: Record<string, unknown>;
}

export interface ContainerState {
  // Open containers: { container_id: ContainerComponent }
  openContainers: Record<string, ContainerComponent>;
  // Mutation tokens: { container_id: mutation_token }
  mutationTokens: Record<string, string>;
  // Currently selected container ID
  selectedContainerId: string | null;
  // Loading state
  isLoading: boolean;
}

export interface ContainerActions {
  // Container lifecycle
  openContainer: (container: ContainerComponent, mutationToken: string) => void;
  closeContainer: (containerId: string) => void;
  updateContainer: (container: ContainerComponent) => void;
  handleContainerDecayed: (containerId: string) => void;

  // Selection
  selectContainer: (containerId: string) => void;
  deselectContainer: () => void;

  // Loading state
  setLoading: (loading: boolean) => void;

  // State management
  reset: () => void;
}

export interface ContainerSelectors {
  // Get container by ID
  getContainer: (containerId: string) => ContainerComponent | null;
  // Get mutation token for container
  getMutationToken: (containerId: string) => string | null;
  // Get all open container IDs
  getOpenContainerIds: () => string[];
  // Check if container is open
  isContainerOpen: (containerId: string) => boolean;
  // Get wearable containers for a player
  getWearableContainersForPlayer: (playerId: string) => ContainerComponent[];
  // Get corpse containers in a room
  getCorpseContainersInRoom: (roomId: string) => ContainerComponent[];
}

type ContainerStore = ContainerState & ContainerActions & ContainerSelectors;

const createInitialState = (): ContainerState => ({
  openContainers: {},
  mutationTokens: {},
  selectedContainerId: null,
  isLoading: false,
});

export const useContainerStore = create<ContainerStore>()(
  devtools(
    (set, get) => ({
      ...createInitialState(),

      // Container lifecycle actions
      openContainer: (container: ContainerComponent, mutationToken: string) =>
        set(
          state => ({
            openContainers: {
              ...state.openContainers,
              [container.container_id]: container,
            },
            mutationTokens: {
              ...state.mutationTokens,
              [container.container_id]: mutationToken,
            },
          }),
          false,
          'openContainer'
        ),

      closeContainer: (containerId: string) =>
        set(
          state => {
            // Destructuring removes containerId from state, _removed variable intentionally unused
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            const { [containerId]: _removed, ...remainingContainers } = state.openContainers;
            // Destructuring removes containerId token from state, _removedToken variable intentionally unused
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            const { [containerId]: _removedToken, ...remainingTokens } = state.mutationTokens;
            return {
              openContainers: remainingContainers,
              mutationTokens: remainingTokens,
              selectedContainerId: state.selectedContainerId === containerId ? null : state.selectedContainerId,
            };
          },
          false,
          'closeContainer'
        ),

      updateContainer: (container: ContainerComponent) =>
        set(
          state => ({
            openContainers: {
              ...state.openContainers,
              [container.container_id]: container,
            },
          }),
          false,
          'updateContainer'
        ),

      handleContainerDecayed: (containerId: string) => {
        // Same as closeContainer - remove from state
        get().closeContainer(containerId);
      },

      // Selection actions
      selectContainer: (containerId: string) => set({ selectedContainerId: containerId }, false, 'selectContainer'),

      deselectContainer: () => set({ selectedContainerId: null }, false, 'deselectContainer'),

      // Loading state
      setLoading: (loading: boolean) => set({ isLoading: loading }, false, 'setLoading'),

      // State management
      reset: () => set(createInitialState(), false, 'reset'),

      // Selectors
      getContainer: (containerId: string) => {
        const state = get();
        return state.openContainers[containerId] || null;
      },

      getMutationToken: (containerId: string) => {
        const state = get();
        return state.mutationTokens[containerId] || null;
      },

      getOpenContainerIds: () => {
        const state = get();
        return Object.keys(state.openContainers);
      },

      isContainerOpen: (containerId: string) => {
        const state = get();
        return containerId in state.openContainers;
      },

      getWearableContainersForPlayer: (playerId: string) => {
        const state = get();
        // Filter open containers to only equipment containers for this player
        return Object.values(state.openContainers).filter(
          container => container.source_type === 'equipment' && container.entity_id === playerId
        );
      },

      getCorpseContainersInRoom: (roomId: string) => {
        const state = get();
        // Filter open containers to only corpse containers in this room
        return Object.values(state.openContainers).filter(
          container => container.source_type === 'corpse' && container.room_id === roomId
        );
      },
    }),
    {
      name: 'container-store',
      enabled: import.meta.env.MODE === 'development',
      partialize: (state: ContainerStore) => ({
        openContainers: state.openContainers,
        selectedContainerId: state.selectedContainerId,
      }),
    }
  )
);
