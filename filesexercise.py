

def invert_list(lista):
    lista.reverse()
    return lista


def conv_txt_lista():
    leitura = open("tabacaria.txt","r")
    lista_texto = leitura.readlines()
    leitura.close()
    return lista_texto

def create_new_txt(lista, nomearquivo):
    new_txt = open(nomearquivo, "w")
    for i in lista:
        new_txt.write(i+"\n")
    new_txt.close()


def read_snake():
    leitura = open("story.txt","r")
    lista_texto = leitura.readlines()
    for i in lista_texto:
        if "snake" in i:
            print(i)


def count_txt_lines():
    leitura = open("tabacaria.txt", "r")
    lista_texto = leitura.readlines()
    for i in range(len(lista_texto)):
        if i <= 8:
            lista_texto[i]= "000" + str(i+1) + " " + lista_texto[i]
        elif i > 8 and i <= 98:
            lista_texto[i]= "00" + str(i+1) + " " + lista_texto[i]
        elif i > 98 and i < 998:
            lista_texto[i]= "0" + str(i+1) + " " + lista_texto[i]
        else:
            lista_texto[i]= str(i+1) + " " + lista_texto[i]
            
    create_new_txt(lista_texto,"tabacaria contada.txt")


def decount_txt_lines():
    leitura = open("tabacaria contada.txt","r")
    lista_texto = leitura.readlines()
    for i in range(len(lista_texto)):
        local_list = lista_texto[i].split()
        del local_list[0]
        lista_texto[i] = " ".join(local_list)
        print(lista_texto[i])
    
    create_new_txt(lista_texto, "tabacaria decontada.txt")



decount_txt_lines()







    
