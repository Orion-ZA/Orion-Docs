# 📘 Third-Party Code

A place to document all our external libraries and third party code used throughout the project. A how we came to the conclusion of using it and how to use it as well.

------------------------------------------------------------------------

## 1. Overview

-   **Library/Service Name**: Mapbox
-   **Category**: Mapping & Geolocation
-   **Purpose**: Provides customizable maps, geolocation, and
    visualization features for our AllTrails clone app.

------------------------------------------------------------------------

## 2. Why We Use It

Mapbox is a powerful mapping and location platform that gives us the
flexibility and customization we need to build an AllTrails-like
application. Unlike out-of-the-box solutions, Mapbox provides deep
control over map styles, interactivity, and data visualization.

### Benefits of Mapbox for Our Project

-   **Customizable Map Styles**: We can design trail maps that match our
    brand and highlight hiking routes better than standard road maps.
-   **Lightweight and Fast**: Mapbox GL JS uses WebGL for rendering,
    making it smooth and performant, even with complex trail overlays.
-   **Offline Support**: Useful for hikers who may not always have
    stable internet connections.
-   **Advanced Features**: Heatmaps, 3D terrain, route drawing, and
    geocoding APIs are included.
-   **Developer Friendly**: Well-documented APIs and strong React
    ecosystem integrations (`react-map-gl`, `mapbox-gl`).

------------------------------------------------------------------------

## 3. Installation & Setup

### Install dependencies

``` bash
npm install react-map-gl mapbox-gl @mapbox/mapbox-sdk
```

### Get a Mapbox access token

