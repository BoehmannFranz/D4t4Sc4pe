from manim import Scene, Polygon, Text, ORIGIN, BLUE, smooth
import numpy as np
import pandas as pd

# Load DataFrame from CSV
df = pd.read_csv("AI Stock Model 1.csv")

class StockTrustBreath(Scene):
    def construct(self):
        num_layers = min(len(df), 14)
        labels = list(df.columns[2:7])
        center = ORIGIN

        # Parameter für Animation
        polygon_color = BLUE
        fill_opacity = 0.2  # 20% Transparenz
        stroke_width = 4
        duration = 1.5
        shrink_duration = duration * 2  # Schrumpfen dauert doppelt so lange

        winkel = np.linspace(0, 2 * np.pi, 6)[:-1]

        polygons = []
        for i in range(num_layers):
            abstaende = [df.iloc[i, 2+j] for j in range(5)]
            max_abstand = max(abstaende)
            scale_factor = 2.5 / max_abstand if max_abstand != 0 else 1.0
            ziel_ecken = [
                np.array([r * np.cos(w), r * np.sin(w), 0]) * scale_factor
                for r, w in zip(abstaende, winkel)
            ]
            polygons.append(ziel_ecken)

        # Labels für die Ecken (nur beim ersten Polygon)
        for i, label in enumerate(labels):
            pos = polygons[0][i]
            label_mob = Text(label, font_size=24).move_to(1.15 * pos)
            self.add(label_mob)

        # Animation: Herzschlag-artiges Ein- und Ausblenden der Polygone (nur Fläche, keine Linien)
        for i, ziel_ecken in enumerate(polygons):
            # Erzeuge ein Polygon, das von innen nach außen wächst
            start_poly = Polygon(*([center]*5), color=polygon_color, fill_opacity=fill_opacity, stroke_width=stroke_width)
            start_poly.set_fill(polygon_color, opacity=fill_opacity)
            start_poly.set_stroke(polygon_color, width=stroke_width)
            start_poly.set_opacity(1)
            self.add(start_poly)

            # Animation: Ecken wachsen nach außen
            self.play(
                start_poly.animate.set_points_as_corners(ziel_ecken + [ziel_ecken[0]]),
                run_time=duration,
                rate_func=smooth
            )

            self.wait(0.3)

            # Fläche schrumpft wieder zum Mittelpunkt, Transparenz bleibt konstant
            if i < num_layers - 1:
                self.play(
                    start_poly.animate.set_points_as_corners([center]*6),
                    run_time=shrink_duration,
                    rate_func=smooth
                )
                self.remove(start_poly)