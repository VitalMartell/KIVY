from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (400,500)

class Container(BoxLayout):

    cut_speed = ObjectProperty()
    diam = ObjectProperty()
    lb_rpm = ObjectProperty()

    def calc(self):
        c_speed = float(self.cut_speed.text)
        dm = float(self.diam.text)
        rpm = 1000 * c_speed / 3.14 / dm
        self.lb_rpm.text = 'You need\n'+str(round(rpm))+'\nRPMs'


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
