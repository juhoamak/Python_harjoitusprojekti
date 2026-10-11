# Importit

import random

from pelaaja import Pelaaja

# Pelaajan nimi ja ikä

nimi = input("Syötä nimi: ")

ikä = int(input("Syötä ikä: "))

print("Nimi: ", nimi + "\nIkä: ", ikä)

pelaaja1 = Pelaaja(nimi, ikä)


# Funktiot, joissa peli toimii

def kaupunki():
    print("--Juokset kylmissäsi synkän metsän läpi kaupunkiin--")
    print("Kaupungissa yrität todistaa virkavallalle, miksi hakkuu on laiton")
    print()
    print("** Noppaa heittämällä saat selville, uskotaanko sinua **")
    print("(Sinulla on paremmat todennäköisyydet onnistua todistamisessa, jos sinulta löytyy todisteita)")

    noppa = random.randint(1, 6)

    print("Heität noppaa...")
    input("Paina Enter nähdäksesi lopputuloksen...")
    print(f"Noppa näyttää lukua {noppa}!")

    if "Vanha Muistio" in pelaaja1.reppu and noppa >= 3:
        print("** Onnistut todistamaan laittomuuden ja hakkuut määrätään lopetettavaksi **")
        print()
        print("** VOITIT PELIN **")

    elif noppa >= 5:
        print("** Kerrot hakkuualueen kauheuksista ja poliisi lähetetään tutkimaan asiaa **")
        print()
        print("-- Voitit pelin, mutta joudut vankilaan kahdeksi vuodeksi työkoneen varastamisesta...")

    else:
        print("** Virkavalta ei usko sinua vaan syyttää sinua työkoneen varastamisesta ja taposta **")
        print()
        print("Sinut tuomitaan sähkötuoliin")
        print("Tuomio pannaan heti täytäntöön ja kuolet")
        print()
        print("**HÄVISIT PELIN**")


def tyokone():
    print("--Saavut työkoneelle\n** Ukkonen Jyrähtää **")
    print('Pelästyt ukkosta, mutta rauhoitut nopeasti\nSamaan aikaan mies huutaa kaukaa: "Olette laittomasti täällä"')
    print("Kuulet moottorisahan käynnistyvän ja juoksuaskelia")
    print()
    print("1. Lähde juoksemaan suoraan eteenpäin pakoon")
    print("2. Jähmety pelosta paikoillesi ja odota mitä tapahtuu")
    print("0. Tallenna ja poistu")

    uhkaavamies = input("Mitä teet: ")

    if uhkaavamies == "1":
        print()
        print("Lähdet juoksemaan ja pääset juuri ja juuri pakoon, mutta eksyt synkkään metsään")
        pelaaja1.pelin_vaihe = kaupunki
        kaupunki()

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
    
    elif uhkaavamies == "0":
        tallenna_peli()
        return


def hakkuualue():
    print("-Näet maassa mudan seassa olevan vanhan repaleisen muistion-")
    print()
    print("1. Poimi muistio maasta ja vilkaise sen sisältöä")
    print("2. Jätä muistio maahan ja jatka matkaa")
    print("0. Tallenna ja poistu")

    muistio = input("Mitä teet muistiolle?: ")

    if muistio == "1":
        print("--Poimit muistion maasta ja puhdistat sen mudasta")
        print("Avaat muistion ja repaleinen sivu tippuu välistä.\nPoimit sivun, jossa kerrotaan alueella olevan uhanalaista liito-oravaa.")
        print("Aivosi raksuttavat ja tajuat, että tämä on juuri se tieto mitä tarvitset.\nPäätät laittaa muistion reppuusi.")

        pelaaja1.reppu.append("Vanha Muistio")

        print("Lähdet synkälle metsäpolulle aikeissasi tuoda muistio julkisuuteen.")
        pelaaja1.pelin_vaihe = "kaupunki"
        kaupunki()

    elif muistio == "2":
        print("Muistio on liian likainen etkä uskalla poimia sitä, jatkat matkaa")
        print("Näet työkoneen jäljet ja lähdet seuraamaan niitä")
        pelaaja1.pelin_vaihe = "tyokone"
        tyokone()

    elif muistio == "0":
        tallenna_peli()
        return


def ranta():
    print("--Rentoutuessa auringon laskun aikaan unohdat mitä sinun piti tehdä ja jäät rannalle.")
    print()
    print("-- Hävisit pelin! --")


def aloita_peli():
    print("-Sinulle on annettu tehtäväksi suojella hakattua metsää-.")

    print("--Saavut metsän reunalle ja näet kolme eri reittiä.")
    print("Vasemmalla näet reitin, joka johtaa järvelle, oikealla on hakkuualue ja keskellä polku, joka vie metsän sydämeen.")
    print()
    print("1. Menet tutkimaan hakkuualuetta")
    print("2. Päätät lähteä järvelle")

    reitti = input("Päätä mitä teet: ")

    if reitti == "1":
        print("--Saavut hakkuualueelle ja edessäsi aukeaa avara näkymä")
        pelaaja1.pelin_vaihe = "hakkuualue"
        hakkuualue()

    elif reitti == "2":
        print("--Päätät lähteä järvelle ja rentoudut heti kun saavut perille")
        ranta()

# Ohjeet funktio

def ohjeet():
    print("---OHJEET---")
    print()
    print("- Pelin ideana on suojella hakattua metsää")
    print("- Etenet pelissä syöttämällä komentoja")
    print("- Jos löydät vihjeitä ja otat ne mukaan, sinulla on parempi todennäköisyys voittaa lopussa")

# Tallennus

def tallenna_peli():
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja1.nimi + "\n")
        tiedosto.write(str(pelaaja1.ikä) + "\n")
        tiedosto.write(",".join(pelaaja1.reppu) + "\n")
        tiedosto.write(pelaaja1.pelin_vaihe + "\n")

    print("Peli tallennettu!")

# Lataus

def lataa_peli():
    try:
        with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:
            nimi = tiedosto.readline().strip()
            ika = int(tiedosto.readline().strip())
            reppu = tiedosto.readline().strip()
            pelin_vaihe = tiedosto.readline().strip()
            pelaaja1.nimi = nimi
            pelaaja1.ikä = ika
            pelaaja1.reppu = reppu.split(",")
            pelaaja1.pelin_vaihe = pelin_vaihe
        print("Peli ladattu!")

    except FileNotFoundError:
        print("Tallennusta ei löytynyt...")

# Päävalikko

if ikä < 12:
    print("Olette liian nuori pelaamaan peliä")

else:
    print("Tervetuloa,", nimi)

    komento = ""

    while komento != "4":
        print("--Kaadetun Metsän Mysteeri--")
        print()
        print("1. Aloita peli")
        print("2. Jatka peliä")
        print("3. Ohjeet")
        print("4. Sulje peli")

        komento = input("Syötä komento: ")

        if komento == "1":
            aloita_peli()

        elif komento == "2":
            lataa_peli()    
            if pelaaja1.pelin_vaihe == "hakkuualue":
                hakkuualue()
            elif pelaaja1.pelin_vaihe == "kaupunki":
                kaupunki()
            elif pelaaja1.pelin_vaihe == "tyokone":
                tyokone()

        elif komento == "3":
            ohjeet()
