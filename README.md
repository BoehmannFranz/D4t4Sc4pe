# Design- und Visualisierungsformen für komplexe Daten- und Informationsebenen  
**Teilprojekte:** Dotcloud, Stock Trusthelix, Stock Trustbreath  
**Projektleitung:** Franz Böhmann  

---

## 1. Einleitung  

Die wachsende Komplexität moderner Datensätze erfordert Visualisierungsansätze, die über lineare und zweidimensionale Darstellungen hinausgehen.  
Traditionelle Diagrammformen stoßen bei hochdimensionalen, dynamischen und relationalen Daten an Grenzen, da diese häufig mehrere Ebenen an Information gleichzeitig enthalten:  
- Zeitliche Dynamik  
- Mehrdimensionale Abhängigkeiten  
- Strukturelle Veränderungen  
- Kontextabhängige Interpretation  

Das vorliegende Forschungsprojekt untersucht neuartige **Designprinzipien und Visualisierungsformen**, die in der Lage sind, solche **mehrschichtigen Informationsstrukturen** gleichzeitig und intuitiv erfassbar zu machen.  

Der gewählte Anwendungsbereich – Aktienmarktdaten – dient als prototypisches Testfeld.  
Aktienmärkte sind ein Paradebeispiel für komplexe Systeme:  
- Sie spiegeln wirtschaftliche, politische und gesellschaftliche Strömungen wider.  
- Sie enthalten explizite Beziehungen (z. B. Branchentrends) und implizite Korrelationen (z. B. Marktpsychologie).  
- Sie bieten kontinuierliche Datenströme für Echtzeitvisualisierungen.  

Das Ziel ist die Entwicklung von Visualisierungen, die **nicht nur Informationen darstellen, sondern zugleich Strukturen, Dynamiken und Muster ästhetisch und interpretierbar inszenieren**.

---

## 2. Forschungsfokus  

Der zentrale Fokus dieser Forschung liegt auf dem **Visual-Design komplexer Datenstrukturen**.  
Dabei werden folgende Gestaltungsfragen untersucht:  

1. **Dimensionalität**  
   - Wie können mehr als drei Dimensionen gleichzeitig erfasst werden, ohne dass die Darstellung unübersichtlich wird?  
   - Welche Kombination aus Raum-, Farb-, Form- und Bewegungscodierung ist sinnvoll?  

2. **Zeitintegration**  
   - Wie lassen sich kontinuierliche Veränderungen in räumlichen Strukturen einbinden?  
   - Welche Darstellung macht Synchronität, Asynchronität und Phasenverschiebungen erkennbar?  

3. **Interaktionspotenzial**  
   - Wie können Visualisierungen interaktiv erweiterbar sein (Zoom, Filter, Layer-Management)?  
   - Welche Gestaltungsprinzipien unterstützen die explorative Datenanalyse?  

4. **Narrative Vermittlung**  
   - Wie können abstrakte Datenformen so gestaltet werden, dass sie auch narrative, kontextbasierte Interpretationen ermöglichen?  

---

## 3. Methodik  

### 3.1 Datenbeschaffung  
- **Quelle:** Mehrere internationale Aktien aus verschiedenen Branchen.  
- **Erhebung:** API-basierte Live-Abfragen in festgelegten Intervallen.  
- **Vorverarbeitung:**  
  - Speicherung in DataFrames (Pandas)  
  - Normalisierung der Zeitreihen  
  - Synchronisierung der Datensätze  

### 3.2 Experimenteller Ansatz  
Das Projekt verfolgt einen **Design-Science-Ansatz**:  
- Iteratives Prototyping unterschiedlicher Visualisierungsformen  
- Ästhetische, funktionale und kognitive Evaluierung der Darstellungen  
- Ziel: Entwurf einer modularen Visualisierungsarchitektur für hochkomplexe Daten  

### 3.3 Technische Werkzeuge  
- **Programmiersprache:** Python  
- **Bibliotheken:** Pandas, Manim, NumPy  
- **Rendering:** 3D-Animationen und dynamische Geometrien  
- **Geplante Erweiterung:** Echtzeitintegration in interaktive Dashboards

---

## 4. Teilprojekte  

