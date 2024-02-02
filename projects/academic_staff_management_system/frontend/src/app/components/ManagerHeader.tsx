import React from "react";

const ManagerHeader = () => {
  return (
    <header className="bg-main-peach w-screen flex justify-between px-12 py-4 items-center box-border max-w-[100%]">
      <p>Welcome, ADMIN_FNAME ADMIN_LNAME</p>
      <h1 className="font-bold text-2xl">Administrative Panel</h1>
      <a href="" className="underline">
        Log out
      </a>
    </header>
  );
};

export default ManagerHeader;
