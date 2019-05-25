from BASE.User import User


from BASE.ProPlayerFinder import *

# get initial summoner & champion name
sn = "bob"
cn = "Ahri"
current_user = User(sn, cn)


cid = current_user.get_champion_id()
print(cid)
"""get_mastery(current_user.get_summoner_id(),
            current_user.get_champion_id())
"""

#find_pro_player()

