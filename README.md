# 28.10.2024
Piedzīvojums Spoku Mājā
Interaktīva teksta piedzīvojumu spēle, kur spēlētājs izpēta spoku māju, sastopoties ar dažādiem izaicinājumiem un pieņemot lēmumus. Šis projekts ir paredzēts kā uzdevums skolēniem, lai praktizētu while ciklus, if nosacījumus un debugošanas prasmes.

## 📋 Uzdevumi
# 1. Lejupielādē un palaid spēli
Lejupielādē šo projektu un palaid start_game() funkciju, lai iepazītos ar spēles gaitu un identificētu esošās kļūdas un nepilnības.
# 2. Atrisini Kļūdas
Kļūda spēles pārtraukšanā: Spēle turpina darboties pat tad, ja player_alive ir False. Pārliecinies, ka spēle beidzas pareizi, izmantojot end_game() funkciju.
Inventāra funkcionalitāte: Funkcijā basement() ir nepieciešama atslēga, bet spēlē pašlaik nav iespējas to iegūt. Pievieno iespēju spēlētājam atrast atslēgu kādā no istabām.
# 3. Papildini Spēli
Pievieno jaunu funkcionalitāti:
Ļauj spēlētājam jebkurā brīdī ierakstīt “inventārs”, lai apskatītu savus priekšmetus.
Pievieno vairākas istabas vai priekšmetus, kas papildinās spēles interesantumu.
Izveido nejaušu iespēju, ka spoks var parādīties dažādās istabās.
# 4. Izaicinājumi (Papildu punkti)
Karte: Pievieno kartes funkciju, kas parāda, kuras istabas ir pieejamas.
Laika limits: Pievieno laika limitu katrai izvēlei, lai spēle kļūtu intensīvāka.
Dažādi beigu scenāriji: Pievieno vairākus beigu scenārijus, pamatojoties uz spēlētāja savāktajiem priekšmetiem un pieņemtajiem lēmumiem.
## 🔧 Koda Struktūra
python
Copy code
def entrance():  # Spēles sākuma funkcija ar izvēlēm
def foyer():  # Foajē istaba ar izvēlēm
def kitchen():  # Virtuve, kur spēlētājs var atrast nazi
def living_room():  # Dzīvojamā istaba ar nolādētu spoguli
def basement():  # Pagrabs ar iespēju izbēgt, ja spēlētājam ir atslēga
def end_game():  # Spēles beigu funkcija
def start_game():  # Galvenā funkcija, kas sāk spēles while ciklu
## 📌 Kā Iesniegt
Debug un papildini kodu: Novērs visas kļūdas un pievieno jaunas funkcijas, kā norādīts uzdevumos.
Pievieno komentārus: Pievieno komentārus savam kodam, lai skaidrotu izdarītās izmaiņas un papildinājumus.
Augšupielādē repozitorijā: Pievieno savu pabeigto projektu savā GitHub kontā un nosūti saiti, lai iesniegtu uzdevumu.
## 📝 Piezīmes
Debugošana: Sekojiet līdzi, lai spēle pareizi pārtraucas, kad player_alive ir False.
Papildus uzdevumi: Šis projekts ir paredzēts ne tikai kļūdu labošanai, bet arī jaunu ideju un funkcionalitātes pievienošanai.
Veiksmi un radošu darbu pie piedzīvojumu spēles uzlabošanas!








### Vērtēšanas Kritēriji: GitHub Python Projekts
## 1. Koda Funkcionalitāte un Pārbaudāmība - 40 punkti
Pilnībā funkcionāls kods (bez kļūdām) - 40 punkti
Kļūdas:
Ja programmas izpildē ir kļūdas (piemēram, sintakses kļūdas vai kļūdas izpildes laikā) - -5 punkti par katru kļūdu
Ja kļūdas ir nenovērstas un liedz kodam darboties kā paredzēts - -10 punkti
Nepareizs rezultāts (programmas iznākums neatbilst prasībām) - -5 punkti par katru neatbilstību
## 2. Koda Lasāmība un Kvalitāte - 20 punkti
Lasāms un sakārtots kods ar komentāriem - 20 punkti
Kļūdas:
Ja kods ir bez komentāriem vai neprecizē sarežģītas vietas - -3 punkti par katru vietu
Ja mainīgo nosaukumi ir nesaprotami vai pārāk īsi (piemēram, x vietā, kur būtu nepieciešams aprakstošs nosaukums) - -3 punkti par katru mainīgo
Papildu punkti:
Ja kods satur sakarīgus, skaidrus komentārus - +5 punkti
## 3. Koda Optimālums un Efektivitāte - 15 punkti
Efektīvi uzrakstīts kods (izvairās no liekiem cikliem, nevajadzīgām darbībām) - 15 punkti
  Kļūdas:
    Ja kods satur nevajadzīgus ciklus vai dublētas darbības - -5 punkti par katru gadījumu
    Ja algoritmi nav optimāli (piemēram, lēni izpildās ar lielu datu apjomu) - -5 punkti
## 4. GitHub Lietošana un Versiju Kontrole - 15 punkti
Pareizi lietots GitHub ar regulāriem commit ziņojumiem - 15 punkti
Kļūdas:
Ja commit ziņojumi ir nesaprotami vai nesniedz informāciju par izmaiņām (piemēram, “Update” bez paskaidrojuma) - -2 punkti par katru neskaidro commit
Ja projekts ir augšupielādēts ar nepareizu vai nesakārtotu failu struktūru - -5 punkti
## 5. Papildu Funkcionalitāte un Radošums - 10 punkti
Papildu funkcijas vai radoši elementi - 10 punkti
Papildu punkti:
Par katru izcilu radošu risinājumu vai papildinājumu - +5 punkti līdz 10 maksimāli
Kļūdas:
Ja ir pievienotas funkcijas, bet tās nedarbojas pareizi vai rada kļūdas - -3 punkti par katru nepareizu papildinājumu
Kopējais Punktu Skaits: 100 punkti
Vērtēšanas Pamatojums: Katra kritērija punktu skaits tiek summēts, un kļūdas tiek atņemtas no kopējā vērtējuma.
