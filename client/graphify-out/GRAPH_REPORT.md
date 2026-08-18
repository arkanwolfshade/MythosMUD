# Graph Report - src  (2026-08-18)

## Corpus Check
- Large corpus: 618 files · ~333,058 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 2860 nodes · 6782 edges · 129 communities (116 shown, 13 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 34 edges (avg confidence: 0.63)
- Token cost: 8,023 input · 1,996 output

## Community Hubs (Navigation)
- Chat Channel Filtering
- Game Client V2
- Game Terminal Core
- Room Map Data
- Connection Hook Tests
- Command Panel Tests
- Lifecycle Tracking Hooks
- Memory Leak Detector
- Profession Character Cards
- Draggable Panel Core
- Event Log Messages
- API Type Guards
- Character Name Screen
- Mythos Time HUD
- Room Info UI
- Event Handler Pipeline
- Map Force Layout
- Chat Panel Tests
- Character Selection Screen
- Map React Flow
- Safe HTML Sanitizer
- API Error Messages
- Chat Message Widgets
- Room Event Handlers
- Panel Manager Reducer
- Health Lucidity Meters
- Map Editor Shell
- Edge Creation Modal
- Chat Channel Header
- Channel Selector UI
- Combat Event Handlers
- Character Select Flows
- Player Event Handlers
- Quest Log Panel
- Monitoring Panel Stats
- Debug Logger Buffer
- Game State Normalization
- App Shell Tests
- Map Editor Modals
- Panel Manager System
- Performance Test Fixtures
- Chat Message Handlers
- Feedback Manager
- Dialogue API Client
- Maps API Client
- Command Panel UI
- Edge Details Panel
- Panel Container Views
- Mythos App ViewModel
- Map Page Router
- Edge Modal Logic
- Room Edit Modal
- Map View Component
- Room Info Panel
- Player Status Hooks
- Game Log Panel
- UI Design Tokens
- Logout Flow Tests
- Game Info Panel
- Expanded Panel Chrome
- Backpack Inventory Tab
- Game Terminal Container
- Chat Export Search
- Theme Preference Context
- Death Delirium Screens
- Chat Panel Presentation
- ASCII Map Viewer
- GameClient V2 Facade
- Game Terminal Context
- Corpse Overlay UI
- ASCII Map Hook
- Profession Selection Screen
- Mythos App State
- E2E Bootstrap Helpers
- Logout Handler
- Chat History Panel
- Panel Layout Clamp
- Panel Context Hooks
- Auth Session Apply
- Command Store
- App Router Pages
- Container Split Handlers
- Game Log Tests
- Empty Occupants Diagnostics
- Container Drag Tests
- Room Edit Form
- GameClient V2 Container
- Creation Flow Views
- Profession Error Tests
- Message Batcher
- Container Split View
- Panel Resize Handles
- Connection Store
- Client Logger
- Session Manager
- Draggable Panel Tests
- Map Performance Utils
- Minimap Panel Section
- Panel Context Runtime
- Grid Layout Manager
- Chat History Dock Tests
- Modal Container Shells
- Session Store
- Panel Layout Validation
- Container Keyboard Tests
- Chat Panel Edge Tests
- Performance Monitor Hook
- Grid Layout Hook
- Game Client Logout
- CSRF Protection
- Connection Panel
- Mythos Login Form
- Logout Integration Tests
- Virtualized Message List
- Error Boundary
- Stat Rolling Tests
- Death Void Location
- Player Panel
- Room Panel
- Login Grace Banner
- Event Schema Docs
- Mythos Theme
- React Logo

## God Nodes (most connected - your core abstractions)
1. `MythosIcons` - 37 edges
2. `Room` - 36 edges
3. `EldritchIcon()` - 34 edges
4. `RoomNodeData` - 33 edges
5. `logger` - 33 edges
6. `Player` - 32 edges
7. `ChatMessage` - 32 edges
8. `Profession` - 27 edges
9. `sanitizeChatMessageForState()` - 26 edges
10. `GameState` - 26 edges

## Surprising Connections (you probably didn't know these)
- `CreateCharacterPayload` --references--> `Stats`  [EXTRACTED]
  components/CharacterNameScreen.tsx → hooks/useStatsRolling.ts
- `MapViewBody()` --calls--> `getVersionedApiBaseUrl()`  [EXTRACTED]
  components/MapView.tsx → utils/config.ts
- `UseProfessionsResult` --references--> `Profession`  [EXTRACTED]
  hooks/useProfessions.ts → components/ProfessionCard.tsx
- `LucidityMeterProps` --references--> `LucidityStatus`  [EXTRACTED]
  components/lucidity/LucidityMeter.tsx → types/lucidity.ts
- `RescueStatusBannerProps` --references--> `RescueState`  [EXTRACTED]
  components/lucidity/RescueStatusBanner.tsx → types/lucidity.ts

## Import Cycles
- 2-file cycle: `components/panels/chatPanelRuntimeUtils.ts -> components/panels/chatPanelUnreadCounts.ts -> components/panels/chatPanelRuntimeUtils.ts`
- 2-file cycle: `components/map/useAsciiMap.ts -> components/map/useAsciiMapState.ts -> components/map/useAsciiMap.ts`
- 3-file cycle: `components/panels/chatPanelRuntimeUtils.ts -> components/panels/chatPanelUnreadCounts.ts -> components/panels/chatPanelUnreadBump.ts -> components/panels/chatPanelRuntimeUtils.ts`
- 3-file cycle: `components/panels/chatPanelChannelFilter.ts -> components/panels/chatPanelChannelVisibility.ts -> components/panels/chatPanelRuntimeUtils.ts -> components/panels/chatPanelChannelFilter.ts`

## Hyperedges (group relationships)
- **MythosMUD UI Components** — components_ui_statuspanel, components_ui_roominfo, components_ui_terminalbutton, components_ui_terminalinput, components_ui_virtualizedmessagelist [EXTRACTED 1.00]
- **Event-Driven State Management** — components_uiv2_eventlog_events_schema, components_uiv2_eventlog_handoffs, components_uiv2_eventlog_projector [EXTRACTED 0.95]

## Communities (129 total, 13 thin omitted)

### Community 0 - "Chat Channel Filtering"
Cohesion: 0.06
Nodes (68): filterMessagesForChannelView(), EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW, isGloballyExcludedFromChannelView(), isVisibleInChannelView(), matchesChannelSelection(), resolveMessageChannelForFilter(), buildChatExportCSV(), buildChatExportCsvRow() (+60 more)

### Community 1 - "Game Client V2"
Cohesion: 0.07
Nodes (47): GameTerminalProps, EventHandlerContext, calculateOccupantCount(), GameClientV2(), GameClientV2Content(), GameClientV2Props, MainDockPanelId, MainDockSlotMeta (+39 more)

### Community 2 - "Game Terminal Core"
Cohesion: 0.06
Nodes (43): buildHealthStatus(), ChatMessage, formatPosture(), GameTerminal(), Player, Room, IncapacitatedBanner, IncapacitatedBannerProps (+35 more)

### Community 3 - "Room Map Data"
Cohesion: 0.10
Nodes (36): fetchSpy, useMapLayout(), buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData(), UseRoomMapDataResult (+28 more)

### Community 4 - "Connection Hook Tests"
Cohesion: 0.07
Nodes (30): useGameConnectionManagement(), ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach() (+22 more)

### Community 5 - "Command Panel Tests"
Cohesion: 0.07
Nodes (36): appendCommands(), CommandCategories(), CommandPanelTest(), COMMAND_CATEGORIES, DEFAULT_COMMAND_HISTORY, EXAMPLES, FEATURES, MOVEMENT_COMMANDS (+28 more)

### Community 6 - "Lifecycle Tracking Hooks"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 7 - "Memory Leak Detector"
Cohesion: 0.07
Nodes (16): ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor, MemoryMonitorOptions (+8 more)

### Community 8 - "Profession Character Cards"
Cohesion: 0.08
Nodes (33): CharacterNameScreenProps, MechanicalEffect, Profession, ProfessionCard(), ProfessionCardProps, StatRequirement, STAT_ROWS, StatsRollingScreen() (+25 more)

### Community 9 - "Draggable Panel Core"
Cohesion: 0.09
Nodes (41): DraggablePanel(), DraggablePanelProps, isMouseEventOnHeader(), isPanelDragBlockedTarget(), PANEL_DRAG_BLOCK_SELECTORS, relativeSizeToAbsolute(), relativeToAbsolute(), applyDragMove() (+33 more)

### Community 10 - "Event Log Messages"
Cohesion: 0.10
Nodes (41): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), messageHandlers, ProjectorHandler, stateHandlers, appendMessage() (+33 more)

