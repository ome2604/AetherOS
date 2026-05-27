import { useEffect } from "react";
import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import WorkflowDetails from "./pages/WorkflowDetails";

import MainLayout from "./components/layout/MainLayout";

import { connectWorkflowSocket } from "./services/websocket";

export default function App() {
  useEffect(() => {
    const socket = connectWorkflowSocket();

    return () => {
      socket.close();
    };
  }, []);

  return (
    <MainLayout>
      <Routes>
        <Route path="/" element={<Dashboard />} />

        <Route
          path="/workflow/:id"
          element={<WorkflowDetails />}
        />
      </Routes>
    </MainLayout>
  );
}