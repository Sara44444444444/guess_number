from tkinter import *

root = Tk()
root.geometry("1000x1000")  # Set the window size

# creating a Label Widget
myLabel1 = Label(root, text="Guess My Number", font=("Helvetica", 16, "bold"),fg=("blue"))
myLabel2 = Label(root, text="Guess a random number", font=("Helvetica",15,"bold"),fg=("blue"))

# Shoving it onto the screen in the center
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Creating Buttons
myButton1 = Button(root, text="1")
myButton2 = Button(root, text="100")

# Placing the buttons side by side
myButton1.grid(row=2, column=0)
myButton2.grid(row=2, column=1)



root.mainloop()
