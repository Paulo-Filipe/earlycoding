

dia_da_semana = input ("pfv coloque que dia da semana você vai sair: ")
duracao_da_viagem = input ("quanto tempo durara a viagem? ")

total = int(dia_da_semana) + int(duracao_da_viagem)

resto_total = total % 7 

if int(dia_da_semana) > 6 or int(dia_da_semana) < 0:
    print ("ei danado que dia eh esse?")


if resto_total == 0:
    print("voce voltará num domingo")
elif resto_total == 1:
    print ("voce voltará numa segunda")
elif resto_total == 2:
    print ("voce voltará numa terca")
elif resto_total == 3:
    print ("voce voltará numa quarta")
elif resto_total == 4:
    print ("voce voltará numa quinta")
elif resto_total == 5:
    print ("voce voltará numa sexta")
elif resto_total == 6:
    print ("voce voltará num sabado")
else:
    print ("voce eh um ninja e quebrou a matematica")
