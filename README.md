# AI Salary Prediction Agent

A Streamlit application that predicts data-science salaries using a Random Forest model.

Select your experience level, job role, company size, location, and remote ratio — click **Predict** to get an estimated annual salary in USD.

---

## Inputs

| Field | Options |
|---|---|
| Experience Level | EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| Job Role | 15 data-science roles (Data Scientist, ML Engineer, etc.) |
| Company Size | S (Small), M (Medium), L (Large) |
| Location | 10 countries (US, CA, UK, IN, DE, FR, AU, BR, ES, NL) |
| Remote Ratio | 0% On-site · 50% Hybrid · 100% Fully Remote |

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
Reads `data/ds_salaries.csv` and saves `model/salary_model.pkl` and `model/encoder.pkl`.

### 3. Launch the app
```bash
streamlit run app.py
```
Open http://localhost:8501 in your browser.

---

## Deployment

### ✅ Render (recommended)
1. Push this repo to GitHub.
2. Create a new **Web Service** on [Render](https://render.com).
3. Set **Start Command** to:
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
│   └── ds_salaries.csv # Training dataset (900 rows, 15 job titles, 10 locations)
└── model/
    ├── salary_model.pkl
    └── encoder.pkl
```
