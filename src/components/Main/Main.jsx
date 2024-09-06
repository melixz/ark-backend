import React, { useRef } from "react";
import styles from "./Main.module.css";
import MainTop from "./MainTop/MainTop";
import MainButton from "./MainButton/MainButton";
import MainCards from "./MainCards/MainCards";
import WhyComponent from "./WhyComponent/WhyComponent";
import crimea_img from "../../assets/Crimea_icon.png";
import Cards from "../Main/Cards/Cards";
import { Col, Container, Row } from "react-bootstrap";
import Form from "../Main/Form/Form";
import shield from "../../assets/secure.png";
import home from "../../assets/home.png";
import peoples from "../../assets/peoples.png";
import hands from "../../assets/hands.png";
const buildsPreority = [
  {
    id: 1,
    title: "Солнце, море, лето круглый год",
  },
  {
    id: 2,
    title: "Мягкий климат",
  },
  {
    id: 3,
    title: "Природные условия",
  },
  {
    id: 4,
    title: "Доступность отдыха",
  },
  {
    id: 5,
    title: "Развитая инфраструктура",
  },
  {
    id: 6,
    title: "Возможность получения дохода",
  },
];
const staticCards = [
  {
    id: 1,
    title: "Более 16 лет успешной работы",
    description:
      "Через наше агентство прошло сотни успешных сделок различной сложности.",
    path: "/about",
    image: shield,
  },
  {
    id: 2,
    title: "АРК – гарант безопасности",
    description:
      "является гарантом безопасности на всех этапах сделки купли/продажи.",
    path: "/about",
    image: home,
  },
  {
    id: 3,
    title: "Экспертная команда",
    description:
      "профессионалы своего дела, которые работают с каждым клиентом от начала и до результата.",
    path: "/about",
    image: peoples,
  },
  {
    id: 4,
    title: "Клиентский  сервис",
    description:
      "Мы оказываем риэлторские, юридические услуги, сопровождение ипотеки  и другие услуги",
    path: "/about",
    image: hands,
  },
];

export default function Main() {
  const formRef = useRef(null);

  const scrollToForm = (e) => {
    e.preventDefault();
    if (formRef.current) {
      formRef.current.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  };

  return (
    <Container fluid className={styles.main}>
      <MainTop scrollToForm={scrollToForm} />
      <MainButton scrollToForm={scrollToForm} />
      <MainCards />
      <Container>
        <WhyComponent
          bgr={crimea_img}
          first={buildsPreority[0].title}
          second={buildsPreority[1].title}
          third={buildsPreority[2].title}
          fourth={buildsPreority[3].title}
          fifth={buildsPreority[4].title}
          sixth={buildsPreority[5].title}
        >
          Почему Крым?
        </WhyComponent>
      </Container>
      <Container className={styles.cards__container}>
        <Row className={styles.cards__row}>
          <Col md={12} sm={12} className={styles.cards__title_section}>
            <h1 className={styles.cards__title}>Почему нам доверяют</h1>
          </Col>
          <Cards cards={staticCards} />
        </Row>
      </Container>
      <Form id="form" formRef={formRef} />
    </Container>
  );
}
