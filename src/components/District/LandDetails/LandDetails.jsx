import React, { useRef } from "react";
import { useParams } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import styles from "./LandDetails.module.css";
import LandSlider from "../LandSlider/LandSlider";
import Form from "../../Main/Form/Form";

const LandDetails = ({ data }) => {
  const { citySlug, districtSlug, landSlug } = useParams();
  const formRef = useRef(null);

  const scrollToForm = (e) => {
    e.preventDefault();
    if (formRef.current) {
      formRef.current.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  // Найдем город по citySlug
  const cityData = data?.find(
    (item) => item.path && item.path.split("/").pop() === citySlug
  );

  if (!cityData) {
    console.log("Город не найден:", citySlug);
    return <div>Город не найден</div>;
  }

  // console.log("City Data:", cityData);

  // Проверяем, есть ли массив plots у cityData
  if (!cityData.plots || !Array.isArray(cityData.plots)) {
    console.error(
      "Массив участков (plots) отсутствует или имеет неверную структуру"
    );
    return <div>Участки для данного города отсутствуют</div>;
  }

  // Найдем район по districtSlug
  const districtData = cityData.plots?.find(
    (item) => item.path && item.path.split("/").pop() === districtSlug
  );

  if (!districtData) {
    console.log("Район не найден:", districtSlug);
    return <div>Район не найден</div>;
  }

  // console.log("District Data:", districtData);

  // Найдем участок по landSlug
  const landData = districtData.lands?.find((item) => item.path === landSlug);

  if (!landData) {
    console.log("Участок не найден:", landSlug);
    return <div>Участок не найден</div>;
  }
  console.log(landData);

  // Получаем данные для слайдера из landData
  const sliderData = landData.slider || [];
  console.log(districtData);
  return (
    <Container fluid className={styles.landDetails}>
      <Container fluid className={styles.landDetails__slider_container}>
        <LandSlider data={sliderData} />
      </Container>
      <Container className={styles.landDetails__container}>
        <Row>
          <Col md={12}>
            <h1 className={styles.landDetails__title}>
              Участок №{landData.number}
            </h1>
            <h1 className={styles.landDetails__title}>
              Площадь:{" "}
              {parseFloat(landData.area)
                .toString()
                .replace(/\.?0+$/, "")}{" "}
              соток
            </h1>
          </Col>
          <Col md={12} className={styles.landDetails__subtitle_col}>
            <h2 className={styles.landDetails__subtitle}>
              {districtData.district}
            </h2>
          </Col>
        </Row>
        <Row className={styles.landDetails__image_row}>
          <Col className={styles.landDetails__image_col_wrapper}>
            <Col
              className={styles.landDetails__image_col}
              style={{ backgroundImage: `url(${landData.image_1_url})` }}
            ></Col>
          </Col>
          <Col className={styles.landDetails__image_col_wrapper}>
            <Col
              className={styles.landDetails__image}
              style={{ backgroundImage: `url(${landData.image_2_url})` }}
            ></Col>
            <Col
              className={styles.landDetails__image}
              style={{ backgroundImage: `url(${landData.image_3_url})` }}
            ></Col>
          </Col>
        </Row>
        <Row className={styles.landDetails__address_row}>
          <Col className={styles.landDetails__address_col}>
            <Col className={styles.landDetails__address}>
              <p className={styles.landDetails__address_p}>
                Участок в районе {districtData.name}
              </p>
              <img
                className={styles.landDetails__image_sector}
                src={landData.image_4_url}
                alt=""
              />
            </Col>
            <Col className={styles.landDetails__address}>
              <p className={styles.landDetails__address_p}>
                Участок в городе {cityData.name}
              </p>
              <img
                className={styles.landDetails__image_sector}
                src={landData.image_5_url}
                alt=""
              />
            </Col>
          </Col>
          <Col className={styles.landDetails__details_col_description}>
            <ul className={styles.landDetails__details}>
              <li className={styles.landDetails__details_li}>
                <p className={styles.landDetails__details_p_desc}>Участок №</p>
                <p className={styles.landDetails__details_p}>
                  {landData.number}
                </p>
              </li>
              <li className={styles.landDetails__details_li}>
                <p className={styles.landDetails__details_p_desc}>Цена: </p>
                <p className={styles.landDetails__details_p}>
                  {parseInt(landData.price).toLocaleString()} ₽
                </p>
              </li>
              <li className={styles.landDetails__details_li}>
                <p className={styles.landDetails__details_p_desc}>
                  Тип участка:
                </p>
                <p className={styles.landDetails__details_p}>{landData.type}</p>
              </li>
              <li className={styles.landDetails__details_li}>
                <p className={styles.landDetails__details_p_desc}>Описание: </p>
                <p className={styles.landDetails__details_p}>
                  {landData.description}
                </p>
              </li>
              <li>
                <button
                  onClick={scrollToForm}
                  className={styles.landDetails__button}
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

export default LandDetails;
