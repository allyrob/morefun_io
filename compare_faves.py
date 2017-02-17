with open ("Sonia_fav_foods.txt") as sonia_foods:
    sonia_list = sonia_foods.readlines()
    sonia_faves = []
    for item in sonia_list:
        item = item.strip()
        sonia_faves.append(item)

with open ("Ally_fav_foods.txt") as ally_foods:
    ally_list = ally_foods.readlines()
    ally_faves = []
    for item in ally_list:
        item = item.strip()
        ally_faves.append(item)

def compare_faves(sonia_faves, ally_faves):
    if sonia_faves == ally_faves:
        print "Our favorite foods are the same!"
    elif sonia_faves != ally_faves:
        print "Our favorite foods are different!"

compare_faves(sonia_faves, ally_faves)
