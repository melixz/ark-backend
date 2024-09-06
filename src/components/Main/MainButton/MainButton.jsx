import React from "react";
import styles from "./MainButton.module.css";
import { Col, Container, Row } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function MainButton({ scrollToForm }) {
  return (
    <Container fluid className={styles.main__container}>
      <Container>
        <Row className={styles.main__row}>
          <Col md={12}>
            <h1 className={styles.main__title}>Крым.</h1>
          </Col>
          <Col md={8}>
            <p className={styles.main__subtitle}>
              Превращаем мечты в реальность
            </p>
          </Col>
          <Col md={4} className={styles.main__col_btn}>
            <Link to="#" onClick={scrollToForm} className={styles.main__button}>
              Связаться с нами
            </Link>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}
