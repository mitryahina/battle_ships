import field_generation as fg


class Ship:
    """
    Represents ship object
    """
    def __init__(self, bow, length, horizontal):
        """
        Initialize ship with bow(left upper cell), length
        and direction(horizontal or vertical)
        """
        self.bow = bow
        self._length = length
        self._hit = [False] * length
        self.horizontal = horizontal

    def shoot_at(self, coordinates):
        """
        Represents shooting to the part of the ship
        """
        self._hit[coordinates[0] - self.bow[0] + coordinates[1] - self.bow[1]] = True

    def check_if_killed(self):
        """
        Check if not all the parts of the ship are landed
        """
        if False not in self._hit:
            return True

    def belong_to(self, coordinates):
        """
        Check if the coordinates belong to certain ship
        """
        if self.horizontal and (coordinates[1] - self.bow[1]) <= self._length:
            return True
        elif not self.horizontal and (coordinates[0] - self.bow[0] <= self._length):
            return True
        return False
