from kivy.app import App                       # Importa a classe base da aplicação
from kivy.uix.boxlayout import BoxLayout       # Usamos BoxLayout para organizar os widgets
from kivy.properties import DictProperty       # DictProperty permite armazenar dicionários reativos

class UserProfileWidget(BoxLayout):
    # Criamos uma propriedade chamada user_data com dados do usuário
    user_data = DictProperty({'name': 'João', 'age': 30, 'city': 'São Paulo'})

    def update_age(self):
        # Esse método é chamado quando o botão for clicado
        # Ele pega o valor atual de 'age' e soma +1
        self.user_data['age'] += 1

class DictPropApp(App):
    def build(self):
        # Retorna a interface principal da aplicação
        return UserProfileWidget()

# Executa o app
if __name__ == '__main__':
    DictPropApp().run()
