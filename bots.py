from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater("5386523840:AAFDd498SkG03PTfsK1ST5DIehWrJJ6Ft4Y",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Welcome!, Kindly drop your full name, Email and a short description of the kind of  bot you want and we will get back to you shortly. Please write /help to see the commands available.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL""")

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "pre.chika.22@gmail.com")

def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://www.linkedin.com/in/precious-chika-14465118b/")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Linkedln', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))   
updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
	Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()




