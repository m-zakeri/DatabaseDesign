import React from 'react'

type Props = {}

export default function Catalog({}: Props) {
  return (
    <div className="bg-main-grey grid md:relative lg:w-full lg:h-[166px]">
      <div className="bg-main-peach/60 flex flex-col text-center lg:text-left text-main-dark p-[35px] lg:w-[600px] lg:absolute lg:top-[88px] lg:pl-[180px]">
        <h3 className="text-[24px] font-bold">ACADEMIC STAFF OF</h3>
        <h1 className="text-[40px] font-bold">UNIVERSITY NAME</h1>
      </div>
    </div>
  );
}
