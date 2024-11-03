import random


# Klase Spēlētājs
class Player:
    def __init__(self) -> None:
        # Iniciē spēlētāja inventāru, stāvokli (vai dzīvs) un pašreizējo telpu
        self.inventory = []
        self.isAlive = True
        self.current_room = None
    
    def show_inventory(self):
        # Izvada inventāru vai paziņo, ja inventārs ir tukšs
        if not self.inventory:
            print("Tavā inventārā nekā nav.")
        else:
            print(*self.inventory, sep=", ", end=".") # sep - atdalītājs, kā tiek atdalīti elementi

    def show_map(self, dictionary, prefix="", is_root=True): # P.S. Šo funkciju labāk pat nevērt vaļā, tā tika uzrakstīta ar ChatGPT palīdzību — galvenais, ka tā darbojas :)
        # Rekursīva funkcija, lai attēlotu telpu karti ar telpu hierarhiju
        keys = list(dictionary.keys()) # Iegūstam visus vārdnīcas atslēgas kā sarakstu, lai varētu iterēt caur tām ar indeksiem
        for i, key in enumerate(keys): # Iterējam caur katru atslēgu sarakstā ar tās indeksu, lai piekļūtu atslēgas secības numuram
            is_last = (i == len(keys) - 1) #  # Pārbaudām, vai pašreizējais elements ir pēdējais sarakstā
            if is_root:
                # Pievienojam tekstu "← [Tu esi šeit]", ja atslēga atbilst spēlētāja pašreizējai telpai (norāda uz spēlētāja atrašanās vietu kartē).
                root_label = " ┐ ← [Tu esi šeit]" if key == self.current_room else " ┐"
                print(key + root_label)  
                new_prefix = "      "  # Pievieno atkāpi, ja telpa ir saknes līmenī
            else:
                # Nosaka, vai telpa ir pašreizējā telpa un pievieno norādi, ja nepieciešams
                room_name = key + " ← [Tu esi šeit]" if key == self.current_room else key
                # Pievienojam tekstu "← [Tu esi šeit]", ja atslēga atbilst spēlētāja pašreizējai telpai, lai norādītu, kur spēlētājs pašlaik atrodas.
                # Ja telpa nav pašreizējā, atstāj tikai telpas nosaukumu.
                connector = "└─ " if is_last else "├─ "
                print(prefix + connector + room_name) # Izdrukā iepriekšējo līmeņu atkāpi (prefix), savienojuma simbolu un pašreizējās telpas nosaukumu ar iespējamo norādi.
                new_prefix = prefix + ("    " if is_last else "│   ")
                # Atjaunina atkāpi nākamajam līmenim: ja elements ir pēdējais, pievieno tukšu atkāpi,
                # citādi pievieno vertikālo līniju "│", lai norādītu uz turpmākiem elementiem šajā līmenī.
            # Rekursīvi izsauc funkciju show_map katram bērna elementam (apakštelpai)
            self.show_map(dictionary[key], new_prefix, is_root=False)


# Klase Spoks
class Ghost:
    def __init__(self) -> None:
        # Iniciē spoka stāvokli un priekšmetus, kurus viņš var nest
        self.isAlive = True
        self.spawn_chance = 0
        self.current_room = None
        self.inventory = ["key"]

    def ghost_event_spawn_attempt(self) -> bool:
        # Funkcija pārbauda, vai spoks parādīsies, izmantojot izlases iespējamību
        if not self.isAlive: # Ja spoks ir miris, tas neparādās
            return
        if random.random() < self.spawn_chance: # Ja tiek izpildīti nosacījumi, atiestata iespējamību uz 0 un izsauc funkciju ghost_event()
            self.spawn_chance = 0 
            self.ghost_event()
        else:
            # Palielina iespēju parādīties nākamajā reizē
            self.spawn_chance += 0.2 

    def ghost_event(self):
        # Funkcija definē mijiedarbību ar spēlētāju, kad parādās spoks
        print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
        user_choice = Game.get_user_choice(["cīnīties", "bēgt"])
        if user_choice == "cīnīties":
            if "knife" not in PLAYER.inventory:
                print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                game.end_game()
            print("Kad spoks ierauga nazi, tas sāk baidīties un piedāvā atslēgu apmaiņā pret mieru. Vai pieņemt piedāvājumu? 'Jā' 'Nē'")
            user_choice = Game.get_user_choice(["jā", "nē"])
            if user_choice == "jā":
                print("Spoks izmantoja mirkli un nogalināja jūs.")
                game.end_game()
            else:
                print("Tu nogalināji spoku un paņēmi no viņa pagraba atslēgu.")
                GHOST.isAlive = False
                GHOST.inventory.remove("key")
                PLAYER.inventory.append("key")
        elif user_choice == "bēgt":
            # Spēlētājs pārvietojas uz nejauši izvēlētu telpu
            random_room = ROOMS.get_random_room()
            random_room.enter()


