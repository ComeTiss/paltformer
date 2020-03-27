import arcade

import game_over

# Game constants
SCREEN_TITLE = "Python Game"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BACKGROUND_COLOR = arcade.csscolor.CORNFLOWER_BLUE

# Block props
BLOCK_SCALING = 0.5
BLOCK_GRAVITY = 3

# Ground props
WALL_SCALING = 0.5
WALL_WIDTH = 64

# Player props
PLAYER_SCALING = 1
PLAYER_CENTER_X = 64
PLAYER_CENTER_Y = 128
PLAYER_SPEED = 5
GRAVITY = 1

class Game(arcade.View):
  def __init__(self):
    super().__init__()
    arcade.set_background_color(BACKGROUND_COLOR)

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
    for x in range(0, SCREEN_WIDTH+WALL_WIDTH, WALL_WIDTH):
      imageWall = ":resources:images/tiles/grassMid.png" 
      wall = arcade.Sprite(imageWall, WALL_SCALING)
      wall.center_x = x
      wall.center_y = 32
      self.walls.append(wall)
    
    self.physicPlayer = arcade.PhysicsEnginePlatformer(
      self.player_sprite,
      self.walls,
      GRAVITY
    )

    self.generateBlock()

  def on_draw(self):
    """ Render game screen """
    arcade.start_render()
    self.blocks.draw()
    self.walls.draw()
    self.players.draw()

  def on_key_press(self, key, modifiers):
    if key == arcade.key.LEFT and self.canMoveLeft():
      self.player_sprite.change_x = -PLAYER_SPEED
    elif key == arcade.key.RIGHT and self.canMoveRight():
      self.player_sprite.change_x = PLAYER_SPEED 

  def on_key_release(self, key, modifiers):
    if key == arcade.key.LEFT:
      self.player_sprite.change_x = 0
    elif key == arcade.key.RIGHT:
      self.player_sprite.change_x = 0

  def on_update(self, delta_time):
    self.physicPlayer.update()
    self.applyGravity()

    # Keep player inside screen
    if self.canMoveLeft() == False or self.canMoveRight() == False:
      self.player_sprite.change_x = 0

    # Check if player touches a block
    collisions = arcade.check_for_collision_with_list(self.player_sprite, self.blocks)
    if len(collisions) > 0:
      gameOverView = game_over.GameOver()
      self.window.show_view(gameOverView)

  def canMoveLeft(self):
    return self.player_sprite.center_x > WALL_WIDTH / 2

  def canMoveRight(self):
    return self.player_sprite.center_x < SCREEN_WIDTH - WALL_WIDTH / 2

  def generateBlock(self):
    newBlock = arcade.Sprite(":resources:images/tiles/grassMid.png", BLOCK_SCALING) 
    newBlock.center_x = SCREEN_WIDTH / 2
    newBlock.center_y = SCREEN_HEIGHT
    self.blocks.append(newBlock)

  def applyGravity(self):
    for block in self.blocks:
      block.change_y = -BLOCK_GRAVITY
      block.update()  

def main():
  window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
  gameView = Game()
  window.show_view(gameView)
  arcade.run()

if __name__ == "__main__":
  main()

  