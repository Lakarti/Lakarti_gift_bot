import configparser
import os


def read_config(config_file_name: str = 'settings.ini'):
    config = configparser.ConfigParser()
    # Создаем папку, если ее не существует.
    logs_dir = os.path.join(os.getcwd(), 'settings')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    config_file_path = os.path.join(os.path.dirname(
        __file__), '..', 'settings', config_file_name)

    # Если файл не существует, создаем его с заданной структурой
    if not os.path.exists(config_file_path):
        create_default_config(config_file_path)

    if os.path.exists(config_file_path):
        config.read(config_file_path)
        return config
    else:
        raise FileNotFoundError(f"Config file not found: {config_file_path}")


def create_default_config(config_file_path):
    # Создаем структуру по умолчанию
    default_config = configparser.ConfigParser()
    default_config['Tg'] = {'password': '', 'api_bot': ''}
    default_config['DB'] = {'host': '',
                            'user': '', 'password': '', 'database': ''}

    # Записываем структуру в файл
    with open(config_file_path, 'w') as configfile:
        default_config.write(configfile)


if __name__ == "__main__":
    config = read_config()
else:
    print(f'{__name__} imported')
