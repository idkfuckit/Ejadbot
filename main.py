import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# تهيئة النظام لتسجيل الأحداث (لو حصل خطأ، نعرفه)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# الحصول على التوكن السري من إعدادات Render (الطريقة الآمنة)
TOKEN = os.environ.get(8442280038:AAHS0V1FUVThrR1FrKvgkSIFRiNonEianOA)  # هيك ما حدا بشوف التوكن

# الدالة التي ترد على الكلمات المفتاحية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text.lower()  # نحول النص لحروف صغيرة لتسهيل المطابقة
    
    # البوت يرد فقط إذا كانت الرسالة في مجموعة أو قناة
    if message_type in ['group', 'supergroup', 'channel']:
        if 'قروب' in text or 'قروبات' in text:
            # هذه هي الرسالة التي سيرسلها البوت
            response = "🌟 روابط مهمة لنادينا الجامعي 🌟\n\n"
            response += "• رابط القروب الرئيسي: https://t.me/+hOqfUhcp-dc5N2Vk\n"
            response += "• قروب المناقشات: 
            response += "• قروب الأنشطة:
            response += "انضم إلى قروباتنا واستفد من أنشطة النادي! 🎉"
            
            # أمر إرسال الرد
            await update.message.reply_text(response)

# الجزء الذي يشغل البوت
if __name__ == '__main__':
    # نبني التطبيق باستخدام التوكن
    app = Application.builder().token(TOKEN).build()
    
    # نضيف "أذن" للبوت لسماع الرسائل النصية وترك الأوامر (/start مثلاً)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # نبدأ بتشغيل البوت
    print("البوت بدأ العمل... وانتظرته على القناة! 🚀")

    app.run_polling()
