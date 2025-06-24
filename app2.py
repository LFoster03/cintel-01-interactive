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
