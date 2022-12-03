import telegram.ext
word = '----BAARRKK---- '
API_KEY = "5065929557:AAGM841efkTOCnproDTzLphuMS7Z1n5IOVo"
#these functions will be executed when specified commands are detected by the code from the  bot
def start_command(update,context): 
    update.message.reply_text('hello there \n what are you doing here \n if your lost try /help ') #reply more bot response
def help_command(update,context): 
    update.message.reply_text('whats wrong little one got lost try going to google.com for help')
def meow_command(update,context): 
    update.message.reply_text(word)

def handle(update, context):
    text = str(update.message.text).lower()

    update.message.reply_text(word) #bot response

if __name__ == "__main__":
    updater = Updater(API_KEY,use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("bark", meow_command))

    dp.add_handler(MessageHandler(Filters.text , handle ))
    updater.start_polling(1.0)
    updater.idle()
