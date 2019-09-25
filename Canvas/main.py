from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)
Config.write()

#Window.size = (800, 500)
#Config.set('kivy', 'keyboard_mode', 'systemanddock')



class Container(Widget):
    def points(self):
        point_list = [0, 0, 0, 50, -10, 60, -50, 60]
        x0 = self.zero_point()
        x0 = x0[0]
        y0 = self.zero_point()
        y0 = y0[1]
        for i in range(0, len(point_list), 2):
            point_list[i] += x0
        for i in range(1, len(point_list), 2):
            point_list[i] += y0
        return point_list

    def params(self):
        cnt = Window.width/2 - 400/2, Window.height/2-200/2, 400, 200
        return cnt

    def zero_point(self):
        x0 = Window.width/2
        y0 = Window.height/2
        xy0 = x0, y0, x0 + 0, x0 + 50
        return xy0


class CanvasApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    CanvasApp().run()
