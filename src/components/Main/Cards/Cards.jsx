import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "./Cards.module.css";
import { Col } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function Cards({ cards }) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    if (cards && cards.length > 0) {
      setLoading(false);
    } else {
      setError(true);
      setLoading(false);
    }
  }, [cards]);

  if (loading) {
    return <div className={styles.loader}></div>;
  }

  if (error) {
    return <div>Ошибка загрузки данных. Пожалуйста, попробуйте позже.</div>;
  }

  return (
    <>
      {cards.map((card, index) => {
        return (
          <Col
            key={index} // Используйте индекс в качестве ключа
            className={styles.card_section}
            itemProp="mainContentOfPage"
            itemScope
            itemType="http://schema.org/BlogPosting"
          >
            {card.image ? (
              <img
                src={card.image}
                alt="card_icon"
                className={styles.card__icon}
              />
            ) : (
              <div>Изображение недоступно</div>
            )}
            <h2 className={styles.card__title_text}>{card.title}</h2>
            <p className={styles.card__desc}>{card.description}</p>
            <Link to={card.path} className={styles.card__btn}>
              <span className={styles.card__btn_text}>Подробнее</span>
            </Link>
          </Col>
        );
      })}
    </>
  );
}
