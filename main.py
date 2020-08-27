from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem, MDList
from kivymd.theming import ThemableBehavior

from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen

Builder.load_string(
"""

<ItemWidget>:
    theme_text_color: "Custom"
    text_color: app.theme_cls.text_color
    on_release: self.parent.set_item_selected(self)
    IconLeftWidget:
        theme_text_color: "Custom"
        text_color: root.text_color
        icon: root.icon

<ContentDrawer>:
    orientation: "vertical"
    FloatLayout:
        size_hint_y: None
        height: "200dp"
        BoxLayout:
            id: box_image
            size_hint_y: None
            height: "200dp"
            x: root.x
            pos_hint: {"top": 1}
            
            FitImage:
                source: "menu.png"
        MDLabel:
            text: "Nombre de la empresa"
            size_hint_y: None
            height: self.texture_size[1]
            x: root.x
            y: root.height - box_image.height + dp(10)
            
    ScrollView:
        ScrollList:
            id: scroll_list

<RootWidget@Screen>:
    NavigationLayout:
        ScreenManager:
            LoginScreen:
                id: login_screen
                email: input_email
                password: input_password
                MDToolbar:
                    title: "Aplicacion de ejemplo"
                    elevation: 10
                    pos_hint: {"top": 1}
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                AnchorLayout:
                    anchor_x: "center"
                    anchor_y: "center"
                    BoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        size_hint_x: .5
                        MDTextField:
                            id: input_email
                            hint_text: "Email"
                        MDTextField:
                            id: input_password
                            hint_text: "password"
                        MDRaisedButton:
                            pos_hint: {"center_x": .5}
                            text: "ingresar"
                            on_release: login_screen.login()
        
        MDNavigationDrawer:
            id: nav_drawer
            ContentDrawer:
                id: content_drawer
"""
)

class LoginScreen(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    def login(self):
        print(self.email.text)
        print(self.password.text)

class ScrollList(ThemableBehavior, MDList):
    def set_item_selected(self, instance):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance.text_color = self.theme_cls.primary_color


class ItemWidget(OneLineAvatarIconListItem):
    icon = StringProperty()

class ContentDrawer(BoxLayout):
    pass


class ExampleApp(MDApp):
    def on_start(self):
        items = {
            "home": "Home",
            "facebook": "Facebook",
            "twitter": "Twitter",
            "git": "Git"
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