import tkinter as tk
from tkinter import Canvas, Radiobutton

class RysowanieAplikacja:
    def __init__(self, okno_glowne):
        self.okno_glowne = okno_glowne
        self.okno_glowne.title("Aplikacja do rysowania")

        self.canvas = Canvas(okno_glowne, width=400, height=400)
        self.canvas.pack(side=tk.RIGHT)

        self.frame_lewy = tk.Frame(okno_glowne, width=150)
        self.frame_lewy.pack(side=tk.LEFT, fill=tk.Y)

        self.przycisk_start = tk.Button(self.frame_lewy, text="Start", command=self.rozpocznij_rysowanie)
        self.przycisk_start.pack()

        self.przycisk_poczatek = tk.Button(self.frame_lewy, text="Początek", command=self.dodaj_poczatek)
        self.przycisk_poczatek.pack()

        self.przycisk_meta = tk.Button(self.frame_lewy, text="Meta", command=self.dodaj_meta)
        self.przycisk_meta.pack()

        self.wybor_algorytmu = tk.StringVar()
        self.wybor_algorytmu.set("Dijkstra")

        self.rozwijalny_wybor_algorytmu = tk.OptionMenu(self.frame_lewy, self.wybor_algorytmu, "Dijkstra", "Bellman-Ford", "BFS", "DFS")
        self.rozwijalny_wybor_algorytmu.pack()

        self.czy_rysowanie = False
        self.czy_dodawanie_poczatku = False
        self.czy_dodawanie_meta = False

    def rozpocznij_rysowanie(self):
        self.czy_rysowanie = not self.czy_rysowanie
        if self.czy_rysowanie:
            self.przycisk_start.config(text="Stop")
            self.canvas.bind("<Button-1>", self.rysuj)
        else:
            self.przycisk_start.config(text="Start")
            self.canvas.unbind("<Button-1>")

    def dodaj_poczatek(self):
        self.czy_dodawanie_poczatku = True

    def dodaj_meta(self):
        self.czy_dodawanie_meta = True

    def rysuj(self, event):
        if self.czy_rysowanie:
            x, y = event.x, event.y
            wybrany_algorytm = self.wybor_algorytmu.get()
            if self.czy_dodawanie_poczatku:
                self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill="green")
                self.czy_dodawanie_poczatku = False
            elif self.czy_dodawanie_meta:
                self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill="red")
                self.czy_dodawanie_meta = False
            else:
                # Tutaj możesz dodać kod do rysowania zgodnie z wybranym algorytmem.

if __name__ == "__main__":
    root = tk.Tk()
    app = RysowanieAplikacja(root)
    root.mainloop()
