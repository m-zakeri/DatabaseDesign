interface CharFieldInputProps {
  id: string;
  name: string;
  children: string;
  is_required?: boolean;
  placeholder?: string;
}

const CharFieldInput = ({
  id,
  name,
  children,
  is_required = true,
  placeholder = "",
}: CharFieldInputProps) => {
  const input_style =
    "px-3 py-2 bg-main-grey/50 outline-none hover:bg-main-peach/50 focus:bg-main-peach/50 text-main-dark duration-300";
  const label_style = "text-main-dark mr-2";
  if (is_required) {
    return (
      <p className="my-3">
        <label htmlFor={id} className={label_style}>
          {children}
        </label>
        <input
          type="text"
          className={input_style}
          id={id}
          name={name}
          placeholder={placeholder}
          required
        />
      </p>
    );
  } else {
    return (
      <p className="my-3">
        <label htmlFor={id} className={label_style}>
          {children}
        </label>
        <input
          type="text"
          className={input_style}
          id={id}
          name={name}
          placeholder={placeholder}
        />
      </p>
    );
  }
};

export default CharFieldInput;
