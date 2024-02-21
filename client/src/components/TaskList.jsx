import React from "react";
import { useEffect, useState } from "react";
import { getAllTasks } from "../api/tasks.api";

export function TaskList() {
  useEffect(() => {
    async function loadTasks() {
      const res = await getAllTasks();
      console.log(res.data);
    }
    loadTasks();
  }, []);

  return <div>TaskList</div>;
}
