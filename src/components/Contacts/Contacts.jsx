import React from "react";
import styles from "./Contacts.module.css";
import { Container, Row, Col } from "react-bootstrap";
import contacts__loc from "../../assets/contacts__loc.png";
import contacts__phone from "../../assets/contacts__call.png";
import contacts__clock from "../../assets/contacts__clock.png";

export default function Contacts() {
  return (
    <Container fluid className={styles.contacts}>
      <Container className={styles.contacts__container}>
        <Row className={styles.contacts__row_title}>
          <Col md={12} className={styles.contacts__title_wrapper}>
            <h1 className={styles.contacts__title}>
              Контакты <span className={styles.contacts__title_color}>АРК</span>
            </h1>
          </Col>
        </Row>
        <Row className={styles.contacts__row_desc}>
          <Col md={12} className={styles.contacts__col_desc}>
            <p className={styles.contacts__desc}>Адреса офисов:</p>
          </Col>
        </Row>
      </Container>
      <Container>
        <Container>
          <Row className={styles.contacts__row_adress}>
            <Col className={styles.adress_col}>
              <h5 className={styles.contacts__card_title}>Симферополь</h5>
              <ul className={styles.contacts__col_loc}>
                <li className={styles.contacts__card_loc}>
                  <img src={contacts__loc} alt="" />
                  <p className={styles.contacts__card_desc}>
                    г. Симферополь, ул. Набережная <br /> им. 60-летия СССР, 75,
                    лит. З,
                    <br /> 2 этаж, пом. 29
                  </p>
                </li>

                <li className={styles.contacts__card_clock}>
                  <img
                    src={contacts__clock}
                    className={styles.contacts__clock_icon}
                    alt=""
                  />
                  <p className={styles.contacts__card_desc}>
                    Пн-Пт с 8:00 до 17:00 офис <br /> С 8:00 до 20:00 прием
                    звонков
                  </p>
                </li>

                <li className={styles.contacts__card_phone}>
                  <img src={contacts__phone} alt="" />
                  <p className={styles.contacts__card_desc}>
                    +7 (978) 682-58-53
                  </p>
                </li>
              </ul>
            </Col>
            <Col className={styles.adress_col}>
              <h5 className={styles.contacts__card_title}>Феодосия</h5>
              <ul className={styles.contacts__col_loc}>
                <li className={styles.contacts__card_loc}>
                  <img src={contacts__loc} alt="" />
                  <p className={styles.contacts__card_desc}>
                    г. Феодосия, ул. Назукина 1,
                    <br /> Напротив Вечного огня
                  </p>
                </li>

                <li className={styles.contacts__card_clock}>
                  <img
                    src={contacts__clock}
                    className={styles.contacts__clock_icon}
                    alt=""
                  />
                  <p className={styles.contacts__card_desc}>
                    Пн-Пт с 8:00 до 17:00 офис <br />С 8:00 до 20:00 прием
                    звонков
                  </p>
                </li>

                <li className={styles.contacts__card_phone}>
                  <img src={contacts__phone} alt="" />
                  <p className={styles.contacts__card_desc}>
                    +7 (978) 692-01-64
                  </p>
                </li>
              </ul>
            </Col>
          </Row>
        </Container>
      </Container>
      <Container className={styles.contacts__centers}>
        <Row className={styles.contacts__row_center}>
          <Col className={styles.contacts__center}>
            <p>Ипотечный центр</p>
            <p>+7(978)692–01–64</p>
          </Col>
          <Col className={styles.contacts__center}>
            <p>Юридическая служба</p>
            <p>+7(978)505–32–92</p>
          </Col>
          <Col className={styles.contacts__center}>
            <p>Служба персонала</p>
            <p>+7(978)692–01–91</p>
          </Col>
        </Row>
      </Container>
      <Container fluid className={styles.contacts__map}>
        <Container className={styles.contacts__map_container}>
          <Row className={styles.contacts__map_row}>
            <Col md={12} className={styles.contacts__map_col}>
              <h1 className={styles.contacts__map_title}>Реквизиты компании</h1>
            </Col>
          </Row>
          <Row className={styles.contacts__form_row}>
            <Col md={6} className={styles.contacts__form_col}>
              <ul className={styles.contacts__form_list}>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>Форма</p>
                  <p className={styles.contacts__form_p}>
                    ООО "АРК Недвижимость" 
                  </p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>Адрес</p>
                  <p className={styles.contacts__form_p}>
                    Феодосия, ул. Назукина 1
                  </p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>ИНН/КПП</p>
                  <p className={styles.contacts__form_p}>
                     9108126365 / 910801001
                  </p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>ОГРН</p>
                  <p className={styles.contacts__form_p}>1219100011790</p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>Р/с</p>
                  <p className={styles.contacts__form_p}>
                    40702810440100000099
                  </p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>К/с</p>
                  <p className={styles.contacts__form_p}>
                    30101810335100000607
                  </p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>Банк</p>
                  <p className={styles.contacts__form_p}>ПАО РНКБ</p>
                </li>
                <li className={styles.contacts__form_li}>
                  <p className={styles.contacts__form_p}>БИК</p>
                  <p className={styles.contacts__form_p}>043510607</p>
                </li>
              </ul>
            </Col>
          </Row>
        </Container>
      </Container>
    </Container>
  );
}
