import React from "react";
import styles from "./Map.module.css";
import { Col, Container, Row } from "react-bootstrap";
import map__img from "../../../assets/choise_img.png";

export default function Map() {
  return (
    <Container className={styles.map}>
      <Row>
        <Col className={styles.map__col_text}>
          <h1 className={styles.map__title}>
            Как правильно выбрать земельный участок
          </h1>
        </Col>
      </Row>
      <Row className={styles.map__row}>
        <Col
          className={styles.map__img}
          style={{ backgroundImage: `url(${map__img})` }}
        ></Col>
        <Col>
          <ul className={styles.map__list}>
            <li className={styles.map__item}>
              <p className={styles.map__text}>
                Купить землю в Крыму несложно, но правильно купить – задача не
                из легких. 
              </p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>
                В первую очередь вам необходимо определить основные критерии
                вашей будущей жизни в доме на земельном участке.
              </p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>
                В большинстве случаев при выборе земельного участка люди
                неправильно расставляют приоритеты. Из-за чего сталкиваются в
                последствии с большим количеством проблем и дополнительными
                затратами.
              </p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>
                Наши опытные квалифицированные специалисты помогут вам выбрать
                участок. Мы предлагаем комплексное обслуживание "под ключ" по
                самым высоким стандартам.
              </p>{" "}
            </li>
          </ul>
        </Col>
      </Row>
    </Container>
  );
}
