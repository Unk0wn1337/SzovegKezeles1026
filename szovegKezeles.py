def szovegKezeles():
    szoveg: str = "Szép nap van!"
    # Szöveg első karaktere
    print(szoveg[0])
    # ird ki a szöveg masodik karakteret
    print(szoveg[1])
    # Ird ki a szoveg hosszát
    print("A hossz:", len(szoveg))
    # Szöveg utolsó karaktere
    print("Utolsó karatere", szoveg[len(szoveg) - 1])

    # Ird ki a szöveg karaktereit egymás alá betünként
    index: int = 0
    while index < len(szoveg):
        print(szoveg[index])
        index += 1


def kettoSzovegKezeles():
    szoveg: str = "Ez egy teszt szöveg."
    print(szoveg)
    print(szoveg.upper())
    # 1 Van -e a szövegben teszt szöveg
    # 2 A szoveg változóban hol szerepel elöszőr s betű
    # 3 Alakítsd át minden szó kezdőbetűjét nagybetűvel
    # 4 Cseréld ki a teszt szót proba-ra

    # 1
    testTalalat = szoveg.find("teszt")
    if testTalalat == szoveg.find("teszt"):
        print("Van benne ")
    else:
        print("Nincsen benne")
    # 2
    print(szoveg.index("s"), " .helyen szerepel s betű")
    # 3
    print(szoveg.title())
    # 4
    print(szoveg.replace("teszt", "próba"))


def szovegVisszaFele(szoveg: str):
    # Paraméterben visszaadva kapott szöveg visszafelé kiirva egymás mellé
    print(szoveg[::-1])


def aBetukSzama(szoveg: str):
    # Hány a karakter van a szövegben
    print("'a' betűk száma:", szoveg.count("a"))
