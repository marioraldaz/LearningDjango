import React from "react";
export function Loading() {
  return (
    <div className="flex min-h-screen items-center justify-center relative ">
      <div className="w-1/5">
        <img alt="loading" src="/reload.svg" className="w-full" />
      </div>
    </div>
  );
}

export default Loading;
