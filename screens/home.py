from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineIconListItem
from kivy.properties import StringProperty
from kivy.app import App
from kivy.clock import Clock

Builder.load_string(
'''
<IconItemWidget>:
    IconLeftWidget:
        icon:root.icon

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar
            title: "Aplicacion de ejemplo"
            elevation: 10
            left_action_items: [["menu", lambda x: app.nav_drawer.set_state('toggle')]]
        BoxLayout:
            orientation: 'vertical'
            BoxLayout:
                size_hint_y:.3
                Image:
                    source: 'company.png'
                    keep_ratio: False
                    allow_stretch: True
            MDList:
                size_hint_y:.7
                id: list_items

'''
)


class IconItemWidget(TwoLineIconListItem):
    def __init__(self, text, secondary, icon):
        self.text = text
        self.icon = icon
        self.secondary_text = secondary
        super().__init__()


class HomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.on_change)

    def on_change(self, *args):
        items = {
            "email": {
                "text": "Email",
                "secondary": "company@company.com"
            },
            "facebook": {
                "text": "Home",
                "secondary": "link to facebook"
            },
            "twitter": {
                "text": "Twitter",
                "secondary": "link to Twitter"
            },
            "git": {
                "text": "Git",
                "secondary": "link to Git"
            }
        }
        app = App.get_running_app()
        list_items = app.root.ids.home_screen.ids.list_items
        for icon, data in items.items():
            item = IconItemWidget(
                text=data['text'],
                secondary=data['secondary'],
                icon=icon,
            )
            list_items.add_widget(item)
