import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import ProfessorForm from "@/app/components/ProfessorForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <ProfessorForm></ProfessorForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
