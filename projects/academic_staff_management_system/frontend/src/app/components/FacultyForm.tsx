import React from "react";
import CharFieldInput from "./CharFieldInput";
import DateTimeInput from "./DateTimeInput";
import SelectInput from "./SelectInput";

const FacultyForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Faculty</legend>
      <CharFieldInput id="faculty_name" name="faculty_name">
        Name*
      </CharFieldInput>
      <DateTimeInput id="faculty_creation_date" name="faculty_creation_date">
        Creation Date*
      </DateTimeInput>
      <SelectInput
        name="building"
        id="building"
        items={["Building#1", "Building#2"]}
      >
        Building*
      </SelectInput>
    </fieldset>
  );
};

export default FacultyForm;
