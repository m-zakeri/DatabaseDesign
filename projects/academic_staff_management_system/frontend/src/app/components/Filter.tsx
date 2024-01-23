import React from "react";

type Props = {};

export default function Filter({}: Props) {
  return (
    <div>
      <h2 className="text-[24px] text-[#B38A6A] font-bold">FILTERS</h2>
      <form action="" className="mt-[30px]">
        <div className="bg-[#FFB67C] py-[15px] px-[11.5px]">
          <input placeholder="Search" className="w-full py-[20px] pl-[15px] text-[24px] font-bold" />
        </div>
        <ul></ul>
      </form>
    </div>
  );
}
