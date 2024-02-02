import React from "react";
import CharFieldInput from "./CharFieldInput";
import SelectInput from "./SelectInput";
import DateTimeInput from "./DateTimeInput";
import PictureInput from "./PictureInput";
import EducationForm from "./EducationForm";
import PhoneForm from "./PhoneForm";

const PersonForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Personal Information</legend>
      <SelectInput name="user" id="user" items={["User#1", "User#2"]}>
        User*
      </SelectInput>
      <SelectInput name="gender" id="gender" items={["Male", "Female"]}>
        Gender*
      </SelectInput>
      <DateTimeInput name="date_of_birth" id="date_of_birth">
        Date of Birth*
      </DateTimeInput>
      <CharFieldInput name="nationality" id="nationality">
        Nationality*
      </CharFieldInput>
      <CharFieldInput name="national_code" id="national_code">
        National Code*
      </CharFieldInput>
      <PictureInput name="picture" id="picture" is_required={false}>
        Photo
      </PictureInput>
      <PhoneForm></PhoneForm>
      <SelectInput
        name="address"
        id="address"
        items={["Address#1", "Address#2"]}
      >
        Address*
      </SelectInput>
      <EducationForm></EducationForm>
    </fieldset>
  );
};

export default PersonForm;
