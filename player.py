import random 

class Player:

    def __init__(self, str_player_name, str_player_location, int_player_age):

        self.str_player_name = str_player_name
        self.str_player_location = str_player_location
        self.int_player_age = int_player_age

        self.int_player_hp = 100
        self.int_player_atk_pwr = 1
        self.int_player_def_pwr = 1

    def __str__(self):
        return (f"Warrior stats: Name - {self.str_player_name} Location - {self.str_player_location} Age - {self.int_player_age}")
    
    def int_launch_atk(self):
        self.int_player_atk_pwr = random.randint(1,20)
        return self.int_player_atk_pwr
    
    def int_launch_def(self):
        self.int_player_def_pwr = random.randint(1,20)
        return self.int_player_def_pwr
    
#Meta methods
def set_player_name():
    return input(f"\nWhat is your name Warrior?\n")

def set_player_location():
    return input(f"\nWhere are you from Warrior?\n")

def set_player_age():
    return int(input(f"\nAnd how old are you Warrior?\n"))

