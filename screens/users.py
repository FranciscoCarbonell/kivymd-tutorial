from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage

import certifi

Builder.load_string(
'''

<ItemUser>:
    AsyncImageLeftWidget:
        source: root.source
        allow_stretch: True
        keep_ratio: False
        size_hint: None, None
        size: [dp(50), root.height - dp(10)]
        pos_hint: {"center_y": .5}

<UserScreen>:
    AnchorLayout:
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id: toolbar
                title: "Aplicacion de ejemplo"
                elevation: 10
                left_action_items: [["menu", lambda x: app.nav_drawer.set_state('toggle')]]
            ScrollView:
                MDList:
                    id: list_user
'''
)

URL = 'https://randomuser.me/api/?inc=picture,name&results=15&nat=es'


class AsyncImageLeftWidget(ImageLeftWidget, AsyncImage):
    pass

class ItemUser(OneLineAvatarListItem):
    source = StringProperty()

class UserScreen(Screen):
    users_loaded = False

    def on_enter(self):
        if not self.users_loaded:
            Clock.schedule_once(self.set_users)

    def on_success(self, request, result):
        users = sorted(result['results'], key=lambda x: x['name']['first'])
        for user in users:
            name = user["name"]["first"]
            item = ItemUser(text=name, source=user['picture']['thumbnail'])
            self.screen.list_user.add_widget(item)
            self.users_loaded = True

    def on_error(self, request, error):
        print(error)

    def set_users(self,*args):
        UrlRequest(URL,
                   on_success=self.on_success,
                   on_error=self.on_error,
                   verify=True,
                   ca_file=certifi.where())

    @property
    def screen(self):
        app = App.get_running_app()
        return app.root.ids.user_screen.ids