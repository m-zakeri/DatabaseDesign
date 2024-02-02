import React from "react";
import CharFieldInput from "./CharFieldInput";
import DateTimeInput from "./DateTimeInput";
import TextAreaInput from "./TextAreaInput";
import IntegerFieldInput from "./IntegerFieldInput";
import SelectInput from "./SelectInput";

const ResearchForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Research</legend>
      <CharFieldInput name="title" id="title">
        Title*
      </CharFieldInput>
      <DateTimeInput name="research_start_date" id="research_start_date">
        Research Start Date*
      </DateTimeInput>
      <DateTimeInput name="research_end_date" id="research_end_date">
        Research End Date*
      </DateTimeInput>
      <TextAreaInput name="search_area" id="search_area">
        Search Area*
      </TextAreaInput>
      <TextAreaInput name="funding_source" id="funding_source">
        Funding Source*
      </TextAreaInput>
      <IntegerFieldInput name="research_budget" id="research_budget">
        Research Budget*
      </IntegerFieldInput>
      <TextAreaInput name="research_description" id="research_description">
        Research Description*
      </TextAreaInput>
      <TextAreaInput name="publications" id="publications">
        Publications*
      </TextAreaInput>
      <TextAreaInput name="keywords" id="keywords">
        Keywords*
      </TextAreaInput>
      <SelectInput
        name="research_status"
        id="research_status"
        items={["ToDo", "InProgress", "Done"]}
      >
        Research Status*
      </SelectInput>
      <TextAreaInput name="website" id="website">
        Website*
      </TextAreaInput>
      <TextAreaInput name="related_research" id="related_research">
        Related Research*
      </TextAreaInput>
    </fieldset>
  );
};

export default ResearchForm;
