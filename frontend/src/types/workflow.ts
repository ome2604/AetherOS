export interface WorkflowEvent {
  event: string;
  payload: any;
}

export interface Workflow {
  id: string;
  title: string;
  status: string;
}