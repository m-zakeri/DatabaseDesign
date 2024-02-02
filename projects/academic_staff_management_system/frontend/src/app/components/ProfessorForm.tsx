import React from "react";
import SelectInput from "./SelectInput";
import CheckInput from "./CheckInput";

const ProfessorForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Professor</legend>
      <SelectInput
        name="employee"
        id="employee"
        items={["Employee#1", "Employee#2"]}
      >
        Employee*
      </SelectInput>
      <SelectInput name="rank" id="rank" items={["Rank#1", "Rank#2"]}>
        Rank*
      </SelectInput>
      <SelectInput name="field" id="field" items={["Field#1", "Field#2"]}>
        Field*
      </SelectInput>
      <CheckInput
        name="is_in_committee"
        id="is_in_committee"
        is_required={false}
      >
        Is in Committee
      </CheckInput>
    </fieldset>
  );
};

export default ProfessorForm;
