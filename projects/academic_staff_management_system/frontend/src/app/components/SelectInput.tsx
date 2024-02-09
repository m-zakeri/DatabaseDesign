interface SelectInputProps {
  id: string;
  name: string;
  children: string;
  is_required?: boolean;
  items: string[];
}

const SelectInput = ({
  id,
  name,
  children,
  is_required,
  items,
}: SelectInputProps) => {
  const p_style = "my-3";
  const label_style = "text-main-dark mr-2";
  const select_style =
    "bg-main-grey/50 outline-none p-1 border border-main-dark rounded-md";
  const values = items.map((item, index) => (
    <option value={item} key={index}>
      {item}
    </option>
  ));
  if (is_required) {
    return (
      <p className={p_style}>
        <label className={label_style} htmlFor={id}>
          {children}
        </label>
        <select className={select_style} name={name} id={id} required>
          {values}
        </select>
      </p>
    );
  } else {
    return (
      <p className={p_style}>
        <label className={label_style} htmlFor={id}>
          {children}
        </label>
        <select className={select_style} name={name} id={id}>
          {values}
        </select>
      </p>
    );
  }
};

export default SelectInput;
