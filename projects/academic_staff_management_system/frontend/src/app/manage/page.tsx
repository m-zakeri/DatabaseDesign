import ManagerHeader from "../components/ManagerHeader";
import ManageMenu from "../components/ManageMenu";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen">
      <ManagerHeader />
      <ManageMenu />
    </div>
  );
};

export default page;
