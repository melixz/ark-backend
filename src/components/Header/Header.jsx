import React, { useState } from "react";
import styles from "./Header.module.css";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Logo from "../Header/Logo/Logo";
import Nav from "./Nav/Nav";
import Contants from "../Header/Contants/Contants";
import BurgerMenu from "../Header/BurgerMenu/BurgerMenu";
import SideMenu from "../Header/SideMenu/SideMenu";
import { Col } from "react-bootstrap";

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <Container fluid className={styles.header}>
      <Container fluid className={styles.header__container}>
        <Row className={styles.header__row}>
          <Col>
            <Logo />
          </Col>
          {/* <Col>
            <Location />
          </Col> */}
          <Col>
            <Nav isOpen={isMenuOpen} />
          </Col>
          <Col md={3}>
            <Contants />
          </Col>
          <BurgerMenu isOpen={isMenuOpen} onClick={toggleMenu} />
        </Row>
      </Container>
      {isMenuOpen && <SideMenu isOpen={isMenuOpen} onClose={toggleMenu} />}
    </Container>
  );
}
