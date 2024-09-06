import React from "react";
import styles from "./Location.module.css";
import location_img from "../../../assets/location_icon.png";

export default function Location() {
  return (
    <div className={styles.location}>
      <img
        className={styles.location_img}
        src={location_img}
        alt="иконка города"
      />
      <select
        className={styles.select}
        aria-label="город"
        itemScope
        itemType="http://schema.org/Language"
      >
        <option className={styles.option} value="ru">
          Симферополь
        </option>
        <option className={styles.option} value="ru">
          Ялта
        </option>
        <option className={styles.option} value="en">
          Феодосия
        </option>
        <option className={styles.option} value="en">
          Алушта
        </option>
      </select>
    </div>
  );
}
