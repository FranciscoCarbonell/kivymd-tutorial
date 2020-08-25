from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string('''
<InfoScreen>:
    AnchorLayout:
        anchor_y: 'top'
        MDToolbar:
            id: toolbar
            title: "Aplicacion de ejemplo"
            elevation: 10
            left_action_items: [["menu", lambda x: app.nav_drawer.set_state('toggle')]]
    AnchorLayout:
        MDLabel:
            halign: 'center'
            text: "Pagina informacion"
            size_hint: 1, None
''')


class InfoScreen(Screen):
    pass