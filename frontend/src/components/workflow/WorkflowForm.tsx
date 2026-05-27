import { useState } from "react";

import api from "../../services/api";

import { useWorkflowStore } from "../../store/workflowStore";

export default function WorkflowForm() {
  const [task, setTask] =
    useState("");

  const fetchWorkflows =
    useWorkflowStore(
      (state) =>
        state.fetchWorkflows
    );

  const createWorkflow =
    async () => {
      try {
        await api.post(
          "/workflows",
          {
            task,
          }
        );

        setTask("");

        fetchWorkflows();
      } catch (error) {
        console.error(error);
      }
    };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5">
      <h2 className="text-xl font-semibold mb-4">
        Create Workflow
      </h2>

      <textarea
        value={task}
        onChange={(e) =>
          setTask(
            e.target.value
          )
        }
        placeholder="Describe your workflow..."
        className="w-full h-32 bg-slate-950 border border-slate-700 rounded-lg p-4 outline-none"
      />

      <button
        onClick={createWorkflow}
        className="mt-4 bg-blue-600 hover:bg-blue-700 transition px-5 py-3 rounded-lg font-medium"
      >
        Execute Workflow
      </button>
    </div>
  );
}