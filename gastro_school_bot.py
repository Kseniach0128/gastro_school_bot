
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

MENU, FAQ, QUESTION = range(3)

reply_keyboard = [['1️⃣ Программа', '2️⃣ FAQ'],
                  ['3️⃣ Поступление', '4️⃣ Кейсы'],
                  ['5️⃣ Задать вопрос']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот приёмной кампании «Школы Гастрономии». Чем могу помочь?",
        reply_markup=markup
    )
    return MENU

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "1️⃣" in text:
        await update.message.reply_text(
            "Наша программа — это 6 месяцев практики с шефами.\nМодули: гастрономия, сервис, стажировка.\nПодробнее: https://school.link/program"
        )
    elif "2️⃣" in text:
        await update.message.reply_text(
            "Частые вопросы:\n1. Как подать заявку?\n2. Сколько стоит?\n3. Есть ли общежитие?\n4. Какие документы нужны?\nНапиши номер или свой вопрос."
        )
        return FAQ
    elif "3️⃣" in text:
        await update.message.reply_text(
            "Поступление:\n1. Заявка онлайн\n2. Собеседование\n3. Ответ комиссии\nФорма: https://school.link/apply"
        )
    elif "4️⃣" in text:
        await update.message.reply_text(
            "💼 Успешные кейсы:\n- Алексей К. — шеф в Мишлен-ресторане\n- Мария П. — открыла гастробар\nБольше: https://school.link/cases"
        )
    elif "5️⃣" in text:
        await update.message.reply_text("Напиши свой вопрос — я постараюсь ответить или передам менеджеру.")
        return QUESTION

    return MENU

async def handle_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
    await update.message.reply_text(f"Спасибо за вопрос: «{question}». Мы свяжемся с вами при необходимости.")
    return MENU

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text
    await update.message.reply_text(f"Ваш вопрос передан менеджеру: «{user_question}». Спасибо!")
    return MENU

def main():
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu)],
            FAQ: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_faq)],
            QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question)],
        },
        fallbacks=[]
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
