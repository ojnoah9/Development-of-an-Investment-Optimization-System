import numpy as np
import pandas as pd
from scipy.optimize import minimize

def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.dot(weights, mean_returns)
    std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, std_dev

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    returns, std_dev = portfolio_performance(weights, mean_returns, cov_matrix)
    return -(returns - risk_free_rate) / std_dev

def optimize_portfolio(data, risk_free_rate=0.01):
    mean_returns = data.pct_change().mean()
    cov_matrix = data.pct_change().cov()
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix, risk_free_rate)

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(num_assets))
    initial_weights = num_assets * [1. / num_assets]

    result = minimize(negative_sharpe_ratio, initial_weights, args=args,
                      method='SLSQP', bounds=bounds, constraints=constraints)

    return result.x