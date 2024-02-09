import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import FacultyForm from "@/app/components/FacultyForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <FacultyForm></FacultyForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
