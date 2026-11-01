import random

base_hp = 20
base_at = 2
base_df = 3
pot_at = 0
pot_df = 0
pot_hp = 0
lvl = 1

dung_diff = 1
dung_len_var = 0

combat = 1
new_enemy = 2
idle = 3
rebirth = 4
death = 0
dmg = 0
game_state = new_enemy

class Player():
    def __init__(self):
        self.hp = base_hp 
        self.at = base_at
        self.df = base_df
        self.lvl = lvl
        print(f'player max hp {self.hp}, atk {self.at}, def {self.df}')

    def hit(self,dmg):
        self.hp -= dmg

    def lvlup(self):
        self.lvl += 1
        self.hp += random.randint(1,8 + pot_hp)
        self.at += random.randint(1,2 + pot_at)
        self.df += random.randint(1,2 + pot_df)

player = Player()

class Dungeon():
    def __init__(self,dung_diff):
        self.diff = dung_diff
        self.hp = 1 + self.diff * 4
        self.df = 1 + round(self.diff * 0.5)
        self.at = 1 + round(self.diff * 0.5)
        self.scale = 1 + (self.diff/100)
        self.len = self.diff * 10

dung = Dungeon(dung_diff)

class Enemy():
    def __init__(self):
        self.hp = random.randint(dung.hp + round(dung_len_var ** dung.scale), (dung.hp + round(dung_len_var ** dung.scale)) + (dung.diff * 2 * player.lvl))
        self.at = random.randint(dung.hp + round(dung_len_var ** dung.scale), (dung.hp + round(dung_len_var ** dung.scale)) + (dung.diff * player.lvl))
        self.df = random.randint(dung.hp + round(dung_len_var ** dung.scale), (dung.hp + round(dung_len_var ** dung.scale)) + (dung.diff * player.lvl))

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
        if player.hp > 0 and enemy.hp > 0:
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
        if dung_len_var != dung.len:
            game_state = combat
        else:
            game_state = idle
            dung_len_var = 0
            continue
        enemy = Enemy()
        print('')
        print(f'new enemy appears, max hp {enemy.hp}, atk {enemy.at}, def {enemy.df}')
        dung_len_var += 1

    elif game_state == death:
        dung_len_var = 0
        print(f'died at level {player.lvl}')
        game_state = rebirth

    elif game_state == rebirth:
        points = player.lvl
        player.lvl = 0
        print('')
        print(f'choose your upgrades, availible points: {points}')
        print('0 - exit')
        print('1 - upgrade starting hp (+5): 1p')
        print('2 - upgrade starting at (+1): 1p')
        print('3 - upgrade starting df (+1): 1p')
        print('4 - upgrade hp gain potential (+2): 2p')
        print('5 - upgrade at gain potential (+1): 2p')
        print('6 - upgrade df gain potential (+1): 2p')
        upgrading = 1
        while upgrading == 1:
            choice = int(input())
            match choice:
                case 0:
                    upgrading = 0
                    print('end')
                case 1:
                    if points >= 1:
                        points -= 1
                        base_hp += 5
                        print('upgraded')
                    else:
                        print('insufficient funds')
                case 2:
                    if points >= 1:
                        points -= 1
                        base_at += 1
                        print('upgraded')
                    else:
                        print('insufficient funds')
                case 3:
                    if points >= 1:
                        points -= 1
                        base_df += 1
                        print('upgraded')
                    else:
                        print('insufficient funds')
                case 4:
                    if points >= 2:
                        points -= 2
                        pot_hp += 2
                        print('upgraded')
                    else:
                        print('insufficient funds')
                case 5:
                    if points >= 2:
                        points -= 1
                        pot_at += 1
                        print('upgraded')
                    else:
                        print('insufficient funds')
                case 6:
                    if points >= 2:
                        points -= 1
                        pot_df += 1
                        print('upgraded')
                    else:
                        print('insufficient funds')               

        player = Player()
        game_state = new_enemy

    elif game_state == idle:
        print('you made it out of the dungeon')
        game_state = 10



