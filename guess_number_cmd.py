#Esta programa tiene que continuar hasta que sea correcto
import random

number1 = random.randint(1, 3)
while True:
    number = int(input("number:"))
    if number==number1:
        print("Is correct,very good")
        break
    else:
        print("Is false, try again")






