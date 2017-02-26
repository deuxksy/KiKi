from slacker import Slacker

from kiki.settings import config


def get_slack_bot(token=None):
    if token is not None:
        return Slacker(token=token)
    return Slacker(token=config['slack']['token'])


def send_message(text, bot=None, channel=None, username=None):
    if bot is None:
        bot = Slacker(config['slack']['token'])
    if username is None:
        username = config['slack']['username']
    if channel is None:
        channel = config['slack']['channel']
    return bot.chat.post_message(channel=channel, text=text, username=username)

    # Get users list
    # response = slack.users.list()
    # users = response.body['members']

    # Upload a file
    # slack.files.upload('hello.txt')
