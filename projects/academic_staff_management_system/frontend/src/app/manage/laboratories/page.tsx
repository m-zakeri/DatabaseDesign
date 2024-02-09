import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import LaboratoryForm from "@/app/components/LaboratoryForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <LaboratoryForm></LaboratoryForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
