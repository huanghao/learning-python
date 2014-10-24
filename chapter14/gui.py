import time
import tkinter as tk
from threading import Thread


def complex_computing():
    time.sleep(4)
    print('done')


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Submit"
        self.hi_there["command"] = self.say_hi
        self.hi_there["command"] = self.say_hi_blocking
        self.hi_there["command"] = self.say_hi_in_background
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def say_hi_blocking(self):
        complex_computing()
        print("It tasks me several seconds to say hi to everyone !")

    def say_hi_in_background(self):
        Thread(target=complex_computing).start()
        print("The complex operations had been put into background threading")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

