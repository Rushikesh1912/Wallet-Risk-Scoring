import pandas as pd

def preprocess_transactions(df):
    # Combine sender & receiver as wallets
    senders = df[['sender', 'amount']].rename(columns={'sender': 'wallet', 'amount': 'amount_sent'})
    receivers = df[['receiver', 'amount']].rename(columns={'receiver': 'wallet', 'amount': 'amount_received'})

    # Add tx count
    senders['tx_count'] = 1
    receivers['tx_count'] = 1

    # Merge sent and received
    all_tx = pd.concat([senders, receivers], axis=0)

    # Aggregate features per wallet
    wallet_features = all_tx.groupby('wallet').agg({
        'tx_count': 'count',
        'amount_sent': 'sum',
        'amount_received': 'sum'
    }).fillna(0)

    # Rename columns
    wallet_features = wallet_features.rename(columns={
        'amount_sent': 'tx_volume_sent',
        'amount_received': 'tx_volume_received'
    })

    # Total volume = sent + received
    wallet_features['tx_volume'] = wallet_features['tx_volume_sent'] + wallet_features['tx_volume_received']

    return wallet_features.reset_index()

def score_wallets(df):
    # Preprocess if needed
    if 'tx_count' not in df.columns or 'tx_volume' not in df.columns:
        df = preprocess_transactions(df)

    # Normalize
    df['risk_score'] = (df['tx_count'] + df['tx_volume']) / 2
    df['risk_level'] = pd.cut(df['risk_score'],
                              bins=[-1, 25, 50, 75, float('inf')],
                              labels=['Low', 'Medium', 'High', 'Critical'])

    return df
