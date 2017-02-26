import telepot

from kiki.config import config


def get_telegram_bot(token=None):
    if token is not None:
        return telepot.Bot(token=token)
    return telepot.Bot(token=config['telegram']['token'])


def send_message(text, bot=None, chat_id=None):
    if bot is None:
        bot = get_telegram_bot()
    if chat_id is None:
        chat_id = config['telegram']['chat_id']
    return bot.sendMessage(chat_id=chat_id, text=text)
