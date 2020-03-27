import arcade

import game 

class GameOver(arcade.View):
  def __init__(self):
    super().__init__()

  def on_show(self):
    arcade.set_background_color(arcade.color.BLACK)

  def on_draw(self):
    arcade.start_render()

    arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
    arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

  def on_mouse_press(self, _x, _y, _button, _modifiers):
    newGame = game.Game()
    self.window.show_view(newGame)