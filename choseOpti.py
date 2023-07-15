from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # TextInput widget
        text_input = TextInput(multiline=False)
        layout.add_widget(text_input)
        selected_option_label = Label(text='Scegli il [b]nome[/b]  della frutta che preferisci: ', markup=True)
        layout.add_widget(selected_option_label)
        selected_option_label.color = (1, 0, 0, 1)  # Red color
        # DropDown widget
        dropdown = DropDown()

        # Example items for the dropdown
        items = ['Apple', 'Orange', 'Banana']

        for item in items:
            btn = Button(text=item, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_item(text_input, btn.text))
            dropdown.add_widget(btn)

        # Button to open the dropdown
        dropdown_button = Button(text='Open Dropdown')
        dropdown_button.bind(on_release=dropdown.open)
        layout.add_widget(dropdown_button)

        return layout

    def select_item(self, text_input, item_text):
        #text_input.text = item_text
        if item_text == 'Apple':
            text_input.text = "You selected  "+item_text
            print("You selected Apple!")
        if item_text == 'Orange':
            text_input.text = "You selected  "+item_text
        if item_text == 'Banana':
            text_input.text = " TU SEI SCIMMIA PERCHE HAI SCELTO LA   "+item_text


if __name__ == '__main__':
    MyApp().run()