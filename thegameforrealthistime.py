import random

base_hp = 20
base_at = 2
base_df = 3
lvl = 1

dung_hp = 5
dung_at = 1
dung_df = 1
dung_diff = 1
dung_scale = 1.1
dung_len = 30
dung_len_var = 0

game_state = 2
combat = 1
new_enemy = 2
idle = 3
death = 0
dmg = 0

class Player():
    def __init__(self):
        self.hp = base_hp
        self.at = base_at
        self.df = base_df
        self.lvl = lvl

    def hit(self,dmg):
        self.hp -= dmg

    def lvlup(self):
        self.lvl += 1
        self.hp += random.randint(1,8)
        self.at += random.randint(1,2)
        self.df += random.randint(1,2)

player = Player()

class Dungeon():
    def __init__(self):
        self.diff = dung_diff
        self.hp = 1 + dung_diff * 2

class Enemy():
    def __init__(self):
        self.hp = random.randint(dung_hp + round(dung_len_var ** dung_scale), (dung_hp + round(dung_len_var ** dung_scale)) + (dung_diff * 2 * player.lvl))
        self.at = random.randint(dung_hp + round(dung_len_var ** dung_scale), (dung_hp + round(dung_len_var ** dung_scale)) + (dung_diff * player.lvl))
        self.df = random.randint(dung_hp + round(dung_len_var ** dung_scale), (dung_hp + round(dung_len_var ** dung_scale)) + (dung_diff * player.lvl))

    def hit(self,dmg):
        self.hp -= dmg



def dmg_calc(attacker, defender, dmg):
    dmg = 0
    avar = attacker + random.randint(1,6)
    dvar = defender + random.randint(1,6)
    if avar <= dvar:
        dodge = random.randint(0,dvar-avar)
        if dodge != 0:
            dmg = 0
        else:
            dmg = avar
    else:
        dmg = avar
    return dmg



while True:
    if game_state == combat:
        if player.hp >= 0 and enemy.hp >= 0:
            dmg = dmg_calc(player.at, enemy.df, dmg)
            enemy.hit(dmg)
            print(f'enemy hit for {dmg}, total hp is {enemy.hp}')
            dmg = dmg_calc(enemy.at, player.df, dmg)
            player.hit(dmg)
            print(f'player hit for {dmg}, total hp is {player.hp}')
        elif player.hp < 0:
            game_state = death
        else:
            print(f'enemy defeated, new level is {player.lvl}')
            player.lvlup()
            print(f'atk = {player.at}, def = {player.df}, hp = {player.hp}')
            game_state = new_enemy

    elif game_state == new_enemy:
        if dung_len_var != dung_len:
            game_state = combat
        else:
            game_state = idle
            dung_len_var = 0
            continue
        enemy = Enemy()
        print(f'new enemy appears, max hp {enemy.hp}, atk {enemy.at}, def {enemy.df}')
        dung_len_var += 1

    elif game_state == death:
        print(f'died at level {player.lvl}')
        game_state = 10

    elif game_state == idle:
        print('you made it out of the dungeon')
        game_state = 10



