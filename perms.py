import json
import general


def get(memb):
    with open(general.settings) as f:
        settings = json.load(f)
        f.close()

    lvl1 = settings["perms"]["lvl1"]
    lvl2 = settings["perms"]["lvl2"]
    lvl3 = settings["perms"]["lvl3"]
    lvl = [0]
    for r in memb.roles:
        if r.name in lvl3:
            lvl.append(3)
        elif r.name in lvl2:
            lvl.append(2)
        elif r.name in lvl1:
            lvl.append(1)

    return max(lvl)


def check(memb, lvl):
    return get(memb) >= lvl
