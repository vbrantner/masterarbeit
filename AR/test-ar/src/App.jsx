import { useState } from "react";
import { ARCanvas, ARMarker } from "@artcom/react-three-arjs";
import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

import "./App.css";

function Scene() {
  const gltf = useLoader(GLTFLoader, "/model-transparent.gltf");
  return (
    <primitive object={gltf.scene} scale={0.111} position={[-0.1, 0.2, -0.4]} />
  );
}

function Box() {
  return (
    <mesh
      onClick={(e) => {
        window.alert("click");
        console.log(e);
      }}
    >
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={"hotpink"} />
    </mesh>
  );
}

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        <h1>test</h1>
        {/* <img src="/hiro.png" alt="Logo"></img> */}
        <ARCanvas
          sourceType={"image"}
          sourceUrl={"./hiro.png"}
          cameraParametersUrl={"./camera_para.dat"}
          matrixCodeType={"4x4"}
          detectionMode={"mono_and_matrix"}
          gl={{
            antialias: false,
            powerPreference: "default",
            physicallyCorrectLights: true,
          }}
          onCameraStreamReady={() => console.log("Camera stream ready")}
          onCameraStreamError={() => console.error("Camera stream error")}
          onCreated={({ gl }) => {
            gl.setSize(window.innerWidth, window.innerHeight);
          }}
        >
          <ambientLight />
          <pointLight position={[0, 0, 0]} intensity={10.0} />
          <ARMarker
            type={"barcode"}
            matrixCodeType={"4x4"}
            barcodeValue={0}
            onMarkerFound={() => {
              console.log("Marker Found");
            }}
          >
            <Scene />
          </ARMarker>
        </ARCanvas>
        ,
      </div>
    </>
  );
}

export default App;
