import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from steganocryptopy.steganography import Steganography

#Steganography.generate_key("")

class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)


    def encrypted(self):
        encrypted_image = Steganography.encrypt("key.key", "input.png", "message.txt")
        encrypted_image.save("output.png")
        print("Шифрую")
        #self.name.text = ""
        #self.email.text = ""

    def decrypted(self):
        decrypted_text = Steganography.decrypt("key.key", "output.png")
        print(decrypted_text)
        print("Расшифорвываю")






class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()