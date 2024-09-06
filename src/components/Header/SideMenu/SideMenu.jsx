import React from "react";
import styles from "./SideMenu.module.css";
import { Link } from "react-router-dom";
import { Col, Container, Row } from "react-bootstrap";

const SideMenu = ({ isOpen, onClose }) => {
  return (
    <div className={`${styles.sideMenu} ${isOpen ? styles.open : ""}`}>
      <button className={styles.closeButton} onClick={onClose}>
        &times;
      </button>
      <div className={styles.menuContent}>
        <Container>
          <Row>
            <Col>
              <Link onClick={onClose} to="/">
                Главная
              </Link>
              <Link onClick={onClose} to="/new">
                Новостройки
              </Link>
              <Link onClick={onClose} to="/plots">
                Участки
              </Link>
              <Link onClick={onClose} to="/services">
                Услуги
              </Link>
              <Link onClick={onClose} to="/about">
                О нас
              </Link>
              <Link onClick={onClose} to="/contacts">
                Контакты
              </Link>
              <Link onClick={onClose} to="/hot-form">
                Заполнить заявку
              </Link>
            </Col>
          </Row>
        </Container>
      </div>
    </div>
  );
};

export default SideMenu;
