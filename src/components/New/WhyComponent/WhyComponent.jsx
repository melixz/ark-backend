import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "./WhyComponent.module.css";
import { Col, Container, Row } from "react-bootstrap";

export default function WhyComponent({
  children,
  bgr,
  first,
  second,
  third,
  fourth,
  fifth,
  sixth,
}) {
  return (
    <Container className={styles.why__container}>
      <Row className={styles.row_title_section}>
        <Col
          md={12}
          sm={12}
          className={styles.why__row_text + " " + styles.orderFirst}
        >
          <h3 className={styles.main__title} itemProp="about">
            {children}
          </h3>
        </Col>
        <Col
          md={6}
          sm={12}
          itemProp="mainContentOfPage"
          itemScope
          itemType="http://schema.org/WebPageElement"
          className={styles.crimea__section + " " + styles.orderMiddle}
        >
          <div
            className={styles.crimea__icon}
            style={{ backgroundImage: `url(${bgr})` }}
            alt="crimea_icon"
          />
        </Col>
        <Col
          md={6}
          sm={12}
          className={
            styles.why__row +
            " " +
            styles.why__row_desc +
            " " +
            styles.orderLast
          }
        >
          <p className={styles.main__text} itemProp="description">
            {first}
          </p>
          <ul className={styles.main__list}>
            <li className={styles.main__list_item}>
              <p itemProp="headline" className={styles.main__list_title}>
                {second}
              </p>
              <p className={styles.main__list_num}>01</p>
            </li>
            <li className={styles.main__list_item}>
              <p itemProp="headline" className={styles.main__list_title}>
                {third}
              </p>
              <p className={styles.main__list_num}>02</p>
            </li>
            <li className={styles.main__list_item}>
              <p itemProp="headline" className={styles.main__list_title}>
                {fourth}
              </p>
              <p className={styles.main__list_num}>03</p>
            </li>
            <li className={styles.main__list_item}>
              <p itemProp="headline" className={styles.main__list_title}>
                {fifth}
              </p>
              <p className={styles.main__list_num}>04</p>
            </li>
            <li className={styles.main__list_item}>
              <p itemProp="headline" className={styles.main__list_title}>
                {sixth}
              </p>
              <p className={styles.main__list_num}>05</p>
            </li>
          </ul>
        </Col>
      </Row>
    </Container>
  );
}
