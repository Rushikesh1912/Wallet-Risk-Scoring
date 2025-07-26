# src/main.py

import os
from src.visualize import plot_top_wallets, plot_transaction_distribution


def main():
    output_file = "output/wallet_risk_scores.csv"

    if not os.path.exists(output_file):
        print("Risk scores file not found. Please run score_wallets.py first.")
        return

    print("🎯 Visualizing Top Risky Wallets...")
    plot_top_wallets(output_file, top_n=10)
    print("✅ Saved: output/plots/top_wallets.png")

    print("📊 Visualizing Risk Score Distribution...")
    plot_transaction_distribution(output_file)
    print("✅ Saved: output/plots/risk_distribution.png")


if __name__ == "__main__":
    main()
