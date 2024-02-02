interface TextAreaInputProps {
  id: string;
  name: string;
  children: string;
  is_required?: boolean;
  placeholder?: string;
}

const TextAreaInput = ({
  id,
  name,
  children,
  is_required = true,
  placeholder = "",
}: TextAreaInputProps) => {
  const p_style = "flex align-top my-3";
  const label_style = "mr-2";
  const textarea_style =
    "bg-main-grey/50 outline-none hover:bg-main-peach/50 focus:bg-main-peach/50 duration-300 py-2 px-3";
  if (is_required) {
    return (
      <p className={p_style}>
        <label className={label_style} htmlFor={id}>
          {children}
        </label>
        <textarea
          className={textarea_style}
          name={name}
          id={id}
          cols={25}
          rows={6}
          placeholder={placeholder}
          required
        ></textarea>
      </p>
    );
  } else {
    return (
      <p className={p_style}>
        <label className={label_style} htmlFor={id}>
          {children}
        </label>
        <textarea
          className={textarea_style}
          name={name}
          id={id}
          cols={25}
          rows={6}
          placeholder={placeholder}
        ></textarea>
      </p>
    );
  }
};

export default TextAreaInput;
