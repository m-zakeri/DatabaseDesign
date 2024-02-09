import CharFieldInput from "./CharFieldInput";
import DateTimeInput from "./DateTimeInput";
import IntegerFieldInput from "./IntegerFieldInput";
import SelectInput from "./SelectInput";

const BuildingForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Building</legend>
      <CharFieldInput name="building_name" id="building_name">
        Building Name*
      </CharFieldInput>
      <DateTimeInput name="building_creation_date" id="building_creation_date">
        Creation Date*
      </DateTimeInput>
      <IntegerFieldInput name="floors" id="floors">
        Floors*
      </IntegerFieldInput>
      <IntegerFieldInput name="capacity" id="capacity">
        Capacity*
      </IntegerFieldInput>
      <IntegerFieldInput name="rooms" id="rooms">
        Rooms*
      </IntegerFieldInput>
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

export default BuildingForm;
