import random
import field_generation as fg
from ship import Ship


class Field:
    """
    Represents battleship field
    """
    def __init__(self):
        """
        Initialize field with the list of ships, and the 
        representation of field
        """
        self.ships = generate_field()[0]
        self.field = generate_field()[1]
        self.shoots = set()

    def shoot_at(self, coordinates):
        """
        Perform shooting at one of the parts of the ship
        """
        self.shoots.add(coordinates)
        for ship in self.ships:
            if ship.belong_to(coordinates):
                return "x"
            else:
                return "-"

    def check_ships_killed(self):
        """
        Check if there are ships remaining
        Return True if all are killed
        """
        count = 0
        for ship in self.ships:
            if ship.check_if_killed():
                count += 1
        return count == 10

    def field_without_ships(self):
        """
        Returns field representation for the enemy.
        Show only shoots and landed ships.
        """
        field = [[" " for i in range(10)] for j in range(10)]
        for line in range(10):
            for column in range(10):
                if (line, column) in self.shoots:
                    field[line][column] = self.shoot_at((line, column))
        return field

    def field_with_ships(self):
        """
        Return field representation for the current player.
        Landed ships are marked with "x"
        """
        field = self.field
        for shoot in self.shoots:
            if field[shoot[0]][shoot[1]] == '*':
                field[shoot[0]][shoot[1]] = 'x'
        return field


def generate_field():
    """
    Function to randomly generate the field
    """
    ships = []
    field = [[" " for i in range(10)] for i in range(10)]
    free_coordinates = [(i, j) for i in range(10) for j in range(10)]
    ship_types = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for ship_type in ship_types:
        bow = random.choice(free_coordinates)
        end_coordinates = fg.get_end_coordinates(bow, ship_type)
        ship, occupied = fg.covered_area(bow, end_coordinates)
        if bow[1] == end_coordinates[1]:
            horizontal = True
        else:
            horizontal = False
        new_ship = Ship(bow, ship_type, horizontal)
        ships.append(new_ship)
        for coordinates in occupied:
            try:
                free_coordinates.remove(coordinates)
            except ValueError:
                pass

        for coordinates in ship:
            field[coordinates[0]][coordinates[1]] = "*"
    return ships, field