### Community 11 - "API Type Guards"
Cohesion: 0.11
Nodes (44): LoginResponse, ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString() (+36 more)

### Community 12 - "Character Name Screen"
Cohesion: 0.08
Nodes (33): buildCreateCharacterPayload(), CharacterNameScreen(), CreateCharacterPayload, getCreateCharacterErrorMessage(), OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, MotdContent() (+25 more)

### Community 13 - "Mythos Time HUD"
Cohesion: 0.11
Nodes (32): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, appendDaypartChange(), appendHourChime() (+24 more)

### Community 14 - "Room Info UI"
Cohesion: 0.09
Nodes (37): MythosMUD UI Component Library Documentation, CompleteRoomInfo(), DebugInfo(), RoomDescription(), RoomEntities(), RoomExits(), RoomInfo(), RoomInfoContext (+29 more)

### Community 15 - "Event Handler Pipeline"
Cohesion: 0.13
Nodes (20): eventHandlers, processGameEvent(), hoisted, EventHandler, GameEvent, EventStore, IEventStore, ensureSelfListedInRoomPlayers() (+12 more)

### Community 16 - "Map Force Layout"
Cohesion: 0.10
Nodes (36): UseMapLayoutOptions, applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyLinkForces() (+28 more)

### Community 17 - "Chat Panel Tests"
Cohesion: 0.08
Nodes (20): ChatMessage, ChatMessageType, ChatPanelTest(), mockClick, mockCreateObjectURL, mockRevokeObjectURL, TailwindTest(), DEFAULT_FEEDBACK (+12 more)

