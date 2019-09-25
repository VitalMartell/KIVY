from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 400)
Config.set('kivy','keyboard_mode','systemanddock')


class Container(Widget):
    bt1 = ObjectProperty()
    bt2 = ObjectProperty()
    bt3 = ObjectProperty()
    bt4 = ObjectProperty()
    bt5 = ObjectProperty()
    bt6 = ObjectProperty()
    bt7 = ObjectProperty()
    bt8 = ObjectProperty()
    bt9 = ObjectProperty()
    bt0 = ObjectProperty()
    btx = ObjectProperty()
    btd = ObjectProperty()
    btpl = ObjectProperty()
    btm = ObjectProperty()
    btc = ObjectProperty()
    btcom = ObjectProperty()
    bteq = ObjectProperty()
    txt_inp = ObjectProperty()

    def ch_txt(self,z):
        res = self.txt_inp.text
        if z == "+" or z == "-" or z == "*" or z == "/":
            if res.endswith('+') or res.endswith('-') or res.endswith('*') or res.endswith('/'):
                pass
            else:
                self.txt_inp.text += z
        else:
            self.txt_inp.text += z

    def eql(self):
        a = self.txt_inp.text
        self.txt_inp.text = str(eval(a))

    def clr(self):
        self.txt_inp.text = ""

class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
