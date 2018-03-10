from ship import Ship
from field import Field
import field_generation as fg


class Player:
    def __init__(self, name):
        self._name = name


class Game:
    def __init__(self, name1, name2):
        self.fields = [Field(), Field()]
        self.players = [Player(name1), Player(name2)]
        self.current_player = 0

    def print_fields(self, current_player):
        if current_player:
            print('YOUR FIELD')
            fg.fiels_to_str(self.fields[1].field_with_ships())
            print("\n\n", "*"*42, sep="")
            print("ENEMY'S FIELD")
            fg.field_to_str(self.fields[0].field_without_ships())
        else:
            print('YOUR FIELD')
            fg.field_to_str(self.fields[0].field_with_ships())
            print("\n\n", "*"*42, sep="")
            print("ENEMY'S FIELD")
            fg.field_to_str(self.fields[1].field_without_ships())

    def read_position(self):
        letter, number = input("Enter the letter: "), int(input("Enter the number: "))
        while letter not in fg.letters or (number > 10 or number < 1):
            print("Incorrect input. Try again!")
            letter, number = input("Enter the letter: "), int(input("Enter the number: "))
        return fg.convert_coordinates((letter, number))


while True:
    name1, name2 = input("Enter your name: "), input("Enter your name: ")
    battle_ships = Game(name1, name2)
    current_player = 0

    winner, landed, killed = False, False, False
    while True:
        if current_player:
            next_player = 0
        else:
            next_player = 1

        battle_ships.print_fields(current_player)
        coordinates = battle_ships.read_position()
        if battle_ships.fields[next_player].shoot_at(coordinates) == "x":
            landed = True

        if landed:
            print("You have landed!")
            killed = battle_ships.fields[next_player].check_ships_killed()
            if killed:
                print("All ships are killed. Congratulations!")
                winner = battle_ships.fields[next_player].check_ships_killed()
        else:
            killed = False

        if not landed:
            input(battle_ships.players[next_player].name + " press something: ")
            battle_ships.current_player = next_player

        if winner:
            print(battle_ships.players[current_player].name + " won!!!")
            break
    if not input("Press something to play again: "):
        break
