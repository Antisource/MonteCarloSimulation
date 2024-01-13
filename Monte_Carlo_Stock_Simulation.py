# Import necessary libraries
import yfinance as yf  # For fetching financial data
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting graphs

# User input for the stock's name and ticker symbol
share = input("Enter name of share i.e company \n")
tic_sym = input("Enter ticker symbol of your stock i.e company \n")

# Download historical stock data using Yahoo Finance API
df = yf.download(tic_sym)
print(df)

# Calculate daily returns using the adjusted closing prices
returns = np.log(1 + df['Adj Close'].pct_change())

# Calculate mean (mu) and standard deviation (sigma) of the returns
mu, sigma = returns.mean(), returns.std()

# Generate random daily returns for a Monte Carlo simulation
sim_rets = np.random.normal(mu, sigma, 252)

# Get the initial stock price
initial = df['Adj Close'].iloc[-1]

# Simulate future stock prices using the generated returns
sim_prices = initial * (sim_rets + 1).cumprod()

# Repeat the simulation and plot multiple paths (100 in this case)
for i in range(100):
    sim_rets = np.random.normal(mu, sigma, 252)
    sim_prices = initial * (sim_rets + 1).cumprod()

    # Plot each simulated price path
    plt.axhline(initial, c='k')  # Add a horizontal line at the initial price
    plt.plot(sim_prices)

# Set plot labels and title
plt.title('Monte Carlo Simulation for ' + tic_sym)
plt.xlabel('Days')
plt.ylabel('Price')

# Display the plot
plt.show()

