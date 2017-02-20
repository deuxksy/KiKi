from commons import arg
from commons import config
from slacker import Slacker

def get_slack_bot(conf=None):
    if not conf:
        conf = config.get_config(file_path=arg.get_args_config().config_path)
    return Slacker(conf['slack']['token'])

def send_message(text, conf=None, bot=None, channel=None, username=None):
    if not conf:
        conf = config.get_config(file_path=arg.get_args_config().config_path)
    if not bot:
        bot = Slacker(conf['slack']['token'])
    if not username:
        username = conf['slack']['username']
    if not channel:
        channel = conf['slack']['channel']
    if bot:
        return bot.chat.post_message(channel=channel, text=text, username=username)

# Get users list
# response = slack.users.list()
# users = response.body['members']

# Upload a file
# slack.files.upload('hello.txt')