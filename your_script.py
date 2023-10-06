import tkinter as tk
from tkinter import ttk
import time

def animate_loading_bar():
    loading_bar.start(10)  # Start the loading animation
    for _ in range(100):
        loading_bar.step(1)  # Advance the loading bar
        root.update_idletasks()
        time.sleep(0.05)  # Delay to control the animation speed
    loading_bar.stop()  # Stop the loading animation
    message_label.config(text="Your brain has been hacked.")  # Update the message

# Create the main window
root = tk.Tk()
root.title("Brain Simulation")
root.geometry("1200x600")

# Make the window come to the forefront
root.attributes('-topmost', True)

# Create a label for the message
message_label = tk.Label(root, text="Running brain simulation", font=("Helvetica", 20))
message_label.pack(pady=20)

# Create a progress bar (loading bar)
loading_bar = ttk.Progressbar(root, length=400, mode="determinate")
loading_bar.pack()

# Create a button to start the animation
start_button = tk.Button(root, text="Start Simulation", command=animate_loading_bar)
start_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
