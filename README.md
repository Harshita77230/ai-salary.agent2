# AI Salary Prediction Agent

A Streamlit application that predicts data-science salaries using a Random Forest model trained on the DS Salaries dataset.

---

## Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model (only once)
```bash
python train_model.py
```
This reads `data/ds_salaries.csv` and saves `model/salary_model.pkl` and `model/encoder.pkl`.

### 3. Launch the app
```bash
streamlit run app.py
```
Open http://localhost:8501 in your browser.

---

## How It Works

Select your experience level, job role, company size, location, and remote ratio, then click **Predict** to get an estimated annual salary in USD.

The prediction is made by a `RandomForestRegressor` trained on real-world data-science salary data.

---

## Deployment

### ✅ Render (recommended)
1. Push this repo to GitHub.
2. Create a new **Web Service** on [Render](https://render.com).
3. Set the **Start Command** to:
   ```
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```
4. Deploy.

### ✅ Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to https://streamlit.io/cloud and sign in.
3. Click **New app** → select your repo → set **Main file path** to `app.py`.
4. Deploy.

### ⚠️ Vercel
Vercel cannot run Streamlit apps. The included `vercel.json` and `api/index.py` serve a static landing page on Vercel instead.

---

## Project Structure

```
├── app.py              # Streamlit UI and salary prediction
├── train_model.py      # Model training script
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment config (landing page only)
├── api/
│   └── index.py        # Vercel serverless handler (landing page)
├── data/
│   └── ds_salaries.csv # Training dataset
└── model/
    ├── salary_model.pkl
    └── encoder.pkl
```
