import random

#attack,defence,koko,liha/kasvisyöjä,uros/naaras

def eläin():
    #jos speed on iso, ravinnontarve on suurempi (kuluttaa enemmän)
    speed = random.randint(1,10)
    #mitä pienempi energia, sitä nopeammin eläimeltä loppuu energia ja se kuolee
    energia = 100-speed*10
    #jos näköaisti on iso, näkee ravinnon ja muut eläimet kauempaa
    näköaisti = 10-speed
    
    eläin = [speed,lisääntymishalukkuus,näköaisti,sukupuoli]

    return eläin
    


def setup():
    grid = []
    for i in range(100):
        for j in range(100):
            try:
                grid[i].append(0)
            except:
                grid.append([0])
                
    animals = {}
    for i in range(10):
        animals["eläin"+str(i)] = eläin()


    food = []
    for i in range(80):
        for j in range(80)
        if random.randint(1,10) < 2:
            grid[i][j] = 1

    return animals,grid


animals,grid = setup()


while True:
    
