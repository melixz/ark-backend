import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

export const DataContext = createContext();

export const DataProvider = ({ children }) => {
  const [data, setData] = useState(
    JSON.parse(localStorage.getItem("data")) || {}
  );
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("https://arkcrimea.ru/api/full-data/");
        const newData = response.data;
        localStorage.setItem("data", JSON.stringify(newData));
        setData(newData);
      } catch (error) {
        console.error(error);
        setError("Ошибка при загрузке данных. Пожалуйста, попробуйте позже.");
      }
    };

    fetchData();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  return <DataContext.Provider value={data}>{children}</DataContext.Provider>;
};
