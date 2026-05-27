import { useWorkflowStore } from "../../store/workflowStore";

export default function RealtimeTimeline() {
  const events = useWorkflowStore(
    (state) => state.events
  );

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5">
      <h2 className="text-xl font-semibold mb-5">
        Realtime Workflow Timeline
      </h2>

      <div className="space-y-3 max-h-[500px] overflow-auto">
        {events.map((event, index) => (
          <div
            key={index}
            className="border border-slate-800 rounded-lg p-3"
          >
            <div className="font-medium text-blue-400">
              {event.event}
            </div>

            <pre className="text-xs text-slate-400 mt-2 overflow-auto">
              {JSON.stringify(
                event.payload,
                null,
                2
              )}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
}