"""
Константы проекта
"""
import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'log.txt')

# мультиплатформенные пути
load_dotenv(os.path.join(BASE_DIR, '.env'))

# имя БД
DB_NAME = os.getenv('DB_NAME')

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# прочие константы
MAX_JOBS_NUM = 5
