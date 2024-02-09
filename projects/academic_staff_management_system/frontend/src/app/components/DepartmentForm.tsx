import React from "react";
import CharFieldInput from "./CharFieldInput";
import IntegerFieldInput from "./IntegerFieldInput";
import DateTimeInput from "./DateTimeInput";
import SelectInput from "./SelectInput";

const DepartmentForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Department</legend>
      <CharFieldInput name="department_name" id="department_name">
        Department Name*
      </CharFieldInput>
      <IntegerFieldInput name="budget" id="budget" min={0}>
        Budget*
      </IntegerFieldInput>
      <DateTimeInput
        name="department_creation_date"
        id="department_creation_date"
      >
        Department Creation Date*
      </DateTimeInput>
      <SelectInput
        name="faculty"
        id="faculty"
        items={["Faculty#1", "Faculty#2"]}
      >
        Faculty*
      </SelectInput>
    </fieldset>
  );
};

export default DepartmentForm;
