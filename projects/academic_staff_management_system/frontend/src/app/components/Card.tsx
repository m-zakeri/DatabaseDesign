import Link from "next/link";
import React from "react";

type Props = {};

export default function Card({}: Props) {
  return (
    <div className="bg-main-peach p-[3px] pl-[10px] rounded-sm">
      <div className="h-[150px] lg:h-auto bg-white rounded-sm px-[15px] py-[10px] flex justify-between">
        <div className="flex flex-col lg:gap-3 justify-between">
          <div>
            <h1 className="text-[24px] text-main-highlight-text font-bold ">
              Professor Name
            </h1>
            <h2 className="text-[20px] text-main-highlight-text font-bold ">
              Academic Rank
            </h2>
          </div>
          <div>
            <div className="hidden lg:block text-main-dark">
              <p>Research Field</p>
              <p>Phone number</p>
              <p>Email</p>
            </div>
            <Link className="text-[16px] text-main-highlight-text" href="">
              More
            </Link>
          </div>
        </div>
        <img className="bg-main-grey w-[90px] lg:w-[120px]"></img>
      </div>
    </div>
  );
}
