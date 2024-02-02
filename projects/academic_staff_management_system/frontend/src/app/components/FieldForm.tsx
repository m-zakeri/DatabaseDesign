import React from "react";
import CharFieldInput from "./CharFieldInput";
import SelectInput from "./SelectInput";

const FieldForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Field</legend>
      <CharFieldInput name="field_name" id="field_name">
        Field Name*
      </CharFieldInput>
      <SelectInput
        id="department"
        name="department"
        items={["Department#1", "Department#2"]}
      >
        Department*
      </SelectInput>
      <SelectInput id="head" name="head" items={["Professor#1", "Professor#2"]}>
        Head*
      </SelectInput>
    </fieldset>
  );
};

export default FieldForm;
