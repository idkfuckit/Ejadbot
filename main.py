import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# تهيئة التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# التوكن من البيئة
TOKEN = os.environ.get('BOT_TOKEN')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'قروب' in text or 'قروبات' in text:
        response = "🌟 روابط مهمة لنادينا الجامعي 🌟\n\n"
        response += "• رابط القروب الرئيسي: https://t.me/+hOqfUhcp-dc5N2Vk\n"
        response += "• قروب المناقشات: (سيتم إضافته قريباً)\n\n"
        response += "انضم إلى قروباتنا للاستفادة من أنشطة النادي!"
        await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running and waiting...")
    app.run_polling()