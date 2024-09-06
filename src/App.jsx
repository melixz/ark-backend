import React from "react";
import Layout from "./components/Layout/Layout";
import { DataProvider } from "./components/DataContext/DataContext";

export default function App() {
  return (
    <DataProvider>
      <Layout />
    </DataProvider>
  );
}
