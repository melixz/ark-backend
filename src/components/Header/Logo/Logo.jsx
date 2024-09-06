import React from "react";
import styles from "./Logo.module.css";
import logo_icon from "../../../assets/ark_logo.png";
import { Link } from "react-router-dom";

export default function Logo() {
  return (
    <Link to="/">
      <img className={styles.logo} src={logo_icon} alt="logo-icon" />
    </Link>
  );
}
