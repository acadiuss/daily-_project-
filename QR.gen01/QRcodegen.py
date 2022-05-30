

import pyqrcode
import tkinter as tk




def generator():
    url = E.get()
    qr = pyqrcode.create(url)
    save = qr.svg('kodQR.svg', scale=10)
    



QR = tk.Tk()
QR.title("GENERATOR KODU QR")
QR.geometry("100x80")
QR.configure(bg="red")
QR.iconbitmap("myIcon.ico")
QR.title("GENERATOR KODU QR") 


L = tk.Label(QR, text="Wprowadź TEKST")
L.grid(row=2, column=4)


E = tk.Entry(QR)
E.grid(row=4, column=4)

B1 = tk.Button(QR, text="Generate", command=generator)
B1.grid(row=6, column=4)



QR.mainloop()