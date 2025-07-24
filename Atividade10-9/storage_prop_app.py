import json
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

# Caminho do arquivo de armazenamento
STORAGE_FILE = 'counter_data.json'

Builder.load_file('storage_prop.kv')


class PersistentCounter(BoxLayout):
    count = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_count()

    def load_count(self):
        if os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, 'r') as f:
                data = json.load(f)
                self.count = data.get('count', 0)

    def save_count(self):
        with open(STORAGE_FILE, 'w') as f:
            json.dump({'count': self.count}, f)

    def increment(self):
        self.count += 1


class StoragePropApp(App):
    def build(self):
        self.root_widget = PersistentCounter()
        return self.root_widget

    def on_stop(self):
        # Salva o contador ao fechar o app
        self.root_widget.save_count()


if __name__ == '__main__':
    StoragePropApp().run()
