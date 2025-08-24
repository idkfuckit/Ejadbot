import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get('BOT_TOKEN')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text.lower()
    
    if message_type in ['group', 'supergroup', 'channel']:
        if 'قروب' in text or 'قروبات' in text:
            response = "🌟 روابط مهمة لنادينا الجامعي 🌟\n\n"
            response += "• رابط القروب الرئيسي: https://t.me/+hOqfUhcp-dc5N2Vk\n"  # ✅ مصحح
            response += "• قروب المناقشات: (سيتم إضافته قريباً)\n\n"
            response += "انضم إلى قروباتنا واستفد من أنشطة النادي! 🎉"
            
            await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("البوت بدأ العمل... وانتظرته على القناة! 🚀")
    app.run_polling()
