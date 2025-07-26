import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
import os

WALLET_CSV_PATH = "data/wallet-ids.csv"
OUTPUT_CSV_PATH = "data/generated_transactions.csv"

NUM_TRANSACTIONS = 5000  
TRANSACTION_TYPES = ['transfer', 'contract', 'mint', 'stake', 'swap']


def generate_random_timestamp(start_date, end_date):
    """Generate a random timestamp between two dates."""
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_date + timedelta(seconds=random_seconds)


def simulate_transactions(wallet_ids, num_transactions):
    transactions = []
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 7, 1)

    for _ in range(num_transactions):
        sender, receiver = random.sample(wallet_ids, 2)

        transaction = {
            'tx_id': str(uuid.uuid4()),
            'sender': sender,
            'receiver': receiver,
            'amount': round(random.uniform(0.001, 5.0), 4),
            'timestamp': generate_random_timestamp(
                start_date, end_date).strftime('%Y-%m-%d %H:%M:%S'),
            'type': random.choice(TRANSACTION_TYPES),
            'status': random.choice(['success', 'pending', 'failed']),
        }
        transactions.append(transaction)
    
    return pd.DataFrame(transactions)


def main():
    if not os.path.exists(WALLET_CSV_PATH):
        print(f"❌ Error: {WALLET_CSV_PATH} not found.")
        return

    wallets_df = pd.read_csv(WALLET_CSV_PATH)
    wallet_ids = wallets_df['wallet_id'].tolist()

    print(f"✅ Loaded {len(wallet_ids)} wallet IDs.")

    transactions_df = simulate_transactions(wallet_ids, NUM_TRANSACTIONS)
    transactions_df.to_csv(OUTPUT_CSV_PATH, index=False)

    print(f"✅ Generated {NUM_TRANSACTIONS} fake transactions.")
    print(f"📁 Saved to: {OUTPUT_CSV_PATH}")


if __name__ == "__main__":
    main()