### Community 18 - "Character Selection Screen"
Cohesion: 0.12
Nodes (27): CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), fetchCharactersList(), formatCharacterDate() (+19 more)

### Community 19 - "Map React Flow"
Cohesion: 0.11
Nodes (22): defaultReactFlowOptions, getEdgeTypes(), getNodeTypes(), ExitEdge, ExitEdgeBody(), ExitEdgeLabels(), ExitEdgeProps, exitFlags() (+14 more)

### Community 20 - "Safe HTML Sanitizer"
Cohesion: 0.09
Nodes (19): SafeHtml(), SafeHtmlProps, createDomPurifyTestWindow(), installDomPurifyTestWindow(), defaultFetchMock, collectWindowCandidates(), COMMAND_PROBE_CONFIG, DOMPurifyInstance (+11 more)

### Community 21 - "API Error Messages"
Cohesion: 0.17
Nodes (27): extractErrorMessageFromResponseBody(), errorMessageFromApiBody(), messageFromCreationRefreshHttpError(), parseRefreshFailure(), isObject(), loginFailureMessage(), formatValidationErrors(), messageFromNestedError() (+19 more)

### Community 22 - "Chat Message Widgets"
Cohesion: 0.11
Nodes (21): ChatHistoryToggle(), ChatHistoryToggleProps, ChatMessage(), ChatMessageProps, formatTimestamp(), getFontSizeClass(), getMessageClass(), ChatMessagesList() (+13 more)

### Community 23 - "Room Event Handlers"
Cohesion: 0.12
Nodes (32): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+24 more)

### Community 24 - "Panel Manager Reducer"
Cohesion: 0.16
Nodes (27): savePanelLayout(), PanelAction, panelActionHandlers, PanelReducerHandler, computeMinimizedDockPosition(), getDefaultViewport(), getMinimizedPanelIds(), MINIMIZED_BAR_HEIGHT (+19 more)

### Community 25 - "Health Lucidity Meters"
Cohesion: 0.09
Nodes (17): formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, computeLucidityBar(), formatChange(), LucidityChangeFooter(), LucidityMeter (+9 more)

### Community 26 - "Map Editor Shell"
Cohesion: 0.09
Nodes (18): edgeTypes, nodeTypes, UseRoomMapDataOptions, MapEditToolbar(), MapEditToolbarProps, MAP_EDITOR_DIRECTIONS, RoomMapEditorProps, useRoomMapEditorSelection() (+10 more)

### Community 27 - "Edge Creation Modal"
Cohesion: 0.12
Nodes (18): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+10 more)

### Community 28 - "Chat Channel Header"
Cohesion: 0.11
Nodes (23): ChannelActivityIndicators(), ChannelActivityIndicatorsProps, getActivityColor(), ChannelSelectorSection(), ChannelSelectorSectionProps, ChatHeader(), ChatHeaderProps, ChatPanelRefactoredToolbar() (+15 more)

### Community 29 - "Channel Selector UI"
Cohesion: 0.10
Nodes (22): Channel, ChannelSelector(), ChannelSelectorProps, useChannelSelectorState(), MOCK_PLAYER, STYLE_GUIDE_CHANNELS, FormsSectionProps, StyleGuideButtonsSection() (+14 more)

### Community 30 - "Combat Event Handlers"
Cohesion: 0.14
Nodes (27): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), fetchSpy (+19 more)

### Community 31 - "Character Select Flows"
Cohesion: 0.15
Nodes (25): handleRefreshCharactersFailure(), postSelectCharacter(), runAfterCharacterCreatedFlow(), isGracePeriodServerUnavailableError(), tryStartLoginGracePeriod(), runSelectCharacterFlow(), selectCharacterNetworkErrorMessage(), SelectCharacterResult (+17 more)

