from flask import Flask, render_template
from get_data import *

app = Flask(__name__)

@app.route('/')
def home():
  
  data = get_data()
  
  return render_template(
    "./basic.html",
    name = data['username'],   # pulls username
    age = data['user_age'],    # pulls user age
    fruits = data['fruit_list']  # pulls fruits
  )

app.run(host="127.0.0.1", port=4444)

if __name__ == "__main__":
  app.run(debug=True)
