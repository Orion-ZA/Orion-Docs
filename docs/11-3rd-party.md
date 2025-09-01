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
npm install react-map-gl mapbox-gl
```

### Get a Mapbox access token

Sign up at [mapbox.com](https://www.mapbox.com/) → create a free account
→ get your API token.

------------------------------------------------------------------------

## 4. Usage Example

### Basic Example

``` jsx
import React from "react";
import Map from "react-map-gl";

const MAPBOX_TOKEN = process.env.REACT_APP_MAPBOX_TOKEN;

export default function TrailMap() {
  return (
    <Map
      initialViewState={{
        longitude: -122.44,
        latitude: 37.78,
        zoom: 12
      }}
      style={{ width: "100%", height: "400px" }}
      mapStyle="mapbox://styles/mapbox/outdoors-v12"
      mapboxAccessToken={MAPBOX_TOKEN}
    />
  );
}
```

### Adding Trails

We can overlay custom trail data using **GeoJSON layers**, markers, and
popups to replicate AllTrails-like functionality.

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

## 6. Risks & Considerations

-   API limits apply (check Mapbox pricing for scale).
-   Some offline features may require paid plans.
-   Dependency on an external third-party service.

------------------------------------------------------------------------

## 7. Conclusion

For our AllTrails clone, **Mapbox is the better choice** because: - It
allows **trail-focused custom maps** (outdoor, satellite,
topographic). - It's **cheaper and more flexible** than Google Maps at
scale. - It integrates smoothly with **React and modern web tech**.

This will give us a professional, scalable, and user-friendly mapping
solution for our hiking/trails app.
