import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import styles from "./About.module.css";
import about__img from "../../assets/about__ark_img.webp";
import garanty_img from "../../assets/about__garanty_img.webp";
import expert_img from "../../assets/expert_image.webp";

export default function About() {
  return (
    <Container fluid className={styles.about_fluid}>
      <Container fluid className={styles.about}>
        <Container className={styles.about__container}>
          <Row>
            <Col md={12}>
              <h1 className={styles.about__title}>О нас </h1>
            </Col>
          </Row>
          <Row className={styles.about__row_text}>
            <Col md={7} className={styles.about__text}>
              <div className={styles.about__text_div}>
                <p className={styles.about__text_title}>
                  Агентство{" "}
                  <span className={styles.about__title_color}>АРК</span>{" "}
                  Феодосия известно в регионе более 16 лет.{" "}
                </p>
                <p className={styles.about__text_p}>
                  За все годы, благодаря действиям слаженной профессиональной
                  команды, агентство заслужило истинное доверие граждан,
                  обратившихся за качественной, востребованной услугой к нам.{" "}
                </p>
                <p className={styles.about__text_p + " " + styles.third}>
                  В 2019 году Агентству{" "}
                  <span className={styles.about__title_color}>АРК</span>{" "}
                  Феодосия вручен диплом конкурса «Народный Бренд».
                </p>
              </div>
              <div>
                <p className={styles.about__text_p}>
                  Самый ценный ресурс в нашей жизни - это время. Мы максимально
                  экономим его для наших клиентов.
                </p>
                <p className={styles.about__text_p}>
                  При сделке с недвижимостью доверьте свои проблемы, заботы и
                  волнения профессионалам!
                </p>
              </div>
            </Col>
            <Col md={5} className={styles.about__img_col}>
              <img src={about__img} className={styles.about__img} alt="" />
            </Col>
          </Row>
        </Container>
      </Container>
      <Container className={styles.about__container}>
        <Container>
          <Row className={styles.about__row_second}>
            <Col md={12} className={styles.about__col}>
              <h1 className={styles.about__title_second}>
                <span className={styles.about__title_color_second}>арк</span>{" "}
                гарант безопасности
              </h1>
            </Col>
          </Row>
          <Row className={styles.about__row_garanty}>
            <Col className={styles.about__col_garanty_img}></Col>
            <Col className={styles.about__col_garanty_text}>
              <h5 className={styles.about__h5}>
                Наши клиенты получают полный спектр услуг специалистов, которые
                не просто сэкономят время клиента, но и:
              </h5>
              <ul className={styles.about__ul}>
                <li className={styles.about__li}>
                  <p className={styles.about__p}>1.</p>
                  <p className={styles.about__p}>
                    грамотно организуют и проведут анализ рынка
                  </p>
                </li>
                <li className={styles.about__li}>
                  <p className={styles.about__p}>2.</p>
                  <p className={styles.about__p}>
                    помогут установить реальную рыночную стоимость объекта,
                  </p>
                </li>
                <li className={styles.about__li}>
                  <p className={styles.about__p}>3.</p>
                  <p className={styles.about__p}>
                    рекламу товара на всех доступных ресурсах, которых у
                    агентств огромное количество, качественно презентуют и
                    покажут предмет продажи потенциальным покупателям,
                  </p>
                </li>
                <li className={styles.about__li}>
                  <p className={styles.about__p}>4.</p>
                  <p className={styles.about__p}>
                    проведут переговоры между сторонами сделки,{" "}
                  </p>
                </li>
                <li className={styles.about__li}>
                  <p className={styles.about__p}>5.</p>
                  <p className={styles.about__p}>
                    обеспечат безопасность расчетов
                  </p>
                </li>
              </ul>
              <p className={styles.about__text_p_last}>
                Главное, будут сопровождать сделку с момента подписания договора
                об оказании услуги до окончания главной процедуры – регистрации
                перехода права на имущество от продавца к покупателю.
              </p>
            </Col>
          </Row>
        </Container>
      </Container>
      <Container className={styles.expert__container}>
        <Container>
          <Row className={styles.expert__row}>
            <Col md={12} className={styles.expert__col}>
              <h1 className={styles.expert__title}>Экспертная команда</h1>
            </Col>
          </Row>
          <Row className={styles.expert__row_text}>
            <Col className={styles.expert__col_text}>
              <ul className={styles.expert__ul}>
                <li className={styles.expert__li}>
                  <p className={styles.expert__p}>01</p>
                  <p className={styles.expert__p}>
                    Комплексное обслуживание «под ключ»
                  </p>
                </li>
                <li className={styles.expert__li}>
                  <p className={styles.expert__p}>02</p>
                  <p className={styles.expert__p}>
                    Доступная цена и выгодные условия ипотеки
                  </p>
                </li>
                <li className={styles.expert__li}>
                  <p className={styles.expert__p}>03</p>
                  <p className={styles.expert__p}>Гарантия законности сделки</p>
                </li>
                <li className={styles.expert__li}>
                  <p className={styles.expert__p}>04</p>
                  <p className={styles.expert__p}>Продажа вашей недвижимости</p>
                </li>
                <li className={styles.expert__li}>
                  <p className={styles.expert__p}>05</p>
                  <p className={styles.expert__p}>Поиск недвижимости</p>
                </li>
                <li className={styles.expert__li}>
                  <p className={styles.expert__p}>06</p>
                  <p className={styles.expert__p}>Выгодная инвестиция</p>
                </li>
              </ul>
            </Col>
            <Col className={styles.about__col_expert_img}></Col>
          </Row>
        </Container>
      </Container>
      <Container className={styles.download__container}>
        <Row className={styles.download__row}>
          <Col className={styles.download_col}>
            <a
              className={styles.download__a}
              href="https://ark-dom.com/%D0%94%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%20%D1%81%20%D0%BF%D0%BE%D0%BA%D1%83%D0%BF%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%BC.%D0%9E%D1%84%D0%B5%D1%80%D1%82%D0%B0.pdf"
            >
              Договор с покупателем.Оферта.pdf
            </a>
          </Col>
          <Col className={styles.download__col}>
            <a
              className={styles.download__a}
              href="https://ark-dom.com/%D0%94%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%20%D1%81%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B2%D1%86%D0%BE%D0%BC.%D0%9E%D1%84%D0%B5%D1%80%D1%82%D0%B0.pdf"
            >
              Договор с продавцом.Оферта.pdf
            </a>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}
