import React from "react";
import styles from "./Nav.module.css";
import { Link } from "react-router-dom";

export default function Nav() {
  return (
    <ul className={styles.menu}>
      <li className={styles.menu__list}>
        <Link to="/new" className={styles.menu__link}>
          Новостройки
        </Link>
      </li>
      <li className={styles.menu__list}>
        <Link to="/plots" className={styles.menu__link}>
          Участки
        </Link>
      </li>
      <li className={styles.menu__list}>
        <Link to="/services" className={styles.menu__link}>
          Услуги
        </Link>
      </li>
      <li className={styles.menu__list}>
        <Link to="/about" className={styles.menu__link}>
          О нас
        </Link>
      </li>
      <li className={styles.menu__list}>
        <Link to="/contacts" className={styles.menu__link}>
          Контакты
        </Link>
      </li>
    </ul>
  );
}
