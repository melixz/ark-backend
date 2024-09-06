import React, { useRef } from "react";
import styles from "./MainTop.module.css";
import { Container, Row, Col } from "react-bootstrap";
import arrow_down from "../../../assets/arrow_down_header_bottom.png";
import { Link } from "react-router-dom";

export default function MainTop({ scrollToForm }) {
  const linkRef = useRef(null);

  return (
    <Container fluid className={styles.main__container}>
      <Row className={styles.main__row}>
        <Col md={12} className={styles.main__col}>
          <h1 className={styles.main__title}>АРК</h1>
        </Col>
        <Col md={4} className={styles.main__col_agency}>
          <p
            className={
              styles.main__subtitle + " " + styles.main__subtitle_agency
            }
          >
            Агентство
          </p>
        </Col>
        <Col
          md={7}
          sm={12}
          className={styles.main__col + " " + styles.main__col_realtor}
        >
          <p
            className={
              styles.main__subtitle + " " + styles.main__subtitle_realtor
            }
          >
            риэлтерского консалтинга
          </p>
        </Col>
      </Row>
      <Row className={styles.main__row_bottom}>
        <Col className={styles.main__col_personal}>
          <p className={styles.main__text_personal}>Персональный подход</p>
          <p className={styles.main__text_security}>Безопасность</p>
          <p className={styles.main__text_transparency}>Прозрачность</p>
        </Col>
        <Col
          md={12}
          sm={12}
          className={
            styles.main__first_description_wrapper + " " + styles.arrow_section
          }
        >
          <Link
            itemProp="url"
            itemScope
            itemType="http://schema.org/URL"
            className={styles.main__first_description_link}
            ref={linkRef}
            // Привязываем реф к ссылке
            onClick={scrollToForm} // Привязываем событие клика
          >
            <img
              src={arrow_down}
              className={styles.arrow}
              itemProp="image url"
              alt="arrow_down_icon"
            />
          </Link>
        </Col>
      </Row>
    </Container>
  );
}
