import React, { forwardRef } from "react";
import styles from "./Legal.module.css";
import { Col, Container, Row } from "react-bootstrap";

const Legal = forwardRef(({ id, scrollToForm }, ref) => {
  return (
    <Container className={styles.legal}>
      <Row className={styles.legal__row}>
        <Col md={12} className={styles.legal__col}>
          <div className={styles.wrapper}>
            <h1 className={styles.legal__title}>Юридические услуги</h1>
          </div>
        </Col>
      </Row>
      <Row className={styles.legal__row_text}>
        <Col md={12} className={styles.legal__col_text}>
          <p className={styles.legal__text}>
            Комплексные услуги по сопровождению сделок с недвижимостью любой
            сложности
          </p>
        </Col>
      </Row>
      <Container id={id} ref={ref} className={styles.content__container}>
        <Row className={styles.content__row}>
          <Col
            className={styles.content__col_img + " " + styles.content__col}
          ></Col>
          <Col className={styles.content__col}>
            <ul className={styles.content__list}>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Мы проверяем действительность каждого документа у физических и
                  юридических лиц, участников сделки
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Запрашиваем и получаем дополнительные сведения из официальных
                  источников и доступных баз данных, государственных реестров
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Мы проверяем всю документацию на недвижимость, чтобы снизить
                  вероятность каких - либо проблем при оформлении сделки
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Организовываем процесс оформления недвижимости строго по
                  разработанным регламентам безопасных расчетов
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  После оформления сделки мы бесплатно для клиента защищаем его
                  интересы в случае, если в будущем возникли какие - либо
                  спорные ситуации с предметом сделки
                </p>
              </li>
              <li className={styles.content__item}>
                <p className={styles.content__text}>
                  Все сделки сопровождаемые нашим юридическим отделом
                  застрахованы от возможных рисков
                </p>
              </li>
            </ul>
          </Col>
        </Row>
        <Row className={styles.button__row}>
          <Col md={6} className={styles.button__col}>
            <button onClick={scrollToForm} className={styles.button}>
              Узнать стоимость услуг
            </button>
          </Col>
        </Row>
      </Container>
    </Container>
  );
});

export default Legal;
