from clean_dms import main as clean_dms
from clean_guild_messages import main as clean_guild_messages
from clean_specific_guild import main as clean_specific_guild
from backup_guild_messages import main as backup_guild_messages
from utils import print_color

def print_menu():
    print_color("╔═════════════════════════════════════════════════════╗", "cyan")
    print_color("║                      Menu Principal                  ║", "cyan")
    print_color("╠═════════════════════════════════════════════════════╣", "cyan")
    print_color("║ 1. Nettoyer les messages privés (DMs)                ║", "white")
    print_color("║ 2. Nettoyer les messages dans tous les serveurs      ║", "white")
    print_color("║    sauf ceux exclus dans le fichier .env             ║", "white")
    print_color("║ 3. Nettoyer les messages dans un serveur spécifique  ║", "white")
    print_color("║ 4. Sauvegarder les messages d'un serveur spécifique  ║", "white")
    print_color("╠═════════════════════════════════════════════════════╣", "cyan")
    print_color("║ 0. Quitter                                           ║", "red")
    print_color("╚═════════════════════════════════════════════════════╝", "cyan")
    choice = input("\033[1;33mSélectionnez une option (1-4, 0 pour quitter): \033[0m")

    return choice

def menu():
    while True:
        choice = print_menu()

        if choice == '1':
            clean_dms()
        elif choice == '2':
            clean_guild_messages()
        elif choice == '3':
            guild_id = input("\033[1;33mEntrez l'ID du serveur à nettoyer : \033[0m")
            clean_specific_guild(guild_id)
        elif choice == '4':
            guild_id = input("\033[1;33mEntrez l'ID du serveur pour backup : \033[0m")
            backup_guild_messages(guild_id)
        elif choice == '0':
            print_color("Au revoir!", "cyan")
            break
        else:
            print_color("Choix invalide. Veuillez réessayer.", "red")

if __name__ == "__main__":
    menu()
