from http.server import BaseHTTPRequestHandler

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>AI Salary Agent</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
      background: #f7f8fa;
      color: #1f2328;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 2rem;
    }
    .card {
      background: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      padding: 2.5rem 2rem;
      max-width: 560px;
      width: 100%;
      text-align: center;
    }
    h1 { font-size: 1.6rem; margin-bottom: 0.5rem; }
    .badge {
      display: inline-block;
      background: #f0f4ff;
      color: #3b82d4;
      border: 1px solid #c7d9f8;
      border-radius: 20px;
      font-size: 0.78rem;
      padding: 0.2rem 0.75rem;
      margin-bottom: 1.5rem;
      font-weight: 600;
      letter-spacing: 0.03em;
    }
    p { color: #57606a; line-height: 1.7; margin-bottom: 1rem; font-size: 0.95rem; }
    .note {
      background: #fff8e1;
      border: 1px solid #ffe082;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      color: #7c5c00;
      font-size: 0.88rem;
      line-height: 1.6;
      text-align: left;
      margin-bottom: 1.5rem;
    }
    .note strong { display: block; margin-bottom: 0.3rem; }
    code {
      background: #f0f4ff;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      font-size: 0.85rem;
      color: #3b82d4;
    }
    .steps {
      text-align: left;
      background: #f7f8fa;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
      line-height: 1.8;
      color: #1f2328;
    }
    .steps ol { padding-left: 1.2rem; }
    footer {
      margin-top: 1.5rem;
      font-size: 0.75rem;
      color: #57606a;
      border-top: 1px solid #e5e7eb;
      padding-top: 1rem;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">Streamlit App</div>
    <h1>AI Salary Prediction Agent</h1>
    <p style="margin-bottom:1.5rem;">
      This is a <strong>Streamlit</strong> application that predicts data-science salaries
      using a RandomForest model and generates AI career advice via a local LLM (Ollama phi3).
    </p>
    <div class="note">
      <strong>&#9888; Vercel cannot run Streamlit apps.</strong>
      Streamlit requires a persistent WebSocket server. Vercel's serverless runtime
      does not support this. To use the full app, run it locally or deploy it to
      <strong>Streamlit Community Cloud</strong>.
    </div>
    <div class="steps">
      <strong>Run locally in 3 steps:</strong>
      <ol>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Train the model (once): <code>python train_model.py</code></li>
        <li>Launch the app: <code>streamlit run app.py</code></li>
      </ol>
    </div>
    <p>
      Then open <code>http://localhost:8501</code> in your browser.
    </p>
    <footer>AI Salary Agent &mdash; Powered by Streamlit, scikit-learn &amp; Ollama</footer>
  </div>
</body>
</html>"""


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def log_message(self, format, *args):
        pass  # suppress Vercel serverless logs
