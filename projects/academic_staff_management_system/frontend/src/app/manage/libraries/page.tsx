import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import LibraryForm from "@/app/components/LibraryForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <LibraryForm></LibraryForm>
          </form>
        </div>
      </div>
    </div>
  );
};
export default page;
