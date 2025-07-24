from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# Carrega o KV diretamente (evita erro de nome ou caminho)
Builder.load_file('validation_prop.kv')


class ValidatedInputWidget(BoxLayout):
    validated_text = StringProperty('Texto válido aparecerá aqui')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._last_valid_value = self.validated_text

    def on_validated_text(self, instance, value):
        # Verifica se tem pelo menos 5 letras e nenhum número
        if len(value) >= 5 and not any(char.isdigit() for char in value):
            self._last_valid_value = value
        else:
            self.validated_text = self._last_valid_value


class ValidationPropApp(App):
    def build(self):
        return ValidatedInputWidget()


if __name__ == '__main__':
    ValidationPropApp().run()