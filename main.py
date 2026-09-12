from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser
import random
import string

class DiscordGenApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="Discord Auto-Gen App", font_size='20sp')
        self.layout.add_widget(self.label)
        self.btn = Button(text="GENERATE & OPEN DISCORD", size_hint=(1, 0.2), background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.generate_and_open)
        self.layout.add_widget(self.btn)
        return self.layout

    def generate_and_open(self, instance):
        username = "".join(random.choices(string.ascii_letters, k=8)) + str(random.randint(100, 999))
        password = "".join(random.choices(string.ascii_letters + string.digits, k=12))
        webbrowser.open("https://discord.com/register")
        self.label.text = f"Done! \nUser: {username}\nPass: {password}"

if __name__ == "__main__":
    DiscordGenApp().run()
