from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.banner import MDBanner
from kivymd.uix.toolbar import MDToolbar

class Example(MDApp):
    data = {
        'Register',
        'Login'
    }

    def build(self):
        screen = MDScreen()
        pos_count = 0.5
        top_bar = MDToolbar()
        top_bar.title = 'Welcome to CasaCRM'
        top_bar.pos_hint = { 'top': 1 }
        top_bar.md_bg_color = (.32, .42, .68, 1)
        screen.add_widget(top_bar)
        for text in self.data:
            custom_btn = MDRaisedButton()
            custom_btn.text = str(text)
            custom_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
            custom_btn.md_bg_color = (.32, .42, .68, 1)
            pos_count += 0.1
            screen.add_widget(custom_btn)
        return screen


Example().run()