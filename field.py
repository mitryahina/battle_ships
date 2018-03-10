import random
import field_generation as fg
from ship import Ship


class Field:
    def __init__(self):
        self.ships = generate_field()[0]
        self.field = generate_field()[1]
        self.shoots = set()

    def shoot_at(self, coordinates):
        self.shoots.add(coordinates)
        for ship in self.ships:
            if ship.belong_to(coordinates):
                return "x"
            else:
                return "-"

    def field_without_ships(self):
        field = [[" " for i in range(10)] for j in range(10)]
        for line in range(10):
            for column in range(10):
                if (line, column) in self.shoots:
                    field[line][column] = self.shoot_at((line, column))
        return field

    def field_with_ships(self):
        field = self.field
        for shoot in self.shoots:
            if field[shoot[0]][shoot[1]] == '*':
                field[shoot[0]][shoot[1]] = 'x'
        return field


def generate_field():
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



