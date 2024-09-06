import React, { forwardRef } from "react";
import styles from "./Credit.module.css";
import { Col, Container, Row } from "react-bootstrap";

const Credit = forwardRef((props, ref) => {
  const { id } = props;

  return (
    <Container className={styles.credit}>
      <Row className={styles.credit__row}>
        <Col md={12} className={styles.credit__col}>
          <div className={styles.wrapper}>
            <h1 className={styles.credit__title}>Ипотечный центр</h1>
          </div>
        </Col>
      </Row>
      <Container className={styles.content__container}>
        <Row className={styles.content__row}>
          <Col ref={ref} id={id} className={styles.content__col}>
            <h5 className={styles.content__title}>
              Ипотека с нами – это просто!
            </h5>
            <ul className={styles.content__list}>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Решаем проблемы первоначального взноса
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Шансы на одобрение выше на 30%
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Сопровождение при оформлении сделки
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Подбор самых выгодных условий
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>Результат за 1 день</p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Возврат до 48% от суммы кредита
                </p>
              </li>
            </ul>
          </Col>
          <Col className={styles.content__img}></Col>
        </Row>
      </Container>
      <Container className={styles.conditions__container}>
        <Row className={styles.conditions__row}>
          <Col className={styles.conditions__img}></Col>
          <Col className={styles.conditions__col}>
            <h5 className={styles.conditions__title}>
              Ипотека с нами – это просто!
            </h5>
            <ul className={styles.conditions__list}>
              <li className={styles.conditions__item}>
                <p className={styles.conditions__text}>
                  Ипотека с использованием материнского капитала
                </p>
              </li>
              <li className={styles.conditions__item}>
                <p className={styles.conditions__text}>
                  Ипотека с господдержкой для семей с детьми
                </p>
              </li>
              <li className={styles.conditions__item}>
                <p className={styles.conditions__text}>Военная ипотека</p>
              </li>
              <li className={styles.conditions__item}>
                <p className={styles.conditions__text}>
                  Программа 450 тысяч на погашение ипотеки при рождении третьего
                  или последующего ребенка (отцовский капитал)
                </p>
              </li>
            </ul>
          </Col>
        </Row>
      </Container>
    </Container>
  );
});

export default Credit;
