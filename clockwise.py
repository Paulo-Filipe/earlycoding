
import sys

N = "North"
E = "East"
S = "South"
W = "West"

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
        print(msg)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

        
def test_suite():
    """ Run the suite of tests for code in this module (this file)."""
    test(turn_clockwise(N)== E)
    test(turn_clockwise(E)== S)
    test(turn_clockwise(S)== W)
    test(turn_clockwise(W)== N)
    test(turn_clockwise(-3.14)== None)
    
def test_suite2():
    test(day_name("sunday")== 0)
    test(day_name("monday")== 1)
    test(day_name("tuesday")== 2)
    test(day_name("wednesday")== 3)
    test(day_name("thursday")== 4)
    test(day_name("friday")== 5)
    test(day_name("saturday")== 6)
    test(day_name("blob")== None)
    test(day_name("545")== None)


def test_suite3():
    test(comeback_calculator("monday", 4) == "friday")
    test(comeback_calculator("tuesday", 0) == "tuesday")
    test(comeback_calculator("tuesday", 14) == "tuesday")
    test(comeback_calculator("sunday", 100) == "tuesday")
    test(comeback_calculator("sunday", -1) == "saturday")
    test(comeback_calculator("sunday", -2) == "friday")
    test(comeback_calculator("sunday", -3) == "thursday")
    test(comeback_calculator("sunday", -4) == "wednesday")
    test(comeback_calculator("sunday", -5) == "tuesday")
    test(comeback_calculator("sunday", -6) == "monday")
    test(comeback_calculator("sunday", -7) == "sunday")
    test(comeback_calculator("tuesday", -100) == "sunday")
    test(comeback_calculator("tuesday",-3) == "saturday")


def test_suite4():
    test(to_secs(2,30,10) == 9010)
    test(to_secs(2,0,0) == 7200)
    test(to_secs(0,2,0) == 120)
    test(to_secs(0,0,42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5,0,10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    
def test_suite5():
    test(compare(5,4) == 1)
    test(compare(7,7) == 0)
    test(compare(2,3) == -1)
    test(compare(42,1) == 1)


def test_suite6():
    test(hypotenuse(3,4) == 5.0)
    test(hypotenuse(12,5) == 13.0)
    test(hypotenuse(24,7) == 25.0)
    test(hypotenuse(9,12) == 15.0)
    test(slope(5,3,4,2) == 1.0)
    test(slope(1,2,3,2) == 0.0)
    test(slope(1,2,3,3) == 0.5)
    test(slope(2,4,1,2) == 2.0)
    test(intercept(4,6,12,8) == 5.0)
    test(intercept(6,1,1,6) == 7.0)
    test(intercept(1,6,3,12) == 3.0)
    test(is_factor(3,12))
    test(not is_factor(5,12))
    test(is_factor(7,14))
    test(not is_factor(7,15))
    test(is_factor(1,15))
    test(is_factor(15,15))
    test(not is_factor(25,15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    test(f2c(212) == 100)    # Boiling point of water
    test(f2c(32) == 0)       # Freezing point of water
    test(f2c(-40) == -40)    # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)

def day_name(nome_do_dia):
    if nome_do_dia == "sunday":
        codigo_do_dia = 0
        return codigo_do_dia
    elif nome_do_dia == "monday":
        codigo_do_dia = 1
        return codigo_do_dia
    elif nome_do_dia == "tuesday":
        codigo_do_dia = 2
        return codigo_do_dia
    elif nome_do_dia == "wednesday":
        codigo_do_dia = 3
        return codigo_do_dia
    elif nome_do_dia == "thursday":
        codigo_do_dia = 4
        return codigo_do_dia
    elif nome_do_dia == "friday":
        codigo_do_dia = 5
        return codigo_do_dia
    elif nome_do_dia == "saturday":
        codigo_do_dia = 6
        return codigo_do_dia
    else:
        print ("that is not a day, sunshine")
        return

    
def name_day(day_code):
    if day_code == 0:
        day = "sunday"
        return day
    elif day_code == 1:
        day = "monday"
        return day
    elif day_code == 2:
        day = "tuesday"
        return day
    elif day_code == 3:
        day = "wednesday"
        return day
    elif day_code == 4:
        day = "thursday"
        return day
    elif day_code == 5:
        day = "friday"
        return day
    elif day_code == 6:
        day = "saturday"
    else:
        return None
        
def turn_clockwise(direcao_atual):
    if direcao_atual == N:
        direcao_atual = E
        return direcao_atual
    elif direcao_atual == E:
        direcao_atual = S
        return direcao_atual
    elif direcao_atual == S:
        direcao_atual = W
        return direcao_atual
    elif direcao_atual == W:
        direcao_atual = N
        return direcao_atual
    else:
        print("esta nao eh uma direcao valida")
        return


def comeback_calculator(hoje, duracao):
    dia_da_volta = int(day_name(hoje)) + int(duracao)
    resultado = dia_da_volta % 7
    if int(day_name(hoje)) + duracao == -1:
        return "saturday"
    return name_day(abs(resultado))


def days_in_month(mes):
    mes_de_30 = 30
    mes_de_31 = 31
    if mes == "january" or mes == "march" or mes == "may" or mes == "july" or mes == "august" or mes == "october" or mes == "december":
        return mes_de_31
    elif mes == "february":
        return 28
    elif mes == "april" or mes == "june" or mes == "september" or mes == "november":
        return mes_de_30
    else:
        return None

def to_secs(horas, minutos, segundos):
    total_sec = segundos + 60*minutos + 3600*horas
    return int(total_sec)

def hours_in(segundos):
    total_hour = int(segundos) // 3600
    return total_hour


def minutes_in(segundos):
    hour_leftovers = int(segundos) % 3600
    total_minute = hour_leftovers // 60
    return total_minute


def seconds_in(segundos):
    hour_leftovers = int(segundos) % 3600
    minute_leftovers = hour_leftovers % 60
    return minute_leftovers


def compare (valor1, valor2):
    if valor1 > valor2:
        return 1
    elif valor1 == valor2:
        return 0
    elif valor1 < valor2:
        return -1
    else:
        return


def hypotenuse (catetoa,catetob):
    hyp = (catetoa**2 + catetob**2)**0.5
    return hyp


def slope (x1,y1,x2,y2):
    result = (y2-y1)/(x2-x1)
    return result


def intercept (x1,y1,x2,y2):
    M = slope(x1,y1,x2,y2)
    y_intercept = y1 - M*x1
    return y_intercept

def is_even(number):
    if int(number) % 2 == 0:
        return True
    elif int (number) % 2 != 0:
        return False
    else:
        return

def is_odd(number):
    if is_even(number) == False:
        return True
    elif is_event(number) == True:
        return False
    else:
        return
    

def is_factor(number1,number2):
    factor = number2 % number1
    if factor == 0:
        return True
    elif factor != 0:
        return False
    else:
        return


def is_multiple(number1,number2):
    multiple = number1 % number2
    if multiple == 0:
        return True
    elif multiple != 0:
        return False
    else:
        return


def f2c(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return round(celsius)


def c2f(celsius):
    fahrenheit = (celsius*1.8) + 32
    return round(fahrenheit)
    
test_suite3()
    
