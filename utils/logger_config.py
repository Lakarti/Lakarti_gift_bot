# logger_config.py
import logging
from logging.handlers import RotatingFileHandler
import logging.config
from pythonjsonlogger import jsonlogger
import os


def configure_logging():
    """
    Настройка системы логирования.

    Эта функция конфигурирует систему логирования для вашего приложения,
    используя модуль `logging` стандартной библиотеки Python. Она определяет
    форматтеры, обработчики и уровни логирования для различных компонентов
    приложения.

    Форматтеры:
        - 'json_formatter': Форматтер в формате JSON для записи в файлы логов.
        - 'simple_formatter': Простой форматтер для консольного вывода и файлов логов.

    Обработчики:
        - 'file_handler': Обработчик для записи логов в файл app.log с ротацией.
        - 'console_handler': Обработчик для консольного вывода с использованием simple_formatter.
        - 'file_debug_handler': Обработчик для записи отладочных логов в файл debug.log с ротацией.
        - 'db_handler': Обработчик для записи логов БД в файл DB.log с ротацией.

    Логгеры:
        - 'db_logger': Логгер для ошибок в БД с уровнем ERROR.
        - 'code_logger': Логгер для ошибок в коде с уровнем ERROR.
        - 'debug_logger': Логгер для отладочных сообщений с уровнем DEBUG в консоль.
        - 'debug_file_logger': Логгер для отладочных сообщений с уровнем DEBUG в файл debug.log.

    Пример использования:
        from logger_config import configure_logging

        if __name__ == '__main__':
            configure_logging()
            asyncio.run(main())

    Дальше остается иницилизировать его в модулях
    Пример инициализации:
        debug_logger = logging.getLogger('debug_logger') # Передаем имя логгера который в конфиге

    """
    # Создаем папку "Logs" в текущей директории, если она не существует
    logs_dir = os.path.join(os.getcwd(), 'Logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_format = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json_formatter': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            },
            'simple_formatter': {
                'format': '%(asctime)s %(levelname)s %(module)s %(message)s %(pathname)s %(lineno)d',
            },
            'formatter_for_debug': {
                'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            },
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'simple_formatter',
                'filename': './Logs/app.log',
                'maxBytes': 1024 * 1024 * 10,
                'backupCount': 3,
                'encoding': 'utf-8',
            },
            'console_handler': {
                'class': 'logging.StreamHandler',
                'formatter': 'formatter_for_debug',
            },
            'file_debug_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'formatter_for_debug',
                'filename': './Logs/debug.log',
                'maxBytes': 1024 * 1024 * 10,
                'backupCount': 3,
                'level': 'DEBUG',
                'encoding': 'utf-8',
            },
            'db_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'simple_formatter',
                'filename': './Logs/DB.log',
                'maxBytes': 1024 * 1024 * 10,
                'backupCount': 3,
                'level': 'ERROR',
                'encoding': 'utf-8',
            }
        },
        'loggers': {
            'db_logger': {
                'handlers': ['db_handler'],
                'level': 'ERROR',
            },
            'code_logger': {
                'handlers': ['file_handler'],
                'level': 'ERROR',
            },
            'debug_logger': {
                'handlers': ['console_handler'],
                'level': 'DEBUG',
            },
            'debug_file_logger': {
                'handlers': ['file_debug_handler'],
                'level': 'DEBUG',
            }
        }
    }

    logging.config.dictConfig(log_format)


if __name__ == "__main__":
    print('logger.py Started on its own')
else:
    print('logger.py importend')