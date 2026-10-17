from euclid import euclid

'''
Zn (basically) represents all the ints from 1 to n-1
Generators of Zn are the ints in this list that are COPRIME with n
As in gcd(k, n) = 1
'''

# this function will hopefully make an array of Zn with whatever n is given
# and then find which values in it are coprime with n
def find_gens(n):
    zn = []
    gens = []
    for x in range(1, n):
        zn.append(x)
    for x in zn:
        if euclid(x, n) == 1:
            gens.append(x)
    return gens

print(find_gens(16))
print(find_gens(19))
