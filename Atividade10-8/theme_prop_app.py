from kivy.app import App
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.boxlayout import BoxLayout

# Carrega o arquivo KV
Builder.load_file('theme_prop.kv')


class RootWidget(BoxLayout):
    pass


class ThemedApp(App):
    # Definindo tema inicial
    app_theme = DictProperty({
        'primary': [0.2, 0.6, 0.8, 1],      # azul
        'secondary': [0.9, 0.9, 0.9, 1]     # cinza claro
    })

    def build(self):
        return RootWidget()

    def toggle_theme(self):
        # Alterna entre dois temas
        if self.app_theme['primary'] == [0.2, 0.6, 0.8, 1]:  # azul
            self.app_theme = {
                'primary': [0.8, 0.3, 0.3, 1],     # vermelho
                'secondary': [1, 1, 0.8, 1]        # amarelo claro
            }
        else:
            self.app_theme = {
                'primary': [0.2, 0.6, 0.8, 1],     # azul
                'secondary': [0.9, 0.9, 0.9, 1]    # cinza claro
            }


if __name__ == '__main__':
    ThemedApp().run()
