import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get('BOT_TOKEN')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # التحقق من وجود الرسالة أولاً
        if not update.message or not update.message.text:
            return  # اخرج إذا لا توجد رسالة نصية
        
        chat_type = update.message.chat.type
        text = update.message.text.lower()
        
        logging.info(f"Received message in {chat_type}: {text}")
        
        if 'قروب' in text or 'قروبات' in text:
            response = "🌟 روابط مهمة لنادينا الجامعي 🌟\n\n"
            response += "• رابط القروب الرئيسي: https://t.me/+hOqfUhcp-dc5N2Vk\n"
            response += "• قروب المناقشات: (سيتم إضافته قريباً)\n\n"
            response += "انضم إلى قروباتنا واستفد من أنشطة النادي! 🎉"
            
            await update.message.reply_text(response)
            logging.info("Bot responded successfully!")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot started...")
    app.run_polling()