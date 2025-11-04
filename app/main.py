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
        
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        
if __name__ == "__main__":
    app = MainApp()
    app.run()