### Community 32 - "Player Event Handlers"
Cohesion: 0.13
Nodes (25): handlePlayerDeliriumRespawned(), handlePlayerDied(), handlePlayerDpUpdated(), handlePlayerEntered(), handlePlayerEnteredGame(), handlePlayerLeft(), handlePlayerLeftGame(), handlePlayerRespawned() (+17 more)

### Community 33 - "Quest Log Panel"
Cohesion: 0.13
Nodes (23): GameStateUpdates, getStateBadgeClassName(), GoalWithProgress, QuestEntryCard(), QuestLogPanel(), QuestLogPanelProps, QuestLogEntry, getNpcsArray() (+15 more)

### Community 34 - "Monitoring Panel Stats"
Cohesion: 0.12
Nodes (23): ConnectionHealthStats(), DualConnectionStats(), formatNumber(), formatPercentage(), formatTime(), loadMonitoringSnapshot(), MonitoringData, MonitoringPanel() (+15 more)

### Community 35 - "Debug Logger Buffer"
Cohesion: 0.13
Nodes (5): debugLogger, LogConfig, LogEntry, LogLevel, mockConsole

### Community 36 - "Game State Normalization"
Cohesion: 0.15
Nodes (19): Player, createEntityMap(), denormalizeGameData(), Entity, EntityMap, extractEntities(), GameData, getEntitiesByIds() (+11 more)

### Community 37 - "App Shell Tests"
Cohesion: 0.28
Nodes (8): App(), fetchSpy, registerAppTestHooks(), fetchSpy, fetchSpy, fetchSpy, fetchSpy, createMockLoginResponse()

### Community 38 - "Map Editor Modals"
Cohesion: 0.15
Nodes (22): useMapEditing(), buildModalCreateEdgeHandler(), buildModalPreviewHandler(), buildModalUpdateEdgeHandler(), buildModalUpdateRoomHandler(), buildPreviewEdge(), createRoomMapEditorModalActions(), filterEditorRooms() (+14 more)

### Community 39 - "Panel Manager System"
Cohesion: 0.16
Nodes (13): PanelManager(), PanelManagerProps, PanelManagerProvider(), PanelManagerProviderProps, PanelManagerContext, PanelManagerContextValue, panelReducer(), localStorageMock (+5 more)

### Community 40 - "Performance Test Fixtures"
Cohesion: 0.12
Nodes (13): Channel, ChannelSelectorProps, MemoryUsageDisplayProps, PerformanceChartProps, TerminalButtonProps, TerminalInputProps, ExtendedPerformance, PerformanceMemory (+5 more)

### Community 41 - "Chat Message Handlers"
Cohesion: 0.16
Nodes (14): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+6 more)

### Community 42 - "Feedback Manager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 43 - "Dialogue API Client"
Cohesion: 0.16
Nodes (18): baseUrl(), buildHeaders(), deleteDialogueDefinition(), DialogueDefinitionDto, DialogueNodeDto, DialogueOptionDto, DialogueTreeDto, listDialogueDefinitions() (+10 more)

### Community 44 - "Maps API Client"
Cohesion: 0.14
Nodes (19): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+11 more)

### Community 45 - "Command Panel UI"
Cohesion: 0.12
Nodes (13): CommandPanel(), CommandPanelProps, logCommandPanelConnectionDebug(), useCommandPanelEffects(), TerminalButtonProps, TerminalInputProps, TerminalButtonProps, TerminalInputProps (+5 more)

### Community 46 - "Edge Details Panel"
Cohesion: 0.11
Nodes (15): buildEdgeFieldModel(), EdgeAdminActionsProps, EdgeDeleteConfirmProps, EdgeDetailRow(), EdgeDetailRowProps, EdgeDetailsFields(), EdgeDetailsFieldsProps, EdgeDetailsPanel() (+7 more)

### Community 47 - "Panel Container Views"
Cohesion: 0.20
Nodes (14): PanelContainerProps, PanelSolidUnderlay(), PanelRndViewProps, getPanelVariantClasses(), usePanelContainerBody(), PanelContainerLayoutInput, usePanelContainerLayout(), PanelContainerProps (+6 more)

### Community 48 - "Mythos App ViewModel"
Cohesion: 0.16
Nodes (19): AppActions, AppState, buildActionViewModel(), buildMythosAppViewModel(), buildStateViewModel(), hoisted, useMythosApp(), authSliceReducer() (+11 more)

### Community 49 - "Map Page Router"
Cohesion: 0.16
Nodes (17): MapPage, RoomMapViewerProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView(), renderMapPageState(), renderStatusGate() (+9 more)

