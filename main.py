from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


#Color para el fondo

Window.clearcolor = get_color_from_hex("#16203B")


########################################################################
class ScreenManagement(ScreenManager):
    pass

class Intro(Screen):
    pass

class AboutScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)

    def getText(self):
        return ("Hola esta es nuestra aplicacion que fue echa usando [b]kivy[/b]\n"
                "grupo esta compuesto por: \n"
                "Ruben Perez \n"
                "Anthony Cambridge \n"
                )
#############################################################################

class RootCalculadora(Screen, GridLayout):

    answer_text= ObjectProperty(None)

    def borrar(self, express):
	    if express:
		    self.answer_text.text = express[:-1]


    def borrar(self, express):
        if express:
            self.answer_text.text = express[:-1]

    def calcular(self, express):
        if not express: return

        try:
            self.answer_text.text = str(eval(express))
        except Exception:
            self.answer_text.text = 'error'

    pass


    def calcular(self, express):
	    try:
		    self. answer_text.text = str( eval(express) )
	    except Exception:
		    self.answer_text.text = 'error'


#############################################################################

kivyfile = Builder.load_file('interfaz.kv')

class Calculator(App):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

    def build(self):
        return kivyfile

if __name__ == '__main__':
    Calculator().run()