import random

base_hp = 20
base_at = 2
base_df = 3
base_sp = 1
base_cru_at = 0
base_abs_df = 0
pot_at = 0
pot_df = 0
pot_hp = 0
lvl = 0

dung_diff = 1
dung_len_var = 0

points = 0

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
        self.sp = base_sp
        self.cru = base_cru_at
        self.abs = base_abs_df
        print(f'player max hp {self.hp}, atk {self.at}, def {self.df}, speed {self.sp}, crushing {self.cru}, absorption {self.abs}')

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
        self.len = round(self.diff * 10 * self.scale)

dung = Dungeon(dung_diff)

class Enemy():
    def __init__(self):
        self.hp = random.randint(dung.hp + round(dung_len_var ** dung.scale), (dung.hp + round(dung_len_var ** dung.scale)) + (dung.diff * 4 * player.lvl))
        self.at = random.randint(dung.hp + round(dung_len_var ** dung.scale), (dung.hp + round(dung_len_var ** dung.scale)) + (dung.diff * player.lvl))
        self.df = random.randint(dung.hp + round(dung_len_var ** dung.scale), (dung.hp + round(dung_len_var ** dung.scale)) + (dung.diff * player.lvl))
        self.sp = 1 + round(dung.diff/30)
        self.cru = 0
        self.abs = 0

    def hit(self,dmg):
        self.hp -= dmg

def dmg_calc(attacker, defender, att_cru, def_abs, dmg):
    dmg = 0
    avar = attacker + random.randint(1,6)
    dvar = defender + random.randint(1,6)
    if avar <= dvar:
        dodge = random.randint(0,dvar-avar)
        if dodge != 0:
            dmg = 0
        else:
            dmg = avar + att_cru - def_abs
    else:
        dmg = avar + att_cru - def_abs
    return dmg


while True:
    if game_state == combat:
        if player.hp > 0:
            for i in range(0,player.sp):
                if enemy.hp > 0:
                    dmg = dmg_calc(player.at, enemy.df, player.cru, enemy.abs, dmg)
                    enemy.hit(dmg)
                    print(f'enemy hit for {dmg}, total hp is {enemy.hp}')
        else:
            game_state = death
    if game_state == combat:
        if enemy.hp > 0:
            for i in range(0,enemy.sp):
                if player.hp > 0:
                    dmg = dmg_calc(enemy.at, player.df, enemy.cru, player.abs, dmg) 
                    player.hit(dmg)
                    print(f'player hit for {dmg}, total hp is {player.hp}')
        else:
            player.lvlup()
            print(f'enemy defeated, new level is {player.lvl}')
            print(f'atk = {player.at}, def = {player.df}, hp = {player.hp}, speed {player.sp}, crushing {player.cru}, absorption {player.abs}')
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
        print(f'new enemy appears ({dung_len_var}/{dung.len}), max hp {enemy.hp}, atk {enemy.at}, def {enemy.df}, speed {enemy.sp}, crushing {enemy.cru}, absorption {enemy.abs}')
        dung_len_var += 1

    elif game_state == death:
        dung_len_var = 0
        print(f'died at level {player.lvl}')
        game_state = rebirth

    elif game_state == rebirth:
        points += player.lvl
        player.lvl = 0
        print('')
        print('0 - exit')
        print('1 - upgrade starting hp (+5): 1p')
        print('2 - upgrade starting at (+1): 1p')
        print('3 - upgrade starting df (+1): 1p')
        print('4 - upgrade hp gain potential (+2): 2p')
        print('5 - upgrade at gain potential (+1): 2p')
        print('6 - upgrade df gain potential (+1): 2p')
        print('7 - upgrade crushing at (+1): 5p')
        print('8 - upgrade absorbing df (+1): 5p')
        print('9 - upgrade base speed - number of attacks (+1): 20p')
        print(f'choose your upgrades, availible points: {points}')
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
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 2:
                    if points >= 1:
                        points -= 1
                        base_at += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 3:
                    if points >= 1:
                        points -= 1
                        base_df += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 4:
                    if points >= 2:
                        points -= 2
                        pot_hp += 2
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 5:
                    if points >= 2:
                        points -= 2
                        pot_at += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 6:
                    if points >= 2:
                        points -= 2
                        pot_df += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 7:
                    if points >= 5:
                        points -= 5
                        base_cru_at += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 8:
                    if points >= 5:
                        points -= 5
                        base_abs_df += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')
                case 9:
                    if points >= 20:
                        points -= 20
                        base_sp += 1
                        print(f'upgraded, remaining points {points}')
                    else:
                        print('insufficient funds')               

        player = Player()
        game_state = new_enemy

    elif game_state == idle:
        print('you made it out of the dungeon')
        game_state = 10



