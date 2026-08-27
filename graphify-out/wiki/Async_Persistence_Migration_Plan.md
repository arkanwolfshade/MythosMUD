# Async Persistence Migration Plan

> 38 nodes

## Key Concepts

- **useRoomEditModal.ts** (18 connections) — `client/src/components/map/useRoomEditModal.ts`
- **RoomEditModal.tsx** (16 connections) — `client/src/components/map/RoomEditModal.tsx`
- **RoomEditModalForm.tsx** (16 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **RoomEditModal()** (4 connections) — `client/src/components/map/RoomEditModal.tsx`
- **useRoomEditModal()** (4 connections) — `client/src/components/map/useRoomEditModal.ts`
- **RoomEditModal.test.tsx** (4 connections) — `client/src/components/map/__tests__/RoomEditModal.test.tsx`
- **fieldBorderClass()** (3 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **buildInitialFormData()** (3 connections) — `client/src/components/map/useRoomEditModal.ts`
- **RoomEditFormData** (2 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **RoomEditModalProps** (2 connections) — `client/src/components/map/useRoomEditModal.ts`
- **RoomEditDescriptionField()** (2 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **RoomEditModalForm()** (2 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **RoomEditNameField()** (2 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **RoomEditModalTabs()** (2 connections) — `client/src/components/map/RoomEditModalTabs.tsx`
- **toFormValue()** (2 connections) — `client/src/components/map/useRoomEditModal.ts`
- **RoomEditModalTabs.tsx** (2 connections) — `client/src/components/map/RoomEditModalTabs.tsx`
- **EnvironmentOption** (1 connections) — `client/src/components/map/RoomEditModal.tsx`
- **EnvironmentOption** (1 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **RoomEditModalFormProps** (1 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- **EditableRoomField** (1 connections) — `client/src/components/map/useRoomEditModal.ts`
- **RoomEditModalContent()** (1 connections) — `client/src/components/map/RoomEditModal.tsx`
- **RoomEditModalFooter()** (1 connections) — `client/src/components/map/RoomEditModal.tsx`
- **RoomEditModalHeader()** (1 connections) — `client/src/components/map/RoomEditModal.tsx`
- **RoomEditModalShell()** (1 connections) — `client/src/components/map/RoomEditModal.tsx`
- **FieldError()** (1 connections) — `client/src/components/map/RoomEditModalForm.tsx`
- *... and 13 more nodes in this community*

## Relationships

- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (4 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (2 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (2 shared connections)

## Source Files

- `client/src/components/map/RoomEditModal.tsx`
- `client/src/components/map/RoomEditModalForm.tsx`
- `client/src/components/map/RoomEditModalTabs.tsx`
- `client/src/components/map/__tests__/RoomEditModal.test.tsx`
- `client/src/components/map/useRoomEditModal.ts`

## Audit Trail

- EXTRACTED: 52 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*