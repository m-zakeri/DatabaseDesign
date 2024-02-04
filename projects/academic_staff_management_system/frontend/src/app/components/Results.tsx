import React from "react";
import Card from "./Card";

type Props = {
  persons: (Person & User)[];
};

export default function Results({ persons }: Props) {
  return (
    <div className="lg:flex-auto">
      <h2 className="text-main-highlight-text text-[24px] font-bold">
        Results
      </h2>
      <div className="mt-[15px] flex flex-col gap-[10px]">
        {persons.map((person) => (<Card key={person.national_code} person={person}/>))}
      </div>
    </div>
  );
}
