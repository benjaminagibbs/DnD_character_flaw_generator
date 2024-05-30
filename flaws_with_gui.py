import csv
import random
import tkinter as tk
from tkinter import messagebox

data = {}

def load_data():
    with open('dnd_character_flaws.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        entry_number = 1

        for row in reader:
            if row:
                flaw_name = row[0].strip()
                description = row[1].strip()
                gameplay_influence = row[2].strip()

                data[entry_number] = {
                    'Flaw Name': flaw_name,
                    'Description': description,
                    'Gameplay Influence': gameplay_influence
                }
                entry_number += 1

def get_flaw(entry_number_input):
    if entry_number_input.lower() == 'rand':
        entry_number_input = random.randint(1, len(data))
    else:
        try:
            entry_number_input = int(entry_number_input)
            if entry_number_input < 1 or entry_number_input > 100:
                raise ValueError("Entry number must be between 1 and 100.")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

    entry_number_input = (entry_number_input - 1) % 57 + 1

    if entry_number_input in data:
        entry = data[entry_number_input]
        flaw_details = (
            f"Flaw Name: {entry['Flaw Name']}\n"
            f"Description: {entry['Description']}\n"
            f"Gameplay Influence: {entry['Gameplay Influence']}"
        )
        messagebox.showinfo("Generated Flaw", flaw_details)
    else:
        messagebox.showerror("Error", "Invalid entry number.")

def on_generate():
    entry_number_input = entry.get()
    get_flaw(entry_number_input)

# Load the data from the CSV file
load_data()

# Create the GUI
root = tk.Tk()
root.title("D&D Flaw Generator")

label = tk.Label(root, text="Enter your d100 dice roll (1-100) or type 'rand' for a random flaw:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Flaw", command=on_generate)
generate_button.pack(pady=10)

root.mainloop()
