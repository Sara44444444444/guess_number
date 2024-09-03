from tkinter import *
import random

target_number = None


def Guess():
    num = int(entryGuessNumber.get())
    global target_number

    if target_number == None:
        resultLabel.config(text="please first click the button New target ")
        return
    if num > target_number:
        resultLabel.config(text="My number is less")
    elif num < target_number:
        resultLabel.config(text="My number is more")
    else:
        resultLabel.config(text="well Done!")


def set_new_target():
    global target_number
    lownumber = int(lowNumberEntry.get())
    highnumber = int(highNumberEntry.get())
    target_number = random.randint(lownumber, highnumber)
    print(target_number)  # adad tasadofi hastesh


root = Tk()
root.geometry("1920x1080")  # Set the window size
root.configure(bg="light blue")  # Set the background color

# Creating a Frame with a border
border_frame = Frame(root, borderwidth=5, relief="ridge", bg="light blue")
border_frame.pack(fill="both", expand=True, padx=10, pady=10)

GuessMyNumber = Label(border_frame, text="Guess My Number", font=("arial", 16, "bold"), bg="light blue")
GuessMyNumber.pack()
myLabel2 = Label(border_frame, text="Guess a random number", bg="light blue")
myLabel2.pack()

frame = Frame(border_frame, bg="light blue")
frame.pack(pady=10)

lowNumberEntry = Entry(frame, width=10)
lowNumberEntry.pack(side=LEFT, padx=10)
lowNumberEntry.insert(0, str(1))
highNumberEntry = Entry(frame, width=10)
highNumberEntry.pack(side=LEFT, padx=10)
highNumberEntry.insert(0, str(100))
buttonSetNewTarget = Button(frame, text="New Target", bg="light blue", fg="dark blue", command=set_new_target)
buttonSetNewTarget.pack(side=LEFT, padx=10)

resultLabel = Label(border_frame, text="Please guess a number, enter it and press guess:", bg="light yellow")
resultLabel.pack()

frame1 = Frame(border_frame, bg="light blue")
frame1.pack(pady=12)

entryGuessNumber = Entry(frame1, width=10)
entryGuessNumber.pack(side=LEFT, padx=10)
buttonGuess = Button(frame1, text="Guess", command=Guess)
buttonGuess.pack(side=LEFT, padx=10)

# Running the main loop
root.mainloop()
