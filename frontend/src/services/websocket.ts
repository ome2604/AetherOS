import { useWorkflowStore } from "../store/workflowStore";

export function connectWorkflowSocket() {
  const socket = new WebSocket(
    "ws://127.0.0.1:8000/ws/workflows"
  );

  socket.onopen = () => {
    console.log("Connected to AetherOS Runtime");
  };

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    useWorkflowStore
      .getState()
      .addEvent(data);

    console.log("Realtime Event:", data);
  };

  socket.onclose = () => {
    console.log("WebSocket Closed");
  };

  socket.onerror = (error) => {
    console.error(error);
  };

  return socket;
}