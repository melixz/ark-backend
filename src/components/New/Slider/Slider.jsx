import React, { useState, useEffect, useRef } from "react";
import styles from "./Slider.module.css";
import control_left from "../../../assets/new__controls_left.png";
import control_right from "../../../assets/new__controls_right.png";
import { Link } from "react-router-dom";

const Slider = ({ data }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [visibleSlides, setVisibleSlides] = useState(3);
  const sliderRef = useRef(null);
  const [slideWidth, setSlideWidth] = useState(100 / 3);
  const gap = 14;
  const [touchStart, setTouchStart] = useState(0);
  const [touchEnd, setTouchEnd] = useState(0);

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => {
      if (prevIndex >= data.length - visibleSlides) {
        return 0;
      }
      return prevIndex + 1;
    });
  };

  const prevSlide = () => {
    setCurrentIndex((prevIndex) => {
      if (prevIndex <= 0) {
        return data.length - visibleSlides;
      }
      return prevIndex - 1;
    });
  };

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 768) {
        setVisibleSlides(3);
        setSlideWidth(100 / 3);
      } else {
        setVisibleSlides(1);
        setSlideWidth(100);
      }
    };

    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  useEffect(() => {
    if (sliderRef.current) {
      const transformValue = `translateX(calc(-${
        currentIndex * slideWidth
      }% - ${currentIndex * gap}px))`;
      sliderRef.current.style.transition = "transform 0.8s ease";
      sliderRef.current.style.transform = transformValue;

      const currentSliderRef = sliderRef.current;
      const transitionEndHandler = () => {
        if (currentIndex === data.length) {
          currentSliderRef.style.transition = "none";
          currentSliderRef.style.transform = `translateX(0)`;
          setCurrentIndex(0);
        } else if (currentIndex === -1) {
          currentSliderRef.style.transition = "none";
          currentSliderRef.style.transform = `translateX(calc(-${
            (data.length - 1) * slideWidth
          }% - ${(data.length - 1) * gap}px))`;
          setCurrentIndex(data.length - 1);
        }
      };

      currentSliderRef.addEventListener("transitionend", transitionEndHandler);
      return () => {
        currentSliderRef?.removeEventListener(
          "transitionend",
          transitionEndHandler
        );
      };
    }
  }, [currentIndex, slideWidth, data]);

  const handleTouchStart = (e) => {
    setTouchStart(e.targetTouches[0].clientX);
  };

  const handleTouchMove = (e) => {
    setTouchEnd(e.targetTouches[0].clientX);
  };

  const handleTouchEnd = () => {
    if (touchStart - touchEnd > 50) {
      nextSlide();
    } else if (touchStart - touchEnd < -50) {
      prevSlide();
    }
  };
  // console.log(data);

  return (
    <div className={styles.slider}>
      <div className={styles.sliderWrapper}>
        <div
          className={styles.sliderContainer}
          ref={sliderRef}
          onTouchStart={handleTouchStart}
          onTouchMove={handleTouchMove}
          onTouchEnd={handleTouchEnd}
        >
          {data.map((item, index) => (
            <div
              key={index}
              className={styles.sliderSlide}
              style={{ backgroundImage: `url(${item.complex_card_bg})` }}
            >
              <h2 className={styles.sliderTitle}>{item.city || item.name}</h2>
              <Link to={item.path} className={styles.sliderButton_more}>
                Подробнее
              </Link>
            </div>
          ))}
        </div>
      </div>
      <div className={styles.sliderControls}>
        <button className={styles.sliderButton} onClick={prevSlide}>
          <img src={control_left} alt="" />
        </button>
        <button className={styles.sliderButton} onClick={nextSlide}>
          <img src={control_right} alt="" />
        </button>
      </div>
    </div>
  );
};

export default Slider;
