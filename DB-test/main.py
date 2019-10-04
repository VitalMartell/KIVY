import pyodbc

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'height', 600)
#Config.set('kivy','keyboard_mode','systemanddock')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SSBSERVER\TAS;'
                      'Database=TAS;'
                      'uid=user;pwd=user;')

#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, #*.accdb)};DBQ=C:\Users\user\Desktop\DB-2017.accdb;')

cursor = conn.cursor()
cursor.execute('select compid , barcodeid from TMS.TAS_COMPMORE')
#cursor.execute('select username,password from users')


    
class Container(Widget):
    txt_input = ObjectProperty()

    def get_text(self):
        i = 1
        c = ""
        rows = cursor.fetchall()
        #print(rows)
        for row in rows:
            try:
                if row.barcodeid is None:
                    barcode = "0"
                else:
                    barcode = row.barcodeid
                a = str(row.compid + "\t\t"+ barcode)
                c += str(i) + "\t\t" + a  + "\n"
                i += 1
                #print(c)
            except:
                c = "ERROR"
        csr = conn.cursor()
        csr.close()
        conn.close()
        return c

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
