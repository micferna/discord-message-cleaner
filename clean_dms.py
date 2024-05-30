import requests
import time
from utils import DISCORD_TOKEN, USER_ID, print_color

headers = {
    'Authorization': DISCORD_TOKEN,
    'Content-Type': 'application/json'
}

def get_dm_channels():
    url = "https://discord.com/api/v9/users/@me/channels"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print_color(f"Erreur lors de la récupération des DMs: {response.status_code}", "red")
        print(response.text)
        return []

def delete_messages(channel):
    url = f"https://discord.com/api/v9/channels/{channel['id']}/messages"
    last_message_id = None
    while True:
        params = {"limit": 100}
        if last_message_id:
            params["before"] = last_message_id
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            messages = response.json()
            if not messages:
                break
            for message in messages:
                if message['author']['id'] == USER_ID:
                    delete_url = f"{url}/{message['id']}"
                    while True:
                        delete_response = requests.delete(delete_url, headers=headers)
                        if delete_response.status_code == 204:
                            print_color(f"Message supprimé dans le DM avec {channel['recipients'][0]['username']}: {message['content']}", "green")
                            break
                        elif delete_response.status_code == 429:
                            retry_after = int(delete_response.headers.get('Retry-After', 1))
                            print_color(f"Limite de taux atteinte. Pause de {retry_after} secondes.", "yellow")
                            time.sleep(retry_after)
                        elif delete_response.status_code == 403:
                            # Ignore 403 errors silently
                            break
                        else:
                            print_color(f"Erreur lors de la suppression du message: {delete_response.status_code}", "red")
                            break
            last_message_id = messages[-1]['id']
        else:
            print_color(f"Erreur lors de la récupération des messages: {response.status_code}", "red")
            break

def main():
    dm_channels = get_dm_channels()
    for channel in dm_channels:
        print_color(f"Vérification du DM avec : {channel['recipients'][0]['username']} ({channel['id']})", "blue")
        delete_messages(channel)

if __name__ == "__main__":
    main()
