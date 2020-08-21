import random

#attack,defence,koko,liha/kasvisyöjä,uros/naaras

def eläin():
    #jos speed on iso, ravinnontarve on suurempi (kuluttaa enemmän)
    speed = random.randint(1,9)
    #mitä pienempi energia, sitä nopeammin eläimeltä loppuu energia ja se kuolee
    energia = 100-speed*10
    #jos näköaisti on iso, näkee ravinnon ja muut eläimet kauempaa
    #näköaisti = 10-speed
    
    eläin = [speed,energia]

    return eläin
    


def setup(koko):
    grid = []
    for i in range(koko):
        for j in range(koko):
            try:
                grid[i].append(0)
            except:
                grid.append([0])
                
    animals = {}
    for i in range(100):
        animals["eläin"+str(i)] = eläin()


    for i in range(int(koko*0.8)):
        for j in range(int(koko*0.8)):
            if random.randint(1,10) < 3:
                grid[i][j] = 1

    return animals,grid

koko = 100
päivä = 720

animals,grid = setup(koko)

#grid[y][x]
for xx in range(5):
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
            #print(animals[animal])

            #animals[animal][0] = nopeus
            for i in range(int(animals[animal][0])):
                
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
                    

            

    #miinustaa kaikista nyt FIXAA
    testilista = []
    for animal in animals:
        testilista.append(animal)
        if animal in testilista:
            pass
        else:
            for other_animal in animals:
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
    
    #tapetaan eläimet
    for animal in poistolista:
        if animal in animals:
            animals.pop(animal,None)

    #lisäännytetään valioyksilöt
    for animal in lisääntymislista:
        if animal in animals:
            animals[animal+"v"+str(xx)] = animals[animal]

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
            if random.randint(1,20) == 1:
                grid[i][j] = 1
                
    
    #tyhjennetään eläinten vatsat
    for animal in animals:
        animals[animal] = animals[animal][:2]

    print(len(animals))
    
##for animal in animals:
##    print(animals[animal])
