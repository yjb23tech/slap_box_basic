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
test_player = Player(set_player_name(), set_player_location(), set_player_age())

print("\nHello New World\n")
print(test_player)

