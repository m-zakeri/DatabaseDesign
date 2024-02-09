import React from "react";
import IntegerFieldInput from "./IntegerFieldInput";
import DateTimeInput from "./DateTimeInput";
import CharFieldInput from "./CharFieldInput";
import CheckInput from "./CheckInput";
import SelectInput from "./SelectInput";

const EmployeeForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Employee</legend>
      <SelectInput name="person" id="person" items={["Person#1", "Person#2"]}>
        Person*
      </SelectInput>
      <IntegerFieldInput name="salary" id="salary">
        Salary*
      </IntegerFieldInput>
      <DateTimeInput name="hire_date" id="hire_date">
        Hire Date*
      </DateTimeInput>
      <CharFieldInput name="office_hours" id="office_hours">
        Office Hours*
      </CharFieldInput>
      <CharFieldInput name="status" id="status">
        Status*
      </CharFieldInput>
      <SelectInput name="office" id="office" items={["Office#1", "Office#2"]}>
        Office*
      </SelectInput>
      <CheckInput name="is_committee" id="is_committee" is_required={false}>
        Is a Committee
      </CheckInput>
    </fieldset>
  );
};

export default EmployeeForm;
