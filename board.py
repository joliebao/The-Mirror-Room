from floor import Floor

class Board:

    def __init__(self):
        self.board_map = self.generate_world()

    def generate_world(self):
        map = []
        row = 0
        y = 0
        for i in range(30):
            floor = []
            column = 0
            x = 0
            for j in range(8):
                f = Floor(x, y, 10, row, column)
                column += 1
                x = x + 150
                floor.append(f)
            row += 5
            y = y + 150
            map.append(floor)
        return map

    def draw_board(self, screen):
        for row in self.board_map:
            for floor in row:
                floor.draw_floor(screen)
