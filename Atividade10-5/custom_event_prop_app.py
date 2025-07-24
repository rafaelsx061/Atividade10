from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class MyCustomWidget(BoxLayout):
    message = StringProperty('')  # propriedade message

    __events__ = ('on_message_changed',)  # declaração do evento personalizado

    # Método chamado sempre que a propriedade message mudar
    def on_message(self, instance, value):
        # dispara o evento personalizado passando o novo valor
        self.dispatch('on_message_changed', value)

    # Definição do evento personalizado (pode ser vazia, é só pra bind)
    def on_message_changed(self, value):
        pass


class CustomEventPropApp(App):
    def build(self):
        return MyCustomWidget()


if __name__ == '__main__':
    CustomEventPropApp().run()
