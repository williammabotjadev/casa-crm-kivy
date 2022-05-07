from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton


class Example(MDApp):
    data = {
        'Register',
        'Login'
    }

    def build(self):
        screen = MDScreen()
        pos_count = 0.5
        for text in self.data:
            custom_btn = MDRaisedButton()
            custom_btn.text = str(text)
            custom_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
            pos_count += 0.1
            screen.add_widget(custom_btn)
        return screen


Example().run()