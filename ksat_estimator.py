import sys
print("Welcome to the Ksat Estimator")

n = input("Enter the number of samples you would like to estimate:\n")

if len(n) > 0 and n.isalpha() == False:
    n = int(n)
    print(f"Enter the oven-dry bulk density values of your {n} samples seperated by a space")
    user_db = input()
    user_db = [float(i) for i in user_db.split()]
    while len(user_db) != n:
            user_db = input("Looks like you forgot some values, try again:\n")
            user_db = [float(i) for i in user_db.split()]
    else: print(user_db)

else:
    sys.exit("Invalid entry, please try again")


print(f"Now, enter the 33 kPa values of your {n} samples seperated by a space.")
user_3kpa = input()
user_3kpa = [float(i) for i in user_3kpa.split()]
while len(user_3kpa) != n:
            user_3kpa = input("Looks like you forgot some values, try again:\n")
            user_3kpa = [float(i) for i in user_3kpa.split()]
print(user_3kpa)


print(f"Finally, enter the fragment percentages of your {n} samples seperated by a space")
user_frag = input()
user_frag = [float(i) for i in user_frag.split()]
while len(user_frag) != n:
        user_frag = input("Looks like you forgot some values, try again:\n")
        user_frag = [float(i) for i in user_frag.split()]
print(user_frag)

print("Ready to calculate!")

def porosity(db):
    return 1 - db / 2.65

p = [porosity(i) for i in user_db]

def fearth(frag):
    """this function calculates the fine earth fraction (<2mm)"""
    return (100 - frag) / 100

fef = [fearth(i) for i in user_frag]

#calculate field capacity
fc = [x / y for x,y in zip(user_3kpa, fef)]

#calculate effective porosity (qe)
qe = [x - y for x,y in zip(p,fc)]

#calculate relative effective porosity
r_qe = [x / y for x,y in zip (qe,fc)]

#calculate ksat of the fine-earth fraction
#first calculate constant used in equation
kcon = 10000 / 86400
ksat2 = [75 * (x ** 2) * kcon for x in r_qe]

#calculate KT, ksat for the whole soil
#first, convert fragment percentage to decimal
frag_rv = [x / 100 for x in user_frag]

kt = [x * ((2 * (1 - y)) / ((2 + y))) for x,y in zip(ksat2,frag_rv)]

conclass = input("Would you like to convert these into the Ksat revised classes (please respond 'y' or 'n')\n")

if conclass == 'y':
    for i in kt:
        if i > 0 and i < .01:
            print("L: 0, RV: 0.005, H: 0.01")
        elif i > 0.01 and i < 0.1:
            print("L: 0.01, RV: 0.055, H: 0.1")
        elif i > 0.1 and i < 0.5:
            print("L: 0.1, RV: 0.3, H: 0.5")
        elif i > 0.5 and i < 1:
            print("L: 0.5, RV: 0.75, H: 1")
        elif i > 1 and i < 5:
            print("L: 1, RV: 3, H: 5")
        elif i > 5 and i < 10:
            print("L: 5, RV: 7.5, H: 10")
        elif i > 10 and i < 50:
            print("L: 10, RV: 30, H: 50")
        elif i > 50 and i < 100:
            print("L: 50, RV: 75, H: 100")
        elif i >100 and i < 500:
            print("L: 100, RV: 300, H: 500")
        elif i > 500 and i < 1000:
            print("L: 500, RV: 750, H: 1000")
        else:
            print("Value falls outside the range of available classes")
else:
    for i in kt:
        print("Output:",i)
