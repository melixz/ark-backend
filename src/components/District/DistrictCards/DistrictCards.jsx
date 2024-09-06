import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "./DistrictCards.module.css"; // Убедитесь, что у вас есть соответствующие стили
import { Col } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function DistrictCards({ lands, citySlug, districtSlug }) {
  if (!lands || lands.length === 0) {
    return <div>Нет доступных участков</div>;
  }

  return (
    <>
      {lands.map((land, index) => {
        const title = land.land_type_display || "Нет данных";
        const price = parseInt(land.price).toLocaleString() + " ₽";

        return (
          <Col
            key={index} // Используйте индекс в качестве ключа
            className={styles.card_section}
            itemProp="mainContentOfPage"
            itemScope
            itemType="http://schema.org/BlogPosting"
          >
            <h2 className={styles.card__title_text}>{title}</h2>
            <p className={styles.card__price}>{price}</p>
            <Link
              to={`/plots/${citySlug}/${districtSlug}/${land.path}`}
              className={styles.card__btn}
            >
              <span className={styles.card__btn_text}>Подробнее</span>
            </Link>
          </Col>
        );
      })}
    </>
  );
}
