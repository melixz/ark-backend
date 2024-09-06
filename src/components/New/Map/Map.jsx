import React from "react";
import styles from "./Map.module.css";
import { Col, Container, Row } from "react-bootstrap";
import map__img from "../../../assets/map.png";
import { Link } from "react-router-dom";

export default function Map({ scrollToForm }) {
  return (
    <Container className={styles.map}>
      <Row>
        <Col>
          <h1 className={styles.map__title}>Направления поиска</h1>
        </Col>
      </Row>
      <Row className={styles.map__row}>
        <Col
          className={styles.map__img}
          style={{ backgroundImage: `url(${map__img})` }}
        ></Col>
        <Col md={4}>
          <ul className={styles.map__list}>
            <li className={styles.map__item}>
              <p className={styles.map__text}>Южный берег</p>{" "}
              <p className={styles.map__text}>01</p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>Западный берег</p>{" "}
              <p className={styles.map__text}>02</p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>Южно–восточное побережье</p>{" "}
              <p className={styles.map__text}>03</p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>Северная часть полуострова</p>{" "}
              <p className={styles.map__text}>04</p>
            </li>
            <li className={styles.map__item}>
              <p className={styles.map__text}>Центральная часть полуострова</p>{" "}
              <p className={styles.map__text}>05</p>
            </li>
          </ul>
        </Col>
      </Row>
      <Row className={styles.map__row_btn}>
        <Col className={styles.map__col_descr}>
          <p className={styles.map__description}>
            Наши опытные квалифицированные специалисты помогут вам определить
            направление и критерии поиска дома вашей мечты.
          </p>
        </Col>
        <Col className={styles.map__col_btn}>
          <Link to="#" onClick={scrollToForm} className={styles.map__button}>
            Связаться с нами
          </Link>
        </Col>
      </Row>
    </Container>
  );
}
