from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.button = Button(text='Click me!', on_press=self.on_button_click)
        return self.button

    def on_button_click(self, instance):
        if instance.text == 'Click me!':
            instance.text = 'Button clicked!'
        else:
            instance.text = 'Click me!'

if __name__ == '__main__':
    MyApp().run()
