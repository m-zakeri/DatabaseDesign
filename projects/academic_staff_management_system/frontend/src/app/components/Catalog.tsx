import React from 'react'

type Props = {}

export default function Catalog({}: Props) {
  return (
    <div className="bg-[#D9D9D9] grid md:relative md:w-full md:h-[166px]">
      <div className="bg-[#FFB67C99] flex flex-col text-center md:text-left text-[#4B3421] p-[35px] md:w-[600px] md:absolute md:top-[88px] md:pl-[180px]">
        <h3 className="text-[24px] font-bold">ACADEMIC STAFF OF</h3>
        <h1 className="text-[40px] font-bold">UNIVERSITY NAME</h1>
      </div>
    </div>
  );
}
