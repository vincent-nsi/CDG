import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MonInterface(Widget):
    entre = ObjectProperty(None)
    message = ObjectProperty(None)
    def clicBouton(self):
        self.message.text = f"J'ai bien lu : {self.entre.text}"


class MonAppli(App):
    def build(self):
        return MonInterface()

if __name__ == "__main__":
    MonAppli().run()