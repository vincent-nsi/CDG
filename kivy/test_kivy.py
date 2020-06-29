import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class MonInterface(Widget):
    pass

class MonAppli(App):
    def build(self):
        return MonInterface()

if __name__ == "__main__":
    MonAppli().run()