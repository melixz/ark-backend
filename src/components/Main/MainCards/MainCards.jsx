import React from "react";
import styles from "./MainCards.module.css";
import { Col, Container, Row } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function MainCards() {
  return (
    <Container fluid className={styles.main__cards_fluid}>
      <Container className={styles.main__cards_container}>
        <Row className={styles.main__cards_row}>
          <Col
            md={6}
            className={
              styles.main__cards_col + " " + styles.main__cards_col_new
            }
          >
            <Link className={styles.main__cards_link} to="/new">
              Новостройки
            </Link>
          </Col>
          <Col
            md={6}
            className={
              styles.main__cards_col + " " + styles.main__cards_col_land
            }
          >
            <Link className={styles.main__cards_link} to="/plots">
              Участки под застройку
            </Link>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}
