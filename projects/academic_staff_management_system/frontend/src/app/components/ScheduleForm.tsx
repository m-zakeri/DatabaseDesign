import React from "react";
import SelectInput from "./SelectInput";
import TimeInput from "./TimeInput";

const ScheduleForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Schedule</legend>
      <SelectInput
        name="day"
        id="day"
        items={["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]}
      >
        Day*
      </SelectInput>
      <TimeInput name="start_time" id="start_time">
        Start Time*
      </TimeInput>
      <TimeInput name="end_time" id="end_time">
        End Time*
      </TimeInput>
    </fieldset>
  );
};

export default ScheduleForm;
