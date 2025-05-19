import React from "react";
import AgentCard from "../components/AgentCard";
import ChartPanel from "../components/ChartPanel";

export default function Dashboard() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div className="grid grid-cols-3 gap-4">
        <AgentCard agent="Lead Agent" status="Active" />
        <AgentCard agent="Chat Agent" status="Idle" />
        <AgentCard agent="Inventory Agent" status="Active" />
      </div>
      <div className="mt-6">
        <ChartPanel />
      </div>
    </div>
  );
}