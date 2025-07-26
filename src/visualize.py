import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid", palette="colorblind")

OUTPUT_DIR = "outputs/plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_top_wallets(filepath, top_n=10):
    """
    Plots and saves the top N wallets with the highest risk scores.
    """
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return

    df = pd.read_csv(filepath)

    if 'wallet_id' not in df or 'risk_score' not in df:
        print("❌ Required columns 'wallet_id' or 'risk_score' not found.")
        return

    top_wallets = df.head(top_n)

    plt.figure(figsize=(12, 6))
    sns.barplot(
        x="risk_score",
        y="wallet_id",
        data=top_wallets,
        palette="coolwarm"
    )
    plt.xlabel("🔥 Risk Score", fontsize=12, color="darkred")
    plt.ylabel("🧾 Wallet ID", fontsize=12)
    plt.title(f"🚨 Top {top_n} High-Risk Wallets", fontsize=15, 
              weight='bold', color="darkblue")
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.tight_layout()

    save_path = os.path.join(OUTPUT_DIR, f"top_{top_n}_wallets.png")
    plt.savefig(save_path, dpi=300)
    print(f"✅ Saved top wallet plot to: {save_path}")

    plt.show()


def plot_transaction_distribution(filepath):
    """
    Plots and saves the distribution of risk scores.
    """
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return

    df = pd.read_csv(filepath)

    if 'risk_score' not in df:
        print("❌ Column 'risk_score' not found.")
        return

    plt.figure(figsize=(10, 5))
    sns.histplot(
        df["risk_score"],
        bins=25,
        kde=True,
        color='orangered',
        edgecolor='black'
    )
    plt.xlabel("📊 Risk Score", fontsize=12)
    plt.ylabel("🔢 Frequency", fontsize=12)
    plt.title("📈 Distribution of Risk Scores Across Wallets", 
              fontsize=14, weight='bold', color="darkgreen")
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.tight_layout()

    save_path = os.path.join(OUTPUT_DIR, "risk_score_distribution.png")
    plt.savefig(save_path, dpi=300)
    print(f"✅ Saved distribution plot to: {save_path}")

    plt.show()
