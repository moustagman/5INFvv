voornaam = input("Wat is je naam: ")
achternaam = input("Wat is je achternaam: ")
titel = input("Wat is je titel: ")
naam = (f"{voornaam} {achternaam}").upper()

if titel.__len__() > naam.__len__():
    naamlengte = titel.__len__() + 2
if titel.__len__() < naam.__len__():
    naamlengte = naam.__len__() + 2
if titel.__len__() == naam.__len__():
    naamlengte = naam.__len__() + 2


print(f"+{"-" *naamlengte}+")
print(f"|{naam.center(naamlengte)}|")
print(f"|{titel.center(naamlengte)}|")
print(f"+{"-" *naamlengte}+")
#met abel gemaakt