### Community 50 - "Edge Modal Logic"
Cohesion: 0.21
Nodes (20): applyModalBodyScrollLock(), deriveEdgeCreationData(), edgeFormCanSubmit(), EdgeFormFields, EdgeFormResetters, edgeFormStateFromExisting(), emptyEdgeFormState(), filterNodesForTargetSelection() (+12 more)

### Community 51 - "Room Edit Modal"
Cohesion: 0.12
Nodes (9): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), RoomEditModalTabs(), buildInitialFormData(), EditableRoomField, FIELD_VALIDATORS, toFormValue() (+1 more)

### Community 52 - "Map View Component"
Cohesion: 0.15
Nodes (12): MapView(), MapViewBody(), MapViewProps, Room, useMapViewEffects(), TabbedInterfaceOverlay(), TabbedInterfaceOverlayProps, Tab (+4 more)

### Community 53 - "Room Info Panel"
Cohesion: 0.13
Nodes (16): applyRoomDefaultFields(), DEV_FALLBACK_ROOM, fixOccupantCountMismatch(), formatDescription(), formatExitDirections(), formatLocationName(), KNOWN_LOCATION_PATTERNS, logRoomInfoRenderDebug() (+8 more)

### Community 54 - "Player Status Hooks"
Cohesion: 0.13
Nodes (18): UseCommandHandlersParams, currentDpOf(), getCurrentLucidity(), markPlayerDead(), PlayerStatusSetters, skipDeadInRespawnRoom(), syncDeathState(), syncDeliriumState() (+10 more)

### Community 55 - "Game Log Panel"
Cohesion: 0.21
Nodes (16): GameLogListMessage, GameLogMessagesList(), GameLogMessagesListProps, GameLogPanelProps, GameLogPanelFilterBar(), GameLogPanelFilterBarProps, GameLogPanelHeader(), GameLogPanelHeaderProps (+8 more)

### Community 56 - "UI Design Tokens"
Cohesion: 0.15
Nodes (19): animations, borderRadius, breakpoints, buildClasses, ButtonVariant, colors, ColorVariant, ComponentSize (+11 more)

### Community 57 - "Logout Flow Tests"
Cohesion: 0.14
Nodes (11): fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler, inputSanitizer, NOTE: For production, this should be stored in httpOnly cookies set by the…, RefreshTokenResponse, secureTokenStorage (+3 more)

### Community 58 - "Game Info Panel"
Cohesion: 0.17
Nodes (16): ChatHistoryMessageBody(), chatMessageVisibleInGameInfo(), GAME_INFO_CHAT_CHANNELS, GameInfoPanel(), GameInfoPanelProps, ANSI_COLORS, ANSI_FG_CODES, AnsiState (+8 more)

### Community 59 - "Expanded Panel Chrome"
Cohesion: 0.19
Nodes (14): ExpandedPanelBody(), ExpandedPanelBodyProps, ExpandedPanelHeader(), ExpandedPanelHeaderProps, EXPANDED_RESIZE_EDGES, ExpandedPanelRnd(), ExpandedPanelRndProps, panelShellStyle() (+6 more)

### Community 60 - "Backpack Inventory Tab"
Cohesion: 0.16
Nodes (16): BackpackTab(), BackpackTabProps, mockDeselectContainer, mockOpenContainers, mockPlayer, mockSelectContainer, mockSelectedContainerId, ContainerActions (+8 more)

### Community 61 - "Game Terminal Container"
Cohesion: 0.16
Nodes (16): GameTerminalContainer(), createDefaultGameTerminalState(), useGameTerminalMock, applyTestCommandHistoryCap(), CHANNEL_TYPE_MAP, ChatMessageLike, GameTerminalState, mockCommandState (+8 more)

### Community 62 - "Chat Export Search"
Cohesion: 0.12
Nodes (11): ChatExportDialog(), ChatExportDialogProps, collectFocusableElements(), ChatPanelHistorySearch(), ChatPanelHistorySearchProps, ChatExportDialogLazy, ChatPanelChannelSectionProps, ChatPanelRuntimeChatAreaProps (+3 more)

### Community 63 - "Theme Preference Context"
Cohesion: 0.22
Nodes (17): useAccessibilityPreference(), useAnimationPreference(), useColorSchemePreference(), useCompactModePreference(), useDebugInfoPreference(), useFontSizePreference(), useTheme(), useThemePreference() (+9 more)

### Community 64 - "Death Delirium Screens"
Cohesion: 0.16
Nodes (10): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, GameClientV2ContainerLayout(), GameClientV2ContainerView() (+2 more)

