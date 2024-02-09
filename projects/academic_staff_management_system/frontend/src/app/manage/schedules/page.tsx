import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import ScheduleForm from "@/app/components/ScheduleForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <ScheduleForm></ScheduleForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
