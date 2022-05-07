from atexit import register
from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.banner import MDBanner
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField

class RegisterButton(MDRaisedButton):
    def on_press(self):
        if self.id == "register":
            self.parent.parent.current = "register"

class LoginButton(MDRaisedButton):
    def on_press(self):
        if self.id == "login":
            self.parent.parent.current = "login"


class CasaCRM(MDApp):

    def build(self):
        sm = ScreenManager()
        screen = MDScreen()
        pos_count = 0.4
        # Top Bar 
        top_bar = MDToolbar()
        top_bar.title = 'Welcome to CasaCRM'
        top_bar.pos_hint = { 'top': 1 }
        top_bar.md_bg_color = (.32, .42, .68, 1)
        screen.add_widget(top_bar)
        # Logo Icon
        icon_btn = MDIconButton()
        icon_btn.pos_hint = { 'center_x': 0.5, 'center_y': 0.6 }
        icon_btn.icon = 'images/landing.png'
        screen.add_widget(icon_btn)
        # Registration Button
        register_btn = RegisterButton()
        register_btn.text = "Register"
        register_btn.id = "register"
        register_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
        register_btn.md_bg_color = (.32, .42, .68, 1)
        pos_count -= 0.1
        screen.add_widget(register_btn)
        # Login Button
        login_btn = LoginButton()
        login_btn.text = "Login"
        login_btn.id = "login"
        login_btn.pos_hint = {'center_x': 0.5, 'center_y': pos_count}
        login_btn.md_bg_color = (.32, .42, .68, 1)
        pos_count -= 0.1
        screen.add_widget(login_btn)
        screen.name = "home"       
        sm.add_widget(screen)
        # Register Screen
        register_screen = MDScreen()
        register_screen.name = "register"
        # Top Bar - Registration
        top_bar_reg = MDToolbar()
        top_bar_reg.title = 'Create an Account'
        top_bar_reg.pos_hint = { 'top': 1 }
        top_bar_reg.md_bg_color = (.32, .42, .68, 1)
        register_screen.add_widget(top_bar_reg)
        # Form - Registration
        email_field = MDTextField()
        email_field.hint_text = "Email"
        email_field.text = "Email Address"
        email_field.helper_text = "Enter your email"
        email_field.mode = "fill"
        register_screen.add_widget(email_field)
        username_field = MDTextField()
        username_field.hint_text = "Email"
        username_field.text = "Email Address"
        username_field.helper_text = "Enter your email"
        username_field.mode = "fill"
        register_screen.add_widget(username_field)
        password_field = MDTextField()
        password_field.hint_text = "Email"
        password_field.text = "Email Address"
        password_field.helper_text = "Enter your email"
        password_field.mode = "fill"
        register_screen.add_widget(password_field)
        password_confirm_field = MDTextField()
        password_confirm_field.hint_text = "Email"
        password_confirm_field.text = "Email Address"
        password_confirm_field.helper_text = "Enter your email"
        password_confirm_field.mode = "fill"
        register_screen.add_widget(password_confirm_field)
        sm.add_widget(register_screen)
        # Login Screen
        login_screen = MDScreen()
        login_screen.name = "login"
        # Top Bar - Login
        top_bar_login = MDToolbar()
        top_bar_login.title = 'Login'
        top_bar_login.pos_hint = { 'top': 1 }
        top_bar_login.md_bg_color = (.32, .42, .68, 1)
        login_screen.add_widget(top_bar_login)
        sm.add_widget(login_screen)
        return sm


CasaCRM().run()