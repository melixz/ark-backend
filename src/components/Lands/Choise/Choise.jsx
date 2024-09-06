import React from "react";
import { Col, Container, Row } from "react-bootstrap";
import styles from "./Choise.module.css";

export default function Choise() {
  return (
    <Container fluid className={styles.choise__container}>
      <Container className={styles.choise}>
        <Row className={styles.choise__row}>
          <Col
            md={12}
            className={styles.choise__col + " " + styles.order__title}
          >
            <h1 className={styles.choise__title}>
              Как правильно выбрать земельный участок{" "}
            </h1>
          </Col>
          <Col
            md={6}
            sm={12}
            className={styles.choise__text_wrapper + " " + styles.order__list}
          >
            <ul className={styles.choise__list}>
              <li className={styles.choise__item}>
                <p className={styles.choise__text}>
                  Купить землю в Крыму несложно, но правильно купить – задача не
                  из легких. 
                </p>
              </li>
              <li className={styles.choise__item}>
                <p className={styles.choise__text + " " + styles.center__text}>
                  В первую очередь вам необходимо определить основные критерии
                  вашей будущей жизни в доме на земельном участке.
                </p>
              </li>
              <li className={styles.choise__item}>
                <p className={styles.choise__text + " " + styles.center__text}>
                  В большинстве случаев при выборе земельного участка люди
                  неправильно расставляют приоритеты. Из-за чего сталкиваются в
                  последствии с большим количеством проблем и дополнительными
                  затратами.
                </p>
              </li>
              <li className={styles.choise__item}>
                <p className={styles.choise__text + " " + styles.center__last}>
                  Наши опытные квалифицированные специалисты помогут вам выбрать
                  участок. Мы предлагаем комплексное обслуживание "под ключ" по
                  самым высоким стандартам.
                </p>
              </li>
            </ul>
          </Col>
          <Col
            md={6}
            sm={12}
            className={styles.choise__img + " " + styles.order__img}
          ></Col>
        </Row>
      </Container>
    </Container>
  );
}
