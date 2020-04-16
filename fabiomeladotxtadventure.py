#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time


print ("Pe. Fabio Melado Fake Text Adventure\ninspirado pelas maravilhas do Zap moderno\ndigite amem para comecar")
inicio = False
while inicio == False:
    iniciar = raw_input ("")
    if iniciar.lower() == "amem":
        inicio = True
inicio = False
opcaoa = False
opcaob = False
opcaoc = False
while inicio == False:
    print ("Hoje vamos aprender a escrever como o Pe. Fabio Melado\ne assim emocionar a todos com a sua sensibilidade\nno grupo da familia do zap") 
    print ("O primeiro passo eh escolher um dos temas abaixo")
    print ("A) Moralidade das Pessoas \nB) Mensagem de um Deus vingativo \nC)Livramento de uma tragedia")
    opcao1 = raw_input("")
    if opcao1.lower() == "a":
        print ("A primeira licao eh deixar claro o quanto as pessoas sao ruins")
        print ("Para isso voce deve reprovar atitudes completamente\n normais e que todos praticam")
        print ("que tipo de comportamento normal deve ser recriminado?")
        moralidade = raw_input("")
        print ("ok... interessante")
        time.sleep(1)
        print ("processando...")
        time.sleep(2)
        print ("Agora eh preciso fazer um juizo de valor. Escolha um adjetivo para esses pecaodres e depravados")
        adjetivo1 =  raw_input("")
        time.sleep(1)
        print ("processando...")
        time.sleep(2)
        print ("Para finalizar, nos diga o que falta a estas pessoas " + adjetivo1)
        falta1 = raw_input("")
        time.sleep(1)
        print ("processando...")
        time.sleep(2)
        print ("vejamos o Pe. Fabio Melado que habita em voce:")
        print ("")
        time.sleep(2)
        print ("")
        print ("O MELHOR TEXTO QUE LI EM MUUITO TEMPO \napenas repassando")
        print ("Cansado e perplexo com tantas baboseiras e falsas justificativas\npras atrocidades que ainda nos surpreendem todos os dias...")
        print ("As pessoas que " + moralidade + ", nao o fazem por conta do governo\nou porque jogam jogos " + adjetivo1 + ". nao meu amigos...")
        print ("Elas vivem assim porque falta " + falta1 + " e entao eles " + moralidade + " na cara da sua familia.")
        print ("precisamos parar de nos omitir e de nos " + moralidade + ", porque cada vez mais as familias estao desestruturadas\ne" + adjetivo1)
        print ("A " + moralidade +" eh o desdobramento de carencias afetivas e da necessidade de ser " + adjetivo1 +" ainda que da pior maneira")
        print ("ASSINADO PADRE FABIO MELADO")
        print ("")
        time.sleep(6)
        opcaoa = True
        if opcaoa == True and opcaob == True and opcaoc == True:
            inicio = False
        print ("Quer aprender mais? y/n")
        reiniciar = raw_input("")
        if reiniciar.lower() == "y":
            inicio = False
            opcaoa = True
        else:
            sys.exit(0)    
    if opcao1.lower() == "b":
        print ("Esta claro que Deus esta muito chateado com geral e fara algo a respeito")
        print ("para se expressar como o Pe. Fabio Melado voce alertar sobre as punicoes vindouras \nalem eh claro, dos punidos")
        print ("Primeiro nos diga que tipo de punicao caira sobre nos")
        punicao = raw_input("")
        print ("Agora nos diga quem ja sofreu as consequencias")
        punir = raw_input("")
        print ("Nossa...")
        time.sleep(1)
        print ("eu nao sabia que isso tinha acontecido...")
        time.sleep(1)
        print ("Eu preciso que voce me ajude e diga o que esta alma fez pra merecer tal coisa")
        crime = raw_input("")
        print ("processando as informacoes...")
        time.sleep(1)
        print ("so mais um pouco...")
        time.sleep(2)
        print ("nao eh todos os dias que estamos inspirados... \ntenha paciencia e nao toque em nada ate que eu peca")
        time.sleep(3)
        print ("ok.... Now we have it")
        time.sleep(2)
        print ("")
        print ("CUIDADO COM O QUE FAZES, IRMAO")
        print ("MUITOS HOJE EM DIA SAO AQUELES QUE ZOMBAM DA BOA VONTADE DO SENHOR")
        print ("MAS POUCOS SAO OS QUE SABEM QUE " + punicao.upper() + " OS AGUARDA.")
        print ("EU CONHECIA A " + punir.upper() + " E AMAVA, COMO TODOS NOS DEVEMOS AMAR O PROXIMO,")
        print ("MAS AS VEZES ESSE PROXIMO NAO AMA A DEUS E PECA, E PECA COMO MEUS QUERIDOS?")
        print ("DESAFIANDO ATRAVES DE " + crime.upper() + " DE FORMA QUE O UNICO RESULTADO EH " + punicao.upper())
        print ("EU LEMBRO DAQUELA NOITE DAQUELA FATIDICA NOITE DE VERAO, QUANDO ME CHEGOU A NOTICIA DE QUE")
        print (punir.upper() + " ESTAVA " + crime.upper() + " QUASE AO MEU LADO E FORA DO ALCANCE DO SENHOR")
        print ("MAS SE O SENHOR EH EDUCADO E NAO CHEGA PERTO DESSAS PESSOAS... SUA JUSTICA NUNCA FALHA E SEMPRE CHEGA")
        print ("E ENQUANTO " + punir.upper() +" " + crime.upper() + " OLHANDO PARA O CEU EM DEBOCHE")
        print ("SUA " + punicao.upper() + " SE PROFETIZAVA")
        print ("POR ISSO OS DIGO, MUITO CUIDADO, MUITO CUIDADO COM O QUE FAZEM\nMEUS AMIGOS E AMIGAS DE TODOS OS GRUPOS DO ZAP")
        print (" ")
        print ("BOM DIA")
        print ("")
        print ("ASSINADO PASTOR FABIO MELADO EM MEMORIA DA ALMA DE " + punir.upper())
        print ("")
        time.sleep(6)
        opcaob = True
        if opcaoa == True and opcaob == True and opcaoc == True:
            inicio = False
        print ("Quer aprender mais? y/n")
        reiniciar = raw_input("")
        if reiniciar.lower() == "y":
            inicio = False
    if opcao1.lower() == "c":
        print ("Voce quer ser um Pe Fabio Melado mais positivo, pra frentex...")
        print ("que tem uma mensagem de esperanca pro futuro.")
        print ("ambos sabemos que isso nao eh possivel.")
        time.sleep(1)
        print ("pra encarnar bem esse espirito primeiro eh necessaria uma tragedia")
        print ("conte-me, o que aconteceu com vc?")
        desgraca = raw_input()
        print ("hahaha nao to acreditando, isso eh serio?")
        print ("por favor, me diga a verdade")
        desgraca1 = raw_input()
        if desgraca == desgraca1:
            print ("entao era verdade... Me desculpe por ter duvidado de vc")
            print ("SIGAMOS EM FRENTE FINGINDO QUE NADA DISSO ACONTECEU.")
            time.sleep(1)
            print ("eu sempre acreditei nessa historia sua de " + desgraca)
            time.sleep(6)
        else:
            print ("eh bem melhor quando se eh honesto... hehehe...")
            time.sleep(2)
        print ("mas entao, como voce conseguiu escapar desta situcao tao tenebrosa?")
        print ("seja breve... Eu n tenho o dia todo")
        sorte = raw_input()
        print ("ok...")
        time.sleep(1)
        print ("processando...")
        time.sleep(2)
        print ("enquanto eu gerava o texto, fiquei com uma duvida: voce eh cristao?")
        cristao = raw_input()
        if cristao.lower() == "sim" or cristao.lower() == "sou" or cristao.lower() == "cristao" or cristao.lower() == "claro" or cristao.lower() == "y":
            print ("Catolico ou Protestante?")
            relig = raw_input()
            if relig != "catolico" and relig != "protestante" and relig != "crente":
                print ("Mormon? Y/N")
                catoupro = raw_input()
                print ("all right then")
            if relig == "catolico":
                print ("qual santo intercedeu por voce?")
                catoupro = raw_input()
            if relig == "protestante" or relig == "crente":
                print ("entao voce foi ungido, saquei")
                catoupro = "ungido"
        if cristao.lower() == "nao" or cristao.lower() == "n":
            print ("*olhar fuminante*")
            relig = "condenado"
            catoupro = "demonio"
        else:
            print ("cruz credo")
            relig = "condenado"
            catoupro = "demonio"
        time.sleep(2)
        print ("entao eh isto...")
        time.sleep(2)
        print ("processando...")
        time.sleep(3)
        print ("ja tenho tudo pronto!")
        time.sleep(1)
        print ("IRMAOS, MEUS IRMAOS " + relig.upper() + " QUE HOJE ESTAO AQUI NESSE GRUPO ZAPEIRO")
        print ("tenho comigo o testemunho das maravilhas de Deus que foi passado a mim")
        print ("sei que nem sempre... \n Mas se fosse putaria todo mundo compartilhava\nDessa vez a misericorida veio na forma de " + desgraca1)
        print ("mas bem que poderia ter sido " + desgraca + " bem no centro")
        print ("Porque entao " + catoupro + " que habita aqui se manifestou quando \npor meio de " + sorte + " livrou um jovem garoto de " + desgraca1)
        print ("Jesus jamais daria uma " + desgraca1 + " que voce nao possa aguentar \nmeu irmao. E hoje esta bem, esta sadio e feliz como o " + relig + " que sempre foi")
        print ("e isso nao sou eu que digo, mas o senhor, homi dos homi, que fala pela minha boca.")
        print ("")
        print ("ASSINADO PASTOR FABIO MELADO")
        print ("")
        opcaob = True
        if opcaoa == True and opcaob == True and opcaoc == True:
            inicio = False
        print ("Quer aprender mais? y/n")
        reiniciar = raw_input("")
        opcaoc = True
        if reiniciar.lower() == "y":
            inicio = False
    if opcaoa == True and opcaob == True and opcaoc == True:
        print ("Uau! Agora voce já tem tudo para ser um Pe. Fabio Melado da porra")
        print ("PARABENS??")
        sys.exit(0)
    else:
        print ("esta nao eh uma forma valida de ser um Fabio Melado, responda de novo")
        time.sleep(3)
