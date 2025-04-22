import numpy as np
import pandas as pd

def run_simulation(data, weights, num_simulations=1000, time_horizon=252):
    log_returns = np.log(1 + data.pct_change())
    mean_returns = log_returns.mean()
    cov_matrix = log_returns.cov()

    portfolio_results = []

    for _ in range(num_simulations):
        simulated_returns = np.random.multivariate_normal(mean_returns, cov_matrix, time_horizon)
        portfolio_return = np.sum(simulated_returns @ weights)
        portfolio_std = np.std(simulated_returns @ weights)
        portfolio_results.append([portfolio_return, portfolio_std])

    return pd.DataFrame(portfolio_results, columns=["Return", "Risk"])