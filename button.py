import pygame.font #moduł generujacy na ekranie tekst

class Button():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #atrybut font do wygenerowania czcionki. Parametr None nakazuje uzyc defaultowej czcionki, 48 to wielkosc czcionki

        self.rect = pygame.Rect(0,0, self.width, self.height) #tworzony jest kwadrat
        self.rect.center = self.screen_rect.center #wysrodkowanie przycisku

        self.prep_msg(msg) #przyhodotanie komunikatu do wyswietlenia

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #zamiana tekstu na obraz
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)