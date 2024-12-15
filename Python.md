# Was ist Python?

Python ist eine weit verbreitete, hochgradig lesbare und leicht zu erlernende Programmiersprache.
Sie wurde in den späten 1980er Jahren von Guido van Rossum entwickelt und 1991 veröffentlicht.
Python zeichnet sich durch eine klare und einfache Syntax aus, die es Programmierern ermöglicht,
ihren Code schnell zu schreiben und zu verstehen.


## Zentrale Merkmale

`Hohe Lesbarkeit`

Anstatt geschweifte Klammern für Blockstrukturen zu verwenden, nutzt Python Einrückungen
(Whitespace), was den Code besonders gut lesbar macht.

`Vielseitigkeit`

- Webentwicklung
- Datenanalyse
- künstliche Intelligenz
- maschinelles Lernen
- wissenschaftliches Rechnen
- Automatisierung
- Netzwerkprogrammierung

`Interaktive Sprache`

- Programmierung über eine Befehlszeile oder eine Entwicklungsumgebung (IDLE)

`Plattformübergreifend`

- läuft auf den meisten Betriebssystemen, ohne größere Anpassungen

## Erste Schritte

`Installation`

1. Ubuntu-Terminal öffnen

- in der Windows-Suchleiste nach "Ubuntu" suchen und starten

2. Paketliste aktualisieren

        sudo apt update

        sudo apt upgrade

3. Python installieren

        sudo apt install python3

4. Überprüfen

        python3

### Datentypen

`Numerischer`

- `int` (Ganzzahlen): Repräsentiert ganze Zahlen, sowohl positive als
auch negative.

         a = 10

         b = -5

- `float` (Fließkommazahlen): Repräsentiert Dezimalzahlen oder Zahlen
mit einer Bruchkomponente.

        pi = 3.14159

        temperature = -5.6

- `complex` (Komplexe Zahlen): Repräsentiert komplexe Zahlen der Form
a + bj, wobei a und b reale Zahlen sind und j die imaginäre Einheit ist.

        z = 2 + 3j

`Textualer`

- `str` (String): Repräsentiert eine Zeichenkette (Text). Strings können
in einfachen (') oder doppelten (") Anführungszeichen geschrieben werden.

        name = "Alice"

        greeting = 'Hallo'

        multiline = '''Dies ist ein mehrzeiliger String'''

`Sequenz`

- `list` (Liste): Eine geordnete Sammlung von Elementen, die veränderlich
(mutable) sind. Eine Liste kann verschiedene Datentypen enthalten.

        fruits = ["Apfel", "Banane", "Kirsche"]
        numbers = [1,2,3.5, "Zahl"]

- `tupel` (Tupel): Eine geordnete Sammlung von Elementen, die unveränderlich
(immutable) sind. Tupel können auch verschiedene Datentypen enthalten.

        coordinates = (10,20)

- `range` Ein spezieller Datentyp, der eine Sequenz von Zahlen erzeugt,
meist für Schleifen verwendet.

        r = range(5)    # Erstellt eine Sequenz: 0, 1, 2, 3, 4

`Mengen`

- `set` (Menge): Eine ungeordnete Sammlung von einzigartigen Elementen.
Sets sind veränderlich und können keine doppelten Werte enthalten.

        unique_number = {1, 2, 3, 4}

- `frozenset` Ein unveränderliches (immutable) Set.

        frozen_numbers = frozenset([1, 2, 3])

`Mapping`

- `dict` (Wörterbuch): Eine Sammlung von Schlüssel-Wert-Paaren.
Ein Wörterbuch ist ungeordnet und veränderlich.

        student = {"Name": "Stephan", "Alter": 36, "Weiterbildung": Cloud-Computing}

`Boolescher`

- `bool` (Boolescher Wert): Ein Datentyp, der nur zwei Werte annehmen kann:
True oder False.

        is_active = True

        is_done = False

`Binär`

- `bytes` Eine unveränderliche Sequenz von Bytes.

        byte_data = b"Hallo"

- `bytearray` Eine veränderliche Sequenz von Bytes.

        byte_array = bytearray([65, 66, 67])

- `memoryview` Ein speichereffizienter Datentyp, der es ermöglicht, auf
Teile von Daten in einem bytes- oder bytearray-Objekt zuzugreifen, ohne die
gesamte Datenstruktur zu kopieren.

        data = bytearray([1, 2, 3, 4])

        view = memoryview(data)

`None`

- `none` Ein spezieller Datentyp, der "keinen Wert" oder "Null" repräsentiert.
Häufig verwendet, um anzuzeigen, dass eine Variable keinen Wert hat oder eine
Funktion keinen Wert zurückgibt.

        nothing = None

Abrufen des Datentyps: `type()`

        print(type(10))         # <class 'int'>

        print(type("Hallo"))    # <class 'str'>

