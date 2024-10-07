# WebRTC Webcam Server

This project implements a simple WebRTC webcam server using Python and JavaScript.

## Setup

1. Create a Python virtual environment:

   ```
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

1. Make sure your virtual environment is activated.

2. Run the server:

   ```
   python server.py
   ```

3. Open a web browser and navigate to `http://localhost:8080`.

4. Click the "Start" button to begin the WebRTC connection and view your webcam feed.

## Files

- `server.py`: The main Python server script.
- `index.html`: The HTML page served to clients.
- `client.js`: The JavaScript code for handling WebRTC on the client side.
- `requirements.txt`: List of Python package dependencies.

## Note

This server is intended for local use and testing. For production use, additional security measures should be implemented.
