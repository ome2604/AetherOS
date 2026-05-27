import { Link } from "react-router-dom";

interface Props {
  title: string;
  status: string;
  id?: string;
}

export default function WorkflowCard({
  title,
  status,
  id,
}: Props) {
  return (
    <Link
      to={`/workflow/${id}`}
    >
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 hover:border-blue-500 transition">
        <div className="flex items-center justify-between mb-4">
          <h3 className="font-semibold text-lg">
            {title}
          </h3>

          <span className="text-xs px-3 py-1 rounded-full bg-slate-800">
            {status}
          </span>
        </div>

        <div className="text-sm text-slate-400">
          Multi-agent orchestration workflow runtime.
        </div>
      </div>
    </Link>
  );
}