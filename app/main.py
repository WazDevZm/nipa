from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "./calculator_11382673.png" # add icon in this field
        self.operators = ["/", "*", "+", "-"] # adding all the operatotrs for this
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "white")
        
if __name__ == "__main__":
    app = MainApp()
    app.run()