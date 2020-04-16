

def find_hyp(sza, szb):
    hyp = (sza**2 + szb**2)**0.5
    return hyp

def is_right_angle (sza, szb, szc):
    if float(sza) + float(szb) < float(szc) or float(sza) + float(szc) < float(szb) or float(szb) + float(szc) < float(sza):
        print ("it's not a triangle!")
    elif float(sza) <= 0 or float(szb) <= 0 or float(szc) <= 0:
        print("only positives allowed")
        return
    lado_maior = max(sza,szb,szc)
    if lado_maior == sza:
        hipo = find_hyp(float(szb), float(szc))
        if float(sza) - hipo <= 0.00001:
            return True
        else:
            return False
    elif lado_maior == szb:
        hipo = find_hyp(float(sza), float(szc))
        if float(szb) - hipo <= 0.00001:
            return True
        else:
            return False
    elif lado_maior == szc:
        hipo = find_hyp(float(sza), float(szb))
        if float(szc) - hipo <= 0.00001:
            return True
        else:
            return False


lado_a = input("primeiro lado :")
lado_b = input("segundo lado :")
lado_c = input ("terceiro lado :")

Resultado = is_right_angle(lado_a,lado_b,lado_c)
print (str(Resultado))
