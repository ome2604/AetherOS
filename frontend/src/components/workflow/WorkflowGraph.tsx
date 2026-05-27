import {
  Background,
  Controls,
  MiniMap,
  ReactFlow,
} from "reactflow";

import "reactflow/dist/style.css";

import { useWorkflowStore } from "../../store/workflowStore";

export default function WorkflowGraph() {
  const activeNode = useWorkflowStore(
    (state) => state.activeNode
  );

  const getNodeStyle = (
    nodeId: string
  ) => ({
    background:
      activeNode === nodeId
        ? "#2563eb"
        : "#1e293b",

    color: "white",

    border:
      activeNode === nodeId
        ? "2px solid #60a5fa"
        : "1px solid #334155",

    padding: 10,

    borderRadius: 12,

    boxShadow:
      activeNode === nodeId
        ? "0 0 20px rgba(59,130,246,0.8)"
        : "none",

    transition: "all 0.3s ease",
  });

  const nodes = [
    {
      id: "planner",

      position: {
        x: 100,
        y: 100,
      },

      data: {
        label: "Planner Agent",
      },

      style: getNodeStyle(
        "planner"
      ),
    },

    {
      id: "executor",

      position: {
        x: 400,
        y: 100,
      },

      data: {
        label: "Executor Agent",
      },

      style: getNodeStyle(
        "executor"
      ),
    },

    {
      id: "reviewer",

      position: {
        x: 700,
        y: 100,
      },

      data: {
        label: "Reviewer Agent",
      },

      style: getNodeStyle(
        "reviewer"
      ),
    },
  ];

  const edges = [
    {
      id: "planner-executor",

      source: "planner",

      target: "executor",

      animated: true,
    },

    {
      id: "executor-reviewer",

      source: "executor",

      target: "reviewer",

      animated: true,
    },

    {
      id: "reviewer-executor",

      source: "reviewer",

      target: "executor",

      label: "retry",

      animated: true,
    },
  ];

  return (
    <div className="h-[500px] bg-slate-900 border border-slate-800 rounded-xl overflow-hidden">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
      >
        <MiniMap />

        <Controls />

        <Background />
      </ReactFlow>
    </div>
  );
}