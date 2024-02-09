import React from "react";

type Props = {};

export default function Search({}: Props) {
  return (
    <div className="bg-main-peach p-[8px] rounded-[10px]">
      <input
        placeholder="Search"
        className="w-full p-[15px] text-[20px]  rounded-[10px] placeholder-main-dark"
      />
    </div>
  );
}
