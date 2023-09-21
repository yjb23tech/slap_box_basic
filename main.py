import random

class Player:

    def __init__(self, str_player_name, str_player_location, int_player_age):

        self.str_player_name = str_player_name
        self.str_player_location = str_player_location
        self.int_player_age = int_player_age

    def __str__(self):
        return (f"Bio: Name ==> {self.str_player_name} Location ==> {self.str_player_location} Age ==> {self.int_player_age}")

#Meta methods
def set_player_name():
    return input("\nWhat is your name Warrior?\n")

def set_player_location():
    return input("\nWhere are you from Warrior?\n")

def set_player_age():
    return int(input("\nAnd how old are you Warrior?\n"))

#Main flow
def play():
    #Events that only need to happen once
    print("\nWelcome to the Slap Box World Championships! It's time to meet our combatants:")

    player_1 = Player(set_player_name(), set_player_location(), set_player_age())
    print(f"\n{player_1}\n")

    player_2 = Player(set_player_name(), set_player_location(), set_player_age())
    print(f"\n{player_2}\n")

    fight_counter = 0 

    #Events that're looped to model actual gameplay
    while (fight_counter < 10):
        print(f"Round {fight_counter + 1}: FIGHT!")
        fight_counter += 1
    print("\nAnd the winner is...\n")

play()


