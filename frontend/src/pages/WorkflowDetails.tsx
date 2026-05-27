import { useEffect, useState } from "react";

import { useParams } from "react-router-dom";

import api from "../services/api";

export default function WorkflowDetails() {
  const { id } = useParams();

  const [workflow, setWorkflow] =
    useState<any>(null);

  useEffect(() => {
    fetchWorkflow();
  }, []);

  const fetchWorkflow =
    async () => {
      try {
        const response =
          await api.get(
            `/workflows/${id}`
          );

        setWorkflow(
          response.data
        );
      } catch (error) {
        console.error(error);
      }
    };

  if (!workflow) {
    return (
      <div>
        Loading workflow...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
        <h1 className="text-3xl font-bold mb-4">
          {workflow.name}
        </h1>

        <div className="space-y-3 text-slate-300">
          <div>
            <strong>ID:</strong>{" "}
            {workflow.id}
          </div>

          <div>
            <strong>Status:</strong>{" "}
            {workflow.status}
          </div>

          <div>
            <strong>Created:</strong>{" "}
            {workflow.created_at}
          </div>
        </div>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
        <h2 className="text-2xl font-semibold mb-4">
          Execution Timeline
        </h2>

        <div className="space-y-3">
          <div className="border border-slate-800 rounded-lg p-3">
            planner_started
          </div>

          <div className="border border-slate-800 rounded-lg p-3">
            planner_completed
          </div>

          <div className="border border-slate-800 rounded-lg p-3">
            executor_started
          </div>

          <div className="border border-slate-800 rounded-lg p-3">
            reviewer_completed
          </div>
        </div>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
        <h2 className="text-2xl font-semibold mb-4">
          Agent Logs
        </h2>

        <pre className="text-sm text-slate-400 overflow-auto">
{`Planner:
Generated execution plan

Executor:
Executed workflow task

Reviewer:
Validated execution output`}
        </pre>
      </div>
    </div>
  );
}