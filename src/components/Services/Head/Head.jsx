import React from "react";
import styles from "./Head.module.css";
import { Col, Container, Row } from "react-bootstrap";

export default function Head() {
  return (
    <Container fluid className={styles.head}>
      <Container className={styles.head__container}>
        <Row className={styles.head__row}>
          <Col md={12} className={styles.head__col}>
            <h1 className={styles.head__title + " " + styles.first}>
              Компетентность
            </h1>
            <br />
            <h1 className={styles.head__title + " " + styles.second}>
              Безопастность
            </h1>
            <br />
            <h1 className={styles.head__title + " " + styles.third}>
              Профессионализм –{" "}
              <span className={styles.head__title_span}>арк</span>
            </h1>
          </Col>
        </Row>
        <Row>
          <Col md={12} className={styles.head__col_desc}>
            <p className={styles.head__text}>
              Услуги специалистов "Агентства Риэлторского Консалтинга" -
              это полный спектр разных сервисов.{" "}
            </p>
          </Col>
        </Row>
      </Container>
      <Row className={styles.head__girl}>
        <Col></Col>
      </Row>
    </Container>
  );
}
