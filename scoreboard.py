import pygame.font

class Scoreboard:
    """A class to report scoring info"""

    def __init__(self, ai_game,):
        """Init scorekeeping attribs"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prep the score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into an image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score at top right of screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)