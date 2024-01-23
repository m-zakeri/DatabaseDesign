import Image from "next/image";
import Filter from "./components/Filter";
import List from "./components/List";

export default function Home() {
  return (
    <main className="mt-[35px] px-[30px]">
        <Filter />
        <List />
    </main>
  );
}
