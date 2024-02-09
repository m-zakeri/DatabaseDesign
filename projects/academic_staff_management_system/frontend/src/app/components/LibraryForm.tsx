import React from "react";
import CharFieldInput from "./CharFieldInput";
import IntegerFieldInput from "./IntegerFieldInput";
import SelectInput from "./SelectInput";

const LibraryForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Library</legend>
      <CharFieldInput name="library_name" id="library_name">
        Library Name*
      </CharFieldInput>
      <IntegerFieldInput name="library_capacity" id="library_capacity">
        Library Capacity*
      </IntegerFieldInput>
      <IntegerFieldInput name="books" id="books">
        Book Quantity*
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

export default LibraryForm;
