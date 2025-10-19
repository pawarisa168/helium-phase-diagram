# Helium Phase Diagram Visualizer  

A simple **Python GUI** built with **Tkinter**, **Matplotlib**, and **Pandas**  
to visualize and export the **Phase Diagram of Helium**.  
This program allows users to input temperature and pressure values, plot them interactively,  
and export the results to Excel for further analysis.

---

## Project Overview

This project visualizes the **physical behavior of Helium** across different states.  
It displays three major scientific curves:

1. **Saturated Vapor Pressure Curve**  
2. **Lambda Line**  
3. **Melting Curve**

Users can also add their own data points and export them to Excel.  
Perfect for **students, researchers, and educators** in physics, cryogenics, and thermodynamics.

---

## GUI Preview

> <img width="478" height="270" alt="image" src="https://github.com/user-attachments/assets/19bfac24-65a4-4208-a708-cf7b15065231" />

**Example layout:**

| **Left Panel** | **Right Panel** |
|----------------|----------------|
| Temperature Input<br>Pressure Input<br>Unit Selection<br>Buttons (Plot / Export) | Interactive Graph displaying Helium Phase Diagram |

---
## How to Run

### 1️⃣ Install dependencies
Make sure you have Python ≥ 3.10 installed, then run:

```bash
pip install -r requirements.txt

### 2️⃣ Run the Application

Once all dependencies are installed, execute the following command to start the program:

```bash
python Helium_Phase_Diagram_V1.1.py


A Tkinter GUI window will appear showing the Helium Phase Diagram.
The right side displays a Matplotlib plot, and the left side contains input fields and buttons.

### 3️⃣ Using the Interface
🟦 Left Panel

Input fields for:

Temperature (K)

Pressure (Pa or Torr)

Dropdown for Pressure Unit

Buttons:

Plot → Adds your input point to the graph

Export to Excel → Saves your input to Data_inputs.xlsx

🟥 Right Panel

Displays the plotted Helium Phase Diagram, including:

Saturated Vapor Pressure Curve (red)

Lambda Line (green)

Melting Curve (yellow)
Your input points appear as magenta dots.

### 4️⃣ Output Example

When you click Export to Excel, the file Data_inputs.xlsx will be generated in the same directory:

Temperature (K)	Pressure (Pa)
1.80	2500000
2.00	2800000

You can open this file with Excel, Google Sheets, or any data tool.

### 5️⃣ Troubleshooting

If the GUI doesn’t open:

Make sure you are in the correct project folder

Check that Python ≥ 3.10 is installed

Try reinstalling dependencies:

```bash
pip install matplotlib pandas openpyxl


If you see:

ValueError: x and y must have same first dimension


→ It means the temperature and pressure lists have mismatched lengths.

### 6️⃣ Example Commands Recap

```bash
# (Optional) Create a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the program
python Helium_Phase_Diagram_V1.1.py

# Exported data file:
Data_inputs.xlsx


