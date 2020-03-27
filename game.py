import arcade

# Game constants
SCREEN_TITLE = "Python Game"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BACKGROUND_COLOR = arcade.csscolor.CORNFLOWER_BLUE

PLAYER_SCALING = 1
BLOCK_SCALING = 0.5
PLAYER_CENTER_X = 64
PLAYER_CENTER_Y = 128


class Game(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(BACKGROUND_COLOR)

    # Game variables
    self.blocks = None
    self.players = None
    # Sprites
    self.player_sprite = None

  def setup(self):
    """ Setup game variables """
    self.walls = arcade.SpriteList()
    self.players = arcade.SpriteList()

    image = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(image, PLAYER_SCALING)
    self.player_sprite.center_x = PLAYER_CENTER_X
    self.player_sprite.center_y = PLAYER_CENTER_Y
    self.players.append(self.player_sprite)

  def on_draw(self):
    """ Render game screen """
    arcade.start_render()
    self.blocks.draw()
    self.players.draw()

def main():
  window = Game()
  window.setup()
  arcade.run()


if __name__ == "__main__":
  main()

  