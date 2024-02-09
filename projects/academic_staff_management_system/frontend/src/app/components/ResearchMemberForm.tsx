import React from "react";
import SelectInput from "./SelectInput";
import CharFieldInput from "./CharFieldInput";

const ResearchMemberForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Research Member</legend>
      <SelectInput
        name="professor"
        id="professor"
        items={["Professor#1", "Professor#2"]}
      >
        Professor*
      </SelectInput>
      <SelectInput
        name="researcher"
        id="researcher"
        items={["Researcher#1", "Researcher#2"]}
      >
        Researcher*
      </SelectInput>
      <SelectInput
        name="research"
        id="research"
        items={["Research#1", "Research#2"]}
      >
        Research*
      </SelectInput>
      <CharFieldInput name="role" id="role">
        Role*
      </CharFieldInput>
    </fieldset>
  );
};

export default ResearchMemberForm;
