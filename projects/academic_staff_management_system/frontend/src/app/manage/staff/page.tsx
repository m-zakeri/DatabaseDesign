import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import PersonForm from "@/app/components/PersonForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <PersonForm></PersonForm>
        </div>
      </div>
    </div>
  );
};

export default page;
