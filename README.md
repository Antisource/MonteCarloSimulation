# Stock Price Simulation with Monte Carlo

This Python script performs a Monte Carlo simulation to generate multiple possible future price paths for a given stock based on historical daily returns. The simulation is implemented using historical stock data fetched from Yahoo Finance.

## Prerequisites

Make sure you have the required Python libraries installed:

- yfinance
- numpy
- matplotlib

You can install them using the following command:

```bash
pip install yfinance numpy matplotlib
```

## Usage
1. **Clone the Repository:**
   
   ```bash
    git clone https://github.com/Antisource/MonteCarloSimulation.git
   ```

2. **Run the App:**
   - Run the script by executing the following command in your terminal:
  ```bash
   python  Monte_Carlo_Stock_Simulation.py
  ```

- Enter the requested information, including the name of the stock/company and its ticker symbol.

- View the generated Monte Carlo simulation plot, which shows multiple possible future price paths for the given stock.

## Code Explanation

- The script downloads historical stock data using the Yahoo Finance API.
- It calculates daily returns and computes the mean and standard deviation of these returns.
= Random daily returns are generated for a Monte Carlo simulation.
- The script simulates future stock prices and plots multiple paths to visualize potential future scenarios.
