import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------
prices = np.array([100, 95, 90, 85, 80])  # DCA prices
dca_steps = len(prices)
increasing_leverage = np.array([2, 4, 6, 7, 10])
decreasing_leverage = np.array([10, 8, 6, 4, 2])
uniform_leverage = np.array([6, 6, 6, 6, 6])

# -----------------------------
# Function to calculate weighted average entry
# -----------------------------
def weighted_avg_entry(prices, leverage):
    return np.sum(prices * leverage) / np.sum(leverage)

avg_increasing = weighted_avg_entry(prices, increasing_leverage)
avg_decreasing = weighted_avg_entry(prices, decreasing_leverage)
avg_uniform = weighted_avg_entry(prices, uniform_leverage)

# -----------------------------
# Plot 1: DCA Levels vs Drawdown
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(range(dca_steps), prices, marker='o', linestyle='-', color='blue', label='DCA Price')
plt.title("DCA Levels vs Drawdown")
plt.xlabel("DCA Step")
plt.ylabel("Price")
plt.grid(True)
plt.xticks(range(dca_steps))
plt.legend()
plt.tight_layout()
plt.savefig("placeholder_dca_levels.png")
plt.close()

# -----------------------------
# Plot 2: Leverage Allocation
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(range(dca_steps), increasing_leverage, marker='o', linestyle='-', color='green', label='Increasing Leverage')
plt.plot(range(dca_steps), decreasing_leverage, marker='s', linestyle='--', color='red', label='Decreasing Leverage')
plt.plot(range(dca_steps), uniform_leverage, marker='^', linestyle='-.', color='purple', label='Uniform Leverage')
plt.title("Leverage Allocation Across DCA Steps")
plt.xlabel("DCA Step")
plt.ylabel("Leverage")
plt.grid(True)
plt.xticks(range(dca_steps))
plt.legend()
plt.tight_layout()
plt.savefig("placeholder_leverage_allocation.png")
plt.close()

# -----------------------------
# Plot 3: Weighted Average Entry
# -----------------------------
avg_entries = [avg_increasing, avg_decreasing, avg_uniform]
labels = ['Increasing', 'Decreasing', 'Uniform']

plt.figure(figsize=(6,5))
plt.bar(labels, avg_entries, color=['green', 'red', 'purple'])
plt.title("Average Entry Price by Leverage Sequence")
plt.ylabel("Average Entry Price")
plt.tight_layout()
plt.savefig("placeholder_avg_entry.png")
plt.close()

# -----------------------------
# Plot 4: Simulated P/L vs Market Drawdown
# -----------------------------
drawdowns = np.linspace(0, 0.1, 50)  # 0% to 10%
# Simulated P/L curves (mock realistic)
pl_increasing = 0.05 - drawdowns*0.2
pl_decreasing = 0.02 - drawdowns*0.25
pl_uniform = 0.03 - drawdowns*0.22

plt.figure(figsize=(8,5))
plt.plot(drawdowns*100, pl_increasing*100, label='Increasing Leverage', color='green')
plt.plot(drawdowns*100, pl_decreasing*100, label='Decreasing Leverage', color='red')
plt.plot(drawdowns*100, pl_uniform*100, label='Uniform Leverage', color='purple')
plt.title("Simulated P/L vs Market Drawdown")
plt.xlabel("Market Drawdown (%)")
plt.ylabel("P/L (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("placeholder_pl_chart.png")
plt.close()

print("Plots generated and saved as PNG files for your research paper.")