### 4.1 Dotcloud – Punktwolken als Amplitudenlandschaften  
Visualisierung von Amplitudenverläufen als 3D-Punktwolken zur Erfassung zeitlicher Synchronität und Asynchronität.  

<video width="640" height="360" controls>
  <source src="./media/videos/DotCloud/480p15/DotCloud.mp4" type="video/mp4">
  Dein Browser unterstützt dieses Video-Format nicht.
</video>
**Ziel:**  


**Designprinzip:**  
- Verwendung von Punktwolken zur Darstellung zeitlicher Wellenmuster.  
- Farbkodierungen zur Hervorhebung potenzieller Abhängigkeiten zwischen Aktienwerten.  

**Besonderheit:**  
Die Punktwolke simuliert eine „interferierende Landschaft“, die in Echtzeit pulsiert und somit dynamische Korrelationen visuell erlebbar macht.

---

### 4.2 Stock Trusthelix – Helixstrukturen als Marktmodell  
**Ziel:**  
Darstellung der Marktbeziehungen in Form einer rotierenden, zeitlich erweiterten Helixstruktur.  

<video width="640" height="360" controls>
  <source src="./media/videos/Stock TrustHelix/480p15/Netzdiagramm.mp4" type="video/mp4">
</video>

**Designprinzip:**  
- Verbindung von Aktienwerten zu einer kontinuierlichen 3D-Röhre.  
- Verengungen/Erweiterungen symbolisieren Marktbewegungen:  
  - **Verengung:** Gleichzeitige Abwärtsbewegung vieler Werte.  
  - **Erweiterung:** Breiter, synchroner Anstieg.  
- Lokale Ausbuchtungen markieren Ausreißerentwicklungen einzelner Titel.  

**Interpretation:**  
Die Helix kann als „Marktpuls“ gelesen werden – sie zeigt implizite Vertrauens- und Misstrauensphasen.

---

### 4.3 Stock Trustbreath – Die organische Atmung des Marktes  
**Ziel:**  
Visualisierung zyklischer Marktbewegungen als „Atmung“ in einer dynamischen Netzstruktur.  
<video width="640" height="360" controls>
  <source src="./media/videos/StockTrustBreath/1080p60/StockTrustBreath.mp4" type="video/mp4">
  Dein Browser unterstützt dieses Video-Format nicht.
</video>

**Designprinzip:**  
- Darstellung fortlaufender Marktveränderungen zugunsten einzelner Akteure.  
- Integration zusätzlicher Dimensionen (z. B. Volumen, Sektorzugehörigkeit) in Form von Farbe oder Formänderung.  

**Interpretation:**  
Das Modell zielt auf eine intuitive Wahrnehmung der Marktspannung und -entspannung, ähnlich einer biologischen Rhythmik.

---

## 5. Wissenschaftlicher Beitrag  

Dieses Projekt leistet Beiträge in folgenden Bereichen:  

1. **Visual Analytics:**  
   Entwicklung neuer Darstellungsformen für mehrdimensionale und zeitabhängige Daten.  

2. **Informationsdesign:**  
   Untersuchung, wie ästhetische und funktionale Gestaltungsprinzipien zusammenwirken, um komplexe Daten interpretierbar zu machen.  

3. **Explorative Datenanalyse:**  
   Schaffung visueller Werkzeuge, die Muster, Anomalien und Korrelationen intuitiv erkennbar machen.  

---

## 6. Erwartete Ergebnisse und Ausblick  

- **Prototypen** für drei neuartige Visualisierungsformen (Punktwolken, Helixkörper, Atmungsnetz).  
- **Designrichtlinien** für Visualisierungen hochdimensionaler, zeitabhängiger Daten.  
- **Grundlagen** für eine Echtzeit-Visualisierungsplattform mit interaktiver Exploration.  

**Langfristige Vision:**  
Die erarbeiteten Visualisierungsformen sollen auf andere komplexe Systeme übertragbar sein, z. B.:  
- Klimadaten und Umweltmonitoring  
- Verkehrsströme in Smart Cities  
- Kommunikationsnetzwerke und soziale Dynamiken  

---

**Projektstatus:** Explorativ, laufende Prototypentwicklung  
**Technologien:** Python, Pandas, Manim, API-Datenquellen  
**Zeithorizont:** Iterative Entwicklung in mehreren Prototypzyklen  
