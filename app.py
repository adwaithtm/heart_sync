from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Incoming Request...</title>
  <style>
    body { background:#ffe6e6; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:Arial; }
    h1 { color:#ff4d6d; }
    #yes { background:#ff4d6d; color:white; padding:10px 20px; border:none; border-radius:6px; font-size:16px; }
    #no { position:absolute; padding:10px 20px; font-size:16px; }
  </style>
</head>
<body>
  <h1>Will you be my valentine?</h1>
  <button id="yes" onclick="alert('Excellent choice! ❤️')">YES</button>
  <button id="no" onmouseover="moveNo()">NO</button>

  <script>
    function moveNo() {
      const no = document.getElementById("no");
      const x = Math.random() * (window.innerWidth - 80);
      const y = Math.random() * (window.innerHeight - 40);
      no.style.left = x + "px";
      no.style.top = y + "px";
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
