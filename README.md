# D&D Flaw Generator

## Overview

Generate unique and interesting character flaws for your D&D campaigns with this Python program featuring a graphical user interface (GUI).

## Features

- Load 100 unique flaws from a CSV file
- Input a specific flaw number (1-100) or generate a random flaw
- Displays flaw name, description, and gameplay influence
- User-friendly GUI with scrollable flaw display

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `dnd_character_flaws.csv` file with columns: `d100`, `Flaw Name`, `Description`, `Gameplay Influence`

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/dnd-flaw-generator.git
    cd dnd-flaw-generator
    ```

2. **Place your CSV file:**
   Ensure `dnd_character_flaws.csv` is in the same directory as the Python script.

3. **Run the program:**
    ```sh
    python dnd_flaw_generator.py
    ```

## Usage

1. **Run the script:**
    ```sh
    python dnd_flaw_generator.py
    ```

2. **Using the GUI:**
   - Enter a number between 1 and 100, or type `rand` for a random flaw.
   - Click the "Generate Flaw" button to view the flaw details.
   - A new window will open with the flaw name, description, and gameplay influence.

## Customization

Feel free to modify the `dnd_character_flaws.csv` file to add, remove, or edit flaws to suit your campaign needs. Ensure you maintain the CSV structure with the correct column headers.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

Enjoy creating more dynamic characters with these flaws for your tabletop adventures!
