from django.db import models


class DynamicFormSubmission(models.Model):
    """Модель для хранения отправок динамических форм."""

    name = models.CharField(max_length=255, verbose_name="Название формы")
    data = models.JSONField(
        verbose_name="Данные формы"
    )  # Поле для хранения данных формы в виде JSON
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Отправка формы"
        verbose_name_plural = "Отправки форм"

    def __str__(self):
        return f"{self.name} - {self.submitted_at}"
