import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import OfficeForm from "@/app/components/OfficeForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <OfficeForm></OfficeForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
