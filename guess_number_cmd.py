#Esta programa tiene que continuar hasta que sea correcto
import random

guessnumber = random.randint(1, 50)
while True:
    number = int(input("number:"))
    if number==guessnumber:
        print("Is correct,very good")
        break
    else:
        if number>guessnumber:
            print("number is less")
        if number<guessnumber:
            print("number is more")






