import random

# Pelaajan nimi ja ikä

nimi = input("Syötä nimi: ")

ikä = int(input("Syötä ikä: "))

print("Nimi: ", nimi + "\nIkä: ", ikä)

# Reppu, lista joka toimii inventaariona

Reppu = []

# funktiot, joissa peli toimii
def synkka_metsa():
    

def tyokone():
    print("--Saavut työkoneelle\n** Ukkonen Jyrähtää **")
    print('Pelästyt ukkosta, mutta rauhoitut nopeasti\nSamaan aikaan mies huutaa kaukaa: "Olette laittomasti täällä"')
    print("Kuulet moottorisahan käynnistyvän ja juoksuaskelia")
    print()
    uhkaavamies = input("Mitä teet?")
    print("1. Lähde juoksemaan suoraan eteenpäin pakoon")
    print("2. Jähmety pelosta paikoillesi ja odota mitä tapahtuu")

    if uhkaavamies == "1":
        print()
        print("Lähdet juoksemaan ja pääset juuri ja juuri pakoon, mutta eksyt synkkään metsään")
        synkka_metsa()
    elif uhkaavamies == "2":
        print()
        print("Joudut taisteluun pelottavan miehen kanssa!")
        print("Heitä noppaa, numero 6 voittaa")
        noppa = random.randint(1, 6)
        if noppa == 6:
            print()
            print("Voitit taistelun!")
            print("Varastat työkoneen ja lähdet pois metsästä")
            print("Kaupungissa kerrot tapahtumista ja hakkuut päätetään lopettaa")
            print()
            print("!! Löysit salaisen lopun, Olet voittaja!!")
        else:
            print()
            print("Hävisit taistelun ja menehdyit hakkuuaukiolle")
            print()
            print("**Hävisit pelin...**")


def hakkuualue():
    print("-Näet maassa mudan seassa olevan vanhan repaleisen muistion-")
    print()
    print("1. Poimi muistio maasta ja vilkaise sen sisältöä")
    print("2. Jätä muistio maahan ja jatka matkaa")

    muistio = input("Mitä teet muistiolle?: ")

    if muistio == "1":
        print("--Poimit muistion maasta ja puhdistat sen mudasta")
        print("Avaat muistion ja repaleinen sivu tippuu välistä.\nPoimit sivun,jossa kerrotaan alueella olevan uhanalaista liito-oravaa.")
        print("Aivosi raksuttavat ja tajuat, että tämä on juuri se tieto mitä tarvitset.\nPäätät laittaa muistion reppuusi.")
        Reppu.append("Vanha Muistio")
        print("Lähdet synkälle metsäpolulle aikeissasi tuoda muistio julkisuuteen.")
    elif muistio == "2":
        print("Muistio on liian likainen etkä uskalla poimia sitä, jatkat matkaa")
        print("Näet työkoneen jäljet ja lähdet seuraamaan niitä")
        tyokone()

def ranta():
    print("--Rentoutuessa auringon laskun aikaan unohdat mitä sinun piti tehdä ja jäät rannalle.")
    print()
    print("-- Hävisit pelin! --")

def aloita_peli():
    print("-Sinulle on annettu tehtäväksi suojella hakattua metsää-.")

    print("--Saavut metsän reunalle ja näet kolme eri reittiä.")
    print("Vasemmalla näet reitin joka johtaa järvelle, oikealla on hakkuualue ja keskellä polku joka vie metsän sydämeen.")
    print()
    print("1. Menet tutkimaan hakkuualuetta")
    print("2. Päätät lähteä järvelle")
    
    reitti = input("Päätä mitä teet: ")

    if reitti == "1":
        print("--Saavut hakkuualueelle ja edessäsi aukeaa avara näkymä")
        hakkuualue()
    elif reitti == "2":
        print("--Päätät lähteä järvelle ja rentoudut heti kun saavut perille")
        ranta()

def ohjeet():
    print("---OHJEET---")
    print()
    print("- Pelin ideana on suojella hakattu metsä")
    print("- Etenet pelissä syöttämällä komentoja")

# Päävalikko

if ikä < 12:
    print("Olette liian nuori pelaamaan peliä")
else:
    print("Tervetuloa,", nimi)

    komento = ""

    while komento != "4":
        print("--Kaadetun Metsän Mysteeri--")
        print()
        print("1.Aloita peli")
        print("2.Jatka Peliä")
        print("3.Ohjeet")
        print("4.Sulje peli")

        komento = input("Syötä komento: ")

        if komento == "1":
            aloita_peli()
        elif komento == "3":
            ohjeet()

