from tkinter import *

root = Tk()
root.geometry("1920x1080")  # Set the window size
root.configure(bg="light blue")  # Set the background color


# creating a Label Widget
myLabel1 = Label(root, text="Guess My Number", font=("Helvetica", 16, "bold"), fg="blue")
myLabel2 = Label(root, text="Guess a random number", font=("Helvetica", 15, "bold"), fg="blue")

# Shoving it onto the screen in the center
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Creating Entry Widgets for user input
entry1 = Entry(root, width=10)
entry2 = Entry(root, width=10)

# Creating a Button
button = Button(root, text="New target", fg="blue", bg="light blue")

# Placing the Entry widgets and Button in the grid
entry1.grid(row=2, column=0)
entry2.grid(row=2, column=1)
button.grid(row=2, column=2)

# Running the main loop
root.mainloop()
