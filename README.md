# Speak4Me

`speak.py` ist ein Python-Skript, das es ermöglicht, Text aus einer Datei (`sentences.txt`) auszuwählen und diesen mithilfe der macOS-Sprachausgabe (`say`-Befehl) vorzulesen. Es bietet eine interaktive Benutzeroberfläche, die auf `fzf` basiert, um Texte schnell und effizient zu durchsuchen und auszuwählen.

## Funktionen

- **Textauswahl mit `fzf`**: Das Skript verwendet `fzf`, ein leistungsstarkes Tool für fuzzy-Suche, um Texte aus der Datei `sentences.txt` oder aus einer Liste der zuletzt gesprochenen Sätze auszuwählen.
- **Sprachausgabe**: Der ausgewählte Text wird mit der macOS-Sprachausgabe (`say`-Befehl) vorgelesen.
- **Geschwindigkeitseinstellungen**: Die Sprechgeschwindigkeit kann durch spezielle Befehle angepasst werden:
  - `computer sprich langsam`: Setzt die Geschwindigkeit auf langsam (50).
  - `computer sprich normal`: Setzt die Geschwindigkeit auf normal (180).
  - `computer sprich schnell`: Setzt die Geschwindigkeit auf schnell (200).
- **Stimmenwechsel**: Durch Eingabe eines Befehls wie `auf Markus umschalten` kann die Stimme gewechselt werden, sofern die Stimme verfügbar ist.
- **Verlauf der gesprochenen Sätze**: Das Skript speichert die letzten fünf gesprochenen Sätze, die bei der nächsten Auswahl priorisiert angezeigt werden.
- **Automatische Duplikatentfernung**: Doppelte Einträge in der Datei `sentences.txt` werden automatisch entfernt.

## Voraussetzungen

- **Betriebssystem**: macOS (da das Skript den `say`-Befehl verwendet).
- **Python-Version**: Python 3.x.
- **Zusätzliche Tools**: 
  - `fzf` muss installiert sein. Es kann über Homebrew installiert werden:
    ```bash
    brew install fzf
    ```

## Installation

1. Klone das Repository oder kopiere die Datei `speak.py` in ein Verzeichnis.
2. Stelle sicher, dass die Datei `sentences.txt` existiert. Falls nicht, wird sie automatisch erstellt.
3. Installiere `fzf`, falls es noch nicht installiert ist.

## Verwendung

1. Starte das Skript:
   ```bash
   python3 speak.py