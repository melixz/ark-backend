import React from "react";
import styles from "./FooterBottom.module.css";
import { Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function FooterBottom() {
  return (
    <Row className={styles.footer__row}>
      <Col className={styles.footer__col_left}>
        <p className={styles.footer__copyright}>© 2024 Все права защищены</p>
      </Col>
      <Col className={styles.footer__col_center}>
        <ul className={styles.footer__menu}>
          <li className={styles.footer__list}>
            <Link to="/new" className={styles.footer__links}>
              Новостройки
            </Link>
          </li>
          <li className={styles.footer__list}>
            <Link to="/plots" className={styles.footer__links}>
              Участки
            </Link>
          </li>
          <li className={styles.footer__list}>
            <Link to="/services" className={styles.footer__links}>
              Услуги
            </Link>
          </li>
          <li className={styles.footer__list}>
            <Link to="/about" className={styles.footer__links}>
              О нас
            </Link>
          </li>
          <li className={styles.footer__list}>
            <Link to="/contacts" className={styles.footer__links}>
              Контакты
            </Link>
          </li>
        </ul>
      </Col>
      <Col className={styles.footer__col_right}>
        <Link to="/confeditial" className={styles.footer__link}>
          <p className={styles.footer__copyright}>
            Политика конфиденциальности
          </p>
        </Link>
      </Col>
    </Row>
  );
}
