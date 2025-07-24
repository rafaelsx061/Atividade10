from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.lang import Builder

# Carrega o arquivo KV diretamente aqui (opcional, se preferir tudo junto)
Builder.load_file('ref_list_prop.kv')

# Widget que desenha e move o ponto
class MovableDot(Widget):
    pos_x = NumericProperty(100)
    pos_y = NumericProperty(100)
    dot_pos = ReferenceListProperty(pos_x, pos_y)

    def move_left(self):
        self.pos_x -= 10

    def move_right(self):
        self.pos_x += 10

    def move_up(self):
        self.pos_y += 10

    def move_down(self):
        self.pos_y -= 10

# Layout principal que inclui o dot e os botões
class MainLayout(BoxLayout):
    pass

class RefListApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    RefListApp().run()
