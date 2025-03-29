import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from summarizer import Summarizer
from utils.config import load_config

# Load configuration
config = load_config()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.updater = Updater(token=config['TELEGRAM_TOKEN'], use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.summarizer = Summarizer()

        # Set up command handlers
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.handle_message))

    def start(self, update, context):
        update.message.reply_text("Hello! I'm your chat summarizer bot. Send me messages and I'll summarize them for you.")

    def handle_message(self, update, context):
        user_message = update.message.text
        logger.info(f"Received message: {user_message}")
        
        # Process the message and generate a summary
        summary = self.summarizer.generate_summary(user_message)
        update.message.reply_text(f"Summary: {summary}")

    def run(self):
        logger.info("Bot is starting...")
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    bot = TelegramBot()
    bot.run()