#print("Gunna Gunna Gunna")

def pvp(player_x, player_y, round_counter):

    #Declare the power of the attacking player; declare the power of the defending player
    print(f"Round {round_counter + 1}: FIGHT!")
    print(f"{player_x.str_player_name} has an attack power of {player_x.int_launch_atk()}")
    print(f"{player_y.str_player_name} has a defensive power of {player_y.int_launch_def()}\n")

    if (player_x.int_player_atk_pwr > player_y.int_player_def_pwr):
        print("Atk wins\n")
    elif (player_x.int_player_atk_pwr < player_y.int_player_def_pwr):
        print("Def wins\n")
    elif (player_x.int_player_atk_pwr == player_y.int_player_def_pwr):
        print("Tie Tie Tie\n")
    else:
        print("Should never be triggered")



