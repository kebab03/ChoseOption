from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.app import MDApp

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(100)
        MDLabel:
            id: value_label
            text: "Slider Value: {}".format(app.slider_value)
            halign: "center"
            font_style: "H6"

    BoxLayout:
        orientation: 'vertical'
        MDSlider:
            id: slider
            min: 0
            max: 100
            value: app.slider_value
            hint: False
            elevation: 2
            color: app.theme_cls.accent_color
            on_value: app.slider_value = self.value
'''

class TestApp(MDApp):
    slider_value = NumericProperty(40)

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    TestApp().run()
