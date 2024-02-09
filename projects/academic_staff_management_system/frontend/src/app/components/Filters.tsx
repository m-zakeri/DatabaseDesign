import React from "react";
import Search from "./Search";
import { DropdownFilter } from "./Filter";

type Props = {};

export default function Filters({}: Props) {
  return (
    <div className="mt-[35px] lg:mt-[0px]">
      <h2 className="text-[24px] text-main-highlight-text font-bold">FILTERS</h2>
      <form action="" className="mt-[15px] flex flex-col gap-[5px]">
        <Search />
        <DropdownFilter
          name="Academic Rank"
          choices={[
            ["full_proffesor", "full_proffesor", "Full Proffesor"],
            [
              "associative_professor",
              "associative_professor",
              "Associative Professor",
            ],
            [
              "assistant_professor",
              "assistent_professor",
              "Assistent Professor",
            ],
            [
              "instructor",
              "instructor",
              "Instructor",
            ],
          ]}
        />
        <DropdownFilter 
          name="Research Area"
          choices={[]}
        />
      </form>
    </div>
  );
}
