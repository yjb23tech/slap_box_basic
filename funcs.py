#print("Gunna Gunna Gunna")
import random

def dice_roll():

    dice_roll_outcome = random.randint(1,6)
    return dice_roll_outcome

def pvp(player_x, player_y, round_counter):

    #Declare the power of the attacking player; declare the power of the defending player
    print(f"Round {round_counter + 1}: FIGHT!")
    print(f"{player_x.str_player_name} has an attack power of {player_x.int_launch_atk()}")
    print(f"{player_y.str_player_name} has a defensive power of {player_y.int_launch_def()}\n")

    if (player_x.int_player_atk_pwr > player_y.int_player_def_pwr):
        print("Atk wins\n")
        int_hp_damage = player_x.int_player_atk_pwr - player_y.int_player_def_pwr
        print(f"The resulting damage from {player_x.str_player_name} is {int_hp_damage}")
        print(f"{player_y.str_player_name} loses -{int_hp_damage} worth of hp")
        player_y.int_player_hp = player_y.int_player_hp - int_hp_damage
    elif (player_x.int_player_atk_pwr < player_y.int_player_def_pwr):
        print("Def wins\n")
        int_hp_damage = player_y.int_player_def_pwr - player_x.int_player_atk_pwr 
        print(f"Through sheer force of will {player_y.str_player_name} has defended and reversed the attack!")
        print(f"{player_x.str_player_name} has been rebuffed and suffers damage of {int_hp_damage}")
        print(f"{player_x.str_player_name} loses - {int_hp_damage} worth of hp")
        player_x.int_player_hp = player_x.int_player_hp - int_hp_damage
    elif (player_x.int_player_atk_pwr == player_y.int_player_def_pwr):
        print("Tie Tie Tie\n")
    else:
        print("Should never be triggered")
    
    print(f"This is the current standing at the end of Round {round_counter + 1}:")
    print(f"{player_x.str_player_name} has a health bar of {player_x.int_player_hp}")
    print(f"{player_y.str_player_name} has a health bar of {player_y.int_player_hp}\n\n")




