from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return render_template(
    "home.html",
  )

@app.route('/user/<username>')
def show_user_profile(username:str):
  return render_template(
    'user_profile.html', 
    name = username
  )

if __name__ == "__main__":
  app.run(host="127.0.0.1", port=4444, debug=True)
