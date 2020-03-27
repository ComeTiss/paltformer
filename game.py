import arcade

# Game constants
SCREEN_TITLE = "Python Game"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BACKGROUND_COLOR = arcade.csscolor.CORNFLOWER_BLUE

# Block props
BLOCK_SCALING = 0.5

# Player props
PLAYER_SCALING = 1
PLAYER_CENTER_X = 64
PLAYER_CENTER_Y = 128
PLAYER_SPEED = 5

class Game(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(BACKGROUND_COLOR)

    # Game variables
    self.blocks = None
    self.players = None
    self.player_sprite = None
    self.physics = None

  def setup(self):
    """ Setup game variables """
    self.blocks = arcade.SpriteList()
    self.players = arcade.SpriteList()

    image = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(image, PLAYER_SCALING)
    self.player_sprite.center_x = PLAYER_CENTER_X
    self.player_sprite.center_y = PLAYER_CENTER_Y
    self.players.append(self.player_sprite)

    self.physics = arcade.PhysicsEngineSimple(self.player_sprite, self.blocks)

  def on_draw(self):
    """ Render game screen """
    arcade.start_render()
    self.blocks.draw()
    self.players.draw()

  def on_key_press(self, key, modifiers):
    if key == arcade.key.LEFT:
      self.player_sprite.change_x = -PLAYER_SPEED
    elif key == arcade.key.RIGHT:
      self.player_sprite.change_x = PLAYER_SPEED 

  def on_key_release(self, key, modifiers):
    if key == arcade.key.LEFT:
      self.player_sprite.change_x = 0
    elif key == arcade.key.RIGHT:
      self.player_sprite.change_x = 0

  def on_update(self, delta_time):
    self.physics.update()


def main():
  window = Game()
  window.setup()
  arcade.run()

if __name__ == "__main__":
  main()

  