"use client"

import Image from "next/image";
import Catalog from "./components/Catalog";
import Filters from "./components/Filters";
import Results from "./components/Results";
import getPersonUsers from "../../lib/getPersonUsers";



export default async function Home() {
  const persons : (Person & User)[] = await getPersonUsers();
  return (
    <>
      <header>
        <Catalog />
      </header>
      <main className="px-[30px] pb-[30px] flex flex-col gap-[30px] lg:flex-row lg:max-w-[1300px] mx-auto lg:pt-[128px]">
        <Filters />
        <Results persons={persons}/>
      </main>
    </>
  );
}
