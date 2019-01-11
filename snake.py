"""
snakegame.py by simon nguyen
"""

import random

delta = {"rechts": (1,0),
         "links" : (-1,0),
         "oben"  : (0,-1),
         "unten" : (0,1)} 
    


#spielfeld 40x20
lines = []
line = "."*40

#Spielfeld in Variable lines
for z in range(20):
    lines.append(list(line))

#snake definieren
head = "D"
body = "o"
pos = [[10,10]]
teile = 1
richtung = "rechts"
futter = (random.randint(0,39), random.randint(0,19))
while True:

    #----Grafik anzeigen----
    for y , line in enumerate(lines):
        for x , char in enumerate(line):
            for nr, (sx, sy) in enumerate (pos):
                if y == sy and x == sx:
                    if nr == 0:
                        print(head,end = "")
                        break
                    else:
                        print(body,end = "")
                        break
            else:
                # keine schlange 
                if futter[0] == x and futter[1] == y:
                   print("@", end="")
                else:
                   print(char,end = "")
        print()
        
    #Bewegung
    dx, dy = 0, 0
    command = input(">>>")
    if command =="a" and richtung != "rechts":
        richtung = "links"
        #pos[0][0] -= 1
    if command =="d" and richtung != "links" :
        richtung = "rechts"
        #pos[0][0] += 1
    if command =="w" and richtung != "unten" :
        richtung = "oben"
        #pos[0][1] -= 1
    if command =="s" and richtung != "oben"  :
        richtung = "unten"
        #pos[0][1] += 1
    # futter essen
    if pos[0][0]==futter[0] and pos[0][1] == futter[1]:
        #pos.append((futter[0], futter[1]))
        teile += 1    
    # richtung auswerten
    dx, dy = delta[richtung]
    # schlange   bewegen
    #for teil in teile:
        
    for  t in range(teile):
       pos[t][0] += dx
       pos[t][1] += dy
    