### Community 65 - "Chat Panel Presentation"
Cohesion: 0.15
Nodes (12): GameTerminalPresentation(), GameTerminalPresentationProps, ChatPanel(), Channel, ChannelSelectorProps, TerminalButtonProps, TerminalInputProps, Channel (+4 more)

### Community 66 - "ASCII Map Viewer"
Cohesion: 0.18
Nodes (12): AsciiMapEditorProps, AsciiMapViewer(), AsciiMapViewerProps, chooseMapView(), getMapClickHandler(), useAsciiMapViewerBindings(), createViewportKeyHandler(), VIEWPORT_BUTTON_CLASS (+4 more)

### Community 67 - "GameClient V2 Facade"
Cohesion: 0.26
Nodes (13): deriveActiveEffectsForHeader(), buildGameClientV2ContainerReturn(), GameClientV2ContainerPublicApi, buildHandlerPublicFields(), buildNetPublicFields(), buildSliceAndPropsPublicFields(), GameClientV2ContainerProps, GameClientV2MergedSlice (+5 more)

### Community 68 - "Game Terminal Context"
Cohesion: 0.22
Nodes (16): GameTerminalContext, GameTerminalContextType, GameTerminalProvider(), GameTerminalProviderProps, useConnectionState(), useGameActions(), useGameState(), useGameTerminalContext() (+8 more)

### Community 69 - "Corpse Overlay UI"
Cohesion: 0.18
Nodes (14): CorpseOverlay(), CorpseOverlayProps, DecayBanner(), GracePeriodBanner(), calculateTimeRemaining(), formatTimeRemaining(), getCorpseTiming(), isCorpseOwner() (+6 more)

### Community 70 - "ASCII Map Hook"
Cohesion: 0.20
Nodes (15): UseAsciiMapParams, UseAsciiMapResult, applyViewportFromRaw(), AsciiMapFields, FetchMapParams, getMapErrorMessage(), resetViewportForRoom(), runFetchMap() (+7 more)

### Community 71 - "Profession Selection Screen"
Cohesion: 0.16
Nodes (14): ProfessionSelectionContentProps, ProfessionSelectionScreen(), ProfessionSelectionScreenProps, fetchSpy, handleProfessionsFetchError(), loadProfessions(), parseDetailMessage(), parseProfessionsBody() (+6 more)

### Community 72 - "Mythos App State"
Cohesion: 0.19
Nodes (16): AuthSlice, authSliceReducer(), creationSliceReducer(), INITIAL_AUTH_SLICE, INITIAL_CREATION_SLICE, PendingSkillsPayload, resolveNextState(), useAuthSliceSetters() (+8 more)

### Community 73 - "E2E Bootstrap Helpers"
Cohesion: 0.17
Nodes (14): appendBootstrapFailureLog(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT, E2E_SERVER_URL (+6 more)

### Community 74 - "Logout Handler"
Cohesion: 0.22
Nodes (16): asRecordUnknown(), createLogoutAbortTimer(), createLogoutHandler(), logoutHandler(), LogoutHandlerOptions, logServerLogoutCommandError(), logSuccessfulLogoutResponse(), nestedErrorMessage() (+8 more)

### Community 75 - "Chat History Panel"
Cohesion: 0.16
Nodes (11): ChatHistoryMessageRow(), ChatHistoryPanelProps, classFromTags(), filterChatHistoryMessages(), formatTimestamp(), getMessageClass(), isExcludedFromChatPanel(), isWhisperOrParty() (+3 more)

### Community 76 - "Panel Layout Clamp"
Cohesion: 0.23
Nodes (11): mergePanelMetadataFromDefault(), resolveInitialPanelLayout(), applyOptionalContentMinHeight(), clampDimensionsToViewport(), clampPanelLayoutToViewport(), clampSinglePanel(), clampTopLeftWithinBounds(), layoutFitsViewport() (+3 more)

### Community 77 - "Panel Context Hooks"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 78 - "Auth Session Apply"
Cohesion: 0.24
Nodes (14): AuthSessionSetters, persistTokensAndApplySession(), SetBool, SetChars, SetStep, toCharacterInfoFromLogin(), AuthSuccessPayload, SanitizedCredentials (+6 more)

### Community 79 - "Command Store"
Cohesion: 0.16
Nodes (15): CommandActions, CommandAlias, CommandHistoryEntry, CommandSelectors, CommandState, CommandStore, CommandStoreGet, CommandStoreSet (+7 more)

### Community 80 - "App Router Pages"
Cohesion: 0.17
Nodes (8): AppRouter(), DialogueEditorPage, SkillsPage, SkillEntry, SkillsPage(), hoisted, getInspectorOptions(), initializeXStateInspector()

### Community 81 - "Container Split Handlers"
Cohesion: 0.20
Nodes (14): createKeyDownHandler(), createTransferHandlers(), DraggedItemSetter, DragSourceSetter, DragTargetSetter, DropEventBag, handleDragStartEvent(), handleDropEvent() (+6 more)

### Community 82 - "Game Log Tests"
Cohesion: 0.17
Nodes (10): GameLogPanel(), TerminalButtonProps, useGameLogPanelState(), TerminalButtonProps, filterGameLogMessages(), GameLogFilterMessage, GameLogFilterState, messagePassesGameLogFilters() (+2 more)

### Community 83 - "Empty Occupants Diagnostics"
Cohesion: 0.29
Nodes (11): getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), useEventProcessing(), useGameClientV2ContainerConnectionEffects(), GameClientV2NetworkPhase, useGameClientV2ContainerNetworkPhase() (+3 more)

### Community 84 - "Container Drag Tests"
Cohesion: 0.17
Nodes (12): ContainerSplitPane(), ContainerSplitPaneProps, ContainerInventoryPaneProps, mockMutationTokens, mockOnTransfer, mockOpenContainers, mockPlayer, mockMutationTokens (+4 more)

### Community 85 - "Room Edit Form"
Cohesion: 0.17
Nodes (9): EnvironmentOption, fieldBorderClass(), RoomEditDescriptionField(), RoomEditFormData, RoomEditModalForm(), RoomEditModalFormProps, RoomEditNameField(), RoomEditSubZoneField() (+1 more)

### Community 86 - "GameClient V2 Container"
Cohesion: 0.27
Nodes (9): GameClientV2Container(), useGameClientV2Container(), useGameClientV2ContainerHealthSync(), useGameClientV2GameModelState(), useGameClientV2SurvivalAndTimeState(), useGameClientV2UiAndTabsState(), useGameClientV2MemoryMonitorEffect(), fetchSpy (+1 more)

### Community 87 - "Creation Flow Views"
Cohesion: 0.27
Nodes (9): AppCreationFlowViews(), creationShell(), renderNameStep(), renderProfessionStep(), renderSkillsStep(), renderStatsStep(), API_BASE_URL, API_V1_BASE (+1 more)

### Community 88 - "Profession Error Tests"
Cohesion: 0.24
Nodes (13): createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions(), createDefaultRollStatsFetchResponse(), createDefaultRollStatsResponseBody(), createMockProfessions(), createMockSkills(), DEFAULT_ROLLED_STATS (+5 more)

### Community 89 - "Message Batcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 90 - "Container Split View"
Cohesion: 0.19
Nodes (10): ContainerItemRow(), ContainerSplitPaneView(), ContainerSplitPaneViewModel, ContainerSplitPaneViewProps, formatWeaponStats(), getItemWeapon(), isFirstPaneItem(), renderSplitPaneItem() (+2 more)

### Community 91 - "Panel Resize Handles"
Cohesion: 0.19
Nodes (10): DraggablePanelResizeHandles(), DraggablePanelResizeHandlesProps, HANDLE_CONFIGS, HandleConfig, DraggablePanelView(), DraggablePanelViewProps, headerClasses, panelLayoutStyle() (+2 more)

### Community 92 - "Connection Store"
Cohesion: 0.21
Nodes (11): ConnectionActions, ConnectionHealth, ConnectionMetadata, ConnectionSelectors, ConnectionState, ConnectionStore, createInitialState(), GameEvent (+3 more)

### Community 95 - "Draggable Panel Tests"
Cohesion: 0.18
Nodes (5): DraggablePanel, DraggablePanelTest(), PANEL_CONTROLS, PANEL_VARIANTS, mockConsoleLog

### Community 96 - "Map Performance Utils"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 97 - "Minimap Panel Section"
Cohesion: 0.23
Nodes (7): minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapPanelSection(), MinimapPanelSectionProps, PanelContainer, { MockRnd }, MockRndProps

### Community 98 - "Panel Context Runtime"
Cohesion: 0.21
Nodes (9): defaultPanels, PanelContext, PanelContextType, PanelLayout, PanelPosition, PanelProvider(), PanelProviderProps, PanelSize (+1 more)

### Community 99 - "Grid Layout Manager"
Cohesion: 0.20
Nodes (5): GridLayoutManager(), GridLayoutManagerProps, layoutConfig, PanelComponent, ResponsiveGridLayout

### Community 100 - "Chat History Dock Tests"
Cohesion: 0.25
Nodes (9): chatHistoryLayoutIdentity, chatHistoryLayoutState, defaultChatHistoryLayoutKey, dockTest, mockPanelRecord(), mockPanelRecordCore(), mockPanelRecordFlags(), mockUsePanelManagerNoops() (+1 more)

