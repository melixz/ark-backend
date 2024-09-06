import React from "react";
import { Container } from "react-bootstrap";
import Form from "../Main/Form/Form";
import styles from "./HotForm.module.css";

export default function HotForm() {
  return (
    <Container fluid className={styles.container}>
      <Form />
    </Container>
  );
}
