import requests
import time
from utils import DISCORD_TOKEN, USER_ID, print_color, save_messages

headers = {
    'Authorization': DISCORD_TOKEN,
    'Content-Type': 'application/json'
}

def get_channels(guild_id):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print_color(f"Erreur lors de la récupération des canaux de la guilde {guild_id}: {response.status_code}", "red")
        print(response.text)
        return []

def backup_messages(channel):
    url = f"https://discord.com/api/v9/channels/{channel['id']}/messages"
    last_message_id = None
    all_messages = []
    while True:
        params = {"limit": 100}
        if last_message_id:
            params["before"] = last_message_id
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            messages = response.json()
            if not messages:
                break
            all_messages.extend(messages)
            last_message_id = messages[-1]['id']
        else:
            print_color(f"Erreur lors de la récupération des messages: {response.status_code}", "red")
            break
    save_messages(f"{channel['name']}_{channel['id']}", all_messages)

def main(guild_id):
    print_color(f"Traitement des canaux dans la guilde cible ({guild_id})", "cyan")
    channels = get_channels(guild_id)
    for channel in channels:
        if channel['type'] in [0, 5]:  # Text channel or announcement channel
            print_color(f"Backup des messages du salon : {channel['name']} ({channel['id']})", "blue")
            backup_messages(channel)

if __name__ == "__main__":
    guild_id = input("Entrez l'ID du serveur pour backup : ")
    main(guild_id)
