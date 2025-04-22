import matplotlib.pyplot as plt

def plot_results(sim_results):
    plt.figure(figsize=(10, 6))
    plt.scatter(sim_results['Risk'], sim_results['Return'], alpha=0.3, c=sim_results['Return']/sim_results['Risk'], cmap='viridis')
    plt.xlabel('Risk (Std. Deviation)')
    plt.ylabel('Expected Return')
    plt.title('Simulated Portfolio Performance')
    plt.colorbar(label='Sharpe Ratio')
    plt.grid(True)
    plt.show()
