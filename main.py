from clean_dms import main as clean_dms
from clean_guild_messages import main as clean_guild_messages
from clean_specific_guild import main as clean_specific_guild
from utils import print_color

def menu():
    print_color("Menu principal:", "cyan")
    print_color("1. Nettoyer les messages privés (DMs)", "blue")
    print_color("2. Nettoyer les messages dans tous les serveurs sauf ceux exclus", "blue")
    print_color("3. Nettoyer les messages dans un serveur spécifique", "blue")
    print_color("4. Quitter", "red")
    choice = input("Sélectionnez une option: ")

    if choice == '1':
        clean_dms()
    elif choice == '2':
        clean_guild_messages()
    elif choice == '3':
        guild_id = input("Entrez l'ID du serveur à nettoyer : ")
        clean_specific_guild(guild_id)
    elif choice == '4':
        print_color("Au revoir!", "cyan")
    else:
        print_color("Choix invalide. Veuillez réessayer.", "red")
        menu()

if __name__ == "__main__":
    menu()
