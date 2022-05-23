
import pyqrcode
import tkinter as tk
from tkinter import*



LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


def generator():
    url = entry.get()
    qr = pyqrcode.create(url)
    save = qr.svg('myqrc.svg', scale=10)

#def dowland():
    



#---------gui

qrcode = tk.Tk()
qrcode.title("QR code Generator")
qrcode.configure(bg="#F5F5F5")
qrcode.geometry("380x663")
qrcode.resizable(0, 0)
qrcode.title("QRgeneratr")
qrcode.iconbitmap("myIcon.ico")


#-----------------
label = tk.Label(qrcode, text="Enter Url")
label.grid(row=7, column=0)

entry = tk.Entry(qrcode)
entry.grid(row=9, column=0)


b=Button(qrcode,padx=60,text="Generate", command=generator)
b.grid(row=11, column=0)


b2=Button(qrcode,text='dowland',padx=58)
b2.grid(row=12, column=0)





qrcode.mainloop()
