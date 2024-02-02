import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import LibraryForm from "@/app/components/LibraryForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen">
      <ManagerHeader />
      <ManageMenu />
      <LibraryForm></LibraryForm>
    </div>
  );
};

export default page;
