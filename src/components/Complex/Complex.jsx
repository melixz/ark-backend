import React from "react";
import { useParams } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import styles from "./Complex.module.css";
import ApartmentsCards from "./ApartmentsCards/ApartmentsCards";
import Form from "../Main/Form/Form";
import ComplexSlider from "./ComplexSlider/ComplexSlider";

const Complex = ({ data, type }) => {
  const { complexSlug } = useParams();
  const { citySlug } = useParams();

  // Найдем город по citySlug
  const cityData = data.find(
    (item) => item.path && item.path.split("/").pop() === citySlug
  );

  if (!cityData) {
    return <div>Город не найден</div>;
  }

  const complexData = cityData[type].find(
    (item) => item.path.split("/").pop() === complexSlug
  );

  if (!complexData) {
    return <div>Жилой комплекс не найден</div>;
  }

  // Получаем цену первой квартиры, если она существует
  const firstApartment =
    complexData.apartments && complexData.apartments.length > 0
      ? complexData.apartments[0]
      : null;
  const firstSection =
    firstApartment &&
    firstApartment.sections &&
    firstApartment.sections.length > 0
      ? firstApartment.sections[0]
      : null;
  const price = firstSection
    ? parseInt(firstSection.price).toLocaleString()
    : "Нет данных";

  return (
    <Container fluid className={styles.complex}>
      <Container fluid className={styles.complex__slider_container}>
        <div className={styles.complex__slider_text}>
          <h1 className={styles.complex__title}>{complexData.name}</h1>
          <p className={styles.complex__subtitle}>{cityData.name}</p>
        </div>
        <ComplexSlider data={complexData.slider} />
      </Container>
      <Container className={styles.complex__container}>
        <Row className={styles.complex__row}>
          <Col className={styles.complex__col + " " + styles.border_right}>
            <p className={styles.complex__details}>Нас. пункт</p>
            <p className={styles.complex__details_desc}>{cityData.name}</p>
          </Col>
          <Col className={styles.complex__col + " " + styles.border_right}>
            <p className={styles.complex__details}>Всего объектов</p>
            <p className={styles.complex__details_desc}>
              {cityData[type].length}
            </p>
          </Col>
          <Col className={styles.complex__col}>
            <p className={styles.complex__details}>Стоимость</p>
            <p className={styles.complex__details_desc}>от {price}</p>
          </Col>
          <Col className={styles.complex__col + " " + styles.border_left}>
            <p className={styles.complex__details}>Высота потолка</p>
            <p className={styles.complex__details_desc}>2.9м</p>
          </Col>
        </Row>
      </Container>
      {complexData.apartments && (
        <Container className={styles.apartments__container}>
          <Row>
            <Col className={styles.apartments__col_title}>
              <h1 className={styles.apartments__title}>
                Квартиры в {complexData.name}
              </h1>
            </Col>
          </Row>
          <Container>
            <Row className={styles.apartments__cards_wrapper}>
              <ApartmentsCards
                apartments={complexData.apartments}
                citySlug={citySlug}
                complexSlug={complexSlug}
              />
            </Row>
          </Container>
        </Container>
      )}
      <Container fluid className={styles.apartments__text_container_fluid}>
        <Container className={styles.apartments__text_container}>
          <Row className={styles.apartments__row}>
            <Col className={styles.apartments__col_title} md={12}>
              <h1 className={styles.apartments__buy_title}>Как купить?</h1>
            </Col>
          </Row>
          <Row className={styles.apartments__row}>
            <Col className={styles.apartments__col_text} md={6}>
              <p className={styles.apartments__text__detail}>100% оплата</p>
              <p className={styles.apartments__text__detail_desc}>
                Оплата стоимости с вашего счета на реквизиты, указанные в
                договоре.
              </p>
            </Col>
            <Col className={styles.apartments__col_text} md={6}>
              <p className={styles.apartments__text__detail}>ипотека</p>
              <p className={styles.apartments__text__detail_desc}>
                Поможем выбрать, рассчитаем и подадим заявку на одобрение
                ипотечного кредита.
              </p>
            </Col>
          </Row>
          <Row className={styles.apartments__row}>
            <Col className={styles.apartments__col_text} md={6}>
              <p className={styles.apartments__text__detail}>Рассрочка 0%</p>
              <p className={styles.apartments__text__detail_desc}>
                Мы предоставляем несколько вариантов удобной рассрочки с
                первоначальным взносом от 20% и без удорожания.
              </p>
            </Col>
            <Col className={styles.apartments__col_text} md={6}>
              <p className={styles.apartments__text__detail}>
                Материнский капитал
              </p>
              <p className={styles.apartments__text__detail_desc}>
                Вы можете использовать материнский (семейный) капитал для
                первого взноса по ипотеке или погашения ипотечного кредита.
              </p>
            </Col>
          </Row>
        </Container>
      </Container>
      <Form />
    </Container>
  );
};

export default Complex;
