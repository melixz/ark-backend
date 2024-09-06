import React, { forwardRef } from "react";
import { Container, Row, Col } from "react-bootstrap";
import styles from "./Selling.module.css";

const Selling = forwardRef((props, ref) => {
  const { id, idCost, refCost } = props;

  return (
    <Container className={styles.sell}>
      <Container className={styles.sell__container}>
        <Row className={styles.sell__row}>
          <Col ref={ref} id={id} className={styles.sell__col}>
            <h1 className={styles.sell__title}>Продажа недвижимости</h1>
            <p className={styles.sell__text}>
              Каждый наш агент – компетентный специалист, обладающий всеми
              необходимыми профессиональными навыками и располагающий самыми
              актуальными сведениями о рынке недвижимости.{" "}
            </p>
            <p className={styles.sell__text + " " + styles.sell__text_large}>
              В Агентстве Риэлторского Консалтинга вы найдете ответы на любые
              вопросы, связанные с недвижимым имуществом.
            </p>
          </Col>
          <Col
            ref={refCost}
            id={idCost}
            className={styles.sell__col + " " + styles.sell__col_cost}
          >
            <h1 className={styles.sell__title}>Оценка</h1>
            <p className={styles.sell__text + " " + styles.sell__text_large}>
              Наши сотрудники проведут экспертизу, помогут определить корректную
              стоимость вашего имущества и дадут советы по их продаже или,
              наоборот, приобретению.
            </p>
            <p className={styles.sell__text}>
              Документы, которые выдаются нашим клиентам, юридически
              удостоверяют стоимость квартир, домов, участков и других объектов.
              Их принимают в работу в банках, судах, в ФНС и нотариате.
            </p>
          </Col>
        </Row>
        <Row className={styles.payment__row}>
          <Col className={styles.payment__col}>
            <p className={styles.payment__text}>
              Размер комиссионного вознаграждения:
            </p>
          </Col>
        </Row>
        <Row className={styles.price__row}>
          <Col className={styles.price__col + " " + styles.price__col_first}>
            <p className={styles.price__text}>
              Продажа любого вида недвижимости <br />
            </p>
            <p className={styles.price__text}>
              Оценка стоимости квартиры <br />
              Оценка стоимости жилого дома, дачи
            </p>
            <p className={styles.price__text}>
              стоимости земельного участка
              <br />
              Оценка стоимости коммерческих и промышленных зданий Оценка
            </p>
          </Col>
          <Col className={styles.price__col}>
            <p className={styles.price__text}>
              3% от итоговой стоимости объекта, но не менее 100 тыс.руб
            </p>
            <p className={styles.price__text}>от 3 000 рублей</p>
            <p className={styles.price__text}>от 5 000 рублей</p>
          </Col>
        </Row>
      </Container>
    </Container>
  );
});

export default Selling;
