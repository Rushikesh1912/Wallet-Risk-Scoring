from flask import Flask, request, render_template, send_file
import pandas as pd
import os
from src.score_wallets import score_wallets
from io import BytesIO

app = Flask(__name__)
scored_df_global = None  # to hold global dataframe for download

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global scored_df_global
    file = request.files['file']
    if not file:
        return "No file uploaded", 400
    
    df = pd.read_csv(file)

    # Basic validation
    if 'sender' not in df.columns or 'receiver' not in df.columns or 'amount' not in df.columns:
        return "CSV must contain 'sender', 'receiver', and 'amount' columns.", 400

    scored_df = score_wallets(df)
    scored_df_global = scored_df  # Save for download

    # Risk Chart Prep
    risk_counts = scored_df['risk_level'].value_counts()
    labels = list(risk_counts.index)
    counts = list(risk_counts.values)

    return render_template(
        'index.html',
        tables=scored_df.to_html(classes='data', index=False),
        risk_labels=labels,
        risk_counts=counts
    )

@app.route('/download', methods=['GET'])
def download():
    global scored_df_global
    if scored_df_global is None:
        return "No data to download", 400

    buffer = BytesIO()
    scored_df_global.to_csv(buffer, index=False)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='scored_wallets.csv', mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
