from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  
  username = "Page Switcher"
  
  return render_template(
    "home.html",
    name = username
  )

@app.route('/page2', methods=['GET'])
def page2():
  return render_template(
    "page2.html"
  )

if __name__ == "__main__":
  app.run(host="127.0.0.1", port=4444, debug=True)
