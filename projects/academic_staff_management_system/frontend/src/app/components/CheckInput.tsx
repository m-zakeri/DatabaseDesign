import { Children } from "react";

interface CheckInputProps {
  id: string;
  name: string;
  children: string;
  is_required?: boolean;
}

const CheckInput = ({
  id,
  name,
  is_required = true,
  children,
}: CheckInputProps) => {
  const p_style = "my-3 flex items-center";
  const label_style = "text-main-dark ml-2";
  const input_style =
    "appearance-none outline-offset-[-1px] w-4 h-4 rounded bg-main-grey checked:bg-main-dark hover:outline-main-dark hover:outline-1 hover:outline hover:outline-offset-[-1px] duration-100";
  if (is_required) {
    return (
      <p className={p_style}>
        <input
          className={input_style}
          type="checkbox"
          id={id}
          name={name}
          required
        />
        <label className={label_style} htmlFor={id}>
          {children}
        </label>
      </p>
    );
  } else {
    return (
      <p className={p_style}>
        <input className={input_style} type="checkbox" id={id} name={name} />
        <label className={label_style} htmlFor={id}>
          {children}
        </label>
      </p>
    );
  }
};

export default CheckInput;
