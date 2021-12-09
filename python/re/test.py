def mod_checker(x, mod=0):
    return  lambda y:  y % x == mod




mod_3_1 = mod_checker(3, 1)(4)
print(mod_3_1) # True