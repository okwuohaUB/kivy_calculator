from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import math


class Calculator(BoxLayout):

    def button_press(self, value):
        self.ids.display.text += value

    def clear(self):
        self.ids.display.text = ""

    def backspace(self):
        self.ids.display.text = self.ids.display.text[:-1]

    def calculate(self):
        try:
            expression = self.ids.display.text
            expression = expression.replace('π', str(math.pi))
            expression = expression.replace('√', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')

            self.ids.display.text = str(eval(expression))
        except:
            self.ids.display.text = "Error"


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
