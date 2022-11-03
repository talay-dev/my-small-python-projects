from tkinter import *

class pencere:
    def __init__(self, master):
        self.master = master
        master.title("Faktöriyel Hesaplayıcı")
        master.geometry("210x120+500+250")

        self.entry = Entry(master,width=20)
        self.entry.place(x=10,y=10)
        self.sonuc = 0
        self.label = Label(master,text=self.sonuc )
        self.label.place(x=120,y=40)
        self.buton1 = Button(master, text=" Hesapla ", command = self.fakt).place(x=10,y=40)
        self.buton2 = Button(master, text="   Çıkış   " , command = master.quit).place(x=10,y=70)

    def fakt(self):
        f = int(self.entry.get())
        a = 1
        b = 1
        while a <f:
            a += 1
            b *= a

        self.label.config(text=b )


root = Tk()
my_gui = pencere(root)
root.mainloop()





