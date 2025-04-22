import numpy as np

def sharpe_ratio(returns, risk_free_rate):
    return (returns.mean() - risk_free_rate) / returns.std()

def alpha_beta(portfolio_returns, market_returns):
    cov_matrix = np.cov(portfolio_returns, market_returns)
    beta = cov_matrix[0, 1] / cov_matrix[1, 1]
    alpha = portfolio_returns.mean() - beta * market_returns.mean()
    return alpha, beta