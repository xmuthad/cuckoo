from Tkinter import *
import itchat
class Application(Frame):
    def login_chat(self):
        itchat.auto_login()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Login",
        self.hi_there["command"] = self.login_chat

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("cuckoo")
root.geometry('309x500')
app = Application(master=root)

app.mainloop()
root.destroy()