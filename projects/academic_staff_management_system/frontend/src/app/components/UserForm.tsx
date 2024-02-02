import React from "react";
import CharFieldInput from "./CharFieldInput";
import PasswordInput from "./PasswordInput";
import EmailInput from "./EmailInput";

const UserForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>User Info</legend>
      <CharFieldInput name="username" id="username">
        Username*
      </CharFieldInput>
      <PasswordInput name="password" id="password">
        Password*
      </PasswordInput>
      <EmailInput name="email" id="email">
        Email*
      </EmailInput>
      <CharFieldInput name="first_name" id="first_name">
        First Name*
      </CharFieldInput>
      <CharFieldInput name="last_name" id="last_name">
        Last Name*
      </CharFieldInput>
    </fieldset>
  );
};

export default UserForm;
