from flask import Flask, render_template
import webbrowser as web

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return render_template(
    "home.html",
  )

if __name__ == "__main__":
  hostIP = '127.0.0.1'
  port_num = '4444'
  # web.open(f'http://{hostIP}:{port_num}')
  app.run(host=hostIP, port=port_num, debug=True)
