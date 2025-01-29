import tkinter as tk  
from tkinter import messagebox  # Import a module for dialog boxes
import time  # For countdown functionality
import webbrowser  # To open YouTube or other links

# Function to start the timer
def start_timer():
    try:
        # Get the user input from the Entry widget and convert it to an integer
        minutes = int(entry.get())
        seconds = minutes * 60  # Convert minutes to seconds
        
        for i in range(seconds, -1, -1):
            mins, secs = divmod(i, 60)  # Divide total seconds into minutes and seconds
            timer_label.config(text=f"{mins:02}:{secs:02}")  # Update the timer label
            root.update()  # Refresh the window
            time.sleep(1)  # Pause for 1 second
  
        messagebox.showinfo("Take a Break", "Time to relax!")  # Show an info dialog box
        webbrowser.open("https://www.youtube.com/ watch?v=Z6rSuKeHBR0")
    except ValueError:
        # Handle invalid input (e.g., if the user doesn't enter a number)
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Take-a-Break Timer")  # Set the title of the window

# Add a label to instruct the user
tk.Label(root, text="Enter time in minutes:").pack(pady=10)

# Add an entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=5)

# Add a button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=10)

# Add a label to display the countdown
timer_label = tk.Label(root, text="00:00", font=("Arial", 24))
timer_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

