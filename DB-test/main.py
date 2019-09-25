import pyodbc

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 600)
#Config.set('kivy','keyboard_mode','systemanddock')

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\user\Desktop\DB-2017.accdb;')
cursor = conn.cursor()
cursor.execute('select username,password from users')


    
class Container(Widget):
    txt_input = ObjectProperty()

    def get_text(self):
        b = []
        i = 1
        c = ""
        rows = cursor.fetchall()
        for row in rows:
            #print (row.username)
            a = str(row.username + "\t\t"+ row.password)
            c += str(i) + "\t\t" +a + "\n"
            i += 1
        print(c)
            #b.append(a)
            #print (b)
        csr = conn.cursor()
        csr.close()
        conn.close()
        return c

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
