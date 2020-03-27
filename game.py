import arcade

# Game constants
SCREEN_TITLE = "Python Game"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BACKGROUND_COLOR = arcade.csscolor.CORNFLOWER_BLUE

# Block props
BLOCK_SCALING = 0.5

# Ground props
WALL_SCALING = 0.5
WALL_WIDTH = 64

# Player props
PLAYER_SCALING = 1
PLAYER_CENTER_X = 64
PLAYER_CENTER_Y = 128
PLAYER_SPEED = 5
GRAVITY = 1

class Game(arcade.Window):
  def __init__(self):
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(BACKGROUND_COLOR)

    # Game variables
    self.blocks = None
    self.walls = None
    self.players = None
    self.player_sprite = None
    self.physics = None

  def setup(self):
    """ Setup game variables """
    self.blocks = arcade.SpriteList()
    self.walls = arcade.SpriteList()
    self.players = arcade.SpriteList()

    # setup player
    imagePlayer = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(imagePlayer, PLAYER_SCALING)
    self.player_sprite.center_x = PLAYER_CENTER_X
    self.player_sprite.center_y = PLAYER_CENTER_Y
    self.players.append(self.player_sprite)

    # setup ground
    for x in range(0, SCREEN_WIDTH, WALL_WIDTH):
      imageWall = ":resources:images/tiles/grassMid.png" 
      wall = arcade.Sprite(imageWall, WALL_SCALING)
      wall.center_x = x
      wall.center_y = 32
      self.walls.append(wall)

    self.physics = arcade.PhysicsEnginePlatformer(
      self.player_sprite,
      self.walls,
      GRAVITY
    )

  def on_draw(self):
    """ Render game screen """
    arcade.start_render()
    self.blocks.draw()
    self.walls.draw()
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

  