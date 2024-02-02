"use client";
import Link from "next/link";
import { useState } from "react";

interface SideMenuProps {
  active_tab: number;
}

const routeButton = (active: number, index: number, item: string) => {
  if (active == -1) {
    return "manage/" + item;
  } else if (active == index) {
    return "";
  } else {
    return item;
  }
};

const styleButton = (active: number, index: number) => {
  if (active == index) {
    return "p-5  mb-1 mt-2 font-bold bg-main-peach";
  } else {
    return "p-5  mb-1 mt-2 font-bold bg-main-peach/50";
  }
};

const SideMenu = ({ active_tab }: SideMenuProps) => {
  const [active, setActive] = useState(-1);
  const links = ["add", "edit", "delete"].map((item, index) => (
    <Link
      href={routeButton(active_tab, index, item)}
      className={styleButton(active_tab, index)}
      onClick={() => {
        setActive(index);
      }}
      key={index}
    >
      {item[0].toUpperCase() + item.slice(1)} Staff
    </Link>
  ));
  return (
    <>
      <nav className="flex flex-col w-[300px] h-full fixed bg-main-peach/50">
        {links}
      </nav>
    </>
  );
};

export default SideMenu;
