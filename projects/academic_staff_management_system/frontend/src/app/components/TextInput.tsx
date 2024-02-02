interface TextInputProps {
  title: string;
  inputname: string;
  type: string;
}

const TextInput = ({ title, inputname, type }: TextInputProps) => {
  return (
    <div className="flex max-w-sm justify-between items-center">
      <label className="mr-2 text-main-dark inline">{title}</label>
      <input
        name={inputname}
        className="bg-main-grey/50 py-[10px] px-3 outline-none focus:bg-main-peach/50 transition duration-300 hover:bg-main-peach/50 rounded"
        type={type}
      />
    </div>
  );
};

export default TextInput;
