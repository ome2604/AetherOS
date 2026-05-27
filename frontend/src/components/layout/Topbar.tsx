export default function Topbar() {
  return (
    <div className="h-16 border-b border-slate-800 bg-slate-900 px-6 flex items-center justify-between">
      <div>
        <h2 className="text-xl font-semibold">
          AI Workflow Operating System
        </h2>
      </div>

      <div className="flex items-center gap-3">
        <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>

        <span className="text-sm text-slate-400">
          Runtime Active
        </span>
      </div>
    </div>
  );
}