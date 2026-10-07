# Pelaajan nimi ja ikä

nimi = input("Syötä nimi: ")

ikä = int(input("Syötä ikä: "))

print("Nimi: ", nimi + "\nIkä: ", ikä)

# Reppu, lista joka toimii inventaariona

Reppu = []

# funktiot, joissa peli toimii

def hakkuualue():
    print("-Näet maassa mudan seassa olevan vanhan repaleisen muistion-")
    print("1. Poimi muistio maasta ja vilkaise sen sisältöä")
    print("2. Jätä muistio maahan ja jatka matkaa")

    muistio = input("Mitä teet muistiolle?: ")

    if muistio == "1":
        print("--Poimit muistion maasta ja puhdistat sen mudasta")
        print("Avaat muistion ja repaleinen sivu tippuu välistä.\nPoimit sivun,jossa kerrotaan alueella olevan uhanalaista liito-oravaa.")
        print("Aivosi raksuttavat ja tajuat, että tämä on juuri se tieto mitä tarvitset.\nPäätät laittaa muistion reppuusi.")
        Reppu.append("Vanha Muistio")
    elif muistio == "2":
        print("Muistio on liian likainen etkä uskalla poimia sitä, jatkat matkaa")

def aloita_peli():
    print("-Sinulle on annettu tehtäväksi suojella hakattua metsää-.")

    print("--Saavut metsän reunalle ja näet kolme eri reittiä.")
    print("Vasemmalla näet reitin joka johtaa järvelle, oikealla on hakkuualue ja keskellä polku joka vie metsän sydämeen.")

    print("1. Menet tutkimaan hakkuualuetta")
    print("2. Päätät lähteä järvelle")
    print("3. Valitset polun")

    reitti = input("Päätä mitä teet: ")

    if reitti == "1":
        print("--Saavut hakkuualueelle ja edessäsi aukeaa avara näkymä")
        hakkuualue()
    elif reitti == "2":
        print("--Päätät lähteä järvelle ja rentoudut heti kun saavut perille")
    elif reitti == "3":
        print("--Astut metsän syvyyksiin ja synkkyys valtaa näkökenttäsi")

def ohjeet():
    print("---OHJEET---")
    print("- Pelin ideana on suojella hakattu metsä")
    print("- Etenet pelissä syöttämällä komentoja")

# Päävalikko

if ikä < 12:
    print("Olette liian nuori pelaamaan peliä")
else:
    print("Tervetuloa,", nimi)

    komento = ""

    while komento != "4":
        print("Kaadetun Metsän Mysteeri")
        print("1.Aloita peli")
        print("2.Jatka Peliä")
        print("3.Ohjeet")
        print("4.Sulje peli")

        komento = input("Syötä komento: ")

        if komento == "1":
            aloita_peli()
        elif komento == "3":
            ohjeet()

