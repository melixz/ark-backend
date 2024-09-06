import React from "react";
import { useParams } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import styles from "./City.module.css";
import Slider from "../New/Slider/Slider";

const City = ({ data }) => {
  const { citySlug } = useParams();

  const cityData = data.find(
    (item) => item.path && item.path.split("/").pop() === citySlug
  );

  if (!cityData) {
    return <div>Город не найден</div>;
  }

  // Проверка на наличие section и его длины
  if (!cityData.section || cityData.section.length === 0) {
    return <div>Данные о городе неполны</div>;
  }

  // Динамический доступ к первому элементу section
  const section = cityData.section[0];

  // Проверка на наличие необходимых свойств
  const title = section.title || "Default Title";
  const desc_1 = section.desc_1 || "Default Description";
  const desc_2 = section.desc_2 || "Default Description";
  const img_1 = section.image_1_url || "";
  const img_2 = section.image_2_url || "";
  const img_3 = section.image_3_url || "";
  const img_4 = section.image_4_url || "";
  const loc = section.loc || "Default Location";

  return (
    <Container fluid className={styles.city_fluid}>
      <Container
        fluid
        style={{ backgroundImage: `url(${cityData.complex_bg})` }}
        className={styles.city__container}
      >
        <Container className={styles.city__contaiiner_title}>
          <Row className={styles.city__row}>
            <Col className={styles.city__col}>
              <h1 className={styles.city__title}>{cityData.title}</h1>
              <p className={styles.city__desc}>{cityData.desc}</p>
            </Col>
          </Row>
        </Container>
        <Slider data={cityData.complexes} />
      </Container>
      <Container fluid className={styles.section__one_container}>
        <Container>
          <Row className={styles.section__one_row}>
            <Col md={12} className={styles.section__one_col}>
              <h1 className={styles.section__one_title}>{title}</h1>
            </Col>
          </Row>
          <Row className={styles.section__image_row}>
            <Col
              md={6}
              className={styles.section__one_img}
              style={{
                backgroundImage: `url(${img_1})`,
              }}
            ></Col>
            <Col md={6} className={styles.section__one_text}>
              <ul className={styles.section__text_list}>
                <li className={styles.section__text_item}>
                  <p className={styles.section__text_item_title}>Климат</p>
                  <p
                    className={
                      styles.section__text_item_title + " " + styles.desc_base
                    }
                  >
                    средиземноморский
                  </p>
                </li>
                <li className={styles.section__text_item}>
                  <p className={styles.section__text_item_title}>
                    Географическое <br /> положение
                  </p>
                  <p
                    className={
                      styles.section__text_item_title + " " + styles.desc_base
                    }
                  >
                    {loc}
                  </p>
                </li>
                <li className={styles.section__text_item}>
                  <p className={styles.section__text_item_title}>
                    Среднегодовая <br /> температура
                  </p>
                  <p
                    className={
                      styles.section__text_item_title + " " + styles.desc_base
                    }
                  >
                    +13,8 °C
                  </p>
                </li>
              </ul>
              <p className={styles.section__text_item_desc}>{desc_1}</p>
            </Col>
          </Row>
        </Container>
      </Container>
      <Container fluid className={styles.section__two_container}>
        <Container>
          <Row className={styles.section__two_row}>
            <Col className={styles.section__two_col}>
              <p className={styles.section__two_text}>{desc_2}</p>
              <img
                className={
                  styles.section__two_icon +
                  " " +
                  styles.section__two_icon_first
                }
                src={img_2}
                alt=""
              />
            </Col>
            <Col className={styles.section__two_col}>
              <img
                className={
                  styles.section__two_icon +
                  " " +
                  styles.section__two_icon_second
                }
                src={img_3}
                alt=""
              />
              <img
                className={
                  styles.section__two_icon +
                  " " +
                  styles.section__two_icon_third
                }
                src={img_4}
                alt=""
              />
            </Col>
          </Row>
        </Container>
      </Container>
    </Container>
  );
};

export default City;
