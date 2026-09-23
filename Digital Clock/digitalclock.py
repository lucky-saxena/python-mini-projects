# ============================================
# PyClock - Live digital clock GUI using Tkinter
# Displays current time (with AM/PM) and date,
# updating every second
# ============================================

import tkinter as tk
from time import strftime

# --- Create the main window ---
root = tk.Tk()
root.title("PYCLOCK")

# --- Function to update the displayed time ---
def time():
    # Format: Hour:Minute:Second AM/PM, newline, Date (MM/DD/YY)
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    # Schedule this function to run again after 1000ms (1 second),
    # creating a continuously updating clock without blocking the GUI loop
    label.after(1000, time)

# --- Label widget that displays the clock ---
label = tk.Label(root, font=('calibri', 50, 'bold'), background='aqua', foreground='black')
label.pack(anchor='center')

# --- Start the clock and run the GUI event loop ---
time()
root.mainloop()