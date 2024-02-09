import React from "react";
import SelectInput from "./SelectInput";
import CharFieldInput from "./CharFieldInput";

const PhoneForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Phone Number</legend>
      <SelectInput
        id="phone_type"
        name="phone_type"
        items={["Mobile", "Work", "Home"]}
      >
        Phone Type*
      </SelectInput>
      <CharFieldInput id="phone_number" name="phone_number">
        Phone Number*
      </CharFieldInput>
    </fieldset>
  );
};

export default PhoneForm;
