import CharFieldInput from "./CharFieldInput";
import IntegerFieldInput from "./IntegerFieldInput";
import TextAreaInput from "./TextAreaInput";

const AddressForm = () => {
  return (
    <fieldset className="text-main-dark border border-solid border-main-grey px-3 m-3">
      <legend>Address Information</legend>
      <CharFieldInput name="state" id="state">
        State*
      </CharFieldInput>
      <CharFieldInput name="city" id="city">
        City*
      </CharFieldInput>
      <CharFieldInput name="street" id="street">
        Street*
      </CharFieldInput>
      <IntegerFieldInput
        name="street_number"
        id="street_number"
        is_required={false}
      >
        Street Number
      </IntegerFieldInput>
      <CharFieldInput
        name="building_name"
        id="building_name"
        is_required={false}
      >
        Building Name
      </CharFieldInput>
      <CharFieldInput name="district" id="district">
        District*
      </CharFieldInput>
      <IntegerFieldInput name="floor" id="floor" is_required={false}>
        Floor:
      </IntegerFieldInput>
      <IntegerFieldInput
        name="unit_number"
        id="unit_number"
        is_required={false}
      >
        Unit Number
      </IntegerFieldInput>
      <CharFieldInput name="plate_number" id="plate_number">
        Plate Number*
      </CharFieldInput>
      <CharFieldInput name="postal_code" id="postal_code">
        Postal Code*
      </CharFieldInput>
      <CharFieldInput name="coordinate" id="coordinate" is_required={false}>
        Coordinate
      </CharFieldInput>
      <TextAreaInput name="note" id="note" is_required={false}>
        Note
      </TextAreaInput>
    </fieldset>
  );
};

export default AddressForm;
