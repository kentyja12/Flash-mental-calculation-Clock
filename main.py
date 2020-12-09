import tkinter as tk
import threading
import datetime
import time

import time_math #オリジナル

class window_time:
    def __init__(self):
        #Labelオブジェクトの配置
        self.root = tk.Tk()
        self.time_changer = time_math.math_change()

        self.label = tk.Label(self.root)
        self.label["font"] = ("Arial",50)
        self.label["bg"] = "black"
        self.label["fg"] = "white"
        self.root.title("数学時計")
        self.root.minsize(width=1000, height=80)
        self.root.maxsize(width=1000, height=80)
        self.label.grid(column=0,row=0)

    #Labelオブジェクトのtext属性を1秒ごとに更新
    def changeLabelText(self):
        while True:
            dt_now = datetime.datetime.now()
            try:
                changed_time = self.time_changer.changeNumber_math(dt_now.hour)+":"+self.time_changer.changeNumber_math(dt_now.minute)+":"+self.time_changer.changeNumber_math(dt_now.second)
            except TypeError:
                pass
            self.label["text"] = changed_time
            time.sleep(1)
            

time_math = window_time()
thread = threading.Thread(target=time_math.changeLabelText)
thread.start()
time_math.root.mainloop()
