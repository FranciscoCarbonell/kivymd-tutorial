from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App


Builder.load_string(
'''
<LoginScreen>:
    email: input_email
    password: input_password
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
                on_release: root.login()
'''
)


class LoginScreen(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    def login(self):
        if self.email.text == 'admin' and self.password.text == 'admin':
            manager = App.get_running_app()
            manager.root.ids.screen_manager.current = 'home'
