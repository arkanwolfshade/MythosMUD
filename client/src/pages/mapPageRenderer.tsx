import { RoomMapEditor } from '../components/map/RoomMapEditor.tsx';
import { RoomMapViewer } from '../components/map/RoomMapViewer.tsx';
import { API_V1_BASE } from '../utils/config.js';
import type { MapPageState } from './mapPageState.ts';
import { MapPageAuthRequiredView, MapPageErrorView, MapPageLoadingView } from './mapPageStatusViews.tsx';

interface AuthenticatedMapProps {
  editMode: boolean;
  plane: string;
  zone: string;
  subZone?: string;
  currentRoomId?: string;
  authToken: string;
}

function renderAuthenticatedMapView({
  editMode,
  plane,
  zone,
  subZone,
  currentRoomId,
  authToken,
}: AuthenticatedMapProps) {
  if (editMode) {
    return (
      <RoomMapEditor
        plane={plane}
        zone={zone}
        subZone={subZone}
        currentRoomId={currentRoomId}
        authToken={authToken}
        baseUrl={API_V1_BASE}
      />
    );
  }

  return (
    <RoomMapViewer
      plane={plane}
      zone={zone}
      subZone={subZone}
      currentRoomId={currentRoomId}
      authToken={authToken}
      baseUrl={API_V1_BASE}
    />
  );
}

interface MapViewResolvedProps {
  plane: string;
  zone: string;
  subZone?: string;
  currentRoomId?: string;
}

function resolveMapViewProps(state: MapPageState): MapViewResolvedProps {
  if (!state.currentRoom) {
    return {
      plane: 'earth',
      zone: 'arkhamcity',
      subZone: undefined,
      currentRoomId: undefined,
    };
  }

  return {
    plane: state.currentRoom.plane,
    zone: state.currentRoom.zone,
    subZone: state.currentRoom.subZone,
    currentRoomId: state.currentRoom.id,
  };
}

function renderStatusGate(state: MapPageState) {
  if (state.isLoading) {
    return <MapPageLoadingView />;
  }

  if (state.error) {
    return <MapPageErrorView error={state.error} />;
  }

  if (!state.authToken) {
    return <MapPageAuthRequiredView />;
  }

  return null;
}

export function renderMapPageState(state: MapPageState) {
  const statusView = renderStatusGate(state);
  if (statusView) {
    return statusView;
  }

  const viewProps = resolveMapViewProps(state);

  return (
    <div className="h-screen w-screen bg-mythos-terminal-background">
      {renderAuthenticatedMapView({
        editMode: state.editMode,
        plane: viewProps.plane,
        zone: viewProps.zone,
        subZone: viewProps.subZone,
        currentRoomId: viewProps.currentRoomId,
        authToken: state.authToken!,
      })}
    </div>
  );
}
