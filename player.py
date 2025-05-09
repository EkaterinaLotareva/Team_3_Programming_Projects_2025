class Player:
    def __init__(self, hint, color, field):
        self.hint = hint
        self.color = color
        self.field = field

    def reply(self, coords: list):
        if self.hint[0] == 0:
            if self.field.hex[coords].zone == self.hint[1][0] or self.field.hex[coords].zone == self.hint[1][1]:
                return True
            else:
                return False
        else:
            for coords_1 in self.field.hex.keys():
                if self.field.calculate_distance(coords, coords_1) <= self.hint[0]:
                    if self.field.hex[coords_1].self.hint[1][0] == self.hint[1][1]:
                        return True
            return False




