interface PictureInputProps {
  id: string;
  name: string;
  children: string;
  is_required?: boolean;
}

const PictureInput = ({
  id,
  name,
  children,
  is_required = true,
}: PictureInputProps) => {
  const input_style = "px-3 py-2 bg-main-grey/50 outline-none";
  const label_style = "text-main-dark mr-2";
  if (is_required) {
    return (
      <p className="my-3">
        <label htmlFor={id} className={label_style}>
          {children}
        </label>
        <input
          type="image"
          className={input_style}
          id={id}
          name={name}
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
        <input type="image" className={input_style} id={id} name={name} />
      </p>
    );
  }
};

export default PictureInput;
