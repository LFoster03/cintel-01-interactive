# cintel-01-interactive
New Shiny App Script

import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app
ui.page_opts(title="Penguin Distribution Plotter", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    ui.input_slider(
        "selected_amount_of_bins",     # Unique ID
        "Amount of Bins",              # Label
        5,                             # Minimum number of bins
        200,                           # Maximum number of bins
        10                             # Initial number of bins
    )

@render.plot(alt="Histogram showing data distribution based on selected amount of bins")
def plot_histogram():
    # Total number of points to generate
    num_points = 500

    # Set seed for reproducibility
    np.random.seed(53)

    # Generate random data centered at 50 with spread of 10
    data = 50 + 10 * np.random.randn(num_points)

    # Create histogram using selected number of bins
    plt.hist(data, bins=input.selected_amount_of_bins(), density=True, color='skyblue', edgecolor='black')

    # Add labels and title for better presentation
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Histogram of Random Data Distribution')
    plt.grid(True)

# Elements Included:
## Page title - "Pemguin Distribution Plotter" used
## Slider input	- ID: "selected_amount_of_bins", Label: "Amount of Bins", Min: 5, Max: 200, Initial: 10
## Reactive plot -	Plot updates automatically when slider changes
## plt.hist() with density=True	-	Used to normalize the histogram

# Bonus
Added:
1. A button to regenerate random data.
2. An input to change the mean of the data.
3. An input to change the spread (standard deviation) of the data.
4. An input to select the color of the histogram.
5. A text output to show the mean and standard deviation of the generated data.

import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from shiny import reactive

# App page options
ui.page_opts(title="Advanced Penguin Distribution Plotter", fillable=True)

# Sidebar: user controls
with ui.sidebar():
    ui.input_slider("selected_amount_of_bins", "Amount of Bins", 5, 200, 10)
    ui.input_numeric("data_mean", "Data Mean", 50)
    ui.input_numeric("data_std", "Data Spread (Std Dev)", 10)
    ui.input_select("hist_color", "Histogram Color", choices=["skyblue", "lightgreen", "salmon", "plum"], selected="skyblue")
    ui.input_action_button("generate_button", "Generate New Data")

# Reactive data generator: runs when the button is clicked
@reactive.calc
def generated_data():
    # Wait for the button to be pressed
    input.generate_button()

    # Random seed changes every time the button is clicked to get new data
    np.random.seed()

    # Generate random data with user-defined mean and spread
    num_points = 500
    data = input.data_mean() + input.data_std() * np.random.randn(num_points)
    return data

# Reactive plot: updates when bins, color, or data change
@render.plot(alt="Histogram showing data distribution based on user input")
def plot_histogram():
    data = generated_data()

    plt.hist(
        data,
        bins=input.selected_amount_of_bins(),
        density=True,
        color=input.hist_color(),
        edgecolor='black'
    )
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Histogram of Random Data Distribution')
    plt.grid(True)

# Text output: display data summary (mean and std dev)
@render.text
def data_summary():
    data = generated_data()
    mean_value = np.mean(data)
    std_value = np.std(data)
    return f"Data Mean: {mean_value:.2f}, Data Standard Deviation: {std_value:.2f}"

