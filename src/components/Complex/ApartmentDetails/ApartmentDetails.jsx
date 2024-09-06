import React, { useRef } from "react";
import { useParams } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import styles from "./ApartmentDetails.module.css";
import ApartmentsSlider from "./ApartmentsSlider/ApartmentsSlider";
import Form from "../../Main/Form/Form";

const ApartmentDetails = ({ data }) => {
  const { citySlug, complexSlug, apartmentSlug } = useParams();
  const formRef = useRef(null);

  const scrollToForm = (e) => {
    e.preventDefault();
    if (formRef.current) {
      formRef.current.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };
  // Найдем город по citySlug
  const cityData = data.find(
    (item) => item.path && item.path.split("/").pop() === citySlug
  );

  if (!cityData) {
    return <div>Город не найден</div>;
  }

  // Найдем комплекс по complexSlug
  const complexData = cityData.complexes.find(
    (item) => item.path.split("/").pop() === complexSlug
  );

  if (!complexData) {
    return <div>Жилой комплекс не найден</div>;
  }

  // Найдем квартиру по apartmentSlug
  const apartmentData = complexData.apartments.find(
    (item) => item.path === apartmentSlug
  );

  if (!apartmentData) {
    return <div>Квартира не найдена</div>;
  }

  // Получаем данные о первом разделе квартиры
  const section = apartmentData.sections[0];

  // Получаем данные для слайдера из apartmentData
  const sliderData = apartmentData.slider || [];
  // console.log(apartmentData.floor_count);

  return (
    <Container fluid className={styles.apartmentDetails}>
      <Container fluid className={styles.apartmentDetails__slider_container}>
        <ApartmentsSlider data={sliderData} />
      </Container>
      <Container className={styles.apartmentDetails__container}>
        <Row>
          <Col md={12}>
            <h1 className={styles.apartmentDetails__title}>
              Тип квартиры: {""}
              {section.title}.
            </h1>
            <h1 className={styles.apartmentDetails__title}>
              Площадь: {""}
              {parseFloat(section.area)
                .toString()
                .replace(/\.?0+$/, "")}{" "}
              м²
            </h1>
          </Col>
          <Col md={12} className={styles.apartmentDetails__subtitle_col}>
            <h2 className={styles.apartmentDetails__subtitle}>
              {complexData.name}
            </h2>
          </Col>
        </Row>
        <Row className={styles.apartmentDetails__image_row}>
          <Col className={styles.apartmentDetails__image_col_wrapper}>
            <Col
              className={styles.apartmentDetails__image_col}
              style={{ backgroundImage: `url(${section.image_1_url})` }}
            ></Col>
          </Col>
          <Col className={styles.apartmentDetails__image_col_wrapper}>
            <Col
              className={styles.apartmentDetails__image}
              style={{ backgroundImage: `url(${section.image_2_url})` }}
            ></Col>
            <Col
              className={styles.apartmentDetails__image}
              style={{ backgroundImage: `url(${section.image_3_url})` }}
            ></Col>
          </Col>
        </Row>
        <Row className={styles.apartmentDetails__address_row}>
          {/* <Col className={styles.apartmentDetails__address_col}>
            <Col className={styles.apartmentDetails__address}>
              <p className={styles.apartmentDetails__address_p}>
                квартира в доме {section.address}
              </p>
              <img
                className={styles.apartmentDetails__image_sector}
                src={section.image_4_url}
                alt=""
              />
            </Col>
            <Col className={styles.apartmentDetails__address}>
              <p className={styles.apartmentDetails__address_p}>
                квартира в секции {section.address}
              </p>
              <img
                className={styles.apartmentDetails__image_sector}
                src={section.image_5_url}
                alt=""
              />
            </Col>
          </Col> */}
          <Col>
            <p>{section.address}</p>
          </Col>
          <Col className={styles.apartmentDetails__details_col_description}>
            <ul className={styles.apartmentDetails__details}>
              <li className={styles.apartmentDetails__details_li}>
                <p className={styles.apartmentDetails__details_p_desc}>
                  Срок сдачи:{" "}
                </p>
                <p className={styles.apartmentDetails__details_p}>
                  {new Date(section.delivery_date).toLocaleDateString()}
                </p>
              </li>
              <li className={styles.apartmentDetails__details_li}>
                <p className={styles.apartmentDetails__details_p_desc}>
                  Количество комнат:{" "}
                </p>
                <p className={styles.apartmentDetails__details_p}>
                  {section.room_count}
                </p>
              </li>
              <li className={styles.apartmentDetails__details_li}>
                <p className={styles.apartmentDetails__details_p_desc}>
                  Этаж:{" "}
                </p>
                <p className={styles.apartmentDetails__details_p}>
                  {section.floor} из {apartmentData.floor_count}
                </p>
              </li>
              <li className={styles.apartmentDetails__details_li}>
                <p className={styles.apartmentDetails__details_p_desc}>Цена:</p>
                <p className={styles.apartmentDetails__details_p}>
                  {parseInt(section.price).toLocaleString()} ₽
                </p>
              </li>
              <li>
                <button
                  onClick={scrollToForm}
                  className={styles.apartmentDetails__button}
                >
                  Забронировать
                </button>
              </li>
            </ul>
          </Col>
        </Row>
      </Container>
      <Row>
        <Form id="form" formRef={formRef} />
      </Row>
    </Container>
  );
};

export default ApartmentDetails;
