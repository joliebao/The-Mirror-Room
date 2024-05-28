import pygame


class Girl:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("girl backward.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.delta = 8
        self.current_direction = "left"
        self.current_direction = "backward"

    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.image.load("girl backward.png")
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.current_direction == "left" and direction == "right":
            self.image = pygame.image.load("girl backward.png")
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.current_face == "forward" and direction == "down":
            self.image = pygame.image.load("girl forward.png")
        if direction == "right":
            self.current_direction = "right"
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left":
            self.current_direction = "left"
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])