from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from menu import ItemWidget

Builder.load_string(
"""
#: import LoginScreen screens.login
#: import HomeScreen screens.home
#: import ContentDrawer menu

<RootWidget@Screen>:
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            HomeScreen:
                id: home_screen
                name: 'home'
            LoginScreen:
                id: login_screen
                name: 'login'

        MDNavigationDrawer:
            id: nav_drawer
            ContentDrawer:
                id: content_drawer
"""
)




class ExampleApp(MDApp):

    @property
    def nav_drawer(self):
        app = self.get_running_app()
        return app.root.ids.nav_drawer

    def on_start(self):
        items = {
            "information": "Information",
            "music-box": "Music",
            "calendar-account": "Calendar",
            "help": "Help",
            "close": "Close"
        }

        for icon, text in items.items():
            item = ItemWidget(text=text, icon=icon)
            self.root.ids.content_drawer.ids.scroll_list.add_widget(
                item
            )
    def build(self):
        return Factory.RootWidget()

if __name__ == '__main__':
    ExampleApp().run()