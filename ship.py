import pygame
ship_image = 'images/ship.bmp'

class Ship():
    def __init__(self, ai_settings, screen):
        self.moving_right = False
        self.moving_left = False
        self.screen = screen #odnosnik do ekranu, na ktorym statek ma zostac wyswietlony
        self.ai_settings = ai_settings

        self.image = pygame.image.load(ship_image) # wczytanie obrazu
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self): #displat image
        self.screen.blit(self.image, self.rect)