import random

def lotto():
    rng = random.Random()
    bingo = list(range(1000,10000))
    continuar = True
    while continuar:
        rng.shuffle(bingo)
        sorteado = bingo[0]
        serase = list(str(sorteado))
        somado = int(serase[0])+int(serase[1])+int(serase[2])+int(serase[3])
        if somado == 20:
            print(somado)
            continuar = False
        else:
            print (sorteado)


lotto()


