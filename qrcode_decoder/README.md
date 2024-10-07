# Latenzerkennungs Script

## Überblick

Dieses Script wandelt Videos in Einzelbilder um, liest QR-Codes aus diesen Bildern und berechnet Zeitunterschiede, um die Video-Latenz zu ermitteln.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Dateistruktur

1. **main.py**: Steuert die Verarbeitung von Videos, die Umwandlung in Bilder und nutzt Funktionen aus anderen Skripten.
2. **summerize.py**: Berechnet Mittelwert und Standardabweichung der 'difference' Spalte aus einer CSV-Datei.
3. **helper.py**: Bietet Funktionen zum Löschen und Abrufen von Dateien in Ordnern.
4. **decode_single_image.py**: Entschlüsselt QR-Codes aus Bildern mithilfe der `pyzbar` und `PIL` Bibliotheken.

## Installation und Nutzung

- Legen Sie das Video im vorgesehenen Verzeichnis ab.
- Starten Sie den Prozess mit `main.py`. Es verarbeitet das Video und extrahiert QR-Code-Daten.
- Verwenden Sie `summerize.py` zur Berechnung von Durchschnittslatenz und Jitter.

## Hinweise

- Achten Sie auf die erforderliche Verzeichnisstruktur.
- Die korrekte Installation der Bibliotheken ist für die Funktion essentiell.

## Zweck

Das Framework bietet detaillierte Einblicke in die Latenz von Videos und unterstützt die Bewertung von Videotechnologien.
