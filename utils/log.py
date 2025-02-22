from colorama import Fore, Style, init
from datetime import datetime

init()

def log(message, color=None):
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    if color:
        return print(f'{color}[{formatted_datetime}] - {message}{Style.RESET_ALL}')

    print(f'[{formatted_datetime}] - {message}')