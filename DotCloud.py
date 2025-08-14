from manim import ThreeDScene, Dot3D, VGroup, UpdateFromAlphaFunc, DEGREES, BLUE, linear
import numpy as np
import pandas as pd

# Daten aus der CSV laden
df = pd.read_csv("AI Stock Model 1.csv")

class DotCloud(ThreeDScene):
    def construct(self):
        # Kamera: schräge Vogelperspektive
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        num_aktien = 5  # Anzahl der Aktien pro Zeile
        num_layers = min(len(df), 14)
        center = np.array([0, 0, 0])

        # Fläche für die Punktwolke (XY-Ebene)
        grid_size = 16  # Feinere Fläche für flüssige Animation
        x_vals = np.linspace(-6, 6, grid_size)
        y_vals = np.linspace(-6, 6, grid_size)

        # Die Punkte werden einmal erzeugt und dann animiert
        dots = []
        for x in x_vals:
            for y in y_vals:
                punkt_pos = np.array([x, y, 0])
                dot = Dot3D(punkt_pos, radius=0.05, color=BLUE)
                dot.set_opacity(0.5)
                self.add(dot)
                dots.append(dot)

        # Die Wellenzentren (Aktien) sind auf einem Kreis verteilt
        winkel = np.linspace(0, 2 * np.pi, num_aktien, endpoint=False)
        wellen_mitte = [np.array([5 * np.cos(w), 5 * np.sin(w)]) for w in winkel]

        # Animation: Die Amplituden schlagen dynamisch wie ein Puls
        def update_dots(mob, alpha):
            # alpha: 0 ... 1 (Animationsfortschritt)
            # Wir interpolieren zwischen Zeile i und i+1 für flüssige Bewegung
            t = alpha * (num_layers - 1)
            i = int(np.floor(t))
            frac = t - i
            if i >= num_layers - 1:
                i = num_layers - 2
                frac = 1.0
            abstaende1 = [df.iloc[i, 2+j] for j in range(num_aktien)]
            abstaende2 = [df.iloc[i+1, 2+j] for j in range(num_aktien)]
            abstaende = [(1-frac)*a1 + frac*a2 for a1, a2 in zip(abstaende1, abstaende2)]
            max_abstand = max(abstaende)
            scale_factor = 2.5 / max_abstand if max_abstand != 0 else 1.0

            idx = 0
            for x in x_vals:
                for y in y_vals:
                    z_sum = 0
                    for j in range(num_aktien):
                        dx, dy = x - wellen_mitte[j][0], y - wellen_mitte[j][1]
                        r2 = dx**2 + dy**2
                        amp = abstaende[j] * scale_factor
                        # Überlagerung von 6 Gaußwellen pro Aktie
                        for k in range(1, 7):
                            amp_k = amp / k
                            z_sum += amp_k * np.exp(-r2 / (0.5 * k))
                    dots[idx].move_to([x, y, z_sum])
                    idx += 1

        # Animation: Die Fläche pulsiert und die Wellen interferieren sichtbar
        self.play(UpdateFromAlphaFunc(VGroup(*dots), update_dots), run_time=10, rate_func=linear)
        self.wait(2)