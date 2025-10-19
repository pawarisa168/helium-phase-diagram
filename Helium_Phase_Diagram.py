import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, OptionMenu, StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.ticker as ticker

# Data for Saturated line
temperature1 = [5.19, 5.13, 5.12, 5.10, 5.0, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8]
pressure1 = [226540, 216450.00, 214820.00, 211580.00, 196000.00, 181310.00, 167430.00, 154310.00, 141930.00, 130260.00, 119270.00, 108940.00, 99233.00, 90136.00, 81620.00, 73664.00, 66247.00, 59351.00, 52956.00, 47044.00, 41595.00, 36590.00, 32010.00, 27835.00, 24047.00, 20625.00, 17552.00, 14807.00, 12372.00, 10228.00, 8354.10, 6730.40, 5335.10, 4140.80, 3129.30, 2299.30, 1638.40, 1127.90, 746.36, 471.54, 282.00, 157.86, 81.48, 38.005, 15.57, 5.3792, 1.4752]

# Data for Lambda line
temperature2 = [1.77, 1.78, 1.79, 1.80, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.88, 1.89, 1.90, 1.91, 1.92, 1.93, 1.94, 1.95, 1.96, 1.97, 1.98, 1.99, 2.00, 2.01, 2.02, 2.03, 2.04, 2.05, 2.06, 2.07, 2.08, 2.09, 2.10, 2.11, 2.12, 2.13, 2.14, 2.15, 2.16, 2.17, 2.177]
pressure2 = [2998300.00, 2942000.00, 2885000.00, 2827300.00, 2768800.00, 2700960.00, 2649800.00, 2589200.00, 
             2527900.00, 2465900.00, 2403200.00, 2339800.00, 2275700.00, 2210900.00, 2145400.00, 2079100.00, 2012000.00, 1944200.00, 1875600.00, 1806100.00, 1735900.00, 1664800.00, 1592800.00, 1519900.00, 1446100.00, 1371300.00, 1295500.00, 1218700.00, 1140700.00, 1061700.00, 981460.00, 899970.00, 817130.00, 732850.00, 646980.00, 559330.00, 469630.00, 377510.00, 282400.00, 183480.00, 79519.00, 5044.3]

# Data for Melting curve
temperature3 = [0.00, 0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.95, 2.00, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30]
pressure3 = [2532800.00, 2532800.00, 2532900.00, 2533100.00, 2533700.00, 2534800.00, 2536600.00, 2539600.00, 2544000.00, 2550200.00, 2558800.00, 2570100.00, 2584900.00, 2603700.00, 2627100.00, 2651900.00, 2680600.00, 2727100.00, 2791300.00, 2873400.00, 2973200.00, 3111600.00, 3265600.00, 3426000.00, 3592800.00, 3765600.00, 3932000.00, 4109800.00, 4292200.00, 4479200.00, 4670500.00, 4865900.00]

# Convert pressures from Pa to MPa
pressure1_kpa = [p / 1000000 for p in pressure1]
pressure2_kpa = [p / 1000000 for p in pressure2]
pressure3_kpa = [p / 1000000 for p in pressure3]

def plot_initial_graph():
    fig, ax = plt.subplots(figsize=(18, 20))

    # Plot the saturated data
    ax.plot(temperature1, pressure1_kpa, linestyle='-', color='r', label='Saturated Vapor Pressure Curve')

    # Plot the Lambda line data
    ax.plot(temperature2, pressure2_kpa, linestyle='-', color='g', label='Lambda Line')

    # Plot the Melting Curve data
    ax.plot(temperature3, pressure3_kpa, linestyle='-', color='y', label='Melting Curve')

    # Labeling and grid
    ax.set_title('Phase Diagram of Helium')
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Pressure (MPa)')
    ax.legend()
    
    ax.set_yscale('linear')
    ax.set_yticks([0, 0.2,2.5])
    ax.set_ylim(-0.1, 3.4)

    return fig, ax

# Data storage for user inputs
user_inputs = {'Temperature (K)': [], 'Pressure (Pa)': []}

def plot_with_user_input(user_temperature, user_pressure, ax):
    user_pressure_kpa = user_pressure / 1000000
    ax.scatter(user_temperature, user_pressure_kpa, color='m', zorder=5)
    canvas.draw()
    
    #input data
    user_inputs['Temperature (K)'].append(user_temperature)
    user_inputs['Pressure (Pa)'].append(user_pressure)

def on_submit():
    try:
        user_temperature = float(temp_var.get())
        user_pressure = float(pressure_var.get())
        
        # Convert Torr to Pa if necessary
        if unit_var.get() == "Torr":
            user_pressure *= 133.322368
        
        plot_with_user_input(user_temperature, user_pressure, ax)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        
def export_to_excel():
    df = pd.DataFrame(user_inputs)
    df.to_excel("Data_inputs.xlsx", index=False)
    print("Data exported to 'Data_inputs.xlsx'")

#main window
root = Tk()
root.title("Helium Phase Diagram")

#frame for inputs
frame = Frame(root)
frame.pack(side='left', padx=10, pady=10)

#set StringVar for inputs
temp_var = StringVar()
pressure_var = StringVar()
unit_var = StringVar(value="Pa")  # Default unit is Pa

#place labels and entries
Label(frame, text="Temperature (K):").grid(row=0, column=0, padx=10, pady=5)
Entry(frame, textvariable=temp_var).grid(row=0, column=1, padx=10, pady=5)

Label(frame, text="Pressure:").grid(row=1, column=0, padx=10, pady=5)
Entry(frame, textvariable=pressure_var).grid(row=1, column=1, padx=10, pady=5)

Label(frame, text="Pressure Unit:").grid(row=2, column=0, padx=10, pady=5)
OptionMenu(frame, unit_var, "Pa", "Torr").grid(row=2, column=1, padx=10, pady=5)

#submit button
Button(frame, text="Plot", command=on_submit).grid(row=3, column=0, columnspan=2, pady=10)

#export button
Button(frame, text="Export to Excel", command=export_to_excel).grid(row=4, column=0, columnspan=2, pady=10)


plot_frame = Frame(root)
plot_frame.pack(side='right', padx=10, pady=10)

# Initial plot
fig, ax = plot_initial_graph()
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack()

root.mainloop()