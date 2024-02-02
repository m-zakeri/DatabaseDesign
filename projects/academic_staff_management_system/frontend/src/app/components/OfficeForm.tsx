import React from "react";
import PhoneForm from "./PhoneForm";
import SelectInput from "./SelectInput";

const OfficeForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Office</legend>
      <PhoneForm></PhoneForm>
      <SelectInput
        name="department"
        id="department"
        items={["Department#1", "Department#2"]}
      >
        Department*
      </SelectInput>
    </fieldset>
  );
};

export default OfficeForm;
