import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "2d game: XYZ"


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        pass

    def on_draw(self):

        arcade.start_render()

def main():

    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()



