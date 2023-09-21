import random

class Player:

    def __init__(self, str_player_name, str_player_location, int_player_age):
        self.str_player_name = str_player_name
        self.str_player_location = str_player_location
        self.int_player_age = int_player_age

    def __str__(self):
        return (f"Please welcome to the stage {self.str_player_name} from {self.str_player_location}")

test_player = Player("Yinka Banjo", "London", 29)

print("Hello New World")
print(test_player)

