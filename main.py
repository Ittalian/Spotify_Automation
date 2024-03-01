#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty

class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加
    is_starting = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def check_app_state(self):      # ボタンをクリック時
        # is_starting = False
        self.is_starting = not self.is_starting
        if self.is_starting:
            self.text = "Starting App"
        else:
            self.text = "Stopping App"

class spotify_automationApp(App):
    def __init__(self, **kwargs):
        super(spotify_automationApp, self).__init__(**kwargs)
        self.title = 'Spotify_Automation'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    spotify_automationApp().run()