# Klases dažādām telpām
class Entrance:
    def enter(self):
        # Apraksta ieejas telpas notikumus un spēlētāja izvēles iespējas
        PLAYER.current_room = "Ieeja"
        print("Tu atrodies spoku mājas ieejā, kur nolādētais spogulis pārvērš cilvēkus par spokiem. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
        user_choice = Game.get_user_choice(["iekšā", "prom"])
        if user_choice == "iekšā":
            ROOMS.foyer.enter()
        elif user_choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            game.end_game()


class Foyer:
    def enter(self):
        # Apraksta foajē telpas notikumus un spēlētāja izvēles iespējas
        PLAYER.current_room = "Foaje"
        print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuvi' un 'dzīvojamo istabu'.")
        user_choice = Game.get_user_choice(["virtuvi", "dzīvojamo istabu"])
        if user_choice == "virtuvi":
            ROOMS.kitchen.enter()
        elif user_choice == "dzīvojamo istabu":
            ROOMS.living_room.enter()


class Kitchen:
    def __init__(self) -> None:
        # Iniciē virtuves priekšmetus
        self.items = ["knife"]

    def enter(self):
        # Apraksta virtuves notikumus un spēlētāja izvēles iespējas
        PLAYER.current_room = "Virtuve"
        if "knife" in self.items:
            print("Tu esi virtuvē un atrod rūsinātu nazi. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
            user_choice = Game.get_user_choice(["ņem", "aizvērtu"])
            if user_choice == "ņem":
                self.items.remove("knife")
                PLAYER.inventory.append("knife")
                print("Jūs paņēmāt nazi, varbūt tagad jūs varat uzvarēt spoku?")
        print("Tu virtuvē neko citu neatrodi un dodies atpakaļ uz foajē")
        ROOMS.foyer.enter()


class Living_Room:
    def enter(self):
        global PLAYER
        # Apraksta dzīvojamās istabas notikumus un spēlētāja izvēles iespējas
        PLAYER.current_room = "Dzīvojama istaba"
        print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis un durvis uz pagrabu, tās ir aizslēgtas, ja tev būtu atslēga, tu varētu tās 'atvērt'. Vai tu vēlies 'skatīties' spogulī, vai iet 'atpakaļ'")
        user_choice = Game.get_user_choice(["skatīties", "atpakaļ", "atvērt"])
        if user_choice == "skatīties":
            print("Spogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.")
            game.end_game()
        elif user_choice == "atpakaļ":
            ROOMS.foyer.enter()
        elif user_choice == "atvērt":
            if not "key" in PLAYER.inventory:
                print("Tev nav atslega, tu dodies atpakaļ uz foajē")
                ROOMS.foyer.enter()
            ROOMS.basement.enter()


class Basement:
    def enter(self):
        # Pagraba telpa bez papildus notikumiem
        PLAYER.current_room = "Pagrabs"
        print("Nokāpjot pagrabā, spēlētājs redz uz grīdas izbalējušas pentagrammas un senus simbolus, kas veido draudīgu ainu. "
      "Istabas centrā paceļas masīvs altāris, un aiz tā stāv sens sarkofāgs, no kura plūst draudīga gaisma. "
      "Spēlētājs saprot, ka spogulis augšstāvā bija radīts, lai ievilinātu dvēseles mājā un savāktu tās rituālam, "
      "lai atdzīvinātu senu būtni, kas ieslēgta sarkofāgā.\n"
      "Spēlētājam ir izvēle: 'palikt' un mēģināt izzināt šo noslēpumu vai izmantot atslēgu un 'aizbēgt' no mājas.")
        user_choice =  Game.get_user_choice(["palikt", "aizbēgt"])
        if user_choice == "aizbēgt":
            print("Tu atvēri durvis un izbēgi no spoku mājas! Tu uzvari!")
            game.end_game()
        elif user_choice == "palikt":
            print("Tu nolemj palikt un pietuvoties, taču pēkšņi pagrabu piepilda ledains aukstums. Viņa priekšā parādās spoks, "
      "rokās turot to pašu spoguli, kas pārvērš cilvēkus par spokiem. Spoks tuvojas, un tu, it kā apburts, nespēj novērst skatienu. "
      "Ļaunais balss liek viņam ieskatīties spogulī. Viņš mēģina pretoties, taču spēki viņu pamet, un, ieskatoties spogulī, "
      "viņš sajūt, kā dvēsele izslīd no viņa ķermeņa. Tagad viņš ir lemts mūžīgi klīst pa šo māju kā viens no tās spoku sargiem.")
            game.end_game()


class Rooms:
    def __init__(self) -> None:
        # Inicializē telpas un kartes struktūru
        self.entrance = Entrance()
        self.foyer = Foyer()
        self.kitchen = Kitchen()
        self.living_room = Living_Room()
        self.basement = Basement()
        self.map_dictionary = {
        "Ieeja": {"Foaje": {"Virtuve":{}, "Dzīvojama istaba":{}}},
        "Pagrabs": {}
        }

    def get_all_rooms(self, dictionary: dict, all_rooms = None) -> list:
        # Rekursīva funkcija, lai iegūtu visu pieejamo telpu sarakstu
        if all_rooms is None:  # Izvairās no dublēšanās starp izsaukumiem
            all_rooms = []
        for key, value in dictionary.items():
            all_rooms.append(key)
            if isinstance(value, dict):
                self.get_all_rooms(value, all_rooms)
        return all_rooms

    def get_random_room(self):
        # Izvēlas nejaušu telpu, izņemot "Ieeja" un "Pagrabs"
        all_rooms = self.get_all_rooms(self.map_dictionary)
        all_rooms.remove("Ieeja")
        all_rooms.remove("Pagrabs")
        if PLAYER.current_room in all_rooms:
            all_rooms.remove(PLAYER.current_room)
        random_room = random.choice(all_rooms)
        match random_room:
            case "Foaje":
                return self.foyer
            case "Virtuve":
                return self.kitchen
            case "Dzīvojama istaba":
                return self.living_room
            case _:
                print(random_room)


# Klase Spēle
class Game:
    def __init__(self) -> None:
        # Izveido spēlētāju un telpas
        global PLAYER
        global GHOST
        global ROOMS
        PLAYER = Player()
        GHOST = Ghost()
        ROOMS = Rooms()

    def start_game(self):
        # Sāk spēli, ielaižot spēlētāju ieejas telpā
        ROOMS.entrance.enter()

    def end_game(self):
        # Beidz spēli un izvada pateicības ziņojumu
        global PLAYER
        PLAYER.isAlive = False
        print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")
        exit()
    
    def get_user_choice(answer_options:list):
        # Apstrādā lietotāja izvēli, ļaujot apskatīt inventāru vai karti, ja tā vēlas
        user_choice = None
        while user_choice not in answer_options:
            if user_choice not in [None, "inventars", "inventory", "map", "karte"]: print("Nepareiza izvēle. Mēģini vēlreiz.")
            user_choice = input(">> ").lower()
            if user_choice in ["inventars", "inventory"]: PLAYER.show_inventory()
            if user_choice in ["map", "karte"]: (PLAYER.show_map(ROOMS.map_dictionary))
        if user_choice not in ["prom", "jā", "nē", "skatīties", "ņem"]:
            GHOST.ghost_event_spawn_attempt()
        return user_choice


# Sākums - palaiž spēli
if __name__ == "__main__":
    game = Game()
    game.start_game()
