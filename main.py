#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty

import requests
import json

# アクセストークンを取得する関数
def get_access_token():
    headers = {
        'Authorization': 'Basic ZDMxNGNhZjdhODIwNDlmZWIwYzgwYzZiOTIzZGNkODA6YzUxOTU3ZmNiYWVhNDAwMDhlYjRkOGJhYzgwMzQwYmU=',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': 'AQDgisALHNFTFI2N1Rlj9_x1XgJdt6sB3wQXHDsvJtgBObpRvAD4O5bx1RjCIeBzA3T4wLSuoFyNyL0fsAvC3aBioPZxyfx8N7bwT6rn4J51V5crgBLdkWQdqfBwhBbd5HA',
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

    return json.loads(response.text)["access_token"]

# APIを叩く関数
def play_music(index):
    headers = {
        'Authorization': 'Bearer ' + get_access_token(),
        'Content-Type': 'application/json',
    }

    json_data = {
        'context_uri': 'spotify:playlist:6OJHpbVGr7JigmFEU9xq0O',
        'offset': {
            'position': index,
        },
        'position_ms': 0,
    }

    response = requests.put('https://api.spotify.com/v1/me/player/play?device_id=4bb8a462453c69392da0985c0084e61c96dadbc7', headers=headers, json=json_data)

    return response

class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加
    is_starting = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def check_app_state(self):      # ボタンをクリック時
        self.is_starting = not self.is_starting
        if self.is_starting:
            self.text = "Starting App"
            play_music(3)
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


