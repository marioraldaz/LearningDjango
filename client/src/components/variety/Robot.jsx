// LottieAnimation.js
import React from "react";
import Lottie from "react-lottie";
import animationData from "../../data/robotAnimation.json"; // replace with your JSON file path
import animationData2 from "../../data/thinkingAnimation.json";
export const Robot = ({ loading }) => {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: animationData,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  };
  const defaultOptions2 = {
    loop: true,
    autoplay: true,
    animationData: animationData2,
    rendererSettings: {
      preserveAspectRatio: "xMidYMid slice",
    },
  };

  return (
    <div style={{ width: 400, height: 400 }}>
      <div className="absolute z-10">
        <Lottie options={defaultOptions} />
      </div>
      {loading && (
        <div className="absolute top-0 z-0 w-32 right-0">
          <Lottie options={defaultOptions2} />
        </div>
      )}
    </div>
  );
};

export default Robot;
