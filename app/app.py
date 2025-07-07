from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def show_ip():
    try:
        result = subprocess.run(
            ["./get_ip.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return f"<h1>Tu IP pública es:</h1><pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<h1>Error ejecutando el script</h1><pre>{e.stderr}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
