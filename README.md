# Speak4Me

`speak.py` ist ein Python-Skript, das es ermöglicht, Text aus einer Datei (`sentences.txt`) auszuwählen und diesen mithilfe der macOS-Sprachausgabe (`say`-Befehl) vorzulesen. Es bietet eine interaktive Benutzeroberfläche, die auf `fzf` basiert, um Texte schnell und effizient zu durchsuchen und auszuwählen.

## Use case und Motivation:

Meine Stimmbänder sind nach einer Operation schwer geschädigt. Ich ermüde schnell beim Reden und man versteht mich schlecht. Ich wollte eine einfache Möglichkeit, das was ich tippe sprechen zu lassen. Ich bin nicht sehr gut beim Tippen und die Kommunikation auf diese Weise geht sehr langsam. Ich möchte das gesprochene nicht nur auf dem Lautsprecher ausgeben sondern auch an ein virtuelles Mikrofon weiterleiten, damit ich ich es in Telefonie Apps und Videokonferenz Programmen verwenden kann, so dass ich tippen kann, aber die anderen Teilnehmer sprechen.

Die Sprachausgabe auf dem Mac in den Bedienungshilfen ist zwar ganz o.k. aber es ist nicht leicht eine grosse Zahl vorgefertigter Texte rasch zu durchsuchen, und man muss zwischen Maus und Tastatur wechseln. Ich verwende deshalb das mächtige fzf. Ein paar Tastentipps schränken sehr rasch die Sätze ein, ohne dass man sich Tastenkombinationen merken muss. Funktioniert in etwa wie die Textvorhersage. Nicht ganz aber fast künstliche Intelligenz. Die letzten fünf Eingaben werden am Kopf der Liste gezeigt um sie rasch wiederholen zu können und als Erinnerung was man gerade gesagt hat, wenn die Gegenseite nicht verstanden hat.

Je länger man das Programm verwendet umso mehr Texte lernt das System und umso effizienter wir man. Die Texte werden permanent in einer Datei gespeichert.

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