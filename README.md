# 🚀 Wallet Risk Scoring System

This project is a **comprehensive risk analysis system for crypto wallets**. Using blockchain transaction data, we score wallets based on behavioral patterns using machine learning. The project supports file uploads via a Flask-based web interface and provides real-time scoring results.

---

## 📁 Project Structure

WALLET-RISK-SCORING/
├── data/ # Raw data files
│ ├── generated_transactions.csv
│ └── wallet-ids.csv
├── notebooks/ # Jupyter Notebooks for modeling and analysis
│ ├── EDA.ipynb
│ ├── Final_Scoring.ipynb
│ └── Model_Training.ipynb
├── output/
│ ├── wallet_risk_scores.csv
│ └── outputs/
│ └── plots/
│ ├── risk_score_distribution.png
│ └── top_10_wallets.png
├── src/
│ ├── fetch_transactions.py
│ ├── model_random_forest.pkl
│ ├── score_wallets.py
│ └── visualize.py
├── templates/
│ └── index.html
├── uploads/
├── app.py # Flask web app
├── main.py # CLI entry-point
├── analysis.md # Detailed project writeup
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 📌 Features

- ✅ ML-Based Wallet Risk Prediction (`RandomForestClassifier`)
- ✅ Real-time Flask Web App with File Upload and Results Display
- ✅ Upload your wallet transaction CSV and get instant risk scoring
- ✅ Easy-to-use UI with table and pie chart visualization
- ✅ Clean risk classification: Low, Medium, High, Critical

---

## 💡 Technologies Used

| Layer       | Tools                             |
|------------|-----------------------------------|
| Language    | Python                            |
| ML Model    | Random Forest (Scikit-learn)       |
| Web Backend | Flask                             |
| Frontend    | HTML, CSS                         |
| Visualization | Matplotlib, Seaborn, Plotly     |
| Deployment | Locally hosted Flask app          |

---

## 📷 Screenshots

### 🔍 Risk Score Distribution  
![Risk Score Distribution](https://raw.githubusercontent.com/Rushikesh1912/Wallet-Risk-Scoring/main/outputs/plots/risk_score_distribution.png)

### 🏆 Top 10 Risky Wallets  
![Top 10 Wallets](https://raw.githubusercontent.com/Rushikesh1912/Wallet-Risk-Scoring/main/outputs/plots/top_10_wallets.png)


---

## 🔥 Risk Levels

| Risk Score Range | Risk Level  |
|------------------|-------------|
| 0 - 40           | Low         |
| 41 - 70          | Medium      |
| 71 - 90          | High        |
| 91 - 100         | Critical    |

---

## 🚀 Dashboard Features

- Upload your own wallet CSV file via a simple dashboard
- Get instant risk scores, visualizations, and top wallet summaries
- Data-driven scoring based on behavior and transaction metrics
- Clean dashboard UI built with Streamlit

---

## 🖼️ Dashboard Screenshots

### 🧾 Upload CSV Interface
![Upload CSV](https://github.com/Rushikesh1912/Wallet-Risk-Scoring/blob/main/outputs/screenshots/upload_csv_ui.png)

### 🧮 Risk Prediction Output
![Risk Prediction Output](https://github.com/Rushikesh1912/Wallet-Risk-Scoring/blob/main/outputs/screenshots/result_output_ui.png)


## 📦 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/wallet-risk-scoring.git
cd wallet-risk-scoring

# 2. Create virtual environment (optional)
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
Then open your browser at http://localhost:5000

📤 How to Use
Prepare a transaction CSV file with wallet details

Upload it via the interface

View scored results instantly with a table and pie chart

🙋‍♂️ Author
Rushi Kadam
BTech – Artificial Intelligence and Data Science
Passionate about building end-to-end AI applications for real-world use cases.

📃 License
This project is licensed for educational use. Commercial use requires permission.
