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
        banner = MDToolbar()
        banner.text = 'Welcome to CasaCRM'
        banner.pos_hint = { 'top': 1 }
        screen.add_widget(banner)
        for text in self.data:
            custom_btn = MDRaisedButton()
            custom_btn.text = str(text)
            custom_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
            pos_count += 0.1
            screen.add_widget(custom_btn)
        return screen


Example().run()