import csv
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext

data = {}

def load_data():
    with open('dnd_character_flaws.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entry_number = int(row['d100'])
            data[entry_number] = {
                'Flaw Name': row['Flaw Name'],
                'Description': row['Description'],
                'Gameplay Influence': row['Gameplay Influence']
            }

def get_flaw(entry_number_input):
    if entry_number_input.lower() == 'rand':
        entry_number = random.randint(1, 100)
    else:
        try:
            entry_number = int(entry_number_input)
            if entry_number < 1 or entry_number > 100:
                raise ValueError("Entry number must be between 1 and 100.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

    if entry_number in data:
        entry = data[entry_number]
        flaw_details = (
            f"Flaw Name: {entry['Flaw Name']}\n\n"
            f"Description: {entry['Description']}\n\n"
            f"Gameplay Influence: {entry['Gameplay Influence']}"
        )
        display_flaw(flaw_details)
    else:
        messagebox.showerror("Error", "Invalid entry number.")

def display_flaw(flaw_details):
    flaw_window = tk.Toplevel(root)
    flaw_window.title("Generated Flaw")
    flaw_window.geometry("400x300")

    text_widget = scrolledtext.ScrolledText(flaw_window, wrap=tk.WORD, width=50, height=15)
    text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    text_widget.insert(tk.END, flaw_details)
    text_widget.config(state=tk.DISABLED)

def on_generate():
    entry_number_input = entry.get()
    get_flaw(entry_number_input)

# Load the data from the CSV file
load_data()

# Create the GUI
root = tk.Tk()
root.title("D&D Flaw Generator")
root.geometry("300x150")

label = tk.Label(root, text="Enter a number (1-100) or 'rand' for a random flaw:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Flaw", command=on_generate)
generate_button.pack(pady=10)

root.mainloop()
