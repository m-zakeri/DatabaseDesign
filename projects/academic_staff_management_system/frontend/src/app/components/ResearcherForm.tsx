import React from "react";
import SelectInput from "./SelectInput";

const ResearcherForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Researcher</legend>
      <SelectInput
        name="employee"
        id="employee"
        items={["Employee#1", "Employee#2"]}
      >
        Employee*
      </SelectInput>
      <SelectInput name="field" id="field" items={["Field#1", "Field#2"]}>
        Field*
      </SelectInput>
    </fieldset>
  );
};

export default ResearcherForm;
