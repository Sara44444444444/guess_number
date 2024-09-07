from tkinter import *  # Import all classes and functions from the tkinter module
import random  # Import the random module to generate random numbers
from PIL import Image, ImageTk

target_number = None  # Initialize the target number variable to None


def Guess():
    num = int(entryGuessNumber.get())  # Get the number entered by the user and convert it to an integer
    global target_number  # Use the global target_number variable

    if target_number is None:  # Check if the target number has not been set
        resultLabel.config(
            text="please first click the button New target ")  # Prompt the user to set a new target number
        return  # Exit the function
    if num > target_number:  # If the guessed number is greater than the target number
        resultLabel.config(text="My number is less")  # Inform the user that the target number is smaller
    elif num < target_number:  # If the guessed number is less than the target number
        resultLabel.config(text="My number is more")  # Inform the user that the target number is larger
    else:  # If the guessed number is equal to the target number
        resultLabel.config(text="well Done!")  # Congratulate the user


def set_new_target():
    global target_number  # Use the global target_number variable
    lownumber = int(lowNumberEntry.get())  # Get the lower bound from the user and convert it to an integer
    highnumber = int(highNumberEntry.get())  # Get the upper bound from the user and convert it to an integer
    target_number = random.randint(lownumber, highnumber)  # Generate a random number within the specified range
    print(target_number)  # Print the generated random number for debugging purposes



root = Tk()  # Create the main window
root.geometry("1920x1080")  # Set the window size
root.configure(bg="#FFA500")  # Set the background color
root.title("Guess My Number")

GuessMyNumber = Label(root, text="Guess My Number", font=("arial", 46, "bold"), fg="#5677fc",
                      bg="#FFA500")  # Create a label with the title
GuessMyNumber.pack()  # Pack the label
myLabel2 = Label(root, text="Guess a random number", font=("arial", 36, "bold"), fg="#03a9fa",
                 bg="#FFA500")  # Create a label with instructions
myLabel2.pack()  # Pack the label

frame = Frame(root, bg="light blue")  # Create another frame for the input fields
frame.pack(pady=10)  # Pack the frame with padding

lowNumberEntry = Entry(frame, width=10)  # Create an entry widget for the lower bound
lowNumberEntry.pack(side=LEFT, padx=10)  # Pack the entry widget with padding
lowNumberEntry.insert(0, str(1))  # Insert the default value of 1
highNumberEntry = Entry(frame, width=10)  # Create an entry widget for the upper bound
highNumberEntry.pack(side=LEFT, padx=10)  # Pack the entry widget with padding
highNumberEntry.insert(0, str(100))  # Insert the default value of 100
buttonSetNewTarget = Button(frame, text="New Target", bg="light blue", fg="dark blue",
                            command=set_new_target)  # Create a button to set a new target number
buttonSetNewTarget.pack(side=LEFT, padx=10)  # Pack the button with padding

resultLabel = Label(root, text="Please guess a number, enter it and press guess:", font=("arial", 16, "bold"),
                    fg="#2923A0", bg="#ffeb3b")  # Create a label to display the result
resultLabel.pack()  # Pack the label

frame1 = Frame(root, bg="light blue")  # Create another frame for the guess input
frame1.pack(pady=12)  # Pack the frame with padding

entryGuessNumber = Entry(frame1, width=10)  # Create an entry widget for the user's guess
entryGuessNumber.pack(side=LEFT, padx=10)  # Pack the entry widget with padding
buttonGuess = Button(frame1, text="Guess", command=Guess)  # Create a button to submit the guess
buttonGuess.pack(side=LEFT, padx=10)  # Pack the button with padding

framephoto = Frame(root, )
framephoto.pack(pady= 10)
framephoto.place(relx=0.5,rely= 0.7, anchor=CENTER)

photooriginal = Image.open("image_guess.png")
resizephoto = photooriginal.resize((300, 300))
tkphoto = ImageTk.PhotoImage(resizephoto)

photo = PhotoImage(file="image_guess.png")
photoLabel = Label(framephoto, image= tkphoto)
#photoLabel.place(x=10, y=20)  # place the image at (10, 20) coordinates
photoLabel.pack()
# Running the main loop
root.mainloop()  # Start the main event loop
