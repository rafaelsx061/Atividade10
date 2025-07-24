from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.event import EventDispatcher
from kivy.properties import StringProperty

class GlobalState(EventDispatcher):
    current_status = StringProperty("Inicial")

class StatusDisplayWidget(BoxLayout):
    pass

class StatusChangerWidget(BoxLayout):
    def change_status(self, text):
        App.get_running_app().global_state.current_status = text

class RootWidget(BoxLayout):
    pass

class EventCommApp(App):
    global_state = GlobalState()

    def build(self):
        Builder.load_file("event_comm.kv")
        return RootWidget()

if __name__ == "__main__":
    EventCommApp().run()
