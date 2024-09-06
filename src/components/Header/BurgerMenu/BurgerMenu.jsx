import React from "react";
import styles from "./BurgerMenu.module.css";

const BurgerMenu = ({ isOpen, onClick }) => {
  return (
    <div className={styles.burger}>
      <div
        className={`${styles.burger__menu} ${isOpen ? "open" : ""}`}
        onClick={onClick}
      >
        <div className={styles.burger__menu_line}></div>
      </div>
    </div>
  );
};

export default BurgerMenu;
