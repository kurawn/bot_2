from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.utils.request import Request
from telegram.ext import CommandHandler
from telegram.ext import Updater
from bot_2.config import TOKEN_BOT
from telegram import Update
from telegram.ext import CallbackContext

from ugc.models import DeepLinking


def start_command_handler(update, context):
    if context.args:
        link_obj = DeepLinking.objects.filter(referral_id=context.args[0]).first()
        if link_obj:
            update.message.reply_text(f'Приветствую {link_obj.user_name}! Твой уникальный код - {link_obj.user_id}')
        else:
            update.message.reply_text('Вы не можете начать использовать бот по незареєстрованой реферальной ссылки.' +
                                      ' Перейдите в бот с помощью реферальной ссылки')
    else:
        update.message.reply_text('Вы не можете начать использовать бот без реферальной ссылки.' +
                                  ' Перейдите в бот с помощью реферальной ссылки')


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=TOKEN_BOT,
        )

        updater = Updater(
            bot=bot,
            use_context=True,
        )

        print(bot.get_me())
        start_handler = CommandHandler('start', start_command_handler)

        updater.dispatcher.add_handler(start_handler)
        updater.start_polling()
        updater.idle()
