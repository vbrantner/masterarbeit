# GStreamer Backend Example

This is a simple example of using GStreamer to stream video and a Python server to serve the HLS playlist and segments.

## Requirements

- GStreamer (with gst-launch-1.0)
- Python 3.7+
- Flask

## Setup

1. Install GStreamer and its plugins.
2. Install Python dependencies:
   ```
   pip install flask
   ```

## Usage

1. Start the GStreamer pipeline:

   ```
   gst-launch-1.0 v4l2src device="/dev/video0" ! videoconvert ! clockoverlay ! x264enc tune=zerolatency ! mpegtsmux ! hlssink playlist-root=http://localhost:8080 location=./segments/segment_%05d.ts target-duration=5 max-files=5
   ```

2. Start the Python server:

   ```
   python server.py
   ```

3. Open a web browser and navigate to `http://localhost:8080` to view the live stream.

## Note

Make sure to adjust the device path (`/dev/video0`) and IP address in the GStreamer command and `index.html` file to match your setup.
