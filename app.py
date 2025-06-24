# Starting script
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="PyShiny App with Plot",fillable=True)

# Create a sidebar with slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 50, 25)


@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 437
    # Set a random seed to ensure reproductability.
    np.random.seed(3)
    # Generate random data:
    # - np.random.randn(count_of_plots) generates 'count_of_points' samples from a standard normal distribution.
    # - Each sample is then scaled by 15 (to increase the spread) and shifted by 100 (to center the distribution around 100).
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
