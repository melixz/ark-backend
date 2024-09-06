import React from "react";
import styles from "./Contants.module.css";
import { Link } from "react-router-dom";
import contants__icon from "../../../assets/call_icon.png";

export default function Contants() {
  return (
    <Link to="tel:+7 (978) 692–01–64" className={styles.contants__link}>
      <img src={contants__icon} alt="call" />
      +7 (978) 692–01–64
    </Link>
  );
}
