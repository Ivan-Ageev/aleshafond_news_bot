import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
import urllib.parse
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7304359723:AAFH8aTxRBoNk_hhvNDV_B5GLH2A4Vih7aU'
SEARCH_URL = 'https://aleshafond.ru/news?search='
LOGO_PATH = '/Users/ivan/Downloads/bear3.png'

# Словарь для хранения последнего сообщения
last_message_ids = {}


def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("О детях 👨‍👧", callback_data='search'),
         InlineKeyboardButton("О фонде 🏢", callback_data='about')],
        [InlineKeyboardButton("Помочь сейчас! ❤️", url='https://aleshafond.ru/how-to-help')]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat.id

    # Удаляем предыдущее сообщение, если оно есть
    if chat_id in last_message_ids:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_message_ids[chat_id])
        except Exception as e:
            logger.warning(f"Не удалось удалить предыдущее сообщение: {e}")

    # Приветственное сообщение
    welcome_message = (
        "Привет! 👋 Я — новостной бот фонда «Алёша». Мы помогаем детям с тяжелыми заболеваниями, и ты тоже можешь внести свой вклад! "
        "Как я могу помочь тебе сегодня?"
    )

    with open(LOGO_PATH, 'rb') as photo:
        sent_message = await update.message.reply_photo(
            photo=photo,
            caption=welcome_message,
            reply_markup=get_main_keyboard()
        )

    # Сохраняем ID нового сообщения
    last_message_ids[chat_id] = sent_message.message_id


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    chat_id = query.message.chat_id

    # Удаляем предыдущее сообщение
    if chat_id in last_message_ids:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_message_ids[chat_id])
        except Exception as e:
            logger.warning(f"Не удалось удалить предыдущее сообщение: {e}")

    if query.data == 'search':
        sent_message = await query.message.reply_text(
            "Отправьте мне фамилию ребёнка, и я расскажу, как у него дела! 💪",
            reply_markup=get_main_keyboard()
        )
    elif query.data == 'about':
        about_text = (
            """Уже более 15 лет мы помогаем детям! 

Наш фонд начинался как волонтерская организация, мы собирали вещи и организовывали мероприятия для детских домов. Затем мы создали фонд «Алёша» для помощи малышам с тяжелыми заболеваниями.

Для многих семей счета за специализированную медицинскую помощь становятся неподъемными. 

Но вместе мы можем им помочь! Ведь чужих детей не бывает.

За эти годы мы собрали средства для сотен детей и оплатили им операции, реабилитации и лекарства. Это стало возможным благодаря вам! 

Огромное спасибо за ваше доброе сердце!"""
        )
        sent_message = await query.message.reply_text(
            about_text,
            reply_markup=get_main_keyboard()
        )

    # Сохраняем ID нового сообщения
    last_message_ids[chat_id] = sent_message.message_id


async def search_news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text
    encoded_query = urllib.parse.quote(query)
    webapp_url = f"https://aleshafond.ru/news?search={encoded_query}"
    web_app = WebAppInfo(url=webapp_url)

    chat_id = update.message.chat.id

    # Удаляем предыдущее сообщение
    if chat_id in last_message_ids:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_message_ids[chat_id])
        except Exception as e:
            logger.warning(f"Не удалось удалить предыдущее сообщение: {e}")

    with open(LOGO_PATH, 'rb') as photo:
        sent_message = await update.message.reply_photo(
            photo=photo,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Вот, что я нашёл! 👈", web_app=web_app)],
                [InlineKeyboardButton("Спросить ещё! 😊", callback_data='search'),
                 InlineKeyboardButton("О фонде 🏢", callback_data='about')],
                [InlineKeyboardButton("Помочь сейчас! ❤️", url='https://aleshafond.ru/how-to-help')]
            ])
        )

    # Сохраняем ID нового сообщения
    last_message_ids[chat_id] = sent_message.message_id


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_news))

    application.run_polling()


if __name__ == '__main__':
    main()



