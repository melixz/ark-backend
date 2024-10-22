from telegram import Bot
from telegram.ext import Updater
from django.conf import settings


# Функция для отправки сообщения в Телеграм
def send_to_telegram(chat_id, message):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=message)


# Основная функция для запуска бота
def run_telegram_bot():
    # Уведомляем, что бот начал работу
    send_to_telegram(settings.TELEGRAM_CHAT_ID, "Бот запущен и готов к работе!")

    # Запускаем бота для обработки событий (здесь можно добавить любые события, если нужно)
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)

    # Запускаем бота
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_telegram_bot()
