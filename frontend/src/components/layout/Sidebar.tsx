import { LayoutDashboard, Workflow } from "lucide-react";

export default function Sidebar() {
  return (
    <div className="w-64 bg-slate-900 border-r border-slate-800 p-5">
      <h1 className="text-2xl font-bold mb-10">
        AetherOS
      </h1>

      <nav className="space-y-4">
        <div className="flex items-center gap-3 text-slate-300 hover:text-white cursor-pointer">
          <LayoutDashboard size={20} />
          Dashboard
        </div>

        <div className="flex items-center gap-3 text-slate-300 hover:text-white cursor-pointer">
          <Workflow size={20} />
          Workflows
        </div>
      </nav>
    </div>
  );
}