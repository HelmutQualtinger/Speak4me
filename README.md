# Speak4Me

`speak.py` ist ein Python-Skript, das es ermöglicht, Text aus einer Datei (`sentences.txt`) auszuwählen und mithilfe der Text-zu-Sprache-Funktion von macOS (`say`-Befehl) laut vorzulesen. Es bietet eine interaktive Benutzeroberfläche basierend auf `fzf`, um Texte schnell und effizient zu durchsuchen und auszuwählen. Neue Texte die nicht noch nicht gespeichert sind, werden automatisch übernommen. Man tippt schneller und einfacher und mit weniger Fehlern.
`speak.sh` ist ein äquivalentes `bash`-Skript, falls kein *Python* auf dem Rechner installiert ist. Ich beherrsche Bash nicht wirklich, daher habe ich das *Python*-Skript einfach automatisch übersetzen lassen, und es scheint zu funktionieren.*

## Anwendungsfall und Motivation

Meine Stimmbänder sind nach einer Operation stark beschädigt. Ich ermüde schnell beim Sprechen und bin schwer zu verstehen. Ich wollte eine einfache Möglichkeit haben, das, was ich tippe, laut aussprechen zu lassen. Ich bin nicht sehr schnell im Tippen, und die Kommunikation auf diese Weise ist sehr langsam. Ich möchte, dass die gesprochene Ausgabe nicht nur über die Lautsprecher abgespielt wird, sondern auch an ein virtuelles Mikrofon weitergeleitet wird, damit ich sie in Telefonie-Apps und Videokonferenzprogrammen verwenden kann. Auf diese Weise kann ich tippen, aber andere Teilnehmer hören gesprochene Worte. Auch längere wiederkehrende Phrasen kann ich mit wenigen Anschlägen erreichen ohne Tastenkürzel auswendig lernen zu müssen. Ich muss nur ein paar Buchstaben oder Wörter tippen und er findet eine Auswahl von Texten aus der ich mit den Pfeiltasten wählen kann.

Die Text-zu-Sprache-Funktion von macOS in den Bedienungshilfen ist zwar brauchbar, aber es ist nicht einfach, schnell durch eine große Anzahl vorgefertigter Texte zu suchen, und man muss zwischen Maus und Tastatur wechseln. Deshalb nutze ich das leistungsstarke `fzf`. Mit wenigen Tastenanschlägen kann man die Sätze schnell eingrenzen, ohne sich Tastenkombinationen merken zu müssen. Es funktioniert ein bisschen wie Textvorhersage – nicht ganz, aber fast wie künstliche Intelligenz. Die letzten fünf Eingaben werden oben in der Liste angezeigt, um sie schnell wiederholen zu können und als Erinnerung daran, was gerade gesagt wurde, falls die andere Partei es nicht verstanden hat.

Je länger man das Programm nutzt, desto mehr Texte lernt das System, und desto effizienter wird es. Die Texte werden dauerhaft in einer Datei gespeichert.

## Funktionen

- **Textauswahl mit `fzf`**: Das Skript verwendet `fzf`, ein leistungsstarkes Fuzzy-Suchtool, um Texte aus der Datei `sentences.txt` oder einer Liste kürzlich gesprochener Sätze auszuwählen.
- **Text-zu-Sprache**: Der ausgewählte Text wird mithilfe der Text-zu-Sprache-Funktion von macOS (`say`-Befehl) laut vorgelesen.
- **Geschwindigkeitseinstellungen**: Die Sprechgeschwindigkeit kann mit bestimmten Befehlen angepasst werden:
  - `computer sprich langsam`: Setzt die Geschwindigkeit auf langsam (50).
  - `computer sprich normal`: Setzt die Geschwindigkeit auf normal (180).
  - `computer sprich schnell`: Setzt die Geschwindigkeit auf schnell (200).
- **Stimmenwechsel**: Durch Eingabe eines Befehls wie `auf Markus umschalten` kann die Stimme geändert werden, sofern die Stimme verfügbar ist. Das ist vorallem notwendig wenn man in mehreren Sprachen kommuniziert, mit geeigneten Stimmen für Sprachen. Mit dem Befehl `say -v \?` sieht man welche Sprachen und Stimmen auf diesem Mac verfügbar sind. Mit Systemeinstellung->Sprachausgabe  kann man weitere Stimmen von Apple installieren
- **Verlauf gesprochener Sätze**: Das Skript speichert die letzten 10 gesprochenen Sätze, ganz oben auf der Liste, sodass man sie bei Bedarf mit den Pfeiltasten schnell wiederholen kann.
- **Automatische Duplikats-Entfernung**: Doppelte Einträge in der Datei `sentences.txt` werden automatisch entfernt.

## Anforderungen

- **Betriebssystem**: macOS (da das Skript den `say`-Befehl verwendet).
- **Python-Version**: Python 3.x.
- **Zusätzliche Tools**:
  - `fzf` muss installiert sein. Es kann über Homebrew installiert werden:
  
    ```bash
    brew install fzf
    ```

## Installation

1. Klonen Sie das Repository oder kopieren Sie die Datei `speak.py` in ein Verzeichnis.
2. Stellen Sie sicher, dass die Datei `sentences.txt` existiert. Falls nicht, wird sie automatisch erstellt.
3. Installieren Sie `fzf`, falls es noch nicht installiert ist.

## Verwendung

1. Starten Sie das Skript:
  
   ```bash
   python3 speak.py
   ```
