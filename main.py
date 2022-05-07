from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.banner import MDBanner
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.card import MDCard

class RegisterButton(MDRaisedButton):
    def on_touch_down(self, touch):
        print(f"You touch down on {self.text}")

class LoginButton(MDRaisedButton):
    def on_touch_down(self, touch):
        print(f"You touch down on {self.text}")

class CasaCRM(MDApp):

    def build(self):
        screen = MDScreen()
        pos_count = 0.4
        top_bar = MDToolbar()
        top_bar.title = 'Welcome to CasaCRM'
        top_bar.pos_hint = { 'top': 1 }
        top_bar.md_bg_color = (.32, .42, .68, 1)
        screen.add_widget(top_bar)
        icon_btn = MDIconButton()
        icon_btn.pos_hint = { 'center_x': 0.5, 'center_y': 0.6 }
        icon_btn.icon = 'images/landing.png'
        screen.add_widget(icon_btn)
        # Registration Button
        register_btn = RegisterButton()
        register_btn.text = "Register"
        register_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
        register_btn.md_bg_color = (.32, .42, .68, 1)
        pos_count -= 0.1
        screen.add_widget(register_btn)
        # Login Button
        login_btn = LoginButton()
        login_btn.text = "Login"
        login_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
        login_btn.md_bg_color = (.32, .42, .68, 1)
        pos_count -= 0.1
        screen.add_widget(login_btn)       
            
        return screen


CasaCRM().run()