import numpy as np
import random
from string import ascii_uppercase as letters
letters = letters[:10]


def read_file(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        res = []
        for line in data:
            line = line[:-1]
            res.append(list(line))
    return np.array(res)


def convert_coordinates(coordinates):
    row = coordinates[1] - 1
    column = letters.index(coordinates[0])
    return row, column


def has_ship(coordinates, field):
    if field[coordinates[0], coordinates[1]] == '*':
        return True
    return False


def is_horizontal(coordinates, field):
    return has_ship((coordinates[0], coordinates[1] + 1), field) or \
           has_ship((coordinates[0], coordinates[1] - 1), field)


def ship_coordinates(coordinates, field):
    if has_ship(coordinates, field):
        ship = [coordinates]

        for i in range(1, 4):
            if (coordinates[0] + i) < 10 and has_ship((coordinates[0] + i, coordinates[1]), field):
                ship.append((coordinates[0] + i, coordinates[1]))
            else:
                break

        for i in range(1, 4):
            if (coordinates[0] - i) > 0 and has_ship((coordinates[0] - i, coordinates[1]), field):
                ship.append((coordinates[0] - i, coordinates[1]))
            else:
                break

        if len(ship) == 1:
            for i in range(1, 4):
                if (coordinates[1] + i) < 10 and has_ship((coordinates[0], coordinates[1] + i), field):
                    ship.append((coordinates[0], coordinates[1] + i))
                else:
                    break

            for i in range(1, 4):
                if (coordinates[1] - i) > 0 and has_ship((coordinates[0], coordinates[1] - i), field):
                    ship.append((coordinates[0], coordinates[1] - i))
                else:
                    break

        return ship


def ship_size(coordinates, field):
    return len(ship_coordinates(coordinates, field)) if has_ship(coordinates, field) else 0


def is_valid(field):
    taken_coordinates = []
    count_ships = [0]*4
    try:
        for row in range(10):
            for cell in range(10):
                if (row, cell) not in taken_coordinates and has_ship((row, cell), field):
                    taken_coordinates.extend(ship_coordinates((row, cell), field))
                    count_ships[ship_size((row, cell), field) - 1] += 1
    except IndexError:
        return False

    if count_ships == [i for i in range(4, 0, -1)] and len(taken_coordinates) == len(set(taken_coordinates)):
        return True
    return False


def get_end_coordinates(start_coordinates, size):
    size -= 1
    x = random.choice([start_coordinates[0] + size, start_coordinates[0], start_coordinates[0] - size])
    y = start_coordinates[1]
    if x > 9:
        x = random.choice([start_coordinates[0], start_coordinates[0] - size])
    elif x < 0:
        x = random.choice([start_coordinates[0], start_coordinates[0] + size])
    elif x == start_coordinates[0]:
        y = random.choice([start_coordinates[1] + size, start_coordinates[1] - size])
        if y < 0:
            y = start_coordinates[1] + size
        elif y > 9:
            y = start_coordinates[1] - size
    return x, y


def covered_area(coordinates1, coordinates2):
    area = set()
    ship = set()

    if coordinates1 > coordinates2:
        coordinates1, coordinates2 = coordinates2, coordinates1

    for line in range(coordinates1[0], coordinates2[0] + 1):
        for column in range(coordinates1[1], coordinates2[1] + 1):
            ship.add((line, column))

    for coordinate in ship:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= coordinate[0] + i < 10 and 0 <= coordinate[1] + j < 10:
                    area.add((coordinate[0] + i, coordinate[1] + j))
    return ship, area


def generate_field():
    field = [[" " for i in range(10)] for i in range(10)]
    free_coordinates = [(i, j) for i in range(10) for j in range(10)]
    ship_types = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for ship_type in ship_types:
        start_coordinates = random.choice(free_coordinates)
        end_coordinates = get_end_coordinates(start_coordinates, ship_type)
        ship, occupied = covered_area(start_coordinates, end_coordinates)
        for coordinates in occupied:
            try:
                free_coordinates.remove(coordinates)
            except ValueError:
                pass

        for coordinates in ship:
            field[coordinates[0]][coordinates[1]] = "*"
    return field


def get_field():
    while True:
        field = generate_field()
        if is_valid(np.array(field)):
            break
    return field
