import pygame


class BodySquare:
    def __init__(self):
        self.active = False
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def add_connection(self, location, body_part):
        if location == 't':  # NOTE may add opposite connections later to body part
            self.top = body_part
        elif location == 'r':
            self.right = body_part
        elif location == 'b':
            self.bottom = body_part
        elif location == 'l':
            self.left = body_part

    def activate(self):
        self.active = True
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None

    def draw(self, screen, colour, x, y, size):
        pygame.draw.rect(screen, colour, (x, y, size, size))
        if self.top is not None:
            self.top.draw(screen, colour, x, y - size, size)
        if self.right is not None:
            self.right.draw(screen, colour, x + size, y, size)
        if self.bottom is not None:
            self.bottom.draw(screen, colour, x, y + size, size)
        if self.left is not None:
            self.left.draw(screen, colour, x - size, y, size)


class BodySquarePool:
    def __init__(self, max_body_parts):
        self.pool = [BodySquare() for _ in range(max_body_parts)]
        
    def get_unused_body_square(self):
        for body_square in self.pool:
            if not body_square.active:
                body_square.activate()
                return body_square
        return None  # Return None if no free body squares