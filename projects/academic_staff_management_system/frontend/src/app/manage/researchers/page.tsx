import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import ResearcherForm from "@/app/components/ResearcherForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <ResearcherForm></ResearcherForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
