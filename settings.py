class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 5

        # Bullet settings
        
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #Alien settings
        self.fleet_drop_speed = 10
        

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # Increase alien point value for new levels
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 4.0
        self.alien_speed = 1.0
        # fleet direction 1 = right, -1 = left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)