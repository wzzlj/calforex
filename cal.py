# encoding:utf-8

from Tkinter import *
import sys,time
import string

root = Tk()
root.geometry('600x30+400+400')

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg='white')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.balance()
        self.riskPercent()
        self.risk()
        self.gridWidgets()
  
    def gridWidgets(self):
        self.balanceLabel.grid(row=0, column=0)
        self.balanceEntry.grid(row=0, column=1)
        self.riskLabel.grid(row=0, column=2)
        self.riskEntry.grid(row=0, column=3)
        self.Percent.grid(row=0, column=4)
        self.riskmoneyLabel.grid(row=0, column=5)
        self.riskmoneyEntry.grid(row=0, column=6)

    def balance(self):
        self.balanceLabel = Label(self, text='总金额')
        self.balanceEntry = Entry(self, width=10)
        self.balanceEntry.bind("<Return>", self.calrisk)

    def riskPercent(self):
        self.riskLabel = Label(self, text='风险率')
        self.riskEntry = Entry(self, width=5)
        self.Percent = Label(self, text='%')
        self.riskEntry.bind("<Return>", self.calrisk)   

    def risk(self):
        self.riskmoneyLabel = Label(self, text='风险金')
        self.d = StringVar()
        self.riskmoneyEntry = Entry(self, textvariable=self.d, width=10)
        
    def calrisk(self,self2):
        try:
            self.a = float(self.balanceEntry.get())
            self.b = float(self.riskEntry.get())
            self.c = self.a * self.b /100
            self.d.set('%s' % self.c)
        except:
            print "error"

def main():

    app = Application(master = root)
    app.master.title('外汇市场头寸计算器')
    app.mainloop()

if __name__ == "__main__":
    main()
