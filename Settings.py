class Settings():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        '''
        Bullet settings
        '''
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        '''
        Alien settings
        '''
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10 # szybkość poruszania sie floty w dół ekranu
        self.fleet_direction = 1