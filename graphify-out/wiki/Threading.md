# Threading

> 22 nodes

## Key Concepts

- **._execute_wander_movement()** (7 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (6 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_wander_action()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (4 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **.stop()** (3 connections) — `server/npc/threading.py`
- **Start a thread for a specific NPC. Args: npc_id: Unique identifier for the NPC…** (1 connections) — `server/npc/threading.py`
- **Stop a specific NPC thread. Args: npc_id: Unique identifier for the NPC…** (1 connections) — `server/npc/threading.py`
- **Internal method to stop an NPC thread.** (1 connections) — `server/npc/threading.py`
- **Restart a specific NPC thread. Args: npc_id: Unique identifier for the NPC…** (1 connections) — `server/npc/threading.py`
- **Worker function for individual NPC threads. This function runs in a separate…** (1 connections) — `server/npc/threading.py`
- **Process a message for an NPC.** (1 connections) — `server/npc/threading.py`
- **Resolve active NPC instance and definition for a WANDER action.** (1 connections) — `server/npc/threading.py`
- **Run idle movement for a resolved wander NPC.** (1 connections) — `server/npc/threading.py`
- **Process a WANDER action for idle movement. Args: npc_id: ID of the NPC to move…** (1 connections) — `server/npc/threading.py`
- **Execute NPC behavior based on its type and configuration.** (1 connections) — `server/npc/threading.py`
- **Stop the NPC thread manager and all active threads. Returns: bool: True if…** (1 connections) — `server/npc/threading.py`

## Relationships

- [Test Npc Thread Manager Internals](Test_Npc_Thread_Manager_Internals.md) (12 shared connections)
- [NPC Models](NPC_Models.md) (4 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Idle Movement](Test_Idle_Movement.md) (1 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*