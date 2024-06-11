import pygame


class Man:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("image files/man_forward.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        scale_size = (self.image_size[0] * 8, self.image_size[1] * 8)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.delta = 15
        self.current_direction = "left"

    def move_direction(self, direction):
        if self.current_direction == "down" and direction == "up":
            self.image = pygame.image.load("image files/man backward.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 8, self.image_size[1] * 8)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
            self.current_direction = "down"

        elif self.current_direction == "up" and direction == "down":
            self.image = pygame.image.load("image files/man_forward.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 8, self.image_size[1] * 8)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
            self.current_direction = "up"

        elif self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = "left"

        elif self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.current_direction = "right"

        if direction == "right":
            self.current_direction = "right"
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left":
            self.current_direction = "left"
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up":
            self.current_direction = "up"
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down":
            self.current_direction = "down"
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])