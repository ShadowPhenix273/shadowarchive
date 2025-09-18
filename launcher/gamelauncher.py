from ursina import *


class GameLauncher(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.background = Entity(parent=camera.ui, model='quad', color=color.black, scale=(2, 1))
        self.title = Text(parent=camera.ui, text='Game Launcher', y=0.4, scale=3, color=color.white)
        self.start_button = Button(parent=camera.ui, text='Start Game', y=0.1, scale=(0.3, 0.1), color=color.azure)
        self.quit_button = Button(parent=camera.ui, text='Quit', y=-0.1, scale=(0.3, 0.1), color=color.red)

        self.start_button.on_click = self.start_game
        self.quit_button.on_click = application.quit

        for key, value in kwargs.items():
            setattr(self, key, value)

    def start_game(self):
        print("Starting the game...")
        # Here you would add the logic to launch your game
        self.disable()  # Hide the launcher UI

    def disable(self):
        self.background.disable()
        self.title.disable()
        self.start_button.disable()
        self.quit_button.disable()

if __name__ == '__main__':
    app = Ursina()
    launcher = GameLauncher()
    app.run()