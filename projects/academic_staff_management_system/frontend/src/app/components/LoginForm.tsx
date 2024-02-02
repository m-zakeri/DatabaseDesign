const LoginForm = () => {
  return (
    <div className="w-[390px] min-h-[400px] flex flex-col justify-evenly bg-main-peach/50 rounded-2xl items-center border border-main-dark">
      <div className="text-center">
        <h3 className="text-2xl font-bold uppercase mt-4 mb-[-5px]">
          University Name
        </h3>
        <h4 className="text-xl mt-0">Manager Login</h4>
      </div>

      <form action="" className="flex flex-col items-center">
        <input
          className="outline-none p-4 rounded-2xl my-3 border border-main-dark bg-main-white/50 w-80 placeholder:text-main-dark/60 hover:bg-main-white/80 focus:bg-main-white/80 duration-300"
          type="text"
          placeholder="Staff ID"
        />
        <input
          className="outline-none p-4 rounded-2xl my-3 border border-main-dark  bg-main-white/50 w-80 placeholder:text-main-dark/60 hover:bg-main-white/80 focus:bg-main-white/80 duration-300"
          type="password"
          placeholder="Password"
        />
        <div className="w-80 flex justify-between">
          <label>
            <input
              className="focus:bg-main-dark mr-1 appearance-none w-3 h-3 rounded bg-main-white checked:bg-main-dark hover:bg-main-dark/20 duration-100"
              type="checkbox"
            />
            Remember Me
          </label>
          <a href="">Forgot Password?</a>
        </div>
        <button className="w-80 p-3 rounded-2xl my-3 border border-main-dark bg-main-dark text-main-white font-bold text-xl mb-4">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginForm;
