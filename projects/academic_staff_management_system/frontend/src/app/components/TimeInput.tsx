interface TimeInputProps {
  id: string;
  name: string;
  children: string;
  is_required?: boolean;
}

const TimeInput = ({
  id,
  name,
  children,
  is_required = true,
}: TimeInputProps) => {
  const label_style = "text-main-dark mr-2";
  const input_style = "bg-main-grey/50 py-1 px-2 cursor-text";
  if (is_required) {
    return (
      <p className="my-3">
        <label htmlFor={id} className={label_style}>
          {children}
        </label>
        <input
          id={id}
          name={name}
          className={input_style}
          type="time"
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
        <input id={id} name={name} className={input_style} type="time" />
      </p>
    );
  }
};

export default TimeInput;
