from commons import arg
from commons import config
import telepot

def get_telegram_bot(conf=None):
    if not conf:
        conf = config.get_config(file_path=arg.get_args_config().config_path)
    return telepot.Bot(token=conf['telegram']['token'])

def send_message(text, conf=None, bot=None, chat_id=None):
    print (arg.get_args_config().config_path)
    if not conf:
        conf = config.get_config(file_path=arg.get_args_config().config_path)
    if not bot:
        bot = telepot.Bot(token=conf['telegram']['token'])
    if not chat_id:
        chat_id = conf['telegram']['chat_id']
    if bot:
        return bot.sendMessage(chat_id=chat_id, text=text)