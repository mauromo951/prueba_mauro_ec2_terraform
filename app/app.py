from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def show_ips():
    # Obtener la IP del cliente (quien abre el navegador)
    client_ip = request.remote_addr

    # Obtener la IP pública del servidor EC2 usando curl
    try:
        result = subprocess.run(
            ["curl", "-s", "http://myip.enix.org/REMOTE_ADDR"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        server_ip = result.stdout.strip()
    except subprocess.CalledProcessError:
        server_ip = "No se pudo obtener la IP del servidor EC2."

    return f"""
        <html>
            <head><title>IP Viewer</title></head>
            <body>
                <h1>IP del navegador (cliente):</h1>
                <pre>{client_ip}</pre>
                <h1>IP pública del servidor EC2:</h1>
                <pre>{server_ip}</pre>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

