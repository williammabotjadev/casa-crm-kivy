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

class RegisterFormButton(MDRaisedButton):
    def on_press(self):
        if self.id == "register_user":
            print("Registered User")

class LoginButton(MDRaisedButton):
    def on_press(self):
        if self.id == "login":
            self.parent.parent.current = "login"

class LoginFormButton(MDRaisedButton):
    def on_press(self):
        if self.id == "login_user":
            print("Logged In")

class PasswordField(MDTextField):
    pass 

class EyeButtonIcon(MDIconButton):
    def on_release(self):
        if self.icon == "eye-off":
            self.icon = "eye"
            self.parent.children[4].password = False
            self.parent.children[2].password = False
        else:
            self.icon = "eye-off"
            self.parent.children[4].password = True
            self.parent.children[2].password = True
          
class EyeButtonLoginIcon(MDIconButton):
    def on_release(self):
        if self.icon == "eye-off":
            self.icon = "eye"
            self.parent.children[2].password = False
        else:
            self.icon = "eye-off"
            self.parent.children[2].password = True
       


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
        email_field.helper_text = "Enter your email"
        email_field.mode = "fill"
        email_field.size_hint = 0.8, 0.1
        email_field.pos_hint = {'center_x': 0.5, 'center_y': 0.7}
        register_screen.add_widget(email_field)
        password_field = PasswordField()
        password_field.id = "password"
        password_field.hint_text = "Enter Password"
        password_field.helper_text = "Enter Password"
        password_field.mode = "fill"
        password_field.size_hint = 0.8, 0.1
        password_field.password = True
        password_field.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        register_screen.add_widget(password_field)
        # Eye Icon - Password
        eye_btn = EyeButtonIcon()
        eye_btn.pos_hint = {'center_x': 0.85, 'center_y': 0.5}
        eye_btn.icon = 'eye-off'
        register_screen.add_widget(eye_btn)
        password_confirm_field = PasswordField()
        password_confirm_field.id = "password_confirm"
        password_confirm_field.hint_text = "Confirm Password"
        password_confirm_field.helper_text = "Enter Password"
        password_confirm_field.mode = "fill"
        password_confirm_field.size_hint = 0.8, 0.1
        password_confirm_field.password = True
        password_confirm_field.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        register_screen.add_widget(password_confirm_field)
        # Eye Icon - Confirm Password
        eye_btn_confirm = EyeButtonIcon()
        eye_btn_confirm.pos_hint = {'center_x': 0.85, 'center_y': 0.3}
        eye_btn_confirm.icon = 'eye-off'
        register_screen.add_widget(eye_btn_confirm)
        register_form_btn = RegisterFormButton()
        register_form_btn.text = "Register"
        register_form_btn.id = "register_user"
        register_form_btn.pos_hint = {'center_x': 0.5, 'center_y': 0.1}
        register_form_btn.md_bg_color = (.32, .42, .68, 1)
        register_screen.add_widget(register_form_btn)
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
        # Form - Login
        email_field_login = MDTextField()
        email_field_login.hint_text = "Email"
        email_field_login.helper_text = "Enter your email"
        email_field_login.mode = "fill"
        email_field_login.size_hint = 0.8, 0.1
        email_field_login.pos_hint = {'center_x': 0.5, 'center_y': 0.7}
        login_screen.add_widget(email_field_login)
        password_login = PasswordField()
        password_login.hint_text = "Password"
        password_login.helper_text = "Enter your Password"
        password_login.mode = "fill"
        password_login.size_hint = 0.8, 0.1
        password_login.password = True
        password_login.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        login_screen.add_widget(password_login)
        # Eye Icon - Login Password
        eye_btn_login = EyeButtonLoginIcon()
        eye_btn_login.pos_hint = {'center_x': 0.85, 'center_y': 0.5}
        eye_btn_login.icon = 'eye-off'
        login_screen.add_widget(eye_btn_login)
        login_form_btn = LoginFormButton()
        login_form_btn.text = "Login"
        login_form_btn.id = "login_user"
        login_form_btn.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        login_form_btn.md_bg_color = (.32, .42, .68, 1)
        login_screen.add_widget(login_form_btn)
        sm.add_widget(login_screen)
        return sm


CasaCRM().run()