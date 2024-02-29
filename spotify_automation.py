#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty 

class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def buttonClicked(self):        # ボタンをクリック時
        pass


class spotify_automationApp(App):
    def __init__(self, **kwargs):
        super(spotify_automationApp, self).__init__(**kwargs)
        self.title = 'Spotify_Automation'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    spotify_automationApp().run()


