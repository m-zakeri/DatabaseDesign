import React from "react";
import CharFieldInput from "./CharFieldInput";
import TextAreaInput from "./TextAreaInput";
import IntegerFieldInput from "./IntegerFieldInput";
import SelectInput from "./SelectInput";

const LaboratoryForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Laboratory</legend>
      <CharFieldInput name="laboratory_name" id="laboratory_name">
        Laboratory Name*
      </CharFieldInput>
      <TextAreaInput name="equipments" id="equipments">
        Equipments*
      </TextAreaInput>
      <IntegerFieldInput name="lab_capacity" id="lab_capacity">
        Laboratory Capacity*
      </IntegerFieldInput>
      <IntegerFieldInput name="lab_budget" id="lab_budget">
        Laboratory Budget*
      </IntegerFieldInput>
      <SelectInput
        name="managers"
        id="managers"
        items={["Manager#1", "Manager#2"]}
      >
        Manager*
      </SelectInput>
      <SelectInput
        name="schedules"
        id="schedules"
        items={["Schedule#1", "Schedule#2"]}
      >
        Schedule*
      </SelectInput>
    </fieldset>
  );
};

export default LaboratoryForm;