Sign up at [mapbox.com](https://www.mapbox.com/) → create a free account
→ get your API token.

### Environment Configuration

Add your Mapbox token to your environment variables:

``` bash
REACT_APP_MAPBOX_TOKEN=your_mapbox_token_here
```

------------------------------------------------------------------------

## 4. How We Use It in Orion

### Core Implementation

Our Mapbox integration is primarily handled through two main components:

#### TrailMap Component (`src/components/trails/TrailMap.js`)

This is our main map component that handles:

- **Interactive Trail Display**: Shows trail markers with difficulty-based colors and icons
- **Trail Routes**: Renders trail paths as GeoJSON LineString layers
- **User Location**: Displays user's current location with a pulsing marker
- **Trail Submission**: Handles map clicks for trail submission mode
- **Hover Cards**: Shows trail details on hover with mini cards
- **Route Drawing**: Supports drawing custom routes for trail submissions

``` jsx
import Map, { Marker, Popup, Source, Layer } from 'react-map-gl/mapbox';
import "mapbox-gl/dist/mapbox-gl.css";

const TrailMap = ({
  viewport,
  setViewport,
  mapRef,
  trails,
  hoveredTrail,
  setHoveredTrail,
  selectedTrail,
  setSelectedTrail,
  onTrailClick,
  onMapClick,
  userLocation,
  // ... other props
}) => {
  return (
    <Map
      ref={mapRef}
      {...viewport}
      onMove={evt => setViewport(evt.viewState)}
      onLoad={handleMapLoad}
      onClick={onMapClick}
      mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
      style={{ width: '100%', height: '100%' }}
      mapStyle="mapbox://styles/mapbox/standard"
    >
      {/* Trail markers with difficulty-based styling */}
      {trails.map(trail => (
        <Marker key={trail.id} longitude={trail.longitude} latitude={trail.latitude}>
          <div className="trail-marker" style={{
            backgroundColor: getDifficultyColor(trail.difficulty)
          }}>
            {getDifficultyIcon(trail.difficulty)}
          </div>
        </Marker>
      ))}
      
      {/* Trail routes as GeoJSON layers */}
      {trails.map(trail => (
        <Source key={`route-${trail.id}`} type="geojson" data={{
          type: 'Feature',
          geometry: { type: 'LineString', coordinates: trail.route }
        }}>
          <Layer type="line" paint={{
            'line-color': getDifficultyColor(trail.difficulty),
            'line-width': 3,
            'line-opacity': 0.8
          }} />
        </Source>
      ))}
    </Map>
  );
};
```

#### MapControls Component (`src/components/trails/MapControls.js`)

Provides interactive map controls:

- **Zoom Controls**: Zoom in/out buttons
- **Compass Reset**: Reset map to north when rotated
- **Location Finding**: Find and center on user's location
- **Recenter**: Recenter map on current location

### Key Features We've Implemented

1. **Trail Visualization**:
   - Color-coded markers based on difficulty (Easy: Green, Moderate: Yellow, Hard: Red)
   - Trail routes displayed as colored lines matching difficulty
   - Hover cards showing trail details

2. **Interactive Map Controls**:
   - Zoom in/out functionality
   - Compass reset for rotated maps
   - User location finding and centering
   - Map state tracking (bearing, pitch, center)

3. **Trail Submission Mode**:
   - Click-to-place trail markers
   - Route drawing with numbered waypoints
   - Real-time route visualization

4. **User Experience**:
   - Loading overlays during data fetching
   - Smooth animations and transitions
   - Responsive design for mobile and desktop

### Map State Management

We track several map states in our main Trails page:

``` jsx
// Map state tracking
const [mapBearing, setMapBearing] = useState(0);
const [mapPitch, setMapPitch] = useState(0);
const [mapCenter, setMapCenter] = useState(null);

// Viewport state for map positioning
const [viewport, setViewport] = useState({
  longitude: 28.0473,  // Default to Johannesburg, South Africa
  latitude: -26.2041,
  zoom: 10
});
```

### Dependencies Used

Our current implementation uses these specific Mapbox packages:

``` json
{
  "dependencies": {
    "@mapbox/mapbox-sdk": "^0.16.1",
    "mapbox-gl": "^3.14.0", 
    "react-map-gl": "^8.0.4"
  }
}
```

### Testing Strategy

We've implemented comprehensive testing for our Mapbox components:

- **Mocked Components**: `TrailMap` and `MapControls` are mocked in Jest tests
- **Test Coverage**: Map interactions, trail rendering, and user controls
- **Environment Setup**: Test token configuration in `test-utils.js`

------------------------------------------------------------------------

## 5. Comparison to Alternatives

### Mapbox vs Google Maps

  --------------------------------------------------------------------------
  Feature             Mapbox                      Google Maps
  ------------------- --------------------------- --------------------------
  **Customization**   Highly customizable styles  Limited customization
                      & layers                    (mostly overlays)

  **Performance**     WebGL rendering, smooth &   Raster-based, less smooth
                      modern                      with many layers

  **Offline Maps**    Supported (paid tiers +     Limited offline support
                      SDKs)                       

  **Pricing**         Free tier generous,         Higher costs for heavy
                      pay-as-you-go               usage

  **Developer         Great React/JS support,     Mature ecosystem, but less
  Ecosystem**         strong community            flexible styling

  **Use Case Fit**    Ideal for                   Best for general-purpose
                      trail/fitness/outdoor apps  navigation
  --------------------------------------------------------------------------

------------------------------------------------------------------------

## 6. Current Implementation Status

### ✅ Completed Features

- **Trail Markers**: Color-coded markers with difficulty indicators
- **Trail Routes**: GeoJSON LineString rendering with custom styling
- **User Location**: GPS location display with pulsing marker
- **Map Controls**: Zoom, compass reset, location finding
- **Trail Submission**: Interactive map clicking for trail placement
- **Route Drawing**: Custom route creation with waypoint markers
- **Hover Cards**: Trail details on marker hover
- **Responsive Design**: Mobile and desktop optimized

### 🔄 In Progress / Future Enhancements

- **Offline Maps**: Caching for areas with poor connectivity
- **3D Terrain**: Elevation visualization for trail profiles
- **Heatmaps**: Popular trail areas visualization
- **Custom Map Styles**: Brand-specific trail-focused map themes

------------------------------------------------------------------------

## 7. Risks & Considerations

-   **API Limits**: Mapbox free tier has usage limits (50,000 map loads/month)
-   **Token Security**: Environment variable management for production
-   **Offline Features**: Some advanced features require paid plans
-   **Dependency Risk**: Reliance on external third-party service
-   **Performance**: Large numbers of trail markers may impact rendering

### Mitigation Strategies

- Monitor API usage through Mapbox dashboard
- Implement marker clustering for high-density areas
- Use environment-specific tokens for development/production
- Consider fallback strategies for service outages

------------------------------------------------------------------------

## 8. Conclusion

For our AllTrails clone, **Mapbox has proven to be the right choice** because:

- ✅ **Trail-focused Features**: Perfect for outdoor/hiking applications
- ✅ **Cost Effective**: Generous free tier suitable for our current scale
- ✅ **React Integration**: Seamless integration with our React ecosystem
- ✅ **Customization**: Full control over map styling and trail visualization
- ✅ **Performance**: Smooth WebGL rendering even with complex overlays

Our current implementation successfully provides a professional, scalable, and user-friendly mapping solution that enhances the hiking/trails experience in our Orion application.
