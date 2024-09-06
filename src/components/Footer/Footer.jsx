import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "./Footer.module.css";
import Container from "react-bootstrap/esm/Container";
import FooterTop from "./FooterTop/FooterTop";
import FooterBottom from "./FooterBottom/FooterBottom";

export default function Footer() {
  return (
    <Container fluid className={styles.footer}>
      <Container className={styles.footer__contaiiner}>
        <FooterTop />
        <FooterBottom />
      </Container>
    </Container>
  );
}
