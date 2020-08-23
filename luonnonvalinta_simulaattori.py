import random
import matplotlib.pyplot as plt

def eliö():
    #jos speed on iso, ravinnontarve on suurempi (kuluttaa enemmän)
    #speed = random.randint(1,9)
    speed = 5
    #mitä pienempi energia, sitä nopeammin eläimeltä loppuu energia ja se kuolee
    energia = energia_alotusarvo - speed*energia_kerroin
    
    eliö = [speed,energia]

    return eliö
    


def setup(koko):
    grid = []
    for i in range(koko):
        for j in range(koko):
            try:
                grid[i].append(0)
            except:
                grid.append([0])
                
    animals = {}
    for i in range(alkupopulaatio):
        animals["eliö"+str(i)] = eliö()


    for i in range(int(koko*0.8)):
        for j in range(int(koko*0.8)):
            if random.randint(1,10) < ruuan_määrä:
                grid[i][j] = 1

    return animals,grid

#alueen koko
koko = 100

##################################
päivä = 300 #päivän pituus
monta_päivää = 150 #monta päivää simuloidaan maksimissaan
alkupopulaatio = 100
energia_alotusarvo = 30
energia_kerroin = 2 #mitä isompi luku, sitä isompi vaikutus nopeudella on energiaan
ruuan_määrä = 3 #1-10, 1=10%, 10=100% kentästä on ruokaa
##################################

animals,grid = setup(koko)

