from kiki import config
import telepot

def get_telegram_bot(conf=None):
    return telepot.Bot(token=config['telegram']['token'])

def send_message(text, bot=None, chat_id=None):
    if not bot:
        bot = telepot.Bot(token=config['telegram']['token'])
    if not chat_id:
        chat_id = config['telegram']['chat_id']
    if bot:
        return bot.sendMessage(chat_id=chat_id, text=text)