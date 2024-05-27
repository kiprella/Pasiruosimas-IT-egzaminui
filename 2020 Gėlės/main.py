def main ():
    with open('U1.txt', 'r') as duomenu_failas:
        duomenys = [list(map(int, line.split())) for line in duomenu_failas.readlines()[0:]]

    informacija = [[], []]
    j = 0
    x =1
    while j < 92:
        informacija[1].append(x)
        x =x+1
        j = j+1

    for duomo in duomenys:
        
        pradzia_men = duomo[1]
        pradzia_dien = duomo[2]
        pabaiga_men = duomo[3]
        pabaiga_dien = duomo[4]
        if pradzia_men == 6:
            while z < 
        print(pradzia_men, pradzia_dien, pabaiga_men, pabaiga_dien)

main()
