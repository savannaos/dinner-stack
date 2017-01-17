from Tkinter import *
from dinnerstack import DinnerStack

class Application(Frame):
    def savequit(self):
        self.ds.save('Jfile.txt')
        self.quit()

    def enterItem(self):
        text = self.e.get()
        if text:
            print("Adding "+ self.e.get())
            self.ds.pushItem(text)
        else:
            print("No text entered")

    def createWidgets(self):
        self.pop = Button(self)
        self.pop["text"] = "Pop"
        self.pop["fg"] = "blue"
        self.pop["command"] = self.ds.popItem
        self.pop.pack({"side": "left"})

        self.peak = Button(self)
        self.peak["text"] = "Peak"
        self.peak["fg"] = "red"
        self.peak["command"] = self.ds.peakItem
        self.peak.pack({"side": "left"})

        self.save = Button(self)
        self.save["text"] = "Save & Quit"
        self.save["fg"] = "purple"
        self.save["command"] = self.savequit
        self.save.pack({"side": "right"})

        self.push = Button(self)
        self.push["text"] = "Push"
        self.push["command"] = self.enterItem
        self.push.pack()

    def __init__(self, master=None):
        w = Label(master,text = "What's for Dinner?")
        w.pack()
        Frame.__init__(self,master)
        self.pack()
        self.e = Entry(master)
        self.e.pack()
        self.ds = DinnerStack('Jfile.txt')
        self.createWidgets()

root = Tk()
root.title("Dinner Plan")
app = Application(master=root)
app.mainloop()
