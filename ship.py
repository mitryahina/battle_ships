import field_generation as fg


class Ship:
    def __init__(self, bow, length, horizontal):
        self.bow = bow
        self._length = length
        self._hit = [False] * length
        self.horizontal = horizontal

    def shoot_at(self, coordinates):
        self._hit[coordinates[0] - self.bow[0] + coordinates[1] - self.bow[1]] = True

    def mark(self, coordinates):
        if self._hit[coordinates[0] - self.bow[0] + coordinates[1] - self.bow[1]]:
            return "X"
        return "*"

    def check_if_killed(self):
        if False not in self._hit:
            return True

    def belong_to(self, coordinates):
        if self.horizontal and (coordinates[1] - self.bow[1]) <= self._length:
            return True
        elif not self.horizontal and (coordinates[0] - self.bow[0] <= self._length):
            return True
        return False


