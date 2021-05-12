items = {
    "ana": "Doomfist, D.Va, Genji, Tracer, Winston, Widowmaker",
    "ashe": "Doomfist, D.Va, Genji, Hanzo, Reinhardt, Widowmaker, Wrecking Ball",
    "baptiste": "Ana, Ashe, Bastion, Doomfist, Hanzo, Mei, Orisa, Roadhog, Soldier: 76, Sombra, Widowmaker, Winston, Wrecking Ball",
    "bastion": "Ana, Ashe, D.Va, Genji, Hanzo, Junkrat, Pharah, Roadhog, Soldier: 76, Tracer, Widowmaker, Zenyatta",
    "brigitte": "Junkrat, Pharah, Reaper, Sombra, Torbjorn, Widowmaker",
    "d.va": "Baptiste, Brigitte, Doomfist, Junkrat, Mei, Reaper, Roadhog, Sombra, Zarya, Zenyatta",
    "doomfist": "McCree, Orisa, Pharah, Reaper, Sombra",
    "echo": "-",
    "genji": "Brigitte, Doomfist, Mei, Moira, Pharah, Roadhog, Winston, Zarya",
    "junkrat": "Baptiste, Genji, Pharah, Widowmaker, Zarya",
    "lucio": "Ana, McCree, Pharah, Roadhog, Sombra, Winston",
    "mccree": "D.Va, Roadhog, Widowmaker, Winston",
    "mei": "Orisa, Pharah, Widowmaker, Zarya",
    "mercy": "Ashe, D.Va, Genji, McCree, Mei, Reaper, Roadhog, Soldier: 76, Sombra, Widowmaker, Tracer, Winston",
    "moira": "Ana, Baptiste, D.Va, McCree",
    "orisa": "Genji, Hanzo, Moira, Junkrat, Reaper, Symmetra, Tracer",
    "pharah": "Ana, Ashe, D.Va, McCree, Soldier: 76, Widowmaker, Zenyatta",
    "reaper": "Ashe, Hanzo, Junkrat, Pharah, McCree, Widowmaker",
    "reinhardt": "Bastion, Doomfist, Junkrat, Mei, Moira, Pharah, Reaper, Sombra, Symmetra, Torbjorn",
    "roadhog": "Ana, Mei, Reaper, Zarya, Zenyatta",
    "sigma": "D.Va, Doomfist, Mei, Reaper, Roadhog, Sombra, Symmetra, Winston, Wrecking Ball, Zarya",
    "soldier: 76": "Orisa, Reinhardt, Roadhog, Widowmaker",
    "sombra": "Hanzo, Junkrat, McCree, Mei, Reaper, Roadhog, Winston",
    "symmetra": "McCree, Pharah, Sombra, Widowmaker, Winston",
    "torbjörn": "Ana, Ashe, Baptiste, D.Va, Genji, Hanzo, Junkrat, Orisa, Pharah, Reaper, Roadhog, Soldier: 76, Widowmaker, Zarya",
    "tracer": "Brigitte, Junkrat, Sombra, Torbjorn, Winston",
    "widowmaker": "D.Va, Genji, Orisa, Reinhardt, Winston, Wrecking Ball",
    "winston": "Bastion, D.Va, Reaper, Roadhog, Torbjorn",
    "wrecking Ball": "Ana, Bastion, Brigitte, Mei, Reaper, Roadhog, Sombra, Torbjorn",
    "zarya": "Baptiste, Bastion, Pharah, Reaper, Zenyatta",
    "zenyatta": "Ana, Doomfist, Genji, McCree, Mei, Reaper, Sombra, Tracer, Widowmaker",
    "hanzo": "D.Va, Genji, Tracer, Reinhardt, Widowmaker, Winston"
}


def counterselector(hero):
    return items.get(hero, "False")
