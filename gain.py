import math
S=(4,6)

def gain(S: tuple, list_of_values: list):
    total = 0
    for x in list_of_values:
        total += sum(x)/sum(S)*entropy(x)
    return entropy(S) - total

def entropy(coll):
    pos = coll[0]/(coll[0]+coll[1])
    neg = coll[1]/(coll[0]+coll[1])
    return -(pos)*math.log(pos, 2)-neg*math.log(neg,2)

def entropy_m(coll: list):
    return sum(-x*math.log(x,2) for x in coll)

print(entropy((1,5)))
print(entropy((1,3)))




