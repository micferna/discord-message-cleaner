import os
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Initialiser colorama
init(autoreset=True)

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = os.getenv('USER_ID')
EXCLUDED_GUILD_IDS = os.getenv('EXCLUDED_GUILD_IDS').split(',')

def print_color(text, color):
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'cyan': Fore.CYAN
    }
    print(f"{colors[color]}{text}{Style.RESET_ALL}")
