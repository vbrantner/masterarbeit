/*
This file handles the client-side WebRTC connection.

1. Initialize WebRTC peer connection
2. Create and send offer to the server
3. Set up media stream from the server
4. Handle the start button click
*/

let pc = null;

function negotiate() {
    pc.addTransceiver('video', { direction: 'recvonly' });
    return pc.createOffer().then(offer => {
        return pc.setLocalDescription(offer);
    }).then(() => {
        return new Promise(resolve => {
            if (pc.iceGatheringState === 'complete') {
                resolve();
            } else {
                function checkState() {
                    if (pc.iceGatheringState === 'complete') {
                        pc.removeEventListener('icegatheringstatechange', checkState);
                        resolve();
                    }
                }
                pc.addEventListener('icegatheringstatechange', checkState);
            }
        });
    }).then(() => {
        let offer = pc.localDescription;
        return fetch('/offer', {
            body: JSON.stringify({ sdp: offer.sdp, type: offer.type }),
            headers: { 'Content-Type': 'application/json' },
            method: 'POST'
        });
    }).then(response => response.json())
        .then(answer => pc.setRemoteDescription(answer))
        .catch(e => console.error(e));
}

function start() {
    pc = new RTCPeerConnection();
    pc.addEventListener('track', evt => {
        if (evt.track.kind == 'video') {
            document.getElementById('video').srcObject = evt.streams[0];
        }
    });
    negotiate();
}

function stop() {
    document.getElementById('stop').style.display = 'none';

    // close peer connection
    setTimeout(() => {
        pc.close();
    }, 500);
}