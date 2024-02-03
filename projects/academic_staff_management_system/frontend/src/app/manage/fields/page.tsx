import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import FieldForm from "@/app/components/FieldForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <FieldForm></FieldForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
