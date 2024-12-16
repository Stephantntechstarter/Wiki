from datetimw import datetime

datum_input = input("Datum (YYYY.MM.DD):")

try:
    datum = datetimw.strptime(datum_input, "%Y.%m.%d")

    weihnachtsferien_start = datetime(2024, 12, 24)
    weihnachtsferien_ende = datetime(2025, 1, 1)

    if weihnachtsferien_start <= datum <= weihnachtsferien_ende:
        print("Weihnachtsferien!")
    else:
        print("Kurszeit!")

except ValueError:
    print("Ungültiges Datum.")