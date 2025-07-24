from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.lang import Builder

Builder.load_file("nested_prop.kv")

class StatusIndicator(BoxLayout):
    is_active = BooleanProperty(False)

class MainControlWidget(BoxLayout):
    status_obj = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status_obj = StatusIndicator()
        self.add_widget(self.status_obj)

    def toggle_status(self):
        print("Botão pressionado! Toggle status.")
        self.status_obj.is_active = not self.status_obj.is_active

class NestedPropApp(App):
    def build(self):
        return MainControlWidget()

if __name__ == "__main__":
    NestedPropApp().run()
