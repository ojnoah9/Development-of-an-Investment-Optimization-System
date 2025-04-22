# Investment Portfolio Optimization System

This project is a simulation-based system to optimize investment portfolios using historical stock market data. The system leverages techniques like Markowitz Portfolio Theory, Monte Carlo simulations, and performance metrics (Sharpe Ratio, Alpha, Beta) to help investors make informed decisions based on their risk preferences.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Implementation](#implementation)
- [Simulation Flow](#simulation-flow)
- [Usage](#usage)
- [Expected Output](#expected-output)
- [Background Studies](#background-studies)

## Project Overview

The goal of this project is to implement a portfolio optimization system that:
1. Fetches historical stock market data.
2. Uses Markowitz Portfolio Theory to optimize asset allocation based on user-defined risk and return preferences.
3. Simulates different market scenarios using Monte Carlo simulations.
4. Visualizes portfolio performance metrics (Sharpe ratio, alpha, beta).
5. Tracks and outputs changes in the portfolio during simulations.

## Technologies

- **Python 3.x**
- **Libraries**:
  - `pandas`: For data manipulation.
  - `numpy`: For numerical operations.
  - `matplotlib`: For plotting graphs.
  - `scipy`: For optimization.
  - `yfinance`: To fetch historical financial data from Yahoo Finance.
  
## Setup Instructions

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/portfolio-optimization.git
   cd portfolio-optimization
2. **Create and activate a virtual environment (optional but recommended)**:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install required dependencies**:

bash
Copy
Edit
pip install -r requirements.txt
4. **Fetch historical data**: You can run the script to fetch historical stock data using the yfinance library. This data will be saved as a CSV file for later use.

bash
Copy
Edit
python src/fetch_data.py
5. **Run the main simulation**: Execute the simulation by running the main.py file:

bash
Copy
Edit
python main.py
This will:

Fetch stock data.

Optimize the portfolio.

Run Monte Carlo simulations to estimate portfolio performance.

Plot the results using matplotlib.

## Implementation
Portfolio Optimization Logic
The portfolio optimization is based on Markowitz Portfolio Theory. The system optimizes the weights of different assets in a portfolio, balancing the trade-off between risk (standard deviation) and return. The objective is to maximize the Sharpe ratio.

Monte Carlo Simulations
We simulate various market scenarios by assuming that returns are log-normally distributed. The system runs multiple simulations of portfolio returns over a specified time horizon to assess the portfolio's risk and performance.

## Visualizations
We use matplotlib to visualize:

The relationship between risk and return.

Simulated portfolio performance under different scenarios.

The Sharpe ratio as a color map on scatter plots.

## Simulation Flow
Data Fetching: We fetch historical stock market data from Yahoo Finance using the yfinance library.

Portfolio Optimization: We use the scipy.optimize function to minimize the negative Sharpe ratio and find the optimal portfolio allocation.

Market Simulations: The Monte Carlo simulation is used to simulate returns and calculate portfolio risk and return over multiple scenarios.

Visualization: The results are visualized in a scatter plot where the color represents the Sharpe ratio, showing the optimal risk-return trade-off.

## Usage
Run the portfolio optimization:

bash
Copy
Edit
python main.py
Visualize results: The matplotlib plot will be displayed showing portfolio performance across different simulated market scenarios.

View portfolio allocation: After optimization, the portfolio weights will be displayed, showing the proportion of each asset in the portfolio.

 ## Expected Output
The expected output of the simulation includes:

A scatter plot showing the risk-return trade-off for the simulated portfolios.

The optimal portfolio weights that maximize the Sharpe ratio.

Key performance metrics such as:

Sharpe Ratio: Measures risk-adjusted return.

Alpha and Beta: Performance of the portfolio relative to the market.

Simulated Portfolio Return and Risk: Based on Monte Carlo simulations.

## Background Studies
Markowitz Portfolio Theory: A model that optimizes a portfolio by balancing risk and return. It uses historical returns and correlations between assets to determine the best allocation.

Risk-Return Tradeoff: The principle that higher returns are generally associated with higher risk. Investment decisions should be based on an investor's risk tolerance.

Simulated Market Scenarios: Modelling various potential market conditions (bullish, bearish, volatile) to assess portfolio performance under different conditions.

Monte Carlo Simulation: A method used to simulate the behavior of financial portfolios under uncertain conditions by running simulations based on random market scenarios.

Sharpe Ratio: A measure of the risk-adjusted return of an investment portfolio.

Alpha and Beta: Measures of a portfolio's performance relative to the market. Alpha represents excess return, while Beta measures the portfolio's volatility compared to the market.