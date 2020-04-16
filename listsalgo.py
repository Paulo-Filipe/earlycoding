

def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we’re done.
        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result
        
        # Both lists still have items, copy smaller item to result.
        
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge_pars(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):              
            return result          
        if yi >= len(ys):          
            return result

        
        if xs[xi] in ys and xs[xi] not in result:
            result.append(xs[xi])
            xi += 1
        if ys[yi] in xs and ys[yi] not in result:
            result.append(ys[yi])
            yi += 1
        else:
            xi += 1
            yi += 1


def only_on_1st_list(xs, ys):
    result = []
    xi = 0
    while True:
        if xi >= len(xs):           
            return result       
        
        
        if xs[xi] not in ys and xs[xi] not in result:
            result.append(xs[xi])
            xi += 1
        else:
            xi += 1


def only_on_2nd_list(xs, ys):
    result = []
    yi = 0
    while True:
        if yi >= len(ys):
            return result
        
        
        if ys[yi] not in xs and ys[yi] not in result:
            result.append(ys[yi])
            yi += 1
        else:
            yi += 1


def on_either_list(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if len(xs) >= len(ys):
            if xi >= len(xs):
                result.sort()
                return result          
        if len(ys) > len(xs):
            if yi >= len(ys):
                result.sort()
                return result
        

        
        if xs[xi] not in result:
            result.append(xs[xi])
            xi += 1
        if ys[yi] not in result:
            result.append(ys[yi])
            yi += 1
        else:
            xi += 1
            yi += 1

            
def bagdiff_on_merge(xs, ys):
    result = []
    match = []
    xi = 0
    while True:
        if xi >= len(xs):           
            return result          
     
        if xs[xi] not in ys:
            result.append(xs[xi])
            xi += 1
        else:
            if xs[xi] in match:
                result.append(xs[xi])
                xi += 1
                continue
            match.append(xs[xi])
            xi += 1
        
def share_diagonal(x0, y0, x1, y1):
     """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
     dy = abs(y1 - y0) # Calc the absolute y distance
     dx = abs(x1 - x0) # CXalc the absolute x distance
     return dx == dy   # They clash if dx == dy



def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
    with any queen to its left. 4 """
    for i in range(c): # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We’re assuming here that the_board is a permutation of column
        numbers, so we’re not explicitly checking row or column clashes."""
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False



def invert_solution_on_x (solution):
    invert_sol = []
    for i in solution:
        resto = 7-i
        invert_sol.append(resto)
        
    return invert_sol



def invert_solution_on_y (solution):
    invert = [0,0,0,0,0,0,0,0]
    for (i,v) in enumerate(solution):
        invert[7-i] += v
    return invert


def turn_90(solution):
    turn = [0,0,0,0,0,0,0,0]
    for (i,v) in enumerate(solution):
        turn[v] += 7-i
    return turn

def turn_180(solution):
    turn = turn_90(solution)
    turn2 = turn_90(turn)
    return turn2

def turn_270(solution):
    turn = turn_180(solution)
    turn2 = turn_90(turn)
    return turn2


def solution_family(solution):
    solutions = []
    solutions.append(solution)
    solutions.append(invert_solution_on_x(solution))
    solutions.append(invert_solution_on_y(solution))
    solutions.append(turn_90(solution))
    solutions.append(turn_180(solution))
    solutions.append(turn_270(solution))
    solutions.append(invert_solution_on_x(turn_270(solution)))
    solutions.append(invert_solution_on_x(turn_90(solution)))
    return solutions


def main():
    import random
    rng = random.Random() 
    bd = list(range(8))   
    num_found = 0
    tries = 0
    solutions = []
    while num_found < 12:
        ac = []
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if not bd in solutions:
                ac += bd
                for i in solution_family(ac):
                    if i not in solutions:
                        solutions.append(i)
                print("Found solution {0} in {1} tries.".format(bd, tries))
                num_found += 1
                
    print(len(solutions))
    return solutions

my_tickets = [[7,17,37,19,23,43], [7,2,13,41,31,43], [2,5,7,11,13,17],[13,17,37,19,23,43]]


def lotto():
    import random
    rng = random.Random()
    lottery = list(range(1,49))
    rng.shuffle(lottery)
    return lottery[:6]

def lotto_match(ticket,draw):
    jackpot = 0
    for i in ticket:
        if i in draw:
            jackpot += 1
    return jackpot


def lotto_matches(tickets,draw):
    jackpots = []
    for i in tickets:
        jackpots.append(lotto_match(i,draw))
    return jackpots


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2,number-1):
        if number % i == 0:
            return False
    else:
        return True

def primes_in(lista):
    total = 0
    for i in lista:
        if is_prime(i):
            total += 1
    return total

def prime_misses():
    prime_list = []
    list_number = list(range(1,49))
    for k in list_number:
        if is_prime(k):
            prime_list.append(k)
    for i in my_tickets:
        for j in i:
            if j in prime_list:
                prime_list.remove(j)
    return prime_list

def lotto_simulation():
    draws = 0
    correct = False
    while not correct:
        draws += 1
        draw = lotto()
        results = lotto_matches(my_tickets,draw)
        if 6 in results:
            correct = True
    return draws

def average():
    total = 0
    for i in range(20):
        number = lotto_simulation()
        print(number)
        total += number
    media = total/20
    return media

main()
    
