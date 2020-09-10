from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage

Builder.load_string(
'''
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors

<ItemUser>:
    AsyncImageLeftWidget:
        source: root.source
        canvas:
            Color:
                rgba: get_color_from_hex(colors["Light"]["Background"])
            Line:
                width: 4.5
                rounded_rectangle: [self.x-3, self.y-3, self.width+6, self.height+6, 20]

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
        for user in result['results']:
            name = user["name"]["first"]
            item = ItemUser(text=name, source=user['picture']['thumbnail'])
            self.screen.list_user.add_widget(item)
            self.users_loaded = True

    def on_error(self, request, error):
        print(error)

    def set_users(self,*args):
        UrlRequest(URL,
                   on_success=self.on_success,
                   on_error=self.on_error)

    @property
    def screen(self):
        app = App.get_running_app()
        return app.root.ids.user_screen.ids