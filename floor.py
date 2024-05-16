import pygame


class Floor:

    def __init__(self, x, y, floor_type, grid_row, grid_column):
        self.floor_type = floor_type
        self.x = x
        self.y = y
        self.row = grid_row
        self.column = grid_column
        self.image = pygame.image.load("Wood floor.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    # def set_image(self):
    #     if self.tile_type == 0:
    #         self.image = pygame.image.load("Wood floor.png")
    #     # elif self.tile_type == 1:
    #     #     self.image = pygame.image.load("images/wall.png")
    #     # elif self.tile_type == 2:
    #     #     self.image = pygame.image.load("images/start_floor.png")