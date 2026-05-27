import { create } from "zustand";

import api from "../services/api";

interface WorkflowEvent {
  event: string;
  payload: any;
}

interface Workflow {
  id: string;
  name: string;
  status: string;
  created_at: string;
}

interface WorkflowStore {
  events: WorkflowEvent[];

  workflows: Workflow[];

  activeNode: string;

  fetchWorkflows: () => Promise<void>;

  addEvent: (
    event: WorkflowEvent
  ) => void;
}

export const useWorkflowStore =
  create<WorkflowStore>((set) => ({
    events: [],

    workflows: [],

    activeNode: "",

    fetchWorkflows: async () => {
      const response =
        await api.get("/workflows");

      set({
        workflows: response.data,
      });
    },

    addEvent: (event) =>
      set((state) => {
        let activeNode =
          state.activeNode;

        if (
          event.event.includes(
            "planner"
          )
        ) {
          activeNode = "planner";
        }

        if (
          event.event.includes(
            "executor"
          )
        ) {
          activeNode = "executor";
        }

        if (
          event.event.includes(
            "reviewer"
          )
        ) {
          activeNode = "reviewer";
        }

        if (
          event.event.includes(
            "completed"
          )
        ) {
          activeNode = "";
        }

        return {
          events: [
            ...state.events,
            event,
          ],

          activeNode,
        };
      }),
  }));