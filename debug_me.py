# Piedzīvojums Spoku Mājā
import random

# Inicializē mainīgos
inventory = []
player_alive = True

# Definē funkciju, kas sāk spēli un vada ciklu, kamēr spēlētājs ir dzīvs
def start_game():
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi' un 'dzīvojamo istabu'.")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba"]:
        choice = input(">>> ").lower()
        if choice == "virtuve":
            kitchen()
        elif choice == "dzīvojamā istaba":
            living_room()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def kitchen():
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod rūsinātu nazi. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
    choice = ""
    while choice not in ["ņem", "aizvērtu"]:
        choice = input(">>> ").lower()
        if choice == "ņem":
            inventory.append("nazis")
            print("Tu paņēmi nazi.")
        print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
        action = input(">>> ").lower()
        if action == "cīnīties":
            if "nazis" in inventory:
                print("Tu uzvarēji spoku ar nazi! Tu atgriezies foajē.")
                foyer()
            else:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                end_game()
        elif action == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        else:
            print("Nepareiza izvēle.")

def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vai tu vēlies 'skatīties' spogulī vai iet 'atpakaļ'?")
    choice = ""
    while choice not in ["skatīties", "atpakaļ"]:
        choice = input(">>> ").lower()
        if choice == "skatīties":
            print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
            end_game()
        elif choice == "atpakaļ":
            foyer()
        else:
            print("Nepareiza izvēle.")

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga, tu varētu tās 'atvērt'.")
    choice = ""
    while choice != "atvērt":
        choice = input(">>> ").lower()
        if choice == "atvērt":
            if "atslēga" in inventory:
                print("Tu atvēri durvis un izbēgi no spoku mājas! Tu uzvari!")
                end_game()
            else:
                print("Durvis ir aizslēgtas. Tev nepieciešama atslēga.")
        else:
            print("Nepareiza izvēle.")
            foyer()

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
print("Sveicināts Piedzīvojums Spoku Mājā!")
start_game()
