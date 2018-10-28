import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption(("SpaceInvaders"))
    ship = Ship(ai_settings, screen)
    bullets = Group() #Grupa do przechowywania pociskow
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen , "Gra")
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()