#grid[y][x]
for xx in range(monta_päivää):
    for animal in animals:
        viime_ruoka = []
        valmis = False
        syöty = 0
        
        reuna = random.randint(1,4)
        paikka = random.randint(10,koko-10)
        #vasen
        if reuna == 1:
            x = 10
            y = paikka

        #ylä
        elif reuna == 2:
            x = paikka
            y = 10

        #oikea
        elif reuna == 3:
            x = koko-10
            y = paikka

        #ala
        elif reuna == 4:
            x = paikka
            y = koko-10
            
        #yksi episode (päivä)
        for t in range(päivä):
            for i in range(int(animals[animal][0])+int(animals[animal][1])):
                #arvotaan mihin suuntaan eliö kulkee (eliöiden liike satunnaista)
                suunta = random.randint(1,4)
                
                #vasen
                if suunta == 1 and koko > x-1 > 0:
                    x -= 1
                    if grid[y][x] == 1 and syöty < 2 and [y,x] != viime_ruoka:
                        syöty += 1
                        animals[animal].append([y,x])
                        viime_ruoka = [y,x]

                #oikea
                elif suunta == 2 and koko > x+1:
                    x += 1
                    if grid[y][x] == 1 and syöty < 2 and [y,x] != viime_ruoka:
                        syöty += 1
                        animals[animal].append([y,x])
                        viime_ruoka = [y,x]

                #ylös
                elif suunta == 3 and koko > y-1 > 0:
                    y -= 1
                    if grid[y][x] == 1 and syöty < 2 and [y,x] != viime_ruoka:
                        syöty += 1
                        animals[animal].append([y,x])
                        viime_ruoka = [y,x]

                #alas
                elif suunta == 4 and koko > y+1 > 0:
                    y += 1
                    if grid[y][x] == 1 and syöty < 2 and [y,x] != viime_ruoka:
                        syöty += 1
                        animals[animal].append([y,x])
                        viime_ruoka = [y,x]

                if syöty > 0 and (x==0 or x==koko-1 or y==0 or y==koko-1):
                    if syöty == 2:
                        animals[animal].append(2)
                    elif syöty == 1:
                        animals[animal].append(1)

                    valmis = True
                    break

            if valmis:
                break

            else:
                pass
        
        else:
            animals[animal] = animals[animal][:2]
                    

            

    #nopein syö ruuat
    #toimii kai
    testilista = []
    for animal in animals:
        testilista.append(animal)
        for other_animal in animals:
            if other_animal in testilista:
                pass
            else:
                if type(animals[animal][-1]) == int and len(animals[animal])>2:
                    if type(animals[other_animal][-1]) == int and len(animals[other_animal])>2:
                        if animals[animal][-2] == animals[other_animal][-2]:
                            if animals[animal][0] > animals[other_animal][0]:
                                animals[other_animal][-1] -= 1
                                animals[other_animal].remove(animals[other_animal][2])

                            else:
                                animals[animal][-1] -= 1
                                animals[animal].remove(animals[animal][2])

                        if animals[animal][-2] == animals[other_animal][-2]:
                            if type(animals[animal][-2]) == list:
                                if animals[animal][0] > animals[other_animal][0]:
                                    animals[other_animal][-1] -= 1
                                    animals[other_animal].remove(animals[other_animal][-2])

                                else:
                                    animals[animal][-1] -= 1
                                    animals[animal].remove(animals[animal][-2])



    #katsotaan mitkä eliöt ansaitsevat kuolla ja mitkä lisääntyä
    poistolista = []
    lisääntymislista = []
    for animal in animals:
        if len(animals[animal]) > 2:
            if animals[animal][-1] == 1:
                pass
            
            elif animals[animal][-1] == 2:
                lisääntymislista.append(animal)

            else:
                poistolista.append(animal)
                
        else:
            poistolista.append(animal)
    
    #tapetaan huonot eliöt
    for animal in poistolista:
        if animal in animals:
            animals.pop(animal,None)

    #lisäännytetään valioyksilöt ja pieni todennäköisyys mutaatiolle (10%)
    for animal in lisääntymislista:
        if animal in animals:
            animals[animal+"v"+str(xx)] = animals[animal]
            arpa = random.randint(1,20)
            if arpa < 18:
                animals[animal+"v"+str(xx)] = animals[animal]

            elif arpa == 19:
                if animals[animal][0] == 9:
                    animals[animal+"v"+str(xx)] = animals[animal]
                else:
                    animals[animal+"v"+str(xx)] = animals[animal]
                    animals[animal+"v"+str(xx)][0] += 1
                    animals[animal+"v"+str(xx)][1] = energia_alotusarvo - animals[animal+"v"+str(xx)][0]*energia_kerroin
                    
            elif arpa == 20:
                if animals[animal][0] == 1:
                    animals[animal+"v"+str(xx)] = animals[animal]
                else:
                    animals[animal+"v"+str(xx)] = animals[animal]
                    animals[animal+"v"+str(xx)][0] -= 1
                    animals[animal+"v"+str(xx)][1] = energia_alotusarvo - animals[animal+"v"+str(xx)][0]*energia_kerroin
                    


    #arvotaan uudet ruuat
    grid = []
    for i in range(koko):
        for j in range(koko):
            try:
                grid[i].append(0)
            except:
                grid.append([0])
                
    for i in range(int(koko*0.8)):
        for j in range(int(koko*0.8)):
            if random.randint(1,10) < ruuan_määrä:
                grid[i][j] = 1
                
    
    #tyhjennetään eliöiden vatsat
    for animal in animals:
        animals[animal] = animals[animal][:2]


    #tehdään lista eliöiden speed-statseista    
    listax = []
    for animal in animals:
        listax.append(animals[animal][0])

    plt.xlim([1,9]) #x-akselin arvot (plot x-akseli ei nyt muutu itsestään)
    plt.hist(listax,10)
    plt.title("Day: "+str(xx))
    plt.xlabel("Speed")
    plt.ylabel("Population size")
    plt.pause(0.05) #pakollinen jos haluaa käyttää plt.draw()
    plt.clf() #clearataan plot
    plt.draw() #plt.draw() piirtää vanhan plotin päälle


#tämä vielä kerran, jotta saadaan kaavio pysymään main loopin loputtua
listax = []
for animal in animals:
    listax.append(animals[animal][0])

plt.xlim([1,9])
plt.hist(listax,10)
plt.title("Day: "+str(xx))
plt.xlabel("Speed")
plt.ylabel("Population size")

plt.show()
