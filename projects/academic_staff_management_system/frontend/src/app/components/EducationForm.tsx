import CharFieldInput from "./CharFieldInput";
import DateTimeInput from "./DateTimeInput";
import DecimalInput from "./DecimalInput";
import SelectInput from "./SelectInput";

const EducationForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Education</legend>
      <DateTimeInput id="start_date" name="start_date">
        Start Date*
      </DateTimeInput>
      <DateTimeInput id="graduation_date" name="graduation_date">
        Graduation Date*
      </DateTimeInput>
      <CharFieldInput name="major" id="major">
        Major*
      </CharFieldInput>
      <CharFieldInput name="degree" id="degree">
        Degree*
      </CharFieldInput>
      <DecimalInput name="gpa" id="gpa" min={0} max={4}>
        GPA*
      </DecimalInput>
      <CharFieldInput name="institution_name" id="institution_name">
        Institution Name*
      </CharFieldInput>
      <SelectInput
        name="address"
        id="address"
        items={["Address#1", "Address#2"]}
      >
        Address*
      </SelectInput>
    </fieldset>
  );
};

export default EducationForm;
