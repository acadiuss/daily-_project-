import tkinter as tk
from tkinter import Canvas, Frame, Button, StringVar, OptionMenu, LEFT
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RysowanieAplikacja:
    def __init__(self, okno_glowne):
        self.okno_glowne = okno_glowne
        self.okno_glowne.title("Aplikacja do rysowania")

        self.frame_lewy = Frame(okno_glowne, width=150)
        self.frame_lewy.pack(side=LEFT, fill=tk.Y)

        self.przycisk_start = Button(self.frame_lewy, text="Start", command=self.rozpocznij_rysowanie)
        self.przycisk_start.pack()

        self.przycisk_dodaj_czerwony_punkt = Button(self.frame_lewy, text="Dodaj czerwony punkt", command=self.rozpocznij_dodawanie_czerwonego_punktu)
        self.przycisk_dodaj_czerwony_punkt.pack()

        self.przycisk_dodaj_zielony_punkt = Button(self.frame_lewy, text="Dodaj zielony punkt", command=self.rozpocznij_dodawanie_zielonego_punktu)
        self.przycisk_dodaj_zielony_punkt.pack()

        self.przycisk_znajdz_droge = Button(self.frame_lewy, text="Znajdź najkrótszą drogę", command=self.znajdz_najkrotsza_droge)
        self.przycisk_znajdz_droge.pack()

        self.wybor_algorytmu = StringVar()
        self.wybor_algorytmu.set("Dijkstra")

        self.rozwijalny_wybor_algorytmu = OptionMenu(self.frame_lewy, self.wybor_algorytmu, "Dijkstra", "Bellman-Ford", "BFS", "DFS")
        self.rozwijalny_wybor_algorytmu.pack()

        self.czy_rysowanie = False
        self.czy_dodawanie_punktu = False
        self.czy_dodawanie_czerwonego_punktu = False
        self.czy_dodawanie_zielonego_punktu = False
        self.punkty = []  # Lista przechowująca punkty na wykresie
        self.punkty_czerwone = []  # Lista przechowująca czerwone punkty na wykresie
        self.punkty_zielone = []  # Lista przechowująca zielone punkty na wykresie

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=okno_glowne)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        

    def rozpocznij_rysowanie(self):
        self.czy_rysowanie = not self.czy_rysowanie
        if self.czy_rysowanie:
            self.przycisk_start.config(text="Stop")
            self.canvas.mpl_connect("button_press_event", self.dodaj_punkt)
        else:
            self.przycisk_start.config(text="Start")
            self.canvas.mpl_disconnect("button_press_event")

    def rozpocznij_dodawanie_czerwonego_punktu(self):
        self.czy_dodawanie_czerwonego_punktu = True

    def rozpocznij_dodawanie_zielonego_punktu(self):
        self.czy_dodawanie_zielonego_punktu = True

    def dodaj_punkt(self, event):
        if self.czy_dodawanie_punktu:
            x = event.xdata
            y = event.ydata
            self.ax.plot(x, y, 'ro')
            self.punkty.append((x, y))  # Dodawanie punktu do listy punktów
            self.canvas.draw()

        if self.czy_dodawanie_czerwonego_punktu:
            x = event.xdata
            y = event.ydata
            self.ax.plot(x, y, 'ro', color="red")
            self.punkty_czerwone.append((x, y))  # Dodawanie czerwonego punktu do listy punktów
            self.canvas.draw()

        if self.czy_dodawanie_zielonego_punktu:
            x = event.xdata
            y = event.ydata
            self.ax.plot(x, y, 'ro', color="green")
            self.punkty_zielone.append((x, y))  # Dodawanie zielonego punktu do listy punktów
            self.canvas.draw()
def znajdz_najkrotsza_droge(self):
    if not self.punkty:
        return

    # Podziel punkty na zielone i czerwone
    green_points = [punkt for punkt in self.punkty if punkt[2] == "zielony"]
    red_points = [punkt for punkt in self.punkty if punkt[2] == "czerwony"]

    # Jeśli brakuje punktów jednego koloru, zwróć
    if not green_points or not red_points:
        return

    G = nx.Graph()

    # Dodaj zielone punkty jako wierzchołki
    for i, (x, y, kolor) in enumerate(green_points):
        G.add_node(i, pos=(x, y))

    # Dodaj czerwone punkty jako wierzchołki
    for i, (x, y, kolor) in enumerate(red_points):
        G.add_node(len(green_points) + i, pos=(x, y))

    # Dodaj krawędzie między punktami z różnych kategorii
    for i, (x1, y1, kolor1) in enumerate(green_points):
        for j, (x2, y2, kolor2) in enumerate(red_points):
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            G.add_edge(i, len(green_points) + j, weight=dist)

    # Znajdź najkrótszą ścieżkę
    try:
        shortest_path = nx.shortest_path(G, source=0, target=len(self.punkty) - 1, weight="weight")
    except nx.NetworkXNoPath:
        return

    shortest_path_points = [G.nodes[i]["pos"] for i in shortest_path]

    # Rysuj najkrótszą ścieżkę na wykresie
    x, y = zip(*shortest_path_points)
    self.ax.plot(x, y, marker="o", linestyle="-", color="blue")

    self.canvas.draw()


    def znajdz_najkrotsza_trase(self):
        if self.punkty and self.wybor_algorytmu.get() == "Dijkstra":
            G = nx.Graph()
            for i in range(len(self.punkty)):
                G.add_node(i, pos=self.punkty[i])
            for i in range(len(self.punkty)):
                for j in range(i + 1, len(self.punkty)):
                    dist = ((self.punkty[i][0] - self.punkty[j][0]) ** 2 + (self.punkty[i][1] - self.punkty[j][1]) ** 2) ** 0.5
                    G.add_edge(i, j, weight=dist)

            shortest_path = nx.shortest_path(G, source=0, target=len(self.punkty) - 1, weight="weight")
            shortest_path_points = [self.punkty[i] for i in shortest_path]

            # Rysowanie najkrótszej ścieżki na wykresie
            x, y = zip

            # Rysowanie najkrótszej ścieżki na wykresie
            x, y = zip(*shortest_path_points)
            self.ax.plot(x, y, marker="o", linestyle="-", color="green")

            self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = RysowanieAplikacja(root)
    root.mainloop()
