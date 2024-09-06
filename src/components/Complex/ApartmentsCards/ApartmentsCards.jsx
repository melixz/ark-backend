import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "./ApartmentsCards.module.css"; // Убедитесь, что у вас есть соответствующие стили
import { Col } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function ApartmentsCards({ apartments, citySlug, complexSlug }) {
  if (!apartments || apartments.length === 0) {
    return <div>Нет доступных квартир</div>;
  }

  return (
    <>
      {apartments.map((apartment, index) => {
        // Проверяем наличие секции, так как это может быть важно
        const section =
          apartment.sections && apartment.sections.length > 0
            ? apartment.sections[0]
            : null;
        const title = section ? section.title : "Нет данных";

        return (
          <Col
            key={index} // Используйте индекс в качестве ключа
            className={styles.card_section}
            itemProp="mainContentOfPage"
            itemScope
            itemType="http://schema.org/BlogPosting"
          >
            <h2 className={styles.card__title_text}>{title}</h2>
            <p className={styles.card__desc}>
              Через наше агентство прошло сотни успешных сделок различной
              сложности.
            </p>
            <Link
              to={`/new/${citySlug}/${complexSlug}/${apartment.path}`}
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
