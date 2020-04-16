import sys
import turtle

##wn = turtle.Screen()
##wn.bgcolor("green")
##tortuga = turtle.Turtle()
##tortuga.color("white")
##tortuga.speed(1)


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
        print(msg)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)



xs1 = [10, 12, 5, 2, 7, 13, 22, 13, 14, 40, 41, 33]
xs2 = [10, -12, 5, -2, 7, -13, 22, -13, 14, -40, 41, -33]
xs3 = ["letra", "casa", "coisa", "mestre", "meios", "cuidado"]
xs4 = ["letra", "casa", "coisa", "sam", "mestre", "meios", "cuidado"]
xs5 = ["letra", "casa", "coisa", "mestre", "meios", "sam", "cuidado"]
xs6 = [(160,20), (-43,10), (270,8), (-43,12)]
xs7 = [(135,70), (90, 50),(0, 50), (-135, 0), (0, 70), (-135,0), (0,50), (90,0), (0, 50), (135,0), (0, 70), (-135,0),(0, 50), (-90,0), (0, 50),(-45,0), (0,70)] ##eu sei que dava pra fazer com menos passos mas estava com preguiça.

def test_suite():
    test(sum_even2(xs1) == sum_even(xs1) -10)
    test(sum_even2(xs2) == sum_even(xs2) -10)
    test(count_to_sam(xs4) == 4)
    test(count_to_sam(xs5) == 6)
    test(count_to_sam(xs3) == 6)
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([0,0,0]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)

    
def count_odd(lista):
    nimpar = 0
    for i in lista:
        if i % 2 != 0:
            nimpar += 1
        else:
            continue
    print("there are " + str(nimpar) + " odd numbers in the list")

def sum_even(lista):
    sumeven = 0
    for i in lista:
        if i % 2 == 0:
            sumeven += i
        else:
            continue
    print ("the total sum of all even numbers in the list is " + str(sumeven))
    return sumeven


def sum_negatives(lista):
    sumnegative = 0
    for i in lista:
        if abs(i) != i:
            sumnegative += i
        else:
            continue
    print ("the total sum of all negative numbers in the list is " + str(sumnegative))


def sum_5lenght (lista):
    sum5 = 0
    for i in lista:
        if len(i) == 5:
            sum5 += 1
        else:
            continue
    print("há um total de " + str(sum5) + " palavras com 5 caracteres")


def sum_even2(lista):
    sumeven = 0
    controle = 0
    for i in lista:
        if i % 2 == 0 and controle == 0:
            controle += 1
            continue
        elif i % 2 == 0 and controle != 0:
            sumeven += i
        else:
            continue
    print ("A soma total dos números pares (com exceção do primeiro) é " + str(sumeven))
    return sumeven


def count_to_sam(lista):
    cota = 0
    for i in lista:
        if i == "sam":
            cota += 1
            break
        elif i != "sam":
            cota += 1
        else:
            continue
    return cota

def newton_sqr(number):
    approx = number/2.0 
    while True:
        better = (approx + number/approx)/2.0
        print (str(better))
        if abs(approx - better) < 0.001:
            return better
            print (str(better))
        approx = better

def print_triangular_numbers(number):
    for i in range(1,number+1):
        triangular = ((i)*(i+1))/2
        print(str(i), end="   ")
        print(str(triangular))


def is_prime(number):
    primo = None
    for i in range(1,abs(number)):
        divisible = number % i
        if divisible == 0 and i != 1 and number != i:
            primo = False
            return primo
        else:
            continue
    if primo == None:
        return True

def drunken_friend(lista):
    for (i,j) in lista:
        tortuga.forward(j)
        tortuga.left(i)

def num_digits(number):
    conte = 0
    if number == 0:
        return 1
    else:
        while number != 0:
            conte += 1
            number = abs(number) // 10
        return conte

def num_even_digits(number):
    conte = 0
    if number == 0:
        return 1
    else:
        while number != 0:
            if number % 2 == 0:
                conte += 1
            number = number  // 10

    return conte

def sum_of_squares(lista):
    soma = 0
    (i,j,k) = lista
    soma = (i**2)+(j**2)+(k**2)
    return soma

def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    is True, the human gets to play first, else the
    computer gets to play first. When the round ends,
    the return value of the function is one of
    -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0}, winner={1} "
    .format(human_plays_first, result))
    return result


def main_game():
    import random
    continuajogando = 0
    placar_maquina = 0
    placar_humano = 0
    empate = 0
    while continuajogando == 0:
        random_bit = random.getrandbits(1)
        random_player = bool(random_bit)
        jogo_result = play_once(random_player)
        if jogo_result == -1:
            print ("You Win!")
            placar_humano += 1
        elif jogo_result == 0:
            print ("Game Drawn!")
            empate += 1
        elif jogo_result == 1:
            print ("I win!")
            placar_maquina += 1
            
        print ("Your points: "+ str(placar_humano), end="    ")
        print ("My points: " + str(placar_maquina), end="    ")
        print ("Ties: " + str(empate))
        
        humanrate = placar_humano/(placar_humano + placar_maquina + empate)
        
        print ("Winrate: "+ str(int(humanrate*100))+"%")
        pergunta_jogo = input("Do you want to play again? ")
        if pergunta_jogo == "y":
            continue
        elif pergunta_jogo != "y":
            print ("Your final points: "+ str(placar_humano), end="    ")
            print ("My final points: " + str(placar_maquina), end="    ")
            print ("Ties: " + str(empate))
            print ("Final Winrate: "+ str(int(humanrate*100))+"%")
            print("goodbye!")
            break


        
main_game()

