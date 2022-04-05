import sys
import bot

from botrequests.common import *
from config import LOG_FILE
from loguru import logger


# логирование
logger.add(sys.stderr, format="{time} {level} {message}")
logger.add(LOG_FILE, rotation="10 MB")
logger.info("Start logging!")


# Точка входа
if __name__ == '__main__':
    # Запуск поллинга
    bot.infinity_polling()
