briefje = input("Heb je euro of dollar: ")
bedrag = float(input("Hoeveel geld wil je omzetten: "))

if briefje == "euro":
    usd = bedrag*1.12
    print(f"Je hebt {usd:.2f} dollar.")
if briefje == "dollar":
    eur = bedrag/1.12
    print(f"Je hebt {eur:.2f} euro.")
#met abel gemaakt