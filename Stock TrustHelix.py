from manim import ThreeDScene, Line, VGroup, VMobject, Dot, Text, Polygon, YELLOW, BLUE, RED, ORANGE, UP, ORIGIN, Rotate, PI, DEGREES, linear
import numpy as np
import pandas as pd

# Load DataFrame from CSV
df = pd.read_csv("AI Stock Model 1.csv")

class Netzdiagramm(ThreeDScene):
    def construct(self):
        # Kamera so setzen, dass die Zeitachse als Y-Achse im Bild erscheint (phi=0°, theta=0°)
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)

        num_layers = min(len(df), 14)
        y_min, y_max = -3, 3
        y_positions = np.linspace(y_min, y_max, num_layers)  # Von unten (y_min) nach oben (y_max)
        labels = list(df.columns[2:7])

        # Zeitachse (Y-Achse) mittig im Bild, von unten nach oben
        achse = Line(np.array([0, y_min, 0]), np.array([0, y_max, 0]), color=YELLOW, stroke_width=6)
        self.add(achse)

        alle_ecken = []
        flaechen = VGroup()

        # Polygone sofort alle anzeigen
        for i, y in enumerate(y_positions):
            center = np.array([0, y, 0])
            a, b, c, d, e = df.iloc[i, 2:7]
            abstaende = [a, b, c, d, e]
            winkel = np.linspace(0, 2 * np.pi, 6)[:-1]
            max_abstand = max(abstaende)
            scale_factor = 2.0 / max_abstand if max_abstand != 0 else 1.0
            ecken = [np.array([r * np.cos(w), 0, r * np.sin(w)]) * scale_factor for r, w in zip(abstaende, winkel)]
            ecken_verschoben = [ecke + center for ecke in ecken]
            alle_ecken.append(ecken_verschoben)

            # Polygon und Mittelpunkt
            netz = VMobject(color=BLUE, stroke_width=4)
            netz.set_points_as_corners(ecken_verschoben + [ecken_verschoben[0]])
            self.add(netz)
            self.add(Dot(center, color=RED, radius=0.06))

            # Labels nur für das erste Polygon
            if i == 0:
                for ecke, label in zip(ecken_verschoben, labels):
                    label_mob = Text(label, font_size=24).move_to(1.15 * (ecke - center) + center)
                    self.add(label_mob)

        # Verbindungslinien zwischen gleichen Ecken (gleiche Spalte)
        linien = VGroup()
        for ecken_index in range(5):
            punkte = [alle_ecken[layer][ecken_index] for layer in range(num_layers)]
            linie = VMobject(color=ORANGE, stroke_width=2)
            linie.set_points_as_corners(punkte)
            linien.add(linie)
        self.add(linien)

        # Transparente Flächen zwischen den Polygonebenen erzeugen
        for i in range(num_layers - 1):
            for j in range(5):
                # Jeweils zwei benachbarte Ecken verbinden (zwischen Ebene i und i+1)
                p1 = alle_ecken[i][j]
                p2 = alle_ecken[i][(j + 1) % 5]
                p3 = alle_ecken[i + 1][(j + 1) % 5]
                p4 = alle_ecken[i + 1][j]
                flaeche = Polygon(
                    p1, p2, p3, p4,
                    color=BLUE, fill_opacity=0.15, stroke_opacity=0.0
                )
                flaechen.add(flaeche)
        self.add(flaechen)

        # Animation: Zeitachse und alles darum 20x um sich selbst drehen, aber doppelt so langsam (120 Sekunden)
        alles = VGroup(achse, *self.mobjects)
        self.play(Rotate(alles, angle=40*PI, axis=UP, about_point=ORIGIN), run_time=120, rate_func=linear)
        self.wait(1)


