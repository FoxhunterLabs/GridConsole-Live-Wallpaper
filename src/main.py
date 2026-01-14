from kivy.app import App
from kivy.core.window import Window
from app.wallpaper_widget import HudWallpaper

class GridConsoleApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return HudWallpaper()

if __name__ == "__main__":
    GridConsoleApp().run()
