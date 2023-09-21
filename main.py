import random
import funcs
import player

#Main flow
def play():
    #Events that only need to happen once
    print("\nWelcome to the Slap Box World Championships! It's time to meet our combatants:")

    #Experimenting...
    #It worked!
    player_1 = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age())
    print(f"\n{player_1}\n")

    #Experimenting
    #It worked!
    player_2 = player.Player(player.set_player_name(), player.set_player_location(), player.set_player_age())
    print(f"\n{player_2}\n")

    fight_counter = 0 

    #Events that're looped to model actual gameplay
    while ((player_1.int_hp_status_check() > 0) and (player_2.int_hp_status_check() > 0)):

        print(f"{player_1.str_player_name}'s health bar: {player_1.int_hp_status_check()}")
        print(f"{player_2.str_player_name}'s health bar: {player_2.int_hp_status_check()}")

        dice_roll_result = funcs.dice_roll()

        if ((dice_roll_result % 2) == 0):
            print(f"{player_2.str_player_name} is on attack!")
            print(f"{player_1.str_player_name} is on defence!")
            funcs.pvp(player_2, player_1, fight_counter)
        else:
            print(f"{player_1.str_player_name} is on attack!")
            print(f"{player_2.str_player_name} is on defence!")
            funcs.pvp(player_1, player_2, fight_counter)
        
        fight_counter += 1 
    
    #Once again, perform actions which do not require looping
    print("\nAnd the winner is...\n")
    slap_box_winner = funcs.calc_winner(player_1, player_2)
    print(f"{slap_box_winner[0].str_player_name} from {slap_box_winner[0].str_player_location}! CONGRATULATIONS!")
    

play()


