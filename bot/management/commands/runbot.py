from aiogram.utils import executor
from django.core.management import BaseCommand

from bot.management.commands.create_bot import dp
from bot.tg import client
from bot.tg import fsm_bot


class Command(BaseCommand):
    """Запуск бота через manage.py"""
    help = 'run bot'

    def handle(self, *args, **kwargs):
        fsm_bot.register_handlers_bot(dp)
        client.register_handlers_client(dp)
        executor.start_polling(dp, skip_updates=True)
