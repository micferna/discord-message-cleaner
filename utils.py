import os
from dotenv import load_dotenv
from colorama import init, Fore, Style
import json

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

def save_messages(file_name, messages):
    with open(f"{file_name}.json", 'w', encoding='utf-8') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)
    print_color(f"Messages sauvegardés dans {file_name}.json", "green")
