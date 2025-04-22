from src.fetch_data import get_data
from src.optimize import optimize_portfolio
from src.simulate import run_simulation
from src.visualize import plot_results

TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
data = get_data(TICKERS)
weights = optimize_portfolio(data)
sim_results = run_simulation(data, weights)
plot_results(sim_results)