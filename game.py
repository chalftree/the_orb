import random

enemy_health = 0
enemy_attack = 0
enemy_defense = 0
enemy_is = 0
enemy = [0, 0, 0, 0]
player_level = 1
player_attack = 2
player_defense = 4
player_health = 25
combat_return = [0,0,0,0,0,0,0,0,0,0]

while True:
    if enemy_is == 1:
        if player_health > 0 and enemy_health > 0:
            print('round begin')
            player_att_var = player_attack + random.randint(1,6)
            print('Player attack is: ' + str(player_att_var))
            enemy_def_var = enemy_defense + random.randint(1,6)
            print('Enemy defense is: ' + str(enemy_def_var))
            if player_att_var < enemy_def_var:
                dodge_var = random.randint(1,enemy_def_var)
                if dodge_var != 1:
                    print('Enemy dodged')
                else:
                    print('Enemy health is :' + str(enemy_health - player_att_var))
                    enemy_health = enemy_health - player_att_var
            else:
                print('Enemy health is :' + str(enemy_health - player_att_var))
                enemy_health = enemy_health - player_att_var

        if enemy_health <= 0:
            print('Victory')
            enemy_is = 0
            player_level += 1
            player_attack += random.randint(1,6)
            player_defense += random.randint(1,4)
            player_health += random.randint(player_level, player_level+5)
            print('New level: ' + str(player_level))
            print(player_attack, player_defense, player_health)
        
        if player_health > 0 and enemy_health > 0:
            player_def_var = player_defense + random.randint(1,6)
            print('Player defense is: '+ str(player_def_var))
            enemy_att_var = enemy_attack + random.randint(1,6)
            print('Enemy attack is: '+ str(enemy_att_var))
            if player_def_var > enemy_att_var:
                dodge_var = random.randint(1,player_def_var)
                if dodge_var != 1:
                    print('you dodged')
                else:
                    player_health = player_health - enemy_att_var
                    print('Player health is: '+ str(player_health))
            else:
                player_health = player_health - enemy_att_var
                print('Player health is: '+ str(player_health))

        if player_health <= 0:
            print('Game over')
            print('Score: ' + str(player_level))
            enemy_is = 2
        


    elif enemy_is == 0:
        enemy_health = random.randint(player_level, round(player_level * 10,456789))
        enemy_attack = random.randint(player_level, round(player_level * 4,6789))
        enemy_defense = random.randint(player_level, round(player_level * 4,6789))
        print('New enemy: ')
        print(enemy_attack, enemy_defense, enemy_health)
        enemy_is = 1





