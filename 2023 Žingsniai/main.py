def skaiciuok(duomenys):
  # mokiniu skaicius kiek ivede
    informacija = [[], [], []]

    for duomuo in duomenys:
        klase = duomuo[0]
        ilgis_cm = duomuo[1]
        zingsniai = duomuo[2:]
        if 0 in zingsniai:
                continue
        x = 1
        if klase not in informacija[0]:
            informacija[0].append(klase)
            informacija[1].append(x)
        else:
            index = informacija[0].index(klase)
            informacija[1][index] += 1
             

    
    print(informacija)



def main():
    with open('U1.txt', 'r') as duomenu_failas:
        duomenys = [list(map(int, line.split())) for line in duomenu_failas.readlines()[1:]]

    
    skaiciuok(duomenys)



main()