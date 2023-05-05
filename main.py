from threading import Thread
from TelegramBotWrapper import TelegramBotWrapper


def run_server():
    # create TelegramBotWrapper instance
    # by default, read parameters in telegram_config.cfg
    tg_server = TelegramBotWrapper()
    # by default - read token from extensions/telegram_bot/telegram_token.txt
    tg_server.run_telegram_bot()


def setup():
    Thread(target=run_server).start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup()
