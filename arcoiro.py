# -*- coding: utf-8 -*-
import sys

print ("manda as menina desenha haha i")
flag_b = False
while flag_b == False:
    b = raw_input("")
    if b == "desenha um arco iro":
        flag_b = True
        print ("nao moises, voce tem que mandar elas desenha, descreva")
        flag_c = False
        while flag_c == False:
            c = raw_input("")
            if c == "desenha uma raqueta do guda":
                flag_c = False
                print ("Nao, mas voce nao pde dizer isso, tem que descrever")
                flag_d = False
                while flag_d == False:
                    d = raw_input("")
                    if d == "desenha aquilo que vcs sabe oq eh":
                        flag_d = True
                        print ("nao consegue nao eh moises")
                        sys.exit(0)
                    else:
                        print ("01. que triste, voce nao conhece o meme :(")
            else:
                print ("02. que triste, voce nao conhece o meme :(")
    else:
        print ("03. que triste, voce nao conhece o meme :(")
