import random

sauna_flavors = [
    "After Eight",
    "Akazienblüte",
    "Alpenkräuter",
    "Ananas",
    "Ananaseis",
    "Anis",
    "Apfelblüte",
    "Apfel-Zimt",
    "Bambus",
    "Banane",
    "Basilikum",
    "Bergamotte",
    "Bergkiefer",
    "Birke",
    "Blutorange",
    "Bounty",
    "Bratapfel",
    "Cassis",
    "Eislimone",
    "Eisminze",
    "Englische Rose",
    "Erdbeere",
    "Eukalyptus"
    "Fenchel",
    "Fichte",
    "Fichtennadel",
    "Firnminze",
    "Flieder",
    "Grapefruit",
    "grüne Limone",
    "Grüner Apfel",
    "Grüner Tee",
    "Heu",
    "Heublume",
    "Himbeere",
    "Honig",
    "Honigmelone",
    "Ingwer",
    "Japanische Minze",
    "Jasminblüten",
    "Kaffee",
    "Kamille",
    "Kardamom",
    "Kirsche",
    "Kirschminze",
    "Kiwi",
    "Knoblauchhonig",
    "Kokos",
    "Latschenkiefer",
    "Lavendel",
    "Lebkuchen",
    "Lemon",
    "Lemongras",
    "Limone",
    "Lindenblüte",
    "Mairose",
    "Mandarine",
    "Mandelblüte",
    "Mango",
    "Maracuja",
    "Melisse",
    "Melone",
    "Menthol",
    "Minzbeere",
    "Minze",
    "Minzpfeffer",
    "Mokka",
    "Muskatellersalbei",
    "Nasaba",
    "Nelke",
    "Nordlandbirke",
    "Orange",
    "Orangeneis",
    "Orchidee",
    "Palmarosa",
    "Papaya",
    "Patchouli",
    "Pfeffer",
    "Pfefferkuchen",
    "Pfefferminz",
    "Pfirsich",
    "Pflaume",
    "Pina colada",
    "Rhabarber",
    "Ringelblume",
    "Rose",
    "Rosenholz",
    "Rosmarin",
    "Roter Apfel",
    "Salbei",
    "Sanddorn",
    "Sandelholz"
    "Schokolade",
    "Schwarze Johannisbeere",
    "Slibowitz",
    "Sommerbirke",
    "Sweet Apple",
    "Tanne",
    "Teebaumöl",
    "Thymian",
    "Tigerminze",
    "Vanille",
    "Wacholder",
    "Wacholderbeere",
    "Waldkiefer",
    "Weisstanne",
    "Weißtanne",
    "Wildkirsche",
    "Zedernholz",
    "Zimt",
    "Zitrone",
    "Zitronengras",
    "Zitronenmyrte"
]

sauna_flavors_mixed = [
    "Advent",
    "Batida Kirsch",
    "Eisfrische",
    "Erotic",
    "Finnischer Winter",
    "Fruchtcocktail",
    "Frühlingszauber",
    "Japanische Heilkräuter",
    "Kaminfeuer",
    "Maharadscha",
    "Nordlicht",
    "Obstgarten",
    "Oriental",
    "Paradies",
    "Polar",
    "Rosengarten",
    "Russische Banja",
    "Saunagold",
    "Sibirischer Wind",
    "Sommerwiese",
    "Sonnenaufgang",
    "Steppenwind",
    "Tango",
    "Tropic",
    "Tundra",
    "Tutti Frutti",
    "Vier Jahreszeiten",
    "Waldfrüchte"
]

# messages_aufguss_pre = [
#     ['<m> lässt einen Moment die Tür offen und wedelt frische Luft in die Sauna..',
#      'Letzte Gelegenheit Leute, wer raus will geht jetzt. Gleich gehts hier zur Sache!']
# ]

# messages_aufguss = [
    

# ]

def saunaboyAufguss(client):
    mixed_prob = 0.1
    rand = random.random()

    if(rand < mixed_prob):
        message = ''.join([
            ' macht einen Aufguss "',
             random.choice(sauna_flavors_mixed),
            '" ...'])
        client.message('\x01ACTION'+message+'\x01')
    else:
        flavors = random.sample(sauna_flavors, 2)
        message = ''.join([
            ' macht einen ',
            flavors[0], '-', flavors[1],
            ' Aufguss ...'])
        client.message('\x01ACTION'+message+'\x01')
        
