from floor import Floor

class Board:

    def __init__(self):
        self.board_map = self.generate_world()

    def generate_world(self):
        map = []
        row = 0
        y = 10
        for i in range(30):
            floor = []
            column = 0
            x = 10
            for j in range(40):
                f = Floor(x, y, 1, row, column)
                column += 1
                x = x + 24
                floor.append(f)
            row += 1
            y = y + 24
            map.append(floor)
        return map