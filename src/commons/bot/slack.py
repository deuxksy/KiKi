from settings import config
from slacker import Slacker

def get_slack_bot():
    return Slacker(config['slack']['token'])

def send_message(text, bot=None, channel=None, username=None):
    if not bot:
        bot = Slacker(config['slack']['token'])
    if not username:
        username = config['slack']['username']
    if not channel:
        channel = config['slack']['channel']
    if bot:
        return bot.chat.post_message(channel=channel, text=text, username=username)

# Get users list
# response = slack.users.list()
# users = response.body['members']

# Upload a file
# slack.files.upload('hello.txt')