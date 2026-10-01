# AI Salary Prediction Agent

A Streamlit app that predicts data-science salaries using a RandomForest model and generates AI career advice via a local LLM (Ollama `phi3`).

---

## Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install and start Ollama
Download from https://ollama.com, then:
```bash
ollama pull phi3
```
Make sure the Ollama service is running before launching the app.

### 3. Train the model (only once)
```bash
python train_model.py
```
This reads `data/ds_salaries.csv` and saves `model/salary_model.pkl` and `model/encoder.pkl`.

### 4. Launch the app
```bash
streamlit run app.py
```
Open http://localhost:8501 in your browser.

---

## Deployment

### ⚠️ Vercel
Vercel **cannot** run Streamlit apps. Streamlit requires a persistent WebSocket server, which Vercel's serverless runtime does not support.

The included `vercel.json` and `api/index.py` allow the project to deploy to Vercel without errors — Vercel will serve an informational landing page explaining how to run the app.

### ✅ Streamlit Community Cloud (recommended)
1. Push this repo to GitHub.
2. Go to https://streamlit.io/cloud and sign in.
3. Click **New app** → select your repo → set **Main file path** to `app.py`.
4. Add any required secrets in the Streamlit Cloud dashboard.
5. Deploy.

> **Note:** Streamlit Cloud does not have Ollama available. For the AI career advice feature to work, you would need to replace the `ollama` call in `agent.py` with an API-based LLM (e.g. OpenAI).

---

## Project Structure

```
├── app.py              # Streamlit UI
├── agent.py            # AI career advice via Ollama phi3
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
