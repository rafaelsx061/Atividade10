from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation

# Carrega o arquivo KV
Builder.load_file('animation_prop.kv')


class AnimatedBox(BoxLayout):
    box_size = NumericProperty(100)  # Tamanho inicial

    def toggle_animation(self):
        # Se for 100, anima para 200. Se for 200, volta pra 100.
        new_size = 200 if self.box_size == 100 else 100
        anim = Animation(box_size=new_size, duration=0.5)
        anim.start(self)


class AnimationPropApp(App):
    def build(self):
        return AnimatedBox()


if __name__ == '__main__':
    AnimationPropApp().run()
