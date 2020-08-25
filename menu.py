from kivymd.uix.list import OneLineAvatarIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_string(
'''

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
            x: root.x
            pos_hint: {"top": 1}
            FitImage:
                source: "menu.png"
        MDLabel:
            text: "Header Text"
            size_hint_y: None
            height: self.texture_size[1]
            x: root.x + 10
            y: root.height - box_image.height + dp(10)
            
    ScrollView:
        ScrollList:
            id: scroll_list

'''
)


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