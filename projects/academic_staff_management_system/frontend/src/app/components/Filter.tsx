import { Dropdown, DropdownItem } from "flowbite-react";
import React from "react";

type Props = {
  name: string;
  choices: [string, string, string][];
};

export function DropdownFilter({ name, choices }: Props) {
  return (
    <div className="bg-main-peach p-[20px] text-[20px] font-bold text-main-white rounded-[10px]">
      <Dropdown className="" label={name} inline dismissOnClick={false}>
        {choices.map((choice) => {
          const [choiceId, choiceName, choiceTitle] = choice;
          return (
            <DropdownItem key={choiceId}>
                <div className="flex gap-5 justify-center items-center">
                    <label htmlFor={choiceId}>{choiceTitle}</label>
                    <input id={choiceId} name={choiceName} type="checkbox" />
                </div>
            </DropdownItem>
          );
        })}
      </Dropdown>
    </div>
  );
}