### Community 101 - "Modal Container Shells"
Cohesion: 0.24
Nodes (5): maxWidthClasses, ModalContainer(), ModalContainerProps, renderOpenModal(), useModalEscapeKey()

### Community 102 - "Session Store"
Cohesion: 0.31
Nodes (8): createInitialState(), createSessionActions(), SessionActions, SessionSelectors, SessionState, SessionStore, touchActivity(), useSessionStore

### Community 103 - "Panel Layout Validation"
Cohesion: 0.56
Nodes (6): isPanelPosition(), isPanelSize(), isPanelState(), isPanelStateRecord(), isRecord(), hasRequiredPanelStateTypes()

### Community 104 - "Container Keyboard Tests"
Cohesion: 0.25
Nodes (7): fetchSpy, mockMutationTokens, mockOpenContainer, mockOpenContainers, mockPlayer, mockRoom, mockSelectContainer

### Community 105 - "Chat Panel Edge Tests"
Cohesion: 0.46
Nodes (4): ChatPanelTestMessage, createChatPanelDefaultProps(), mockMessages, mockConsoleLog

### Community 106 - "Performance Monitor Hook"
Cohesion: 0.29
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 107 - "Grid Layout Hook"
Cohesion: 0.33
Nodes (5): layoutConfig, PanelState, STORAGE_KEYS, useGridLayout(), UseGridLayoutReturn

### Community 108 - "Game Client Logout"
Cohesion: 0.60
Nodes (4): forceLogoutFallback(), performGameClientLogout(), stillShowingGameClient(), useGameClientV2ContainerLogoutAndRespawn()

### Community 110 - "Connection Panel"
Cohesion: 0.50
Nodes (3): ConnectionPanel(), ConnectionPanelProps, localStorageMock

### Community 112 - "Logout Integration Tests"
Cohesion: 0.50
Nodes (3): fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full

### Community 120 - "Event Schema Docs"
Cohesion: 1.00
Nodes (3): Event Schema (Client Event Log), Critical State Handoffs, Event-Sourced Projector

## Knowledge Gaps
- **526 isolated node(s):** `fetchSpy`, `mockLogoutHandler`, `fetchSpy`, `fetchSpy`, `mockLogoutHandler` (+521 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `EldritchIcon()` connect `Chat Message Widgets` to `Chat Channel Filtering`, `Monitoring Panel Stats`, `Corpse Overlay UI`, `Command Panel Tests`, `Expanded Panel Chrome`, `Chat History Panel`, `Chat Channel Header`, `Command Panel UI`, `Mythos Time HUD`, `Panel Container Views`, `Chat Panel Tests`, `Game Log Panel`, `Game Info Panel`, `Panel Resize Handles`, `Backpack Inventory Tab`, `Channel Selector UI`, `Chat Export Search`, `Draggable Panel Tests`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Why does `logger` connect `Player Status Hooks` to `Game Client V2`, `Connection Hook Tests`, `Profession Character Cards`, `Event Log Messages`, `Character Name Screen`, `Mythos Time HUD`, `Event Handler Pipeline`, `Character Selection Screen`, `Room Event Handlers`, `Combat Event Handlers`, `Player Event Handlers`, `Chat Message Handlers`, `Dialogue API Client`, `Map Page Router`, `Room Info Panel`, `Death Delirium Screens`, `Profession Selection Screen`, `Logout Handler`, `App Router Pages`, `Game Client Logout`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `MythosIcons` connect `Chat Message Widgets` to `Chat Channel Filtering`, `Corpse Overlay UI`, `Command Panel Tests`, `Expanded Panel Chrome`, `Chat History Panel`, `Chat Channel Header`, `Command Panel UI`, `Mythos Time HUD`, `Panel Container Views`, `Chat Panel Tests`, `Game Log Panel`, `Game Info Panel`, `Panel Resize Handles`, `Backpack Inventory Tab`, `Channel Selector UI`, `Chat Export Search`, `Draggable Panel Tests`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **What connects `fetchSpy`, `mockLogoutHandler`, `fetchSpy` to the rest of the system?**
  _526 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Chat Channel Filtering` be split into smaller, more focused modules?**
  _Cohesion score 0.05641025641025641 - nodes in this community are weakly interconnected._
- **Should `Game Client V2` be split into smaller, more focused modules?**
  _Cohesion score 0.0712280701754386 - nodes in this community are weakly interconnected._
- **Should `Game Terminal Core` be split into smaller, more focused modules?**
  _Cohesion score 0.059322033898305086 - nodes in this community are weakly interconnected._