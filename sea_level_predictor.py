import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (in meters)')
    # Create first line of best fit
    dt = df[df['Year'] >= 2000]
    slope, intercept, r, p, se = linregress(dt['Year'], dt['CSIRO Adjusted Sea Level'])
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    first_line = slope * dt['Year'] + intercept
    plt.plot(dt['Year'], first_line, color='blue', label ='Line of Best Fit')

    years_extended = range(dt['Year'].min(), 2051)
    sea_level_fit_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_level_fit_extended, color='green', linestyle='--', label='Prediction to 2050')
    # Create second line of best fit
    slope2, intercept2, r2, p2, se2 = linregress(dt['Year'], dt['CSIRO Adjusted Sea Level'])
    
    second_line = slope2 * dt['Year'] + intercept2
    plt.plot(dt['Year'], second_line, color='red', label='Second Line of Best Fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()