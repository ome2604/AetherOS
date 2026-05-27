import { useEffect } from "react";

import WorkflowCard from "../components/workflow/WorkflowCard";

import WorkflowForm from "../components/workflow/WorkflowForm";

import RealtimeTimeline from "../components/realtime/RealtimeTimeline";

import WorkflowGraph from "../components/workflow/WorkflowGraph";

import { useWorkflowStore } from "../store/workflowStore";

export default function Dashboard() {
  const workflows =
    useWorkflowStore(
      (state) => state.workflows
    );

  const fetchWorkflows =
    useWorkflowStore(
      (state) =>
        state.fetchWorkflows
    );

  useEffect(() => {
    fetchWorkflows();
  }, []);

  return (
    <div className="space-y-6">
      <WorkflowForm />

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
        {workflows.map((workflow) => (
          <WorkflowCard
            key={workflow.id}
            id={workflow.id}
            title={workflow.name}
            status={workflow.status}
          />
        ))}
      </div>

      <RealtimeTimeline />

      <WorkflowGraph />
    </div>
  );
}