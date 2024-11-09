import tkinter as tk
from tkinter import colorchooser
from time import strftime

# Function to pick a color for the clock text
def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        time_label.config(fg=color)
        date_label.config(fg=color)

# Initialize the main window
root = tk.Tk()
root.title("Customizable Digital Clock")
root.configure(bg='black')
root.geometry("400x200")  # Set a fixed window size

# Function to update time and date
def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %d %B %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)

# Set up labels
time_label = tk.Label(root, font=('Helvetica', 48), fg='cyan', bg='black')
time_label.pack(pady=10)
date_label = tk.Label(root, font=('Helvetica', 24), fg='cyan', bg='black')
date_label.pack()

# Add button to change color
color_button = tk.Button(root, text="Change Text Color", command=change_text_color)
color_button.pack(pady=10)

# Start the clock
update_time()
root.mainloop()
