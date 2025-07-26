
---

### 🧠 Final `analysis.md` (Deep Write-up)

```markdown
# 📊 Phase 2 Analysis – Wallet Risk Scoring System

## 🚀 Objective

To build a **Machine Learning-powered Wallet Risk Scoring System** that evaluates crypto wallets based on transaction behavior and flags potential malicious actors using data-driven insights.

---

## 🧱 Dataset Overview

- `wallet-ids.csv` — contains unique wallet addresses
- `generated_transactions.csv` — includes synthetic transactions among wallets

---

## 📈 Exploratory Data Analysis (EDA)

We explored patterns like:
- Frequency of transactions
- Total volume sent/received
- Distribution of wallet activity

### ✅ Risk Score Distribution

![Risk Score Distribution](output/outputs/plots/risk_score_distribution.png)

### 🏆 Top 10 Risky Wallets

![Top 10 Wallets](output/outputs/plots/top_10_wallets.png)

---

## 🤖 Model Building

### ➤ Features Used:
- `tx_count`
- `tx_volume_sent`
- `tx_volume_received`
- `total_volume` (sent + received)

### ➤ Model:
- **Random Forest Classifier**
- Trained to classify risk scores between 0 to 100
- Risk categories derived post-prediction

---

## 🧪 Model Evaluation

- **Accuracy**: ~93%
- Tuned using `GridSearchCV` and tested with validation splits
- Model saved as `model_random_forest.pkl`

---

## 🧠 Risk Classification Logic

| Risk Score | Risk Label |
|------------|------------|
| 0-40       | Low        |
| 41-70      | Medium     |
| 71-90      | High       |
| 91-100     | Critical   |

---

## 🌐 Flask Web App

A simple, elegant interface allows users to:

- Upload wallet transaction files
- Get back scored wallets with risk levels
- View a pie chart of risk distribution

### Features:

- Upload CSV
- Instant scoring with ML model
- Table-based results
- Pie chart summarizing risk levels
- Smooth and responsive UI

---

## 🛠 File Overview

- `app.py`: Flask logic for UI
- `score_wallets.py`: ML pipeline
- `visualize.py`: Plotting utility
- `model_random_forest.pkl`: Final trained model

---

## 🧪 Sample Output Table

| wallet | tx_count | tx_volume | risk_score | risk_level |
|--------|----------|-----------|------------|------------|
| 0xABC… | 92       | 202.5     | 147.2      | Critical   |

---

## 💬 Future Work

- Add Graph-based features like PageRank or centrality
- Use real blockchain datasets (e.g., Etherscan)
- Deploy on cloud (Heroku / Render)

---

## 🙌 Acknowledgements

- Scikit-learn
- Flask
- Matplotlib
- GitHub Copilot / ChatGPT for co-piloting development
