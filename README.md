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

### 1️⃣ Install Dependencies
Make sure you have Python ≥ 3.10 installed, then run:
```bash
pip install matplotlib pandas openpyxl
```
---

### 2️⃣ Run the Application
Once installed, launch the GUI by running:
```bash
python Helium_Phase_Diagram_V1.1.py
```

A Tkinter window will open showing the Helium Phase Diagram.
The right panel displays a live Matplotlib graph.
The left panel provides input boxes and buttons for interaction.

---

### 3️⃣ Using the Interface
🟦 LEFT PANEL
- Temperature (K): Enter value in Kelvin
- Pressure (Pa or Torr): Enter numeric value
- Pressure Unit: Choose between Pa (default) or Torr
Buttons:
  • Plot → Adds your input point to the graph (magenta dot)
  • Export to Excel → Saves input data into Data_inputs.xlsx

🟥 RIGHT PANEL
 Displays the Helium Phase Diagram:
  • Red Line   = Saturated Vapor Pressure Curve
  • Green Line = Lambda Line
  • Yellow Line = Melting Curve
  • Your points appear as magenta dots
  
---

### 4️⃣ Output Example
After clicking "Export to Excel", a file is created in the same folder:
 Data_inputs.xlsx

Example contents:
 Temperature (K) | Pressure (Pa)
 ----------------|---------------
       1.80      |     2500000
       2.00      |     2800000
 You can open this file in Excel or Google Sheets.
 
----

### 5️⃣ Troubleshooting

 If GUI doesn’t open:
   - Check that you are in the correct project folder
   - Ensure Python ≥ 3.10 is installed
  - Reinstall dependencies:
```bash
pip install matplotlib pandas openpyxl
```
Common error:
ValueError: x and y must have same first dimension
 → means the temperature and pressure lists in the code are mismatched.
 
----

### 6️⃣ Example Commands Recap
```bash
# (Optional) Create a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install matplotlib pandas openpyxl

# Run the program
python Helium_Phase_Diagram_V1.1.py

# Exported data file will appear as:
Data_inputs.xlsx